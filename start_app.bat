@echo off
REM filepath: c:\Users\jstuckman\CodeProjects\credit_review_ai\start_app.bat

REM Activate virtual environment
call venv\Scripts\activate

REM Start FastAPI backend
start cmd /k "cd app && uvicorn main:app --reload"

REM Start Streamlit frontend
start cmd /k "cd app && streamlit run streamlit_app.py"

echo Both backend and frontend have been started in new windows.