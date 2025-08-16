import streamlit as st
from typing import List, Tuple, Any, Dict
from config import Config

class UIComponents:
    """UI components for the Streamlit application"""
    
    @staticmethod
    def setup_page():
        """Setup Streamlit page configuration"""
        st.set_page_config(
            page_title=Config.PAGE_TITLE,
            page_icon="🐨",
            layout="wide",
            initial_sidebar_state="expanded"
        )
    
    @staticmethod
    def render_header():
        """Render the main header"""
        st.title(Config.PAGE_HEADER)
        st.markdown("---")
    
    @staticmethod
    def render_sidebar():
        """Render the sidebar with database information"""
        with st.sidebar:
            st.header("📊 Database Information")
            
            # Database status
            st.subheader("Connection Status")
            if st.session_state.get('db_info', {}).get('connection_status'):
                st.success("✅ Connected")
            else:
                st.error("❌ Not Connected")
            
            # Table schema
            st.subheader("Table Schema")
            db_info = st.session_state.get('db_info', {})
            if db_info.get('schema'):
                for col in db_info['schema']:
                    st.text(f"• {col[1]} ({col[2]})")
            
            # Sample data
            st.subheader("Sample Data")
            if db_info.get('sample_data'):
                for row in db_info['sample_data'][:3]:  # Show first 3 rows
                    st.text(f"• {row}")
    
    @staticmethod
    def render_query_input() -> str:
        """Render the query input section"""
        st.subheader("🔍 Ask a Question")
        st.markdown("Ask questions about students in natural language:")
        
        examples = [
            "How many students are there?",
            "Show me all students in Data Science class",
            "What are the different sections available?",
            "List students in section A"
        ]
        
        with st.expander("💡 Example Questions"):
            for example in examples:
                st.text(f"• {example}")
        
        question = st.text_input(
            "Your question:",
            key="question_input",
            placeholder="e.g., How many students are in Data Science class?"
        )
        
        return question
    
    @staticmethod
    def render_submit_button() -> bool:
        """Render the submit button"""
        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            submit = st.button("🚀 Generate & Execute Query", type="primary")
        return submit
    
    @staticmethod
    def render_results(result: Dict[str, Any]):
        """Render the query results"""
        if result['success']:
            st.subheader("✅ Query Results")
            
            # Show the generated SQL
            with st.expander("🔍 Generated SQL Query"):
                st.code(result['sql_query'], language="sql")
            
            # Show results
            st.subheader(f"📊 Results ({result['row_count']} rows)")
            
            if result['results']:
                # Convert to DataFrame for better display
                import pandas as pd
                df = pd.DataFrame(result['results'], columns=['Name', 'Class', 'Section'])
                st.dataframe(df, use_container_width=True)
                
                # Download button
                csv = df.to_csv(index=False)
                st.download_button(
                    label="📥 Download Results as CSV",
                    data=csv,
                    file_name="query_results.csv",
                    mime="text/csv"
                )
            else:
                st.info("No results returned from the query.")
        else:
            st.error("❌ Error Processing Query")
            st.error(result['error'])
    
    @staticmethod
    def render_error_handling():
        """Render error handling information"""
        with st.expander("⚠️ Troubleshooting"):
            st.markdown("""
            **Common Issues:**
            - Make sure your Google API key is set in the `.env` file
            - Ensure the database file exists and is accessible
            - Check that your question is clear and specific
            
            **API Key Setup:**
            1. Get your API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
            2. Create a `.env` file in the project root
            3. Add: `GOOGLE_API_KEY=your_api_key_here`
            """)
    
    @staticmethod
    def render_footer():
        """Render the footer"""
        st.markdown("---")
        st.markdown(
            "Built with ❤️ using Streamlit and Google Gemini AI | "
            "[GitHub](https://github.com/yourusername/text-to-sql)"
        ) 