import os
import json
import re
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import google.generativeai as genai
import pdfplumber

# --- CONFIGURATION ---
# Load environment variables from a .env file
load_dotenv()
app = Flask(__name__)

# Configure the Google Gemini API with your API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# --- HELPER FUNCTIONS ---
def extract_text_from_pdf(file_storage):
    """
    Extracts text content from an uploaded PDF file file_storage object.
    Returns the extracted text as a string, or None if an error occurs.
    """
    try:
        with pdfplumber.open(file_storage) as pdf:
            text = "".join([page.extract_text() or "" for page in pdf.pages])
        return text.strip()
    except Exception as e:
        print(f"PDF extraction error: {str(e)}")  # Debug logging
        return None

def call_gemini(prompt, expect_json=True):
    """
    Sends a prompt to the Gemini API and returns the response.
    Handles JSON parsing if expect_json is True.
    """
    try:
        # Using a fast, capable model. Adjust as needed.
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(prompt)

        if not expect_json:
            return response.text

        # Clean potential markdown formatting from the response
        text = response.text.strip()
        text = re.sub(r'```json\s*', '', text)
        text = re.sub(r'```', '', text)

        # Attempt to find and extract a JSON object from the text
        match = re.search(r'\{.*\}', text, re.DOTALL)
        if match:
            json_str = match.group(0)
            return json.loads(json_str)

        # Fallback: try parsing the entire text
        return json.loads(text)

    except json.JSONDecodeError as e:
        print(f"JSON Parse Error: {str(e)}")
        print(f"Response text: {response.text}")
        return {"error": "Failed to parse AI response. Please try again.", "raw_response": response.text[:200]}
    except Exception as e:
        print(f"Gemini API Error: {str(e)}")
        return {"error": f"AI Service Error: {str(e)}"}

# --- PAGE ROUTES ---

@app.route('/')
def home():
    """Renders the home/landing page."""
    return render_template('index.html')

@app.route('/analyze')
def analyze_page():
    """Renders the Resume Analysis page."""
    return render_template('analyze.html')

@app.route('/about')
def about_page():
    """Renders the About Us page."""
    return render_template('about.html')

@app.route('/ask-ai')
def ask_ai_page():
    """Renders the General AI Chat page."""
    return render_template('ask_ai.html')

@app.route('/find-jobs')
def find_jobs_page():
    """Renders the Find Jobs page."""
    return render_template('find_jobs.html')


# --- API ROUTES: ANALYZE RESUME FLOW ---

@app.route('/analyze-jd', methods=['POST'])
def analyze_jd():
    """
    Step 1 of Analysis: Receives a Job Description (text or PDF),
    extracts key information using AI, and returns it as JSON.
    """
    jd_text = request.form.get('jd_text', '').strip()
    jd_file = request.files.get('jd_file')

    # Prioritize file upload if provided
    if jd_file and jd_file.filename.endswith('.pdf'):
        jd_text = extract_text_from_pdf(jd_file)
        if not jd_text:
            return jsonify({"error": "Failed to extract text from the uploaded PDF."}), 400

    if not jd_text:
        return jsonify({"error": "Please provide a Job Description (paste text or upload a PDF)."}), 400

    prompt = f"""
    Analyze the following Job Description and extract key information.

    Job Description:
    {jd_text[:10000]} # Limit text length to avoid token limits

    Return ONLY a valid JSON object with this exact structure (no additional text):
    {{
        "job_role": "Detected Job Title",
        "key_skills": ["Skill1", "Skill2", "Skill3", "Skill4", "Skill5", "Skill6"],
        "experience_required": "e.g., 3-5 years",
        "summary": "A brief 2-sentence summary of the core responsibilities."
    }}
    """
    analysis = call_gemini(prompt, expect_json=True)

    if "error" in analysis:
        return jsonify(analysis), 500

    return jsonify(analysis)

@app.route('/analyze-resume', methods=['POST'])
def analyze_resume():
    """
    Step 2 of Analysis: Receives the JD analysis from Step 1 and a Resume PDF.
    Compares them using AI and returns a detailed match analysis as JSON.
    """
    jd_text = request.form.get('jd_text', '').strip()
    jd_analysis_str = request.form.get('jd_analysis', '{}')
    resume_file = request.files.get('resume_file')

    if not jd_text or not resume_file:
        return jsonify({"error": "Missing information. Please provide both the JD and your Resume."}), 400

    resume_text = extract_text_from_pdf(resume_file)
    if not resume_text:
        return jsonify({"error": "Failed to extract text from your Resume PDF."}), 400

    try:
        jd_data = json.loads(jd_analysis_str)
        jd_skills = ', '.join(jd_data.get('key_skills', []))
    except Exception:
        jd_skills = "N/A"

    prompt = f"""
    You are an expert Technical Recruiter. Compare this candidate's resume against the job requirements.

    Job Title: {jd_data.get('job_role', 'N/A')}
    Key Skills Required: {jd_skills}

    Candidate Resume:
    {resume_text[:10000]} # Limit text length

    Provide a detailed, unbiased analysis. Return ONLY a valid JSON object with this exact structure:
    {{
        "match_score": 7, # An integer from 1 to 10 representing the overall fit.
        "candidate_summary": "A 2-3 sentence summary of the candidate's relevant background and key strengths for this specific role.",
        "skills_found": ["Skill from JD found in Resume", "Another skill found"],
        "missing_skills": ["Important skill from JD NOT found in resume"],
        "strengths": ["A key strength of the candidate relative to the JD"],
        "recommendations": "A concise, actionable piece of advice on how to improve their chances for this specific role (e.g., 'Highlight experience with X', 'Build a project using Y')."
    }}
    """
    analysis = call_gemini(prompt, expect_json=True)

    if "error" in analysis:
        return jsonify(analysis), 500

    return jsonify(analysis)

@app.route('/chat', methods=['POST'])
def chat():
    """
    Contextual Chat: Handles follow-up questions on the resume analysis results.
    """
    data = request.json
    user_msg = data.get('message', '').strip()
    jd_text = data.get('jd_text', '')
    resume_analysis = data.get('resume_analysis', {})

    if not user_msg:
        return jsonify({"error": "Please enter a message."}), 400

    missing_skills = resume_analysis.get('missing_skills', [])
    skills_found = resume_analysis.get('skills_found', [])
    role = resume_analysis.get('job_role', 'the role')

    prompt = f"""
    You are an AI Career Coach helping a candidate bridge their skill gaps for a specific job application.

    Context:
    - Target Role: {role}
    - Skills they have: {', '.join(skills_found)}
    - Skills they are missing: {', '.join(missing_skills)}

    User's Question: "{user_msg}"

    Provide a helpful, practical, and actionable answer in 3-4 sentences.
    Focus on giving specific advice, learning resource types (e.g., "look for a course on X"), or project ideas that would help them demonstrate the missing skills. Be encouraging but direct.
    """
    response = call_gemini(prompt, expect_json=False)
    return jsonify({"reply": response})


# --- API: GENERAL ASK-AI CHAT ---

@app.route('/ask-ai-chat', methods=['POST'])
def ask_ai_chat():
    """
    General Chat: Handles general career-related questions.
    """
    data = request.json
    user_msg = data.get('message', '').strip()

    if not user_msg:
        return jsonify({"error": "Please enter a message."}), 400

    prompt = f"""
    You are Career Compass, a friendly, professional, and direct AI career counselor.
    Your goal is to provide helpful, actionable advice to users' career questions.
    Keep your answers concise (around 3-5 sentences) and practical.

    User's Question:
    "{user_msg}"
    """
    response = call_gemini(prompt, expect_json=False)
    return jsonify({"reply": response})


# --- API: FIND JOBS FROM RESUME ---

@app.route('/api/find-jobs', methods=['POST'])
def api_find_jobs():
    """
    Analyzes a resume and suggests potential job roles and live job search links.
    """
    resume_file = request.files.get('resume_file')

    if not resume_file:
        return jsonify({"error": "Please upload your resume as a PDF."}), 400

    resume_text = extract_text_from_pdf(resume_file)
    if not resume_text:
        return jsonify({"error": "Failed to extract text from your Resume PDF."}), 400

    prompt = f"""
    You are an expert AI Career Coach. Analyze the following resume to identify the candidate's core strengths, skills, and experience level.
    Based on this profile, suggest 3 distinct types of job roles that would be a strong fit.

    Resume:
    {resume_text[:10000]} # Limit text length

    Return ONLY a valid JSON object with this exact structure:
    {{
      "profile_summary": "A concise 2-3 sentence summary of the candidate's professional profile.",
      "suggested_roles": [
        {{
          "role_title": "A specific, common job title (e.g., 'Frontend Developer', 'Data Analyst')",
          "reason": "A 1-2 sentence explanation of why this role is a good fit based on their resume.",
          "example_jobs": [
            {{
              "title": "A realistic example job title",
              "company": "A well-known company that hires for this role",
              "location": "Example location (e.g., 'Remote', 'New York, NY')",
              # Create a realistic LinkedIn search URL for this role title
              "apply_link": "https://www.linkedin.com/jobs/search/?keywords=Title+Here"
            }},
            {{
              "title": "Another example job title",
              "company": "Another company",
              "location": "Another location",
              "apply_link": "https://www.linkedin.com/jobs/search/?keywords=Title+Here"
            }}
          ]
        }},
        # ... (Repeat for 2 more role suggestions)
      ]
    }}
    """
    result = call_gemini(prompt, expect_json=True)

    if "error" in result:
        return jsonify(result), 500

    # Post-process to generate valid LinkedIn URLs
    try:
        for role in result.get('suggested_roles', []):
            role_title_encoded = role['role_title'].replace(' ', '+')
            for job in role.get('example_jobs', []):
                # Ensure the link is a valid search URL
                job['apply_link'] = f"https://www.linkedin.com/jobs/search/?keywords={role_title_encoded}"
    except Exception as e:
        print(f"Error processing job links: {e}")

    return jsonify(result)


if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)