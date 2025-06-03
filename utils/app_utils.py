import subprocess
import time

def open_app(app_name):
    print(f"Opening {app_name}...")
    subprocess.Popen(["open", "-a", app_name])
    time.sleep(6)

def force_quit_app(app_name):
    print(f"Force quitting {app_name}...")
    subprocess.run(["osascript", "-e", f'tell application "{app_name}" to quit'])
    time.sleep(5) 