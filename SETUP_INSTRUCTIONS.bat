@echo off
title Praires Africa - Quick Setup
color 0A
cls

echo.
echo ================================================
echo    PRAIRES AFRICA BOOKING SYSTEM - SETUP
echo ================================================
echo.
echo This script will help you set up the system.
echo.
pause

cd /d "%~dp0backend"

echo.
echo [1/5] Installing dependencies...
echo.
.venv\Scripts\python.exe -m pip install -r requirements.txt

echo.
echo [2/5] Running database migrations...
echo.
.venv\Scripts\python.exe manage.py makemigrations
.venv\Scripts\python.exe manage.py migrate

echo.
echo [3/5] Collecting static files...
echo.
.venv\Scripts\python.exe manage.py collectstatic --noinput

echo.
echo [4/5] Creating admin user...
echo.
echo Please enter admin credentials:
.venv\Scripts\python.exe manage.py createsuperuser

echo.
echo [5/5] Setup complete!
echo.
echo ================================================
echo    NEXT STEPS
echo ================================================
echo.
echo 1. Configure email settings in backend\.env
echo 2. Update bank details in bookings\views.py
echo 3. Start server with START_SERVER_FOREVER.bat
echo 4. Open index.html in your browser
echo 5. Access admin panel at http://127.0.0.1:8000/admin/
echo.
echo ================================================
echo.
pause
