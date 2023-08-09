set title="Title"
set /p host="Host: "
set /p message="Message: "
python.exe ../toast.py -s "%host%" "%title%" "%message%"