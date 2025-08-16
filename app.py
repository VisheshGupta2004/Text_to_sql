"""
Text-to-SQL Application
A Streamlit application that converts natural language questions to SQL queries using Google Gemini AI
"""

import streamlit as st
from src.query_processor import QueryProcessor
from src.ui_components import UIComponents
import pandas as pd

def main():
    """Main application function"""
    
    # Initialize UI components
    UIComponents.setup_page()
    UIComponents.render_header()
    
    # Initialize query processor
    try:
        query_processor = QueryProcessor()
        
        # Get database information for sidebar
        if 'db_info' not in st.session_state:
            st.session_state.db_info = query_processor.get_database_info()
        
        # Render sidebar
        UIComponents.render_sidebar()
        
        # Main content area
        col1, col2 = st.columns([2, 1])
        
        with col1:
            # Get user question
            question = UIComponents.render_query_input()
            
            # Submit button
            submit = UIComponents.render_submit_button()
            
            # Process query if submitted
            if submit and question:
                with st.spinner("🤖 Generating SQL query and executing..."):
                    result = query_processor.process_natural_language_query(question)
                    st.session_state.last_result = result
                
                # Render results
                if 'last_result' in st.session_state:
                    UIComponents.render_results(st.session_state.last_result)
            
            # Show error handling info
            UIComponents.render_error_handling()
        
        with col2:
            st.subheader("📚 Quick Stats")
            if st.session_state.get('db_info', {}).get('sample_data'):
                sample_data = st.session_state['db_info']['sample_data']
                total_students = len(sample_data)
                st.metric("Total Students", total_students)
                
                # Show class distribution
                if sample_data:
                    classes = [row[1] for row in sample_data if len(row) > 1]
                    if classes:
                        unique_classes = len(set(classes))
                        st.metric("Unique Classes", unique_classes)
        
        # Render footer
        UIComponents.render_footer()
        
    except Exception as e:
        st.error(f"Application Error: {str(e)}")
        st.error("Please check your configuration and try again.")

if __name__ == "__main__":
    main()


