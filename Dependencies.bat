@echo off
echo Checking for dependencies...
python -c "import os"
python -c "import cv2"
python -c "import time"
python -c "import moviepy.editor as mpe"
if %errorlevel%==0 (
  echo Dependencies are installed!
) else (
  echo Some dependencies are missing. Please install them.
)
pause
