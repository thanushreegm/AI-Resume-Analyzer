# AI Resume Analyzer

## Live Demo
Try the AI Resume Analyzer : (https://ai-resume-analyzer-upyc5kd6fczzlthjdwxnbh.streamlit.app)

A web-based Resume Analyzer built using Python and Streamlit.

## Project Overview

The AI Resume Analyzer allows users to upload a PDF resume and enter a job description. The application extracts the resume text, identifies relevant skills, compares the resume skills with the job requirements, calculates a resume match score, highlights missing skills, and provides recommendations for improvement.

## Features

- Upload PDF resumes
- Extract text from PDF files
- Detect skills from resumes
- Detect required skills from job descriptions
- Calculate Resume Match Score
- Display matching skills
- Display missing skills
- Provide learning recommendations
- Provide resume improvement suggestions
- Download an analysis report
- View extracted resume text

## Technologies Used

- Python
- Streamlit
- PyPDF
- Python-dotenv
- Regular Expressions

## How It Works

1. Upload a PDF resume.
2. Enter the required job description.
3. Click **Analyze Resume**.
4. The application extracts the resume text.
5. Skills are detected from the resume and job description.
6. Matching and missing skills are identified.
7. A match percentage is calculated.
8. Recommendations and resume improvement suggestions are displayed.

## Project Structure

```text
AI-Resume-Analyzer/
│
├── app.py
├── resume_reader.py
├── requirements.txt
├── .gitignore
└── README.md
