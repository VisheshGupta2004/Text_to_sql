import sqlite3
import os
from typing import List, Tuple, Any
from config import Config

class DatabaseService:
    """Service class for handling database operations"""
    
    def __init__(self, db_path: str = None):
        """
        Initialize database service
        
        Args:
            db_path (str): Path to the database file
        """
        self.db_path = db_path or Config.DATABASE_PATH
        self._ensure_data_directory()
    
    def _ensure_data_directory(self):
        """Ensure the data directory exists"""
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
    
    def execute_query(self, sql_query: str) -> List[Tuple[Any, ...]]:
        """
        Execute SQL query and return results
        
        Args:
            sql_query (str): SQL query to execute
            
        Returns:
            List[Tuple]: Query results
        """
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute(sql_query)
            rows = cursor.fetchall()
            conn.commit()
            conn.close()
            return rows
        except sqlite3.Error as e:
            raise Exception(f"Database error: {str(e)}")
        except Exception as e:
            raise Exception(f"Error executing query: {str(e)}")
    
    def get_table_schema(self, table_name: str = "STUDENT") -> List[Tuple[str, str, str, str, str, str]]:
        """
        Get table schema information
        
        Args:
            table_name (str): Name of the table
            
        Returns:
            List[Tuple]: Table schema information
        """
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute(f"PRAGMA table_info({table_name})")
            schema = cursor.fetchall()
            conn.close()
            return schema
        except sqlite3.Error as e:
            raise Exception(f"Error getting table schema: {str(e)}")
    
    def get_sample_data(self, table_name: str = "STUDENT", limit: int = 5) -> List[Tuple[Any, ...]]:
        """
        Get sample data from table
        
        Args:
            table_name (str): Name of the table
            limit (int): Number of rows to return
            
        Returns:
            List[Tuple]: Sample data
        """
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM {table_name} LIMIT {limit}")
            rows = cursor.fetchall()
            conn.close()
            return rows
        except sqlite3.Error as e:
            raise Exception(f"Error getting sample data: {str(e)}")
    
    def test_connection(self) -> bool:
        """
        Test database connection
        
        Returns:
            bool: True if connection successful
        """
        try:
            conn = sqlite3.connect(self.db_path)
            conn.close()
            return True
        except Exception:
            return False 