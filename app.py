import streamlit as st
from pypdf import PdfReader
import re


# Page configuration
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

# Title
st.title("AI Resume Analyzer")
st.markdown(
    "Analyze your resume against a job description, identify skill gaps, "
    "and get personalized improvement suggestions."
)


# Resume upload
uploaded_file = st.file_uploader(
    "Upload your Resume",
    type=["pdf"]
)


# Job description
job_description = st.text_area(
    "Paste Job Description",
    height=200,
    placeholder="Paste the job requirements here..."
)


# Analyze button
if st.button("Analyze Resume"):

    if uploaded_file is None:
        st.warning("Please upload your resume.")

    elif not job_description.strip():
        st.warning("Please paste a job description.")

    else:

        # -----------------------------
        # Extract resume text
        # -----------------------------

        reader = PdfReader(uploaded_file)

        resume_text = ""

        for page in reader.pages:
            extracted_text = page.extract_text()

            if extracted_text:
                resume_text += extracted_text + "\n"


        # -----------------------------
        # Skills list
        # -----------------------------

        skills = [
            "Python",
            "SQL",
            "C",
            "C++",
            "Java",
            "R",
            "JavaScript",
            "HTML",
            "CSS",

            "Machine Learning",
            "Deep Learning",
            "Artificial Intelligence",
            "Natural Language Processing",
            "Computer Vision",
            "Data Science",
            "Data Analysis",

            "Pandas",
            "NumPy",
            "Scikit-learn",
            "TensorFlow",
            "PyTorch",
            "Matplotlib",
            "Seaborn",

            "Git",
            "GitHub",
            "Docker",
            "FastAPI",
            "Flask",
            "Streamlit",

            "MySQL",
            "PostgreSQL",
            "MongoDB",

            "Power BI",
            "Tableau",
            "Excel",

            "Communication",
            "Problem Solving",
            "Teamwork",
            "Leadership",
            "Analytical Skills",
            "Time Management",
            "Creativity",
            "Critical Thinking",
            "Adaptability",
            "Research"
        ]


        # -----------------------------
        # Detect resume skills
        # -----------------------------

        resume_lower = resume_text.lower()

        resume_skills = []

        for skill in skills:

            pattern = r"\b" + re.escape(skill.lower()) + r"\b"

            if re.search(pattern, resume_lower):
                resume_skills.append(skill)


        # -----------------------------
        # Detect job skills
        # -----------------------------

        job_lower = job_description.lower()

        job_skills = []

        for skill in skills:

            pattern = r"\b" + re.escape(skill.lower()) + r"\b"

            if re.search(pattern, job_lower):
                job_skills.append(skill)


        # -----------------------------
        # Find matching skills
        # -----------------------------

        matched_skills = []

        for skill in job_skills:

            if skill in resume_skills:
                matched_skills.append(skill)


        # -----------------------------
        # Find missing skills
        # -----------------------------

        missing_skills = []

        for skill in job_skills:

            if skill not in resume_skills:
                missing_skills.append(skill)


        # -----------------------------
        # Calculate match score
        # -----------------------------

        if len(job_skills) > 0:

            match_score = (
                len(matched_skills) / len(job_skills)
            ) * 100

        else:

            match_score = 0


        # -----------------------------
        # Success message
        # -----------------------------

        st.success("Resume analyzed successfully.")


        # -----------------------------
        # Resume Match Score
        # -----------------------------

        st.subheader("Resume Match Score")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Match Score",
                f"{match_score:.1f}%"
            )

        with col2:
            st.metric(
                "Matched Skills",
                len(matched_skills)
            )

        with col3:
            st.metric(
                "Missing Skills",
                len(missing_skills)
            )

        st.progress(
            min(int(match_score), 100)
        )


        # -----------------------------
        # Score interpretation
        # -----------------------------

        if match_score >= 80:

            st.success(
                "Strong match for this job."
            )

        elif match_score >= 60:

            st.info(
                "Good match, but some skills are missing."
            )

        else:

            st.warning(
                "Several important skills are missing. "
                "Consider improving your resume or learning the missing skills."
            )


        # -----------------------------
        # Skill Summary
        # -----------------------------

        st.subheader("Skill Summary")

        col1, col2, col3, col4 = st.columns(4)

        with col1:

            st.metric(
                "Matched Skills",
                len(matched_skills)
            )

        with col2:

            st.metric(
                "Missing Skills",
                len(missing_skills)
            )

        with col3:

            st.metric(
                "Resume Skills",
                len(resume_skills)
            )

        with col4:

            st.metric (
                "Job Skills",
                len(job_skills)
            )
            


        # -----------------------------
        # Matching and Missing Skills
        # -----------------------------

        col1, col2 = st.columns(2)

        with col1:

            st.subheader("Matching Skills")

            if matched_skills:

                for skill in matched_skills:

                    st.success(f"✓ {skill}")

            else:

                st.info("No matching skills found.")


        with col2:

            st.subheader("Missing Skills")

            if missing_skills:

                for skill in missing_skills:

                    st.warning(f"• {skill}")

            else:

                st.success("No missing skills found.")

        # -----------------------------
        # Resume Skills
        # -----------------------------

        st.subheader("Skills Found in Resume")

        if resume_skills:
            for skill in resume_skills:
                st.write(f"• {skill}")
        else:
            st.write("No recognized skills found.")

        # -----------------------------
        # Job Skills
        # -----------------------------

    st.subheader("Skills Found in Job Description")

    if job_skills:
            for skill in job_skills:
                st.write(f"• {skill}")
    else:
            st.write("No recognized skills found in the job description.")


        # -----------------------------
        # Recommendations
        # -----------------------------

    recommendations = {

            "Pandas":
                "Learn Pandas for data manipulation and analysis.",

            "NumPy":
                "Learn NumPy for numerical computing with Python.",

            "TensorFlow":
                "Explore TensorFlow for deep learning and neural networks.",

            "PyTorch":
                "Explore PyTorch for deep learning and neural networks.",

            "Scikit-learn":
                "Learn Scikit-learn for machine learning model development.",

            "FastAPI":
                "Learn FastAPI for building Python-based APIs.",

            "Git":
                "Learn Git for version control and collaborative development.",

            "GitHub":
                "Practice using GitHub for project collaboration and portfolio building.",

            "Power BI":
                "Learn Power BI to create dashboards and visualize business data.",

            "Tableau":
                "Learn Tableau to build interactive data visualizations and dashboards.",

            "Excel":
                "Improve Excel skills including formulas, data analysis, pivot tables, and charts.",

            "Analytical Skills":
                "Practice data interpretation, logical reasoning, and structured problem-solving.",

            "Communication":
                "Improve written and verbal communication through presentations and collaborative projects.",

            "Problem Solving":
                "Practice solving coding problems and real-world technical challenges.",

            "Teamwork":
                "Work on collaborative projects and practice contributing effectively within a team.",

            "Leadership":
                "Develop leadership through project ownership, teamwork, and taking responsibility for tasks.",

            "Time Management":
                "Practice planning tasks, setting priorities, and completing projects within deadlines.",

            "Creativity":
                "Develop creativity by exploring different approaches to technical and real-world problems.",

            "Critical Thinking":
                "Practice evaluating information, comparing solutions, and making logical decisions.",

            "Adaptability":
                "Learn new tools and technologies regularly and practice adapting to changing requirements.",

            "Research":
                "Develop research skills by studying technical documentation, papers, and reliable online resources."
        }


    st.subheader("Recommendations")

    if missing_skills:

            for skill in missing_skills:

                with st.expander(f"Learn: {skill}"):

                    if skill in recommendations:

                        st.write(
                            recommendations[skill]
                        )

        # -----------------------------
        # Resume Improvement Suggestions
        # -----------------------------

    st.subheader("Resume Improvement Suggestions")

    if missing_skills:

            for skill in missing_skills:

                if skill == "Pandas":

                    st.write(
                        "Pandas: Consider adding a data analysis project "
                        "that demonstrates your ability to use Pandas."
                    )

                elif skill == "NumPy":

                    st.write(
                        "NumPy: Consider adding a project where you used "
                        "NumPy for numerical or data processing tasks."
                    )

                elif skill == "Scikit-learn":

                    st.write(
                        "Scikit-learn: Add a machine learning project showing "
                        "model training, evaluation, and prediction."
                    )

                elif skill == "Git":

                    st.write(
                        "Git: Mention your Git experience and version-control "
                        "usage in your projects."
                    )

                elif skill == "Power BI":

                    st.write(
                        "Power BI: Consider adding a dashboard or data "
                        "visualization project using Power BI."
                    )

                elif skill == "Excel":

                    st.write(
                        "Excel: Mention relevant Excel skills such as formulas, "
                        "pivot tables, charts, or data analysis if you have them."
                    )

                elif skill == "Analytical Skills":

                    st.write(
                        "Analytical Skills: Highlight projects or experiences "
                        "that demonstrate data analysis, logical reasoning, "
                        "and problem-solving."
                    )

                elif skill == "Communication":

                    st.write(
                        "Communication: Highlight presentations, teamwork, "
                        "documentation, or other experiences that demonstrate "
                        "communication skills."
                    )

                elif skill == "Problem Solving":

                    st.write(
                        "Problem Solving: Highlight coding projects, "
                        "problem-solving tasks, or technical challenges "
                        "you have completed."
                    )

                elif skill == "Teamwork":

                    st.write(
                        "Teamwork: Mention collaborative projects, hackathons, "
                        "or team-based technical work."
                    )

        # -----------------------------
        # Download Analysis Report
        # -----------------------------

    report = f"""
AI RESUME ANALYZER REPORT

=========================

RESUME MATCH SCORE: {match_score:.1f}%

MATCHED SKILLS ({len(matched_skills)}):

{", ".join(matched_skills) if matched_skills else "None"}

MISSING SKILLS ({len(missing_skills)}):

{", ".join(missing_skills) if missing_skills else "None"}

SKILLS FOUND IN RESUME:

{", ".join(resume_skills) if resume_skills else "None"}

SKILLS FOUND IN JOB DESCRIPTION:

{", ".join(job_skills) if job_skills else "None"}

RECOMMENDATIONS:

"""

    for skill in missing_skills:
            report += f"\n- {skill}: {recommendations.get(skill, 'Consider learning and practicing this skill.')}"

    st.download_button(
            label="Download Analysis Report",
            data=report,
            file_name="resume_analysis_report.txt",
            mime="text/plain"
        )
        # -----------------------------
        # Extracted Resume Text
        # -----------------------------

    with st.expander("View Extracted Resume Text"):
            st.text(resume_text)