@echo off
cd ..\dist\
set /p host="Host: "
set /p title="Title: "
set /p message="Message: "
toaster.exe -s "%host%" "%title%" "%message%"