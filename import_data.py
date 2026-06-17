import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
CSV_DIR = r"C:\Users\amand\OneDrive\Desktop\career_navogator\data"
engine = create_engine(DATABASE_URL)

files = {
    "students_profile": "students_profile.csv",
    "career_assessment": "career_assessment.csv",
    "skills_and_gaps": "skills_and_gaps.csv",
    "progress_tracking": "progress_tracking.csv",
    "internships": "internships.csv",
    "careers": "careers.csv",
    "scholarships": "scholarships.csv",
    "student_applications": "student_applications.csv",
}

BOOL_COLS = ["is_first_gen_college","has_laptop","has_internet","is_paid",
    "ppo_available","is_active","exam_required","is_full_scholarship",
    "covers_tuition","covers_hostel","is_renewable","first_gen_preferred",
    "rural_preferred","girl_student_preferred","resume_submitted"]

print("Data import start...\n")
for table, filename in files.items():
    path = os.path.join(CSV_DIR, filename)
    if not os.path.exists(path):
        print(f"  SKIP - {path}")
        continue
    df = pd.read_csv(path, low_memory=False)
    for col in BOOL_COLS:
        if col in df.columns:
            df[col] = df[col].map({1:True,0:False}).fillna(False)
    df.to_sql(table, engine, if_exists="replace", index=False, chunksize=1000)
    print(f"  done {table} - {len(df)} rows")
print("\nComplete!")