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
    log_attempt,
    send_telegram_photo,
    TARGET_CHESTS
)

# Create debug folder if it doesn't exist
DEBUG_FOLDER = 'debug_screenshots'
TREASURE_TROVE='treasure_trove'

os.makedirs(DEBUG_FOLDER, exist_ok=True)
os.makedirs(TREASURE_TROVE, exist_ok=True)

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
        
        if rarity.name in TARGET_CHESTS:
            print(f"Success! Found {rarity.name} chest. Stopping automation.")

            # Send treasure chest contents
            click_image(f'{rarity.name.lower()}_chest')
            time.sleep(2)
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            screenshot_path = os.path.join(TREASURE_TROVE, f'{attempt}_{rarity.name}_{timestamp}.png')
            img = pyautogui.screenshot(screenshot_path)
            img.save(screenshot_path)
            time.sleep(2)
            send_telegram_photo(screenshot_path, f"Found an {rarity.name} chest! Reply Y to Keep or N to restart search")

            # Collect the item and pause the time
            click_image('inventory_button')
            pyautogui.press('esc')
            break

        elif rarity == ChestRarity.NONE:
            # Capture screenshot when no chest is found
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            screenshot_path = os.path.join(DEBUG_FOLDER, f'no_chest_attempt_{attempt}_{timestamp}.png')
            img = pyautogui.screenshot(screenshot_path)
            img.save(screenshot_path)
            time.sleep(2)
            print(f"No chest found. Screenshot saved to: {screenshot_path}")
            force_quit_app(APP_NAME)
            attempt += 1
        else:
            print(f"Found {rarity.name} chest. Restarting search...")
            force_quit_app(APP_NAME)
            attempt += 1

if __name__ == '__main__':
    try:
        main_loop()
    except KeyboardInterrupt:
        print("Script interrupted by user.")
        sys.exit(0)
