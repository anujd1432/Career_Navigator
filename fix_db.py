from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

load_dotenv()
engine = create_engine(os.getenv("DATABASE_URL"))

bool_columns = [
    "extra_curricular",
    "leadership_roles", 
    "volunteering",
    "has_laptop",
    "has_internet",
    "is_first_gen_college",
]

with engine.connect() as conn:
    for col in bool_columns:
        try:
            sql = f"ALTER TABLE students_profile ALTER COLUMN {col} TYPE boolean USING CASE WHEN {col} = 0 THEN FALSE ELSE TRUE END"
            conn.execute(text(sql))
            conn.commit()
            print(f"Fixed: {col}")
        except Exception as e:
            conn.rollback()
            print(f"Skip {col}: {str(e)[:60]}")

print("\nDone! Ab register karo.")