@echo off
ECHO Starting NanchiPlot
set "nanchif=nanchi_script.py"
set "pathnanchi=%~dp0%nanchif%"
python "%pathnanchi%"
ECHO Closing NanchiPlot
pause
