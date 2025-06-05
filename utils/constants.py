# Adjust these as needed
APP_NAME = "Chef RPG"
DIG_KEY1 = 'x'
DIG_KEY2 = ' '
WAIT_AFTER_LOAD = 4 # Seconds to wait after loading (before starting the movement towards treasure spot)
# WALK_PATTERN e.g. [[1,1],[-1,0]] -> walk diagonally up and right for 1s, then left for 1s
WALK_PATTERN = [[0.9, -0.8],[0,-0.4],[-0.9,-1.8]]
# DISPLAY_SCALE_FACTOR = 2 # Usually 2 for retina displays, 1 for normal displays
TARGET_CHESTS = ['EPIC','LEGENDARY','COMMON','RARE'] # Example supported values: ['LEGENDARY'], ['EPIC'], ['LEGENDARY','EPIC'], ['EPIC','LEGENDARY','COMMON','RARE']
# Auto-detect display scale factor (macOS only)
try:
    from AppKit import NSScreen
    DISPLAY_SCALE_FACTOR = NSScreen.mainScreen().backingScaleFactor()
    print(f"DISPLAY_SCALE_FACTOR: {DISPLAY_SCALE_FACTOR}")
except Exception:
    DISPLAY_SCALE_FACTOR = 1  # Fallback for non-Retina or non-macOS environments