# Adjust these as needed
APP_NAME = "Chef RPG"
DIG_KEY1 = 'x'
DIG_KEY2 = ' '
WAIT_AFTER_LOAD = 4 # Seconds to wait after loading (before starting the movement towards treasure spot)
# WALK_PATTERN e.g. [[1,1],[-1,0]] -> walk diagonally up and right for 1s, then left for 1s
WALK_PATTERN = [[0.9, -0.8],[0,-0.4],[-0.9,-1.8]]
DISPLAY_SCALE_FACTOR = 1 # Usually 2 for retina displays, 1 for normal displays
TARGET_CHESTS = ['EPIC','LEGENDARY'] # Supported Values: ['LEGENDARY'], ['EPIC'], ['LEGENDARY','EPIC']