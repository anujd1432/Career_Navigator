from sqlalchemy import create_engine, text 
from dotenv import load_dotenv 
import os 
 
load_dotenv() 
 
engine = create_engine(os.getenv("DATABASE_URL")) 
 
with engine.connect() as conn: 
    print("Students:    ", conn.execute(text("SELECT COUNT(*) FROM students_profile")).scalar()) 
    print("Internships: ", conn.execute(text("SELECT COUNT(*) FROM internships")).scalar()) 
    print("Careers:     ", conn.execute(text("SELECT COUNT(*) FROM careers")).scalar()) 
    print("Scholarships:", conn.execute(text("SELECT COUNT(*) FROM scholarships")).scalar()) 
