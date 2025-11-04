@echo off
echo.
echo ========================================
echo   Starting Prairies Africa Backend
echo ========================================
echo.
echo Server is starting...
echo.

REM Change to the backend directory
cd /d "C:\Users\sean\Desktop\my website\backend"

REM Check if virtual environment exists
if not exist ".venv\Scripts\python.exe" (
    echo ERROR: Virtual environment not found!
    echo Looking for: .venv\Scripts\python.exe
    echo Current directory: %CD%
    pause
    exit /b 1
)

REM Start the Django server
.venv\Scripts\python.exe manage.py runserver

echo.
echo Server stopped!
pause
