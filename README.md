# 🧭 Career Compass – AI-Powered Career Assistant

Career Compass is a full-stack AI-powered web application that helps students and job-seekers navigate their career paths.  
It analyzes resumes, compares them with job descriptions, identifies skill gaps, provides personalized guidance, and suggests suitable job roles — all in one place.

The app uses **Google Gemini (via `google-generativeai`)** for:
- Resume and JD understanding
- Skill-gap analysis
- Career coaching and suggestions

---

## 🚀 Features

### 📄 Smart Resume Analysis

1. **Job Description Parsing**
   - Upload a **Job Description** as:
     - PDF file, or  
     - Plain text
   - AI extracts:
     - Job role  
     - Key skills  
     - Experience range  
     - Short summary of the role  

2. **Resume vs JD Comparison**
   - Upload your **resume (PDF)**.
   - AI compares it against the JD and returns:
     - **Match score (1–10)**
     - Skills found in your resume
     - Missing / weak skills
     - Strengths
     - Brief recommendations to improve your match

---

### 🤖 AI Career Coach Chat (Contextual)

After running a resume analysis:

- Ask the AI how to:
  - Improve missing skills
  - Choose projects to build
  - Prepare for interviews for that specific role
- The chat is **aware of your JD + resume analysis**, so responses are not generic.

---

### 💬 General Career AI Chat

- Independent “Ask AI” page.
- You can ask any career-related question, such as:
  - How to transition into a new role
  - What skills to focus on next
  - How to structure a resume or portfolio
- Works without uploading a JD or resume.

---

### 💼 Job Finder

- Upload your resume (PDF).
- The AI generates:
  - A short profile summary
  - Suggested role titles that match your background
  - Example job listings with:
    - Job title  
    - Example company  
    - Location  
    - A link to search/apply (e.g. LinkedIn search URL)

---

### ℹ️ About Page

- Explains the idea, motivation, and goals behind **Career Compass**.

---

## 🛠️ Tech Stack

**Backend**
- Python  
- Flask

**AI / ML**
- Google Gemini (`google-generativeai`)

**Document Handling**
- `pdfplumber` for extracting text from PDFs

**Frontend**
- HTML5  
- CSS3 (custom styling, responsive layout)

**Config / Environment**
- `python-dotenv` for `.env` management

---

## 📋 Prerequisites

You’ll need:

- **Python 3.7+**
- **pip**
- A **Google AI Studio API Key**  
  👉 Get one here: https://aistudio.google.com/app/apikey

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

https://github.com/Madhavansathish/Career-Compass.git
cd Career-Compass

### 2️⃣ Create a Virtual Environment (Recommended)
python -m venv venv

Activate it:

Windows:

venv\Scripts\activate


macOS / Linux:

source venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Set Up Environment Variables

Create a .env file in the project root:

GOOGLE_API_KEY=your_actual_api_key_here


Make sure this file is not committed to Git (it should be in .gitignore).

▶️ Running the Application

With the virtual environment activated:

python app.py


Open your browser and go to:

http://127.0.0.1:5000/

📂 Project Structure
career-compass/
│
├── app.py                  # Main Flask backend (routes + AI logic)
├── check.py                # Optional utility / testing script
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables (API keys, etc.)
├── .gitignore              # Ignore rules for Git
├── README.md               # Project documentation
├── venv/                   # Python virtual environment (local only)
│
├── static/                 # Static assets (images, CSS, JS if any)
│   ├── chatbot1.png
│   ├── chatbot2.png
│   ├── jobs.png
│   └── resume.png
│
└── templates/              # HTML templates for all pages
    ├── index.html          # Landing page
    ├── analyze.html        # Resume + JD analysis (3-step flow)
    ├── prepare_skill.html  # Role-based skill preparation
    ├── ask_ai.html         # General AI chat UI
    ├── find_jobs.html      # Resume-based job finder
    └── about.html          # About Us page
📸 Screenshots

These are sample UI screenshots of the running application.
🏠 Landing Page
<img width="1898" height="831" alt="Screenshot 2025-12-10 124106" src="https://github.com/user-attachments/assets/0777b451-3bcf-4fff-916a-eccac46c1a92" /><br>
📄 Resume & JD Analysis
<img width="1901" height="910" alt="Screenshot 2025-12-10 124206" src="https://github.com/user-attachments/assets/66a36e1b-5fcc-4a9b-b35f-ea4cebd89194" /><br>
🎯 Chat Bot
<img width="1914" height="904" alt="Screenshot 2025-12-10 124123" src="https://github.com/user-attachments/assets/4acb1446-fa02-4f2d-b04e-e550a1099726" /><br>
💼 Job Finder
<img width="1897" height="905" alt="Screenshot 2025-12-10 124151" src="https://github.com/user-attachments/assets/7ef24aeb-4268-41cf-8a0b-e6f3ccb5c5e9" />



