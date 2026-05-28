# FUTURE_ML_03 — AI Resume Screening & Candidate Ranking System

## Project Overview

This project is an AI-powered Resume Screening and Candidate Ranking System developed using Machine Learning and Natural Language Processing (NLP).

The system automatically analyzes resumes, extracts important skills, compares resumes with a job description, ranks candidates based on relevance, and identifies missing skills required for a specific role.

This project was developed as part of Future Interns Machine Learning Task 3 (2026).

---

# Problem Statement

Recruiters receive hundreds of resumes for a single job role.

Manual screening:

- takes a lot of time
- may lead to inconsistent evaluations
- increases recruiter workload

This project helps automate the resume screening process using NLP and similarity-based ranking techniques.

---

# Project Objectives

The main objectives of this project are:

- Read and analyze resume data
- Perform NLP-based text preprocessing
- Extract important technical skills
- Compare resumes with job descriptions
- Rank candidates based on job relevance
- Identify missing skills
- Generate recruiter-friendly outputs

---

# Dataset Used

Dataset Name:
Resume Dataset (Kaggle)

Dataset Link:
https://www.kaggle.com/datasets/snehaanbhawal/resume-dataset

Dataset contains:

- Resume text
- Resume categories
- Multiple job domains

---

# Technologies Used

## Programming Language

- Python

## Libraries Used

- Pandas
- NumPy
- Matplotlib
- Seaborn
- NLTK
- spaCy
- Scikit-learn
- Streamlit

---

# Project Workflow

```text
Resume Dataset
       ↓
Text Preprocessing
       ↓
Skill Extraction
       ↓
Job Description Matching
       ↓
Similarity Calculation
       ↓
Candidate Ranking
       ↓
Missing Skill Analysis
       ↓
Recruiter-Friendly Output
```

---

# Steps Performed in the Project

## 1. Dataset Loading

- Loaded Resume.csv dataset
- Explored dataset structure
- Checked missing values
- Analyzed resume categories

---

## 2. Exploratory Data Analysis (EDA)

Performed:

- Dataset shape analysis
- Resume category distribution visualization
- Category frequency analysis

Visualization:

- Resume category distribution chart

---

## 3. NLP Text Preprocessing

Applied NLP preprocessing techniques:

- Lowercase conversion
- Punctuation removal
- Number removal
- Stopword removal
- Extra whitespace removal
- Lemmatization

Purpose:

- Clean resume text
- Improve similarity matching
- Reduce NLP noise

---

# Example Preprocessing

## Original Resume Text

```text
Dedicated Customer Service Manager with 15+ years of experience
```

## Cleaned Resume Text

```text
dedicated customer service manager year experience
```

---

# 4. Skill Extraction

Created a predefined technical skills database.

Extracted skills such as:

- Python
- SQL
- Machine Learning
- Deep Learning
- TensorFlow
- NLP
- AWS
- Git
- Data Analysis

Created:

- Extracted_Skills column
- Skill_Count column

---

# 5. Job Description Parsing

Created a sample job description for:
Machine Learning Engineer role.

The system extracts:

- required skills
- keywords
- technologies

from the job description.

---

# 6. Resume Similarity Matching

Used:

- TF-IDF Vectorization
- Cosine Similarity

to compare:

- resumes
- job descriptions

Generated:

- Similarity_Score for each candidate

---

# 7. Hybrid Candidate Ranking System

Implemented a hybrid ATS scoring system using:

- Similarity Score
- Skill Match Percentage

Final Score Formula:

```python
Final_Score =
(0.7 * Similarity_Score) +
(0.3 * Skill_Match_Percentage)
```

Purpose:

- Improve ranking quality
- Prioritize technically relevant resumes

---

# 8. Missing Skill Analysis

Compared:

- candidate skills
- required job description skills

Generated:

- Missing_Skills column
- Matched_Skills_Count column

Purpose:

- Identify skill gaps
- Help recruiters evaluate candidates

---

# 9. Candidate Ranking

Sorted candidates based on:

- Final Hybrid Score

Generated:

- Top ranked candidates
- Recruiter-friendly ranking table

---

# 10. Data Visualization

Created visualizations for:

- Resume category distribution
- Top extracted skills
- Top ranked candidates
- Skill match distribution

---

# 11. Streamlit Web Application

Developed a Streamlit-based ATS application.

Features:

- Upload resume dataset
- Enter job description
- Analyze resumes
- View ranked candidates
- Download CSV reports

Run App:

```bash
streamlit run app.py
```

---

# Project Output

The system generates:

- Resume similarity score
- Skill match percentage
- Final ATS ranking score
- Missing skills analysis
- Ranked candidate list

---

# Example Output

## Top Candidate

Category:
ENGINEERING

Similarity Score:
11.51%

Skill Match Percentage:
44.44%

Final Hybrid Score:
21.39%

Extracted Skills:

- Python
- SQL
- Machine Learning
- Data Analysis

Missing Skills:

- Deep Learning
- NLP
- TensorFlow
- AWS
- Git

---

# Project Structure

```text
FUTURE_ML_03/
│
├── app.py
├── Resume.csv
├── FUTURE_ML_03_Resume_Screening.ipynb
├── requirements.txt
├── README.md
│
├── outputs/
│   └── Top_Candidate_Results.csv
│
└── screenshots/
```

---

# How to Run the Project

## Step 1 — Install Libraries

```bash
pip install -r requirements.txt
```

---

## Step 2 — Run Notebook

Open:

```text
FUTURE_ML_03_Resume_Screening.ipynb
```

---

## Step 3 — Run Streamlit Application

```bash
streamlit run app.py
```

---

# Future Improvements

Possible future enhancements:

- PDF resume parsing
- Advanced NLP skill extraction
- Semantic similarity using transformers
- Better ATS dashboard
- Cloud deployment

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
