import subprocess
import time
import platform
import os
from .constants import (WINDOWS_FULL_PATH_TO_APP_EXE,APP_NAME)

def open_app(app_name):
    
    subprocess.Popen(["open", "-a", app_name])
    

def open_app():
    system = platform.system()
    if system == "Darwin":
        print(f"Opening {APP_NAME}...")
        subprocess.run(["open", "-a", APP_NAME])
    elif system == "Windows":
        print(f"Running {WINDOWS_FULL_PATH_TO_APP_EXE}...")
        # e.g., [r"C:\Program Files (x86)\Steam\steamapps\common\chef_rpg\ChefRPG.exe"]
        subprocess.Popen([WINDOWS_FULL_PATH_TO_APP_EXE])
    else:
        raise NotImplementedError(f"Unsupported OS: {system}")
    time.sleep(6)

def force_quit_app():
    print(f"Force quitting {APP_NAME}...")

    system = platform.system()
    if system == "Darwin":
        # macOS: quit app gracefully via AppleScript
        subprocess.run(["osascript", "-e", f'tell application "{APP_NAME}" to quit'])
    elif system == "Windows":
        # Windows: force kill by process name
        subprocess.run(["taskkill", "/F", "/IM", os.path.basename(WINDOWS_FULL_PATH_TO_APP_EXE)], shell=True)
    else:
        raise NotImplementedError(f"Unsupported OS: {system}") 
    time.sleep(5)