import streamlit as st
import PyPDF2
import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load API key from .env
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

# Extract text from uploaded PDF
def extract_text_from_pdf(uploaded_file):
    reader = PyPDF2.PdfReader(uploaded_file)
    return " ".join([page.extract_text() or "" for page in reader.pages])

# ATS score
def get_ats_score(resume_text, job_description):
    prompt = f"""
Given the resume and job description below, rate how well the resume matches the job description on a scale of 0 to 100.
Resume:
{resume_text}

Job Description:
{job_description}

Return only the number.
"""
    response = model.generate_content(prompt)
    return response.text.strip()

# Missing keywords
def get_missing_keywords(resume_text, job_description):
    prompt = f"""
Compare the resume and job description. List important keywords from the job description that are missing or weak in the resume.
Return the keywords as short, simple bullet points using plain words.

Resume:
{resume_text}

Job Description:
{job_description}
"""
    response = model.generate_content(prompt)
    return response.text.strip()

# Suggestions
def get_suggestions(resume_text, job_description):
    prompt = f"""
Give short and simple bullet-point suggestions to improve this resume based on the job description. Use clear and plain language for each point.

Resume:
{resume_text}

Job Description:
{job_description}
"""
    response = model.generate_content(prompt)
    return response.text.strip()

# Chatbot Q&A (limit to 10 lines)
def ask_question_to_resume_bot(question, resume_text):
    prompt = f"""
You are a helpful resume assistant. Based on the resume below, answer the user's question clearly and briefly in **10 lines or less**.

Resume:
{resume_text}

Question:
{question}
"""
    response = model.generate_content(prompt)
    return response.text.strip()

# Streamlit UI
st.set_page_config(page_title="Resume Analyzer", layout="centered")
st.title("📄 Rezoome")

st.markdown("Upload your resume and paste the job description below.")

uploaded_file = st.file_uploader("Upload your resume (PDF only)", type=["pdf"])
job_description = st.text_area("Paste the job description here", height=150)

if uploaded_file and job_description:
    resume_text = extract_text_from_pdf(uploaded_file)

    if st.button("🔍 Analyze Resume"):
        with st.spinner("Analyzing your resume..."):
            score = get_ats_score(resume_text, job_description)
            keywords = get_missing_keywords(resume_text, job_description)
            suggestions = get_suggestions(resume_text, job_description)

        st.markdown("### 🎯 ATS Score")
        st.markdown(f"**{score} / 100**")

        st.markdown("### 🧩 Missing Keywords")
        st.markdown(keywords)

        st.markdown("### 💡 Suggestions to Improve Your Resume")
        st.markdown(suggestions)

    st.markdown("### 💬 Ask a Question About Your Resume")
    user_question = st.text_input("Type your question (e.g., How can I improve my experience section?)")
    if user_question:
        with st.spinner("Generating answer..."):
            answer = ask_question_to_resume_bot(user_question, resume_text)
        st.markdown("**🤖 Answer:**")
        st.markdown(answer)
