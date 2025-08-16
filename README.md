# 🐨 Text-to-SQL Generative AI Application

A modern, modular Streamlit application that converts natural language questions to SQL queries using Google's Gemini AI model.

## ✨ Features

- **Natural Language to SQL**: Ask questions in plain English
- **AI-Powered**: Uses Google Gemini 2.0 Flash for intelligent conversion
- **Interactive Web Interface**: Built with Streamlit
- **Database Integration**: Works with SQLite databases
- **Results Export**: Download query results as CSV

## 🏗️ Project Structure

```
Text_to_sql/
├── src/                    # Source code modules
│   ├── __init__.py
│   ├── ai_service.py      # Google Gemini AI integration
│   ├── database_service.py # Database operations
│   ├── query_processor.py # Main business logic
│   └── ui_components.py   # Streamlit UI components
├── data/                   # Data storage
│   └── student.db         # SQLite database
├── config.py              # Configuration management
├── app.py                 # Main application
├── requirements.txt       # Dependencies
└── README.md             # This file
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Google AI API key (Gemini)

### Installation

1. **Clone and setup**

   ```bash
   git clone https://github.com/yourusername/text-to-sql.git
   cd text-to-sql
   python -m venv venv
   venv\Scripts\activate  # Windows
   # source venv/bin/activate  # Unix/Mac
   pip install -r requirements.txt
   ```
2. **Configure API key**

   - Create `.env` file from `env.example`
   - Add your Google API key: `GOOGLE_API_KEY=your_key_here`
   - Get API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
3. **Run the app**

   ```bash
   streamlit run app.py
   ```

## 📊 Database Schema

The app works with a `STUDENT` table:

- `NAME` - Student names
- `CLASS` - Course/class information
- `SECTION` - Section details

## 💡 Usage Examples

Ask questions like:

- "How many students are there?"
- "Show me all students in Data Science class"
- "List students in section A"
- "Count students by class"

## 🔧 Configuration

All settings are in `config.py`:

- AI model configuration
- Database paths
- UI text and labels
- System prompts

## 🛠️ Development

### Adding Features

- **New AI Models**: Extend `AIService` class
- **New Databases**: Extend `DatabaseService` class
- **New UI**: Add methods to `UIComponents` class
- **New Logic**: Extend `QueryProcessor` class

### Module Overview

- **`AIService`**: Handles Google Gemini AI interactions
- **`DatabaseService`**: Manages database operations
- **`QueryProcessor`**: Orchestrates AI and database services
- **`UIComponents`**: Streamlit UI components

## 📝 API Reference

```python
from src.query_processor import QueryProcessor

processor = QueryProcessor()
result = processor.process_natural_language_query("How many students?")
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test locally with `streamlit run app.py`
5. Submit a pull request
