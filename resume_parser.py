import docx2txt
import PyPDF2
import os

def extract_text(uploaded_file):
    if uploaded_file.name.endswith('.pdf'):
        reader = PyPDF2.PdfReader(uploaded_file)
        return " ".join([page.extract_text() for page in reader.pages])
    elif uploaded_file.name.endswith('.docx'):
        return docx2txt.process(uploaded_file)
    return ""

def match_keywords(resume_text, role_name):
    path = os.path.join("job_keywords", role_name.replace(" ", "_") + ".txt")
    with open(path, "r") as f:
        keywords = [kw.lower() for kw in f.read().splitlines()]
    resume_text = resume_text.lower()
    matched = [kw for kw in keywords if kw in resume_text]
    score = len(matched) / len(keywords) * 100
    return score, matched
