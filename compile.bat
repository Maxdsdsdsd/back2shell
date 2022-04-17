@echo off
title 
pip install pyinstaller
pyinstaller --onefile files/main.py
del build\main\* /q
rmdir build\main
rmdir build
del main.spec /q