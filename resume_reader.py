from pypdf import PdfReader
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()  

def extract_resume_text(pdf_path):
    reader = PdfReader(pdf_path)

    text = ""

    for page in reader.pages:
        extracted_text = page.extract_text()

        if extracted_text:
            text += extracted_text + "\n"

    return text


def find_skills(text):
    skills = [
        "Python",
        "SQL",
        "C",
        "R",
        "Machine Learning",
        "Artificial Intelligence",
        "Data Analysis",
        "Git",
        "GitHub",
        "Pandas",
        "NumPy",
        "Scikit-learn",
        "TensorFlow",
        "PyTorch",
        "FastAPI",
        "Streamlit"
    ]

    found_skills = []

    text_lower = text.lower()

    for skill in skills:
        if skill.lower() in text_lower:
            found_skills.append(skill)

    return found_skills


# Main program
pdf_path = "resume.pdf"

extracted_text = extract_resume_text(pdf_path)

skills_found = find_skills(extracted_text)

print("\n===== RESUME SKILLS =====")

if skills_found:
    for skill in skills_found:
        print("✓", skill)
else:
    print("No matching skills found.")
    # Job description skills
job_skills = [
    "Python",
    "SQL",
    "Pandas",
    "NumPy",
    "Machine Learning",
    "TensorFlow",
    "Git",
    "GitHub"
]

# Find missing skills
missing_skills = []

for skill in job_skills:
    if skill not in skills_found:
        missing_skills.append(skill)

print("\n===== JOB MATCH =====")

if missing_skills:
    print("Missing skills:")
    for skill in missing_skills:
        print("✗", skill)
else:
    print("You have all the required skills! 🎉")
    # Calculate resume match percentage

matched_skills = len([skill for skill in skills_found if skill in job_skills])
total_job_skills = len(job_skills)

match_percentage = (matched_skills / total_job_skills) * 100

print("\n===== RESUME MATCH SCORE =====")
print(f"Match Score: {match_percentage:.1f}%")
# Skill recommendations

recommendations = {
    "Pandas": "Learn Pandas for data manipulation and analysis.",
    "NumPy": "Learn NumPy for numerical computing with Python.",
    "TensorFlow": "Explore TensorFlow for deep learning and neural networks.",
    "Git": "Learn Git for version control and collaborative development.",
    "GitHub": "Practice using GitHub for project collaboration and portfolio building."
}

print("\n===== RECOMMENDATIONS =====")

if missing_skills:
    for skill in missing_skills:
        if skill in recommendations:
            print("•", recommendations[skill])
else:
    print("Your resume covers all the required skills! 🎉")
    