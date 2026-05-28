# FUTURE_ML_03 — AI Resume Screening & Candidate Ranking System

An internship-level NLP and Machine Learning project that screens resumes, extracts skills, compares candidates to a job description, and ranks applicants using an ATS-style workflow.

## Overview

This project automates resume screening with NLP, semantic matching, and hybrid scoring. It is designed to simulate a real Applicant Tracking System used by recruitment teams.

## Key Capabilities

- Resume parsing and text preprocessing
- Skill extraction from resumes and job descriptions
- TF-IDF and cosine similarity scoring
- Weighted skill matching
- Candidate ranking and shortlist generation
- Skill gap analysis
- Streamlit-based reporting interface

## Tech Stack

- Python
- Pandas
- NumPy
- NLTK
- spaCy
- Scikit-learn
- Matplotlib
- Seaborn
- Streamlit

## Dataset

- Resume dataset: [Kaggle Resume Dataset](https://www.kaggle.com/datasets/snehaanbhawal/resume-dataset)
- Local file: `Resume.csv`

## Notebook

Primary notebook: `FUTURE_ML_03.ipynb`

## Project Flow

```text
Resume Dataset
    -> Preprocessing
    -> Skill Extraction
    -> Job Description Processing
    -> TF-IDF Vectorization
    -> Similarity Scoring
    -> Weighted Skill Matching
    -> Candidate Ranking
    -> Skill Gap Analysis
    -> Ranked Output
```

## Outputs

- Ranked candidate table
- Top candidate summary
- Skill distribution charts
- Match score analysis
- Exported CSV results in `outputs/`

## Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Repository Structure

```text
FUTURE_ML_03/
├── app.py
├── FUTURE_ML_03.ipynb
├── README.md
├── requirements.txt
├── Resume.csv
├── outputs/
└── screenshots/
```

## Notes

- `Resume.csv` is tracked with Git LFS.
- The repository includes notebook documentation suitable for GitHub presentation and recruiter review.

---

# Learning Outcomes

Through this project, I learned:

- Natural Language Processing (NLP)
- Resume preprocessing
- Skill extraction techniques
- TF-IDF similarity matching
- Candidate ranking systems
- Streamlit web app development
- ML project structuring

---

# Conclusion

This project demonstrates how Machine Learning and NLP can automate the resume screening process.

The system helps:

- reduce recruiter workload
- identify relevant candidates faster
- improve hiring efficiency
- provide explainable candidate evaluation

---

# Author

Harsha Vardhan

Future Interns — Machine Learning Task 3 (2026)
