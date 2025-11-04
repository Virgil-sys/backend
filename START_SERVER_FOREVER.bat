@echo off
title Prairies Africa Backend Server
color 0A
cls

echo.
echo ===============================================
echo    PRAIRIES AFRICA BACKEND SERVER
echo ===============================================
echo.
echo Starting server...
echo Please wait...
echo.
echo IMPORTANT: DO NOT CLOSE THIS WINDOW!
echo Keep this window open to keep server running.
echo.
echo ===============================================
echo.

cd /d "C:\Users\sean\Desktop\my website\backend"

REM Check if virtual environment exists
if not exist ".venv\Scripts\python.exe" (
    echo ERROR: Virtual environment not found!
    echo.
    echo Expected: C:\Users\sean\Desktop\my website\backend\.venv
    echo.
    echo Please check your folder structure.
    echo.
    pause
    exit /b 1
)

echo [OK] Virtual environment found
echo [OK] Starting Django server...
echo.

REM Run the server - this keeps the window open
.venv\Scripts\python.exe manage.py runserver

REM This only runs if server stops or crashes
echo.
echo ===============================================
echo    SERVER STOPPED
echo ===============================================
echo.
echo The server has stopped running.
echo.
echo If you see error messages above, please:
echo 1. Take a screenshot
echo 2. Read the error carefully
echo 3. Try running again
echo.
echo Press any key to close this window...
pause > nul
