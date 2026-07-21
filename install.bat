@echo off
title Install Meridian-X
echo ==========================================================================
echo                 🪐 Downloading & Installing Meridian-X                    
echo ==========================================================================
echo.
powershell -ExecutionPolicy Bypass -Command "irm https://raw.githubusercontent.com/Aryan4132/Meridian-X/main/install.ps1 | iex"
echo.
echo Setup script completed.
pause
