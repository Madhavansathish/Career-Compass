# Career Compass - AI-Powered Career Assistant

Career Compass is a web application designed to help job seekers navigate their career paths with confidence. It leverages the power of Google's Gemini Pro AI to provide actionable insights, resume analysis, and personalized career coaching.

## 🚀 Features

* **Smart Resume Analysis:**
    * **Step 1: Job Description Parsing:** Upload a PDF job description (JD) or paste the text. The AI extracts key information, including the job role, required skills, and experience level.
    * **Step 2: Resume vs. JD Comparison:** Upload your resume (PDF). The AI compares it against the analyzed JD to calculate a match score, identify missing skills, highlight your strengths, and provide actionable recommendations for improvement.
* **AI Career Coach Chat:**
    * After a resume analysis, engage in a contextual chat with an AI coach. Ask follow-up questions about bridging skill gaps, interview preparation, or specific advice related to the target role.
* **General AI Career Chat:**
    * Have a general career-related question? Use the "Ask AI" feature for direct, practical advice on any career topic, independent of a specific job application.
* **Job Finder:**
    * Upload your resume to get a professional profile summary and receive AI-suggested job roles that are a strong fit for your background. Each suggestion includes example companies and a direct link to search for that role on LinkedIn.
* **About Us Page:**
    * Learn more about the mission and vision behind Career Compass.

## 🛠️ Tech Stack

* **Backend:** Python, Flask
* **AI Model:** Google Gemini Pro (`gemini-1.5-flash`) via the `google-generativeai` library
* **PDF Processing:** `pdfplumber`
* **Frontend:** HTML5, CSS3 (custom styling with CSS variables for theming)
* **Environment Management:** `python-dotenv`

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

* **Python 3.7+**
* **pip** (Python package installer)
* A **Google AI Studio API Key**. You can get one [here](https://aistudio.google.com/app/apikey).

## ⚙️ Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/career-compass.git](https://github.com/your-username/career-compass.git)
    cd career-compass
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    # Activate on Windows:
    venv\Scripts\activate
    # Activate on macOS/Linux:
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up environment variables:**
    * Create a file named `.env` in the root directory of the project.
    * Add your Google API key to this file:
        ```
        GOOGLE_API_KEY=your_actual_api_key_here
        ```

## ▶️ Running the Application

1.  Make sure your virtual environment is activated.
2.  Run the Flask app:
    ```bash
    python app.py
    ```
3.  Open your web browser and navigate to:
    ```
    [http://127.0.0.1:5000/](http://127.0.0.1:5000/)
    ```

## 📂 Project Structure
career-compass/
│
├── app.py
│   └── Main Flask application file  
│       - Handles routing  
│       - Resume & JD analysis API  
│       - AI chat, skill preparation, and job finder logic  
│
├── check.py
│   └── Optional utility/testing script
│
├── requirements.txt
│   └── List of all Python dependencies required to run the project
│
├── .env
│   └── Environment variables (stores sensitive keys like GOOGLE_API_KEY)
│
├── .gitignore
│   └── Specifies files and folders ignored by Git (e.g., venv, .env)
│
├── README.md
│   └── Project documentation
│
├── venv/
│   └── Python virtual environment (auto-generated, not pushed to GitHub)
│
├── static/
│   └── All static assets (images, icons, etc.)
│
│   ├── chatbot1.png
│   ├── chatbot2.png
│   ├── jobs.png
│   └── resume.png
│
└── templates/
    └── HTML templates for all frontend pages
    │
    ├── index.html
    │   └── Landing page (Career Compass home)
    │
    ├── analyze.html
    │   └── Resume & Job Description analysis (3-step process)
    │
    ├── prepare_skill.html
    │   └── Role-based skill preparation roadmap
    │
    ├── ask_ai.html
    │   └── General AI chat interface
    │
    ├── find_jobs.html
    │   └── Resume-based job recommendation page
    │
    └── about.html
        └── About Us page


