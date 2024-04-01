@echo off
setlocal enabledelayedexpansion

REM Encontrar o PID do processo que está usando a porta 3306
for /f "tokens=5" %%a in ('netstat -ano ^| findstr :3306') do (
    set "pid=%%a"
)

REM Encerrar o processo usando o PID
if defined pid (
    taskkill /F /PID !pid!
    echo Processo com PID !pid! encerrado.
) else (
    echo Nenhum processo encontrado usando a porta 3306.
)