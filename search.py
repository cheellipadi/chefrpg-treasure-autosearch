import time
import sys
import pyautogui
import os
from datetime import datetime
from utils import (
    APP_NAME,
    WAIT_AFTER_LOAD,
    WALK_PATTERN,
    click_image,
    open_app,
    force_quit_app,
    walk_pattern,
    dig,
    ChestRarity,
    log_attempt
)

# Create debug folder if it doesn't exist
DEBUG_FOLDER = 'debug_screenshots'
os.makedirs(DEBUG_FOLDER, exist_ok=True)

def main_loop():
    attempt = 1
    while True:
        print(f"\n--- Attempt #{attempt} ---")
        open_app(APP_NAME)

        # Click Continue button
        if not click_image('continue_button'):
            print("Failed to click Continue button. Retrying...")
            force_quit_app(APP_NAME)
            attempt += 1
            continue

        # Click Load Game button
        if not click_image('load_game_button'):
            print("Failed to click Load Game button. Retrying...")
            force_quit_app(APP_NAME)
            attempt += 1
            continue

        # Click User Account button
        if not click_image('username'):
            print("Failed to click username button. Retrying...")
            force_quit_app(APP_NAME)
            attempt += 1
            continue

        time.sleep(WAIT_AFTER_LOAD)

        walk_pattern(WALK_PATTERN)
        
        # Dig and check for chests, logging the result
        rarity = dig()
        log_attempt(attempt, rarity)
        
        if rarity == ChestRarity.LEGENDARY:
            print(f"Success! Found Legendary chest. Stopping automation.")
            # Collect the item and pause the time
            click_image('legendary_chest')
            click_image('inventory_button')
            pyautogui.press('esc')

            break
        elif rarity == ChestRarity.NONE:
            # Capture screenshot when no chest is found
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            screenshot_path = os.path.join(DEBUG_FOLDER, f'no_chest_attempt_{attempt}_{timestamp}.png')
            img = pyautogui.screenshot(screenshot_path)
            img.save(screenshot_path)
            print(f"No chest found. Screenshot saved to: {screenshot_path}")
            force_quit_app(APP_NAME)
            attempt += 1
        else:
            print(f"Found {rarity.name} chest. Continuing search...")
            force_quit_app(APP_NAME)
            attempt += 1

if __name__ == '__main__':
    try:
        main_loop()
    except KeyboardInterrupt:
        print("Script interrupted by user.")
        sys.exit(0)
