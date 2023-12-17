@echo off
title clock
@mode con cols=30 lines=7
color 03
: main
cls
echo.
echotime: %time%
echo.
echoDAte: %date%
echo.
ping -n 2 0.0.0.0>nul
goto main