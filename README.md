MediExplain Pro
AI-Powered Medical Report Simplification System
Overview
MediExplain Pro is an AI-powered system that converts complex medical reports into simple, patient-friendly explanations using GroqCloud's Llama 3.3 70B model.

Problem: Over 80% of patients cannot understand their medical reports due to technical jargon.

Solution: AI-powered simplification with clinical summary, findings analysis, patient education, and doctor questions.

Features
Text input for pasting medical reports

PDF upload with text extraction (up to 10 MB)

AI analysis using Llama 3.3 70B model

Structured output with clinical summary and findings

Patient education in plain language

Auto-generated questions for doctors

HTML and PDF export options

Glassmorphism UI with CSS animations

Technology Stack
Streamlit 1.35.0 - Web framework

GroqCloud API - LLM inference (840 tokens/sec)

Llama 3.3 70B - Medical text analysis

PyPDF2 - PDF text extraction

ReportLab - PDF report generation

Python 3.11 - Core language

Prerequisites
Python 3.8 or higher

8 GB RAM (16 GB recommended)

GroqCloud API key (free at console.groq.com/keys)

Internet connection for API calls

Installation:
# Clone repository
git clone https://github.com/your-username/mediExplain-pro.git
cd mediExplain-pro

# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Mac/Linux)
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

Configuration:
Create .env file in root directory:and put api inside it

Run Application:
streamlit run app.py
