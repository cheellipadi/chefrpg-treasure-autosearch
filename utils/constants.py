# For Mac OS users.
APP_NAME = "Chef RPG"

# For windows users. 
# Change this to point to your desination executable file. Remember to retain the r in r"your_full_exe_path" . This helps python escape the backslashes
WINDOWS_FULL_PATH_TO_APP_EXE = r"C:\Program Files (x86)\Steam\steamapps\common\chef_rpg\ChefRPG.exe"

# Adjust these as needed
DIG_KEY1 = 'x'
DIG_KEY2 = ' '
WAIT_AFTER_LOAD = 4 # Seconds to wait after loading (before starting the movement towards treasure spot)
TARGET_CHESTS = ['EPIC','LEGENDARY'] # Example supported values: ['LEGENDARY'], ['EPIC'], ['LEGENDARY','EPIC'], ['EPIC','LEGENDARY','COMMON','RARE']

# Adjust these patterns to move your character to the treasure spot (WALK_PATTERN) and sweep surrounding area for treasure chests (SWEEP_PATTERN)
# WALK_PATTERN is a list of tuples (A tuple is a list of exactly 2 elements), with each tuple representing movement as a cartesian grid vector [x,y]
# e.g. [[1,0]] -> walk right for 1s 
# e.g. [[1,1]] -> walk diagonally to top-right for 1s
# e.g. [[0,-1],[-0.1,-0.1]] -> walk down for 1s, then walk diagonally towards bottom left for 0.1s
# e.g. [[-1,0],[0,0.2]] -> walk left for 1s, then up for 0.2s
# e.g. [[1,1],[-1,0],[0,-1]] -> walk diagonally up and right for 1s, then left for 1s, then down for 1s (returns character to original position)
WALK_PATTERN = [[-2.35,0],[0,-0.03]]
SWEEP_PATTERN = [[0.2,0],[0,-0.2],[-0.4,0],[0,0.4],[0.2,0]]


# DISPLAY_SCALE_FACTOR = 1 # Uncomment this if the below code doesn't work properly
# Auto-detect display scale factor (macOS only)
try:
    from AppKit import NSScreen
    DISPLAY_SCALE_FACTOR = NSScreen.mainScreen().backingScaleFactor()
    print(f"DISPLAY_SCALE_FACTOR: {DISPLAY_SCALE_FACTOR}")
except Exception:
    DISPLAY_SCALE_FACTOR = 1  # Fallback for non-Retina or non-macOS environments