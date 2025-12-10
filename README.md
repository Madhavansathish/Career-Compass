🧭 Career Compass – AI-Powered Career Assistant

Career Compass is a full-stack AI-powered web application designed to help students and job-seekers confidently navigate their career paths. It analyzes resumes, compares them with job descriptions, identifies skill gaps, generates personalized career guidance, and finds relevant job opportunities — all in one platform.

Powered by Google Gemini AI, Career Compass acts as a personal career mentor, guiding users from skill development to job application.

🚀 Features
📄 Smart Resume Analysis

Upload a Job Description (PDF or text).

AI extracts:

Job role

Required skills

Experience level

Role summary

Upload a Resume (PDF) and get:

Resume–JD Match Score (out of 10)

Extracted skills

Missing skills

Strengths

Personalized improvement suggestions

🤖 AI Career Coach Chat (Contextual)

Chat with AI after resume analysis

Ask:

How to improve weak areas

What projects to build

How to prepare for interviews

💬 General Career AI Chat

Ask any career-related question

Works independently from resume analysis

🎯 Skill Preparation Roadmap

Select from multiple predefined roles:

Data Scientist

Software Developer

Cyber Security Analyst

ML Engineer

Cloud Engineer

DevOps Engineer

Product Manager

Business Analyst

Get:

Role summary

Required skills

Topics to learn

Learning resources

Practice questions

💼 Job Finder

Upload resume and get:

AI-generated profile summary

Suggested job roles

Example companies

Direct LinkedIn job search links

ℹ️ About Page

Explains the mission and vision of Career Compass

🛠️ Tech Stack
Layer	Technology
Backend	Python, Flask
AI Model	Google Gemini (gemini-1.5-flash)
AI SDK	google-generativeai
PDF Processing	pdfplumber
Frontend	HTML5, CSS3
Environment	python-dotenv
📋 Prerequisites

Before running the project, ensure you have:

Python 3.7+

pip installed

A Google AI Studio API Key
👉 Get it here: https://aistudio.google.com/app/apikey

⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/your-username/career-compass.git
cd career-compass

2️⃣ Create Virtual Environment
python -m venv venv


Activate it:

Windows:

venv\Scripts\activate


macOS / Linux:

source venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Setup Environment Variables

Create a file named .env in the project root:

GOOGLE_API_KEY=your_actual_api_key_here

▶️ Running the Application
python app.py


Open in browser:

http://127.0.0.1:5000/

📂 Project Structure
career-compass/
│
├── app.py                  # Main Flask backend
├── check.py                # Optional utility/testing script
├── requirements.txt        # Python dependencies
├── .env                    # API keys (hidden)
├── .gitignore              # Git ignored files
├── README.md               # Documentation
├── venv/                   # Virtual environment
│
├── static/
│   ├── chatbot1.png
│   ├── chatbot2.png
│   ├── jobs.png
│   └── resume.png
│
└── templates/
    ├── index.html          # Landing Page
    ├── analyze.html        # Resume vs JD analysis
    ├── prepare_skill.html # Skill roadmap
    ├── ask_ai.html         # General AI chat
    ├── find_jobs.html      # Job finder
    └── about.html          # About page
