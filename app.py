
import streamlit as st
import pandas as pd
import re
import nltk
import spacy

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer

# -------------------------
# PAGE CONFIG
# -------------------------

st.set_page_config(
    page_title="FUTURE_ML_03 Resume Screening",
    layout="wide"
)

st.title("FUTURE_ML_03 — AI Resume Screening System")

st.write("Upload resume dataset and compare candidates against job descriptions.")

# -------------------------
# NLP SETUP
# -------------------------

nltk.download('stopwords')
nltk.download('wordnet')

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

# -------------------------
# CLEANING FUNCTION
# -------------------------

def clean_resume(text):

    text = str(text).lower()

    text = re.sub(r'http\S+', ' ', text)

    text = re.sub(r'[^a-zA-Z\s]', ' ', text)

    text = re.sub(r'\s+', ' ', text).strip()

    words = text.split()

    cleaned_words = [
        lemmatizer.lemmatize(word)
        for word in words
        if word not in stop_words
    ]

    return " ".join(cleaned_words)

# -------------------------
# SKILLS
# -------------------------

skills_db = [
    'python','java','sql','mysql','mongodb','excel',
    'power bi','tableau','machine learning',
    'deep learning','data science','nlp',
    'tensorflow','keras','pytorch','aws',
    'docker','git','html','css','javascript'
]

def extract_skills(text):

    text = text.lower()

    found = []

    for skill in skills_db:
        if skill in text:
            found.append(skill)

    return found

# -------------------------
# MODEL
# -------------------------

model = SentenceTransformer('all-MiniLM-L6-v2')

# -------------------------
# FILE UPLOAD
# -------------------------

uploaded_file = st.file_uploader(
    "Upload Resume CSV File",
    type=["csv"]
)

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    if 'Resume_str' not in df.columns:
        st.error("CSV must contain Resume_str column")
        st.stop()

    st.success("Dataset uploaded successfully.")

    job_description = st.text_area(
        "Paste Job Description Here"
    )

    if st.button("Analyze Candidates"):

        if not job_description.strip():
            st.warning("Please enter a job description")
            st.stop()

        df['Cleaned_Resume'] = df['Resume_str'].apply(clean_resume)

        df['Extracted_Skills'] = df['Cleaned_Resume'].apply(extract_skills)

        resume_texts = df['Cleaned_Resume'].tolist()

        resume_embeddings = model.encode(resume_texts)

        jd_embedding = model.encode([job_description])

        similarity_scores = cosine_similarity(
            jd_embedding,
            resume_embeddings
        )

        df['Similarity_Score'] = similarity_scores[0] * 100

        jd_skills = extract_skills(job_description)

        def missing(candidate):
            return [skill for skill in jd_skills if skill not in candidate]

        df['Missing_Skills'] = df['Extracted_Skills'].apply(missing)

        df['Matched_Skills_Count'] = df['Extracted_Skills'].apply(
            lambda x: len(set(x).intersection(set(jd_skills)))
        )

        total_required = len(jd_skills)

        if total_required > 0:
            df['Skill_Match_Percentage'] = (
                df['Matched_Skills_Count'] / total_required
            ) * 100
        else:
            df['Skill_Match_Percentage'] = 0

        df['Final_Score'] = (
            (0.75 * df['Similarity_Score']) +
            (0.25 * df['Skill_Match_Percentage'])
        )

        final_ranked_df = df.sort_values(
            by='Final_Score',
            ascending=False
        )

        st.subheader("Top Ranked Candidates")

        st.dataframe(
            final_ranked_df[
                [
                    'Category',
                    'Similarity_Score',
                    'Skill_Match_Percentage',
                    'Final_Score'
                ]
            ].head(10)
        )

        top_candidate = final_ranked_df.iloc[0]

        st.subheader("Top Candidate Analysis")

        st.write("Category:", top_candidate['Category'])
        st.write("Similarity Score:", round(top_candidate['Similarity_Score'], 2))
        st.write("Skill Match %:", round(top_candidate['Skill_Match_Percentage'], 2))
        st.write("Missing Skills:", top_candidate['Missing_Skills'])

        csv = final_ranked_df.to_csv(index=False)

        st.download_button(
            label="Download Results CSV",
            data=csv,
            file_name="ranked_candidates.csv",
            mime="text/csv"
        )
