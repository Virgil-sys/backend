Write-Host "Starting Prairies Africa Backend Forever" -ForegroundColor Green

while ($true) {
    Write-Host "$(Get-Date) - Starting Django server..." -ForegroundColor Yellow
    Set-Location "C:\Users\sean\Desktop\my website\backend"
    & .\venv\Scripts\python.exe manage.py runserver 0.0.0.0:8000

    Write-Host "$(Get-Date) - Server crashed. Restarting in 5 seconds..." -ForegroundColor Red
    Start-Sleep -Seconds 5
}
