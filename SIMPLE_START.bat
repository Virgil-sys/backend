@echo off
title Praires Africa - Simple System Start
color 0A
cls

echo.
echo ================================================
echo    PRAIRES AFRICA - STARTING SERVER
echo ================================================
echo.

cd /d "%~dp0backend"

echo [1/2] Running migrations...
.venv\Scripts\python.exe manage.py migrate

echo.
echo [2/2] Starting server...
echo.
echo ================================================
echo    SERVER IS STARTING
echo ================================================
echo.
echo Admin Panel: http://127.0.0.1:8000/admin/
echo API: http://127.0.0.1:8000/api/bookings/
echo.
echo Open booking.html in your browser to test
echo.
echo KEEP THIS WINDOW OPEN!
echo ================================================
echo.

.venv\Scripts\python.exe manage.py runserver

pause
