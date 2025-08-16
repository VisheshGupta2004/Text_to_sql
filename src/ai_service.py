import google.generativeai as genai
from config import Config

class AIService:
    """Service class for handling Google Gemini AI interactions"""
    
    def __init__(self):
        """Initialize the AI service with Google Gemini configuration"""
        if not Config.GOOGLE_API_KEY:
            raise ValueError("GOOGLE_API_KEY not found in environment variables")
        
        genai.configure(api_key=Config.GOOGLE_API_KEY)
        self.model = genai.GenerativeModel(Config.GEMINI_MODEL)
    
    def generate_sql_query(self, question: str) -> str:
        """
        Generate SQL query from natural language question using Gemini AI
        
        Args:
            question (str): Natural language question
            
        Returns:
            str: Generated SQL query
        """
        try:
            response = self.model.generate_content([Config.SYSTEM_PROMPT, question])
            return response.text.strip()
        except Exception as e:
            raise Exception(f"Error generating SQL query: {str(e)}")
    
    def validate_sql_query(self, sql_query: str) -> bool:
        """
        Basic validation of generated SQL query
        
        Args:
            sql_query (str): SQL query to validate
            
        Returns:
            bool: True if query appears valid
        """
        # Basic validation - check if it contains common SQL keywords
        sql_keywords = ['SELECT', 'FROM', 'WHERE', 'INSERT', 'UPDATE', 'DELETE']
        return any(keyword in sql_query.upper() for keyword in sql_keywords) 