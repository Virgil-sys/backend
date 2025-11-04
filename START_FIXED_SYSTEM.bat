@echo off
title Praires Africa - Fixed System Startup
color 0A
cls

echo.
echo ================================================
echo    PRAIRES AFRICA - STARTING FIXED SYSTEM
echo ================================================
echo.

cd /d "%~dp0backend"

echo [1/4] Running migrations for new unlimited activities system...
.venv\Scripts\python.exe manage.py makemigrations activities
.venv\Scripts\python.exe manage.py makemigrations bookings
.venv\Scripts\python.exe manage.py migrate

echo.
echo [2/4] Populating activities database...
.venv\Scripts\python.exe manage.py shell < populate_activities.py

echo.
echo [3/4] Collecting static files...
.venv\Scripts\python.exe manage.py collectstatic --noinput

echo.
echo [4/4] Starting server...
echo.
echo ================================================
echo    SERVER IS STARTING
echo ================================================
echo.
echo Admin Panel: http://127.0.0.1:8000/admin/
echo API Activities: http://127.0.0.1:8000/api/activities/
echo.
echo New Booking Page: Open booking-new.html in browser
echo.
echo KEEP THIS WINDOW OPEN!
echo ================================================
echo.

.venv\Scripts\python.exe manage.py runserver

pause
