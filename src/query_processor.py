from typing import List, Tuple, Any, Dict
from src.ai_service import AIService
from src.database_service import DatabaseService

class QueryProcessor:
    """Main processor class that orchestrates AI and database operations"""
    
    def __init__(self):
        """Initialize the query processor with AI and database services"""
        self.ai_service = AIService()
        self.db_service = DatabaseService()
    
    def process_natural_language_query(self, question: str) -> Dict[str, Any]:
        """
        Process natural language question and return results
        
        Args:
            question (str): Natural language question
            
        Returns:
            Dict: Contains SQL query, results, and metadata
        """
        try:
            # Generate SQL query using AI
            sql_query = self.ai_service.generate_sql_query(question)
            
            # Validate the generated SQL
            if not self.ai_service.validate_sql_query(sql_query):
                return {
                    "success": False,
                    "error": "Generated SQL query appears invalid",
                    "sql_query": sql_query,
                    "results": None
                }
            
            # Execute the SQL query
            results = self.db_service.execute_query(sql_query)
            
            return {
                "success": True,
                "sql_query": sql_query,
                "results": results,
                "row_count": len(results),
                "question": question
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "sql_query": None,
                "results": None
            }
    
    def get_database_info(self) -> Dict[str, Any]:
        """
        Get database information including schema and sample data
        
        Returns:
            Dict: Database information
        """
        try:
            schema = self.db_service.get_table_schema()
            sample_data = self.db_service.get_sample_data()
            connection_status = self.db_service.test_connection()
            
            return {
                "connection_status": connection_status,
                "schema": schema,
                "sample_data": sample_data,
                "table_name": "STUDENT"
            }
        except Exception as e:
            return {
                "connection_status": False,
                "error": str(e),
                "schema": None,
                "sample_data": None
            } 