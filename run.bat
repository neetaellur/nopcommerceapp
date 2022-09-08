@ECHO OFF
python -m pytest -m "sanity" tests\ --browser chrome
pause