import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    """Configuration class for the Text-to-SQL application"""
    
    # Google AI Configuration
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    GEMINI_MODEL = "gemini-2.0-flash-exp"
    
    # Database Configuration
    DATABASE_PATH = "data/student.db"
    
    # Streamlit Configuration
    PAGE_TITLE = "Text-to-SQL Query Generator"
    PAGE_HEADER = "AI-Powered SQL Query Generator"
    
    # AI Prompt Configuration
    SYSTEM_PROMPT = """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name STUDENT and has the following columns - NAME, CLASS, 
    SECTION \n\nFor example,\nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ;
    \nExample 2 - Tell me all the students studying in Data Science class?, 
    the SQL command will be something like this SELECT * FROM STUDENT 
    where CLASS="Data Science"; 
    also the sql code should not have ``` in beginning or end and sql word in output
    """ 