﻿import re
from pdfminer.high_level import extract_text
import docx2txt
import spacy
from spacy.matcher import Matcher
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np


def extract_text_from_pdf(pdf_path):
    return extract_text(pdf_path)


def extract_text_from_docx(docx_path):
    return docx2txt.process(docx_path)


def extract_contact_number_from_resume(text):
    contact_number = None
    pattern = r"\b(?:\+?\d{1,3}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b"
    match = re.search(pattern, text)
    if match:
        contact_number = match.group()
    return contact_number


def extract_email_from_resume(text):
    email = None
    pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
    match = re.search(pattern, text)
    if match:
        email = match.group()
    return email


def extract_skills_from_resume(text, skills_list):
    skills = []
    for skill in skills_list:
        pattern = r"\b{}\b".format(re.escape(skill))
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            skills.append(skill)
    return skills


def extract_education_from_resume(text):
    education = []
    pattern = r"(?i)(?:Bsc|\bB\.\w+|\bM\.\w+|\bPh\.D\.\w+|\bBachelor(?:'s)?|\bMaster(?:'s)?|\bPh\.D)\s(?:\w+\s)*\w+"
    matches = re.findall(pattern, text)
    for match in matches:
        education.append(match.strip())
    return education


def extract_name(resume_text):
    nlp = spacy.load('en_core_web_sm')
    matcher = Matcher(nlp.vocab)
    patterns = [
        [{'POS': 'PROPN'}, {'POS': 'PROPN'}],
        [{'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}],
        [{'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}]
    ]
    for pattern in patterns:
        matcher.add('NAME', patterns=[pattern])
    doc = nlp(resume_text)
    matches = matcher(doc)
    for match_id, start, end in matches:
        span = doc[start:end]
        return span.text
    return None


def calculate_ats_score(skills_list, extracted_skills):
    total_skills = len(skills_list)
    matched_skills = len(extracted_skills)
    score = (matched_skills / total_skills) * 100
    return score


def main():
    st.title("Resume Information Extractor")
    uploaded_file = st.file_uploader("Upload a resume (PDF or DOCX format)", type=["pdf", "docx"])

    if uploaded_file is not None:
        if uploaded_file.type == "application/pdf":
            text = extract_text_from_pdf(uploaded_file)
        elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            text = extract_text_from_docx(uploaded_file)
        else:
            st.error("Unsupported file format. Please upload a PDF or DOCX file.")
            return

        st.header("Extracted Information")

        name = extract_name(text)
        st.subheader("Name")
        st.write(name if name else "Name not found")

        contact_number = extract_contact_number_from_resume(text)
        st.subheader("Contact Number")
        st.write(contact_number if contact_number else "Contact Number not found")

        email = extract_email_from_resume(text)
        st.subheader("Email")
        st.write(email if email else "Email not found")

        skills_list = ['Python', 'Data Analysis', 'Machine Learning', 'AWS', 'Time Series Analysis',
                       'Deep Learning', 'SQL', 'Natural Language Processing', 'Descriptive Statistics',
                       'Inferential Statistics', 'Docker']
        extracted_skills = extract_skills_from_resume(text, skills_list)
        st.subheader("Skills")
        st.write(extracted_skills if extracted_skills else "No skills found")

        extracted_education = extract_education_from_resume(text)
        st.subheader("Education")
        st.write(extracted_education if extracted_education else "No education information found")

        ats_score = calculate_ats_score(skills_list, extracted_skills)
        st.subheader("ATS Score")
        st.write(f"Total Score: {ats_score:.2f}%")

        # Plotting donut chart
        labels = ['Matched Skills', 'Remaining Skills']
        sizes = [ats_score, 100 - ats_score]
        fig, ax = plt.subplots()
        ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=['lightblue', 'lightgrey'])
        ax.add_artist(plt.Circle((0, 0), 0.6, color='white'))
        ax.set_title('ATS Score')
        st.pyplot(fig)


if __name__ == '__main__':
    main()

