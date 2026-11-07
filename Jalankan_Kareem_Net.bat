@echo off
title Server Kareem.net - Sistem Monitoring Work Order
echo ==========================================================
echo           MENJALANKAN SERVER KAREEM.NET (FLASK)
echo ==========================================================
echo.
echo Mengaktifkan Virtual Environment (.venv)...
if not exist ".venv\Scripts\python.exe" (
    echo [ERROR] Folder .venv tidak ditemukan!
    echo Pastikan virtual environment sudah terinstal di folder ini.
    pause
    exit /b
)
echo Server sedang berjalan...
echo Silakan buka browser dan akses: http://127.0.0.1:8000
echo.
echo Tekan tombol silang (X) atau Ctrl+C pada jendela ini untuk mematikan server.
echo ----------------------------------------------------------
.venv\Scripts\python.exe app.py
pause
