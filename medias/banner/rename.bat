@echo off
setlocal enabledelayedexpansion
set count=0
for /f %%i in ('dir /b *.jpg') do (
    set /a count+=1
    echo 改名：%%i !count!
    rename %%i !count!.jpg
)