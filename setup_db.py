# """
# Career Navigator — PostgreSQL Full Setup
# Run: python setup_db.py
# """

# import os
# import time
# import pandas as pd
# from sqlalchemy import create_engine, text
# from sqlalchemy.exc import SQLAlchemyError
# from dotenv import load_dotenv

# load_dotenv()

# DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:yourpassword@localhost:5432/career_navigator")
# CSV_DIR = os.getenv("CSV_DIR", "./data")

# SCHEMAS = {

# "students_profile": """
# CREATE TABLE IF NOT EXISTS students_profile (
#     student_id          VARCHAR(10) PRIMARY KEY,
#     full_name           VARCHAR(100),
#     gender              VARCHAR(10),
#     date_of_birth       DATE,
#     age                 INTEGER,
#     email               VARCHAR(150),
#     phone               VARCHAR(15),
#     city                VARCHAR(60),
#     state               VARCHAR(60),
#     religion            VARCHAR(30),
#     category            VARCHAR(20),
#     annual_family_income VARCHAR(20),
#     parent_education    VARCHAR(30),
#     parent_occupation   VARCHAR(40),
#     is_first_gen_college BOOLEAN DEFAULT FALSE,
#     school_type         VARCHAR(30),
#     twelfth_stream      VARCHAR(30),
#     twelfth_percentage  NUMERIC(5,2),
#     twelfth_year        INTEGER,
#     college_type        VARCHAR(50),
#     current_degree      VARCHAR(30),
#     current_branch      VARCHAR(60),
#     current_year        INTEGER,
#     current_cgpa        NUMERIC(4,2),
#     learning_style      VARCHAR(30),
#     has_laptop          BOOLEAN DEFAULT FALSE,
#     has_internet        BOOLEAN DEFAULT FALSE,
#     hours_study_per_day INTEGER,
#     extra_curricular    BOOLEAN DEFAULT FALSE,
#     leadership_roles    BOOLEAN DEFAULT FALSE,
#     volunteering        BOOLEAN DEFAULT FALSE,
#     created_at          TIMESTAMP DEFAULT CURRENT_TIMESTAMP
# );
# """,

# "career_assessment": """
# CREATE TABLE IF NOT EXISTS career_assessment (
#     assessment_id           SERIAL PRIMARY KEY,
#     student_id              VARCHAR(10),
#     interest_score          NUMERIC(5,2),
#     aptitude_score          NUMERIC(5,2),
#     personality_type        VARCHAR(10),
#     logical_reasoning       NUMERIC(5,2),
#     verbal_ability          NUMERIC(5,2),
#     numerical_ability       NUMERIC(5,2),
#     spatial_ability         NUMERIC(5,2),
#     creativity_score        NUMERIC(5,2),
#     leadership_score        NUMERIC(5,2),
#     communication_score     NUMERIC(5,2),
#     risk_appetite           VARCHAR(10),
#     work_preference         VARCHAR(30),
#     career_readiness_score  NUMERIC(5,2),
#     recommended_career_1    VARCHAR(80),
#     recommended_career_2    VARCHAR(80),
#     recommended_career_3    VARCHAR(80),
#     career_suitability_score_1 NUMERIC(5,2),
#     career_suitability_score_2 NUMERIC(5,2),
#     career_suitability_score_3 NUMERIC(5,2),
#     assessed_at             TIMESTAMP DEFAULT CURRENT_TIMESTAMP
# );
# """,

# "skills_and_gaps": """
# CREATE TABLE IF NOT EXISTS skills_and_gaps (
#     skill_id             SERIAL PRIMARY KEY,
#     student_id           VARCHAR(10),
#     technical_skills     TEXT,
#     soft_skills          TEXT,
#     domain_knowledge     TEXT,
#     total_skills_count   INTEGER,
#     certifications       TEXT,
#     internship_done      BOOLEAN DEFAULT FALSE,
#     internship_months    INTEGER DEFAULT 0,
#     projects_built       INTEGER DEFAULT 0,
#     github_profile       BOOLEAN DEFAULT FALSE,
#     linkedin_profile     BOOLEAN DEFAULT FALSE,
#     target_career        VARCHAR(80),
#     skills_matched       INTEGER,
#     skills_missing       INTEGER,
#     skill_gap_count      INTEGER,
#     improvement_priority VARCHAR(60),
#     updated_at           TIMESTAMP DEFAULT CURRENT_TIMESTAMP
# );
# """,

# "progress_tracking": """
# CREATE TABLE IF NOT EXISTS progress_tracking (
#     progress_id              SERIAL PRIMARY KEY,
#     student_id               VARCHAR(10),
#     courses_completed        INTEGER DEFAULT 0,
#     courses_in_progress      INTEGER DEFAULT 0,
#     total_learning_hours     INTEGER DEFAULT 0,
#     last_assessment_date     DATE,
#     assessment_attempts      INTEGER DEFAULT 0,
#     resume_score             NUMERIC(5,2),
#     resume_uploaded          BOOLEAN DEFAULT FALSE,
#     mock_interviews_taken    INTEGER DEFAULT 0,
#     avg_mock_interview_score NUMERIC(5,2),
#     scholarships_applied     INTEGER DEFAULT 0,
#     scholarships_received    INTEGER DEFAULT 0,
#     jobs_applied             INTEGER DEFAULT 0,
#     placement_status         VARCHAR(30),
#     monthly_progress_pct     NUMERIC(5,2),
#     mentor_assigned          BOOLEAN DEFAULT FALSE,
#     community_posts          INTEGER DEFAULT 0,
#     login_streak_days        INTEGER DEFAULT 0,
#     engagement_level         VARCHAR(20),
#     updated_at               TIMESTAMP DEFAULT CURRENT_TIMESTAMP
# );
# """,

# "internships": """
# CREATE TABLE IF NOT EXISTS internships (
#     internship_id          VARCHAR(10) PRIMARY KEY,
#     company_name           VARCHAR(100),
#     company_type           VARCHAR(20),
#     role_title             VARCHAR(100),
#     domain                 VARCHAR(50),
#     location               VARCHAR(60),
#     mode                   VARCHAR(20),
#     duration_months        INTEGER,
#     stipend_per_month      INTEGER DEFAULT 0,
#     is_paid                BOOLEAN DEFAULT FALSE,
#     ppo_available          BOOLEAN DEFAULT FALSE,
#     min_cgpa               NUMERIC(4,2),
#     eligible_streams       VARCHAR(60),
#     eligible_degrees       VARCHAR(60),
#     eligible_years         VARCHAR(60),
#     skills_required        TEXT,
#     skills_preferred       TEXT,
#     openings               INTEGER,
#     applications_received  INTEGER,
#     selection_process      VARCHAR(100),
#     application_deadline   DATE,
#     start_date             DATE,
#     description            TEXT,
#     perks                  TEXT,
#     industry_sector        VARCHAR(50),
#     experience_level       VARCHAR(30),
#     avg_match_score        NUMERIC(5,2),
#     total_placed_last_year INTEGER,
#     rating                 NUMERIC(3,1),
#     is_active              BOOLEAN DEFAULT TRUE,
#     created_at             TIMESTAMP DEFAULT CURRENT_TIMESTAMP
# );
# """,

# "careers": """
# CREATE TABLE IF NOT EXISTS careers (
#     career_id                 VARCHAR(10) PRIMARY KEY,
#     career_title              VARCHAR(100),
#     domain                    VARCHAR(50),
#     employment_type           VARCHAR(20),
#     avg_salary_lpa_entry      NUMERIC(6,2),
#     avg_salary_lpa_mid        NUMERIC(6,2),
#     avg_salary_lpa_senior     NUMERIC(6,2),
#     growth_rate_pct           INTEGER,
#     demand_level              VARCHAR(20),
#     job_market_size           VARCHAR(20),
#     top_hiring_states         TEXT,
#     top_hiring_companies      TEXT,
#     min_education             VARCHAR(30),
#     required_degrees          VARCHAR(100),
#     required_skills           TEXT,
#     preferred_certifications  TEXT,
#     years_to_senior           INTEGER,
#     exam_required             BOOLEAN DEFAULT FALSE,
#     exam_name                 VARCHAR(50),
#     difficulty_level          VARCHAR(20),
#     work_life_balance         VARCHAR(20),
#     job_security              VARCHAR(20),
#     remote_work_possible      BOOLEAN DEFAULT FALSE,
#     suitable_for_introvert    BOOLEAN DEFAULT FALSE,
#     suitable_for_extrovert    BOOLEAN DEFAULT FALSE,
#     suitable_for_analytical   BOOLEAN DEFAULT FALSE,
#     suitable_for_creative     BOOLEAN DEFAULT FALSE,
#     suitable_streams          VARCHAR(30),
#     min_twelfth_pct           INTEGER,
#     min_cgpa                  NUMERIC(4,2),
#     avg_placement_time_months INTEGER,
#     total_jobs_india_2024     INTEGER,
#     international_scope       BOOLEAN DEFAULT FALSE,
#     starting_age              INTEGER,
#     description               TEXT,
#     created_at                TIMESTAMP DEFAULT CURRENT_TIMESTAMP
# );
# """,

# "scholarships": """
# CREATE TABLE IF NOT EXISTS scholarships (
#     scholarship_id          VARCHAR(10) PRIMARY KEY,
#     scholarship_name        VARCHAR(200),
#     sponsoring_body         VARCHAR(50),
#     scholarship_type        VARCHAR(40),
#     amount_per_year         INTEGER,
#     is_full_scholarship     BOOLEAN DEFAULT FALSE,
#     covers_tuition          BOOLEAN DEFAULT FALSE,
#     covers_hostel           BOOLEAN DEFAULT FALSE,
#     covers_books            BOOLEAN DEFAULT FALSE,
#     monthly_stipend         INTEGER DEFAULT 0,
#     eligible_categories     VARCHAR(60),
#     eligible_gender         VARCHAR(10),
#     eligible_streams        VARCHAR(40),
#     eligible_degrees        VARCHAR(60),
#     eligible_states         VARCHAR(100),
#     min_twelfth_percentage  INTEGER,
#     min_family_income_limit INTEGER,
#     max_family_income_limit INTEGER,
#     min_cgpa                NUMERIC(4,2),
#     is_renewable            BOOLEAN DEFAULT FALSE,
#     renewal_criteria        VARCHAR(100),
#     application_start_date  DATE,
#     application_deadline    DATE,
#     result_date             DATE,
#     total_seats             INTEGER,
#     applications_last_year  INTEGER,
#     selection_criteria      VARCHAR(60),
#     documents_required      TEXT,
#     official_website        VARCHAR(100),
#     helpline                VARCHAR(20),
#     is_active               BOOLEAN DEFAULT TRUE,
#     first_gen_preferred     BOOLEAN DEFAULT FALSE,
#     rural_preferred         BOOLEAN DEFAULT FALSE,
#     girl_student_preferred  BOOLEAN DEFAULT FALSE,
#     difficulty_to_get       VARCHAR(20),
#     avg_processing_days     INTEGER,
#     description             TEXT,
#     created_at              TIMESTAMP DEFAULT CURRENT_TIMESTAMP
# );
# """,

# "student_applications": """
# CREATE TABLE IF NOT EXISTS student_applications (
#     application_id   VARCHAR(10) PRIMARY KEY,
#     student_id       VARCHAR(10),
#     opportunity_type VARCHAR(20),
#     opportunity_id   VARCHAR(10),
#     applied_date     DATE,
#     status           VARCHAR(30),
#     match_score      NUMERIC(5,2),
#     resume_submitted BOOLEAN DEFAULT FALSE,
#     cover_letter     BOOLEAN DEFAULT FALSE,
#     referred_by      VARCHAR(30),
#     rejection_reason VARCHAR(60),
#     feedback         VARCHAR(60),
#     created_at       TIMESTAMP DEFAULT CURRENT_TIMESTAMP
# );
# """,
# }

# INDEXES = [
#     "CREATE INDEX IF NOT EXISTS idx_students_category   ON students_profile(category);",
#     "CREATE INDEX IF NOT EXISTS idx_students_stream     ON students_profile(twelfth_stream);",
#     "CREATE INDEX IF NOT EXISTS idx_students_state      ON students_profile(state);",
#     "CREATE INDEX IF NOT EXISTS idx_students_first_gen  ON students_profile(is_first_gen_college);",
#     "CREATE INDEX IF NOT EXISTS idx_assessment_student  ON career_assessment(student_id);",
#     "CREATE INDEX IF NOT EXISTS idx_assessment_career1  ON career_assessment(recommended_career_1);",
#     "CREATE INDEX IF NOT EXISTS idx_skills_student      ON skills_and_gaps(student_id);",
#     "CREATE INDEX IF NOT EXISTS idx_progress_student    ON progress_tracking(student_id);",
#     "CREATE INDEX IF NOT EXISTS idx_progress_placement  ON progress_tracking(placement_status);",
#     "CREATE INDEX IF NOT EXISTS idx_internship_domain   ON internships(domain);",
#     "CREATE INDEX IF NOT EXISTS idx_internship_active   ON internships(is_active);",
#     "CREATE INDEX IF NOT EXISTS idx_career_domain       ON careers(domain);",
#     "CREATE INDEX IF NOT EXISTS idx_career_demand       ON careers(demand_level);",
#     "CREATE INDEX IF NOT EXISTS idx_scholarship_firstgen ON scholarships(first_gen_preferred);",
#     "CREATE INDEX IF NOT EXISTS idx_scholarship_active  ON scholarships(is_active);",
#     "CREATE INDEX IF NOT EXISTS idx_applications_student ON student_applications(student_id);",
#     "CREATE INDEX IF NOT EXISTS idx_applications_status ON student_applications(status);",
# ]

# CSV_MAPPING = {
#     "students_profile":     "students_profile.csv",
#     "career_assessment":    "career_assessment.csv",
#     "skills_and_gaps":      "skills_and_gaps.csv",
#     "progress_tracking":    "progress_tracking.csv",
#     "internships":          "internships.csv",
#     "careers":              "careers.csv",
#     "scholarships":         "scholarships.csv",
#     "student_applications": "student_applications.csv",
# }

# BOOL_COLS = [
#     "is_first_gen_college","has_laptop","has_internet","extra_curricular",
#     "leadership_roles","volunteering","internship_done","github_profile",
#     "linkedin_profile","resume_uploaded","mentor_assigned","is_paid",
#     "ppo_available","is_active","exam_required","remote_work_possible",
#     "suitable_for_introvert","suitable_for_extrovert","suitable_for_analytical",
#     "suitable_for_creative","international_scope","is_full_scholarship",
#     "covers_tuition","covers_hostel","covers_books","is_renewable",
#     "first_gen_preferred","rural_preferred","girl_student_preferred",
#     "resume_submitted","cover_letter",
# ]

# def setup():
#     print("\n" + "="*55)
#     print("  Career Navigator — PostgreSQL Setup")
#     print("="*55)

#     print(f"\nConnecting to: {DATABASE_URL[:50]}...")
#     try:
#         engine = create_engine(DATABASE_URL, echo=False)
#         with engine.connect() as conn:
#             conn.execute(text("SELECT 1"))
#         print("  ✓ Database connected!\n")
#     except Exception as e:
#         print(f"\n  ✗ Connection failed: {e}")
#         print("\n  Check karo:")
#         print("  1. PostgreSQL service chal rahi hai?")
#         print("  2. .env mein password sahi hai?")
#         print("  3. career_navigator database bana hua hai pgAdmin mein?")
#         return

#     # 1. Create tables
#     print("[1/3] Creating tables...")
#     with engine.connect() as conn:
#         for table, ddl in SCHEMAS.items():
#             conn.execute(text(ddl))
#             conn.commit()
#             print(f"  ✓ {table}")

#     # 2. Load CSVs
#     print("\n[2/3] Loading CSV data...")
#     for table, csv_file in CSV_MAPPING.items():
#         csv_path = os.path.join(CSV_DIR, csv_file)
#         if not os.path.exists(csv_path):
#             print(f"  ⚠ SKIP — {csv_file} not found in {CSV_DIR}")
#             continue
#         try:
#             t0 = time.time()
#             df = pd.read_csv(csv_path, low_memory=False)

#             for col in BOOL_COLS:
#                 if col in df.columns:
#                     df[col] = df[col].map({
#                         1: True, 0: False,
#                         "1": True, "0": False,
#                         True: True, False: False
#                     }).fillna(False)

#             df.to_sql(table, engine, if_exists="append",
#                       index=False, method="multi", chunksize=2000)
#             elapsed = time.time() - t0
#             print(f"  ✓ {table:35s} {len(df):>8,} rows  ({elapsed:.1f}s)")
#         except SQLAlchemyError as e:
#             print(f"  ✗ {table}: {e}")

#     # 3. Indexes
#     print("\n[3/3] Creating indexes...")
#     with engine.connect() as conn:
#         for idx_sql in INDEXES:
#             try:
#                 conn.execute(text(idx_sql))
#                 conn.commit()
#             except Exception:
#                 pass
#     print(f"  ✓ {len(INDEXES)} indexes created")

#     # 4. Verify
#     print("\n─── Verification ─────────────────────────────────────")
#     with engine.connect() as conn:
#         for table in SCHEMAS.keys():
#             try:
#                 count = conn.execute(text(f"SELECT COUNT(*) FROM {table}")).scalar()
#                 print(f"  {table:35s} {count:>8,} rows")
#             except Exception as e:
#                 print(f"  {table}: ERROR — {e}")

#     print("\n✅ Database setup complete!\n")

# if __name__ == "__main__":
#     setup()


from app.database import engine, Base
from app.models import Student

Base.metadata.create_all(bind=engine)

print("Tables Created Successfully")