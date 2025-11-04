Write-Host ""
Write-Host "========================================"
Write-Host "  Starting Prairies Africa Backend"
Write-Host "========================================"
Write-Host ""
Write-Host "Server is starting..." -ForegroundColor Green
Write-Host ""

Set-Location $PSScriptRoot
& .\venv\Scripts\python.exe manage.py runserver

Write-Host ""
Write-Host "Server stopped!" -ForegroundColor Yellow
Read-Host "Press Enter to close"
