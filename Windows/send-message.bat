@echo off
cd ..\dist\
set /p host="Host: "
set /p title="Title: "
set /p message="Message: "
@echo off
setlocal enabledelayedexpansion
for /f "delims=" %%i in ('toaster.exe -s "%host%" "%title%" "%message%"') do set app_message=%%i
if "!app_message!" == "Notification sent." (
  echo Notification sent.
) else (
  echo Error: !app_message!
  pause
)
endlocal