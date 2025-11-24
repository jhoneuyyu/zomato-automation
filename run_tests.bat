@echo off
echo Running tests...
".venv\Scripts\pytest.exe" tests\test_spot.py --html=report.html
pause
