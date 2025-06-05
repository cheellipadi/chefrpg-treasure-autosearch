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
    TARGET_CHESTS,
    wait_for_user_input,
    send_telegram_message,
    get_chest_summary,
    format_elapsed,
    get_total_chests,
    chest_counts
)
from dotenv import load_dotenv

load_dotenv()  # Loads from .env file in current directory

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

# Create debug folder if it doesn't exist
DEBUG_FOLDER = 'debug_screenshots'
TREASURE_TROVE='treasure_trove'

os.makedirs(DEBUG_FOLDER, exist_ok=True)
os.makedirs(TREASURE_TROVE, exist_ok=True)

start_time = time.time()
total_user_input_time = 0

def log_perf():
    time_elapsed = int(time.time() - start_time - total_user_input_time)  # or use round() for float
    print(f"📈 STATISTICS: \n\tScript has run for {format_elapsed(time_elapsed)} seconds (excluding user input)")
    print(f"\ttotal user input time: {total_user_input_time}s")
    total_chests = get_total_chests()
    print(f"\tTotal chests found: {total_chests}")
    if total_chests > 0:
        print(f"\tChest finding speed: {time_elapsed / total_chests:.2f} seconds per chest")
        for rarity in ChestRarity:
            if rarity == ChestRarity.NONE:
                continue  # Skip the 'NONE' type if it's just a placeholder
            count = chest_counts[rarity]
            percentage = (count * 100) / total_chests
            print(f"\t{rarity.name.upper()} chests found: {count} (Find rate: {percentage:.2f}%)")

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
        log_perf()
        
        if rarity.name in TARGET_CHESTS:
            print(f"Success! Found {rarity.name} chest. Opening and saving chest contents")
            telegram_bot_enabled = bool(TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID)
            click_image(f'{rarity.name.lower()}_chest')
            time.sleep(2)
            timestamp = datetime.now().strftime('%Y-%m-%d_%I-%M%p')
            screenshot_path = os.path.join(TREASURE_TROVE, f'{timestamp}_{rarity.name}_attempt{attempt}.png')
            img = pyautogui.screenshot(screenshot_path)
            img.save(screenshot_path)
            time.sleep(2)

            if not telegram_bot_enabled:
                print("Telegram bot not enabled. To enable, refer to README.md")
                print("Keeping chest contents in inventory.")
                click_image('inventory_button')
                pyautogui.press('esc')
                print(f"Kept items in inventory. Check {screenshot_path} for results")
                break;

            else: # Send treasure chest contents to TG bot
                print("Sending chest contents to TG bot")
                send_telegram_photo(screenshot_path, f"Found {rarity.name} chest! Reply Y to keep or N to restart search")
                time.sleep(2)

                # Collect the item and pause the time
                print("Keeping chest contents in inventory.")
                click_image('inventory_button')
                pyautogui.press('esc')

                user_input_start_time = time.time()
                user_reply = wait_for_user_input()
                global total_user_input_time
                total_user_input_time += time.time() - user_input_start_time

                if user_reply == "Y":
                    print("User confirmed to keep it. Stopping automation.")
                    send_telegram_message("Congratulations! I'll keep your treasure chest. Your findings so far:\n" + get_chest_summary())
                    break
                elif user_reply == "N":
                    print("User chose to restart search.")
                    send_telegram_message("Ok, I'll keep searching. Your findings so far:\n" + get_chest_summary())
                    force_quit_app(APP_NAME)
                    attempt += 1
                else:
                    print(f"No user input. Assume that user is away for a long while and might want to keep it. Stopping automation")
                    break;
                

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
