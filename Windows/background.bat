@echo off
powershell.exe -Command "Start-Process ..\dist\toaster.exe -ArgumentList '-l' -WindowStyle Hidden"