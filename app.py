import streamlit as st
from resume_parser import extract_text, match_keywords
import os

st.title("Resume Screening Bot")

uploaded_file = st.file_uploader("Upload Resume (PDF or DOCX)", type=["pdf", "docx"])
job_roles = [f.replace(".txt", "").replace("_", " ") for f in os.listdir("job_keywords")]

selected_role = st.selectbox("Select Job Role", job_roles)

if uploaded_file and selected_role:
    text = extract_text(uploaded_file)
    score, matched = match_keywords(text, selected_role)

    st.subheader("Screening Result")
    st.write(f"**Match Score:** {score:.2f}%")
    st.write("**Matched Keywords:**")
    st.write(", ".join(matched))
