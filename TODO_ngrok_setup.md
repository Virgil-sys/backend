# Step-by-Step Guide: Connect Local Django Backend to Netlify Frontend using Ngrok

## Prerequisites
- Django backend running locally (python manage.py runserver)
- Ngrok installed (download from https://ngrok.com/download)
- Netlify site deployed with frontend code

## Step 1: Install Ngrok
1. Go to https://ngrok.com/download
2. Download and install ngrok for your operating system (Windows)
3. Sign up for a free account at ngrok.com
4. Authenticate ngrok: `ngrok config add-authtoken YOUR_AUTH_TOKEN`

## Step 2: Start Your Django Backend Locally
```bash
cd backend
python manage.py runserver 8000
```
Backend should be running on http://127.0.0.1:8000

## Step 3: Start Ngrok Tunnel
```bash
ngrok http 8000
```
This will create a secure tunnel to your local port 8000.

## Step 4: Get Your Ngrok URL
Ngrok will display something like:
```
Forwarding    https://abc123.ngrok.io -> http://localhost:8000
```
Copy the HTTPS URL (e.g., https://abc123.ngrok.io)

## Step 5: Update Frontend API_BASE_URL
In `assets/js/main.js`, change:
```javascript
const API_BASE_URL = 'https://cruel-towns-work.loca.lt'; // old
const API_BASE_URL = 'https://abc123.ngrok.io'; // new ngrok URL
```

## Step 6: Update Django Settings for CORS and ALLOWED_HOSTS
In `backend/backend/settings.py`, add your ngrok URL:

```python
ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    'abc123.ngrok.io',  # Add your ngrok URL here
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "https://your-netlify-site.netlify.app",  # Your Netlify URL
    "https://abc123.ngrok.io",  # Add your ngrok URL here
]
```

## Step 7: Test the Connection
1. Deploy frontend to Netlify with updated API_BASE_URL
2. Test API endpoints:
   - Visit: https://abc123.ngrok.io/api/bookings/create/
   - Visit: https://abc123.ngrok.io/api/payments/bank-details/
3. Check browser console for CORS errors
4. Test full booking flow from Netlify frontend

## Keeping Your Server Running Forever

### Option 1: Using a Batch Script (Windows)
Create a new file called `START_SERVER_FOREVER.bat` in your project root:

```batch
@echo off
echo ========================================
echo Starting Prairies Africa Backend Forever
echo ========================================
echo.

:loop
echo [%date% %time%] Starting Django server...
cd /d "C:\Users\sean\Desktop\my website\backend"
.\venv\Scripts\python.exe manage.py runserver 0.0.0.0:8000

echo [%date% %time%] Server crashed or stopped. Restarting in 5 seconds...
timeout /t 5 /nobreak > nul
goto loop
```

**To run forever:**
1. Double-click `START_SERVER_FOREVER.bat`
2. The server will automatically restart if it crashes
3. Close the command window to stop

### Option 2: Using PowerShell Script
Create `START_SERVER_FOREVER.ps1`:

```powershell
Write-Host "Starting Prairies Africa Backend Forever" -ForegroundColor Green

while ($true) {
    Write-Host "$(Get-Date) - Starting Django server..." -ForegroundColor Yellow
    Set-Location "C:\Users\sean\Desktop\my website\backend"
    & .\venv\Scripts\python.exe manage.py runserver 0.0.0.0:8000

    Write-Host "$(Get-Date) - Server crashed. Restarting in 5 seconds..." -ForegroundColor Red
    Start-Sleep -Seconds 5
}
```

**To run forever:**
```powershell
.\START_SERVER_FOREVER.ps1
```

### Option 3: Using Process Manager (Recommended for Production)
Install PM2 globally:
```bash
npm install -g pm2
```

Create ecosystem.config.js:
```javascript
module.exports = {
  apps: [{
    name: 'prairies-backend',
    script: 'manage.py',
    args: 'runserver 0.0.0.0:8000',
    cwd: 'C:/Users/sean/Desktop/my website/backend',
    interpreter: './venv/Scripts/python.exe',
    instances: 1,
    autorestart: true,
    watch: false,
    max_memory_restart: '1G',
    env: {
      DJANGO_SETTINGS_MODULE: 'backend.settings'
    }
  }]
}
```

**Commands:**
```bash
# Start
pm2 start ecosystem.config.js

# Stop
pm2 stop prairies-backend

# Restart
pm2 restart prairies-backend

# View status
pm2 status

# View logs
pm2 logs prairies-backend
```

## Troubleshooting
- If CORS errors: Double-check CORS_ALLOWED_ORIGINS in settings.py
- If connection fails: Ensure ngrok tunnel is active and URL is correct
- Ngrok free tier has limitations; consider paid plan for production

## Tasks to Complete
- [x] Install ngrok on the system (used localtunnel instead)
- [x] Run Django backend locally (python manage.py runserver)
- [x] Start ngrok tunnel (localtunnel used: https://bumpy-women-fly.loca.lt)
- [x] Get the ngrok public URL (https://bumpy-women-fly.loca.lt)
- [x] Update assets/js/main.js API_BASE_URL to ngrok URL
- [x] Update backend/backend/settings.py ALLOWED_HOSTS and CORS_ALLOWED_ORIGINS with ngrok URL
- [ ] Test API endpoints with ngrok URL
- [ ] Verify frontend-backend connection works
