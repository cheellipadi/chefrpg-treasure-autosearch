import platform
import time
from .constants import DIG_KEY1, DIG_KEY2, SWEEP_PATTERN
from .movement import walk_pattern
from .images import locate_image_on_screen
from .chest_counter import ChestRarity
if platform.system() == 'Windows':
    import keyboard
else:
    import pyautogui

def dig():
    """
    Press dig keys and check for chests after each keystroke.
    Returns:
        ChestRarity: The rarity of chest found, or NONE if no chest is found
    """
    print(f"Pressing dig key: '{DIG_KEY1}' and '{DIG_KEY2}'")
    if platform.system() == 'Windows':
        return dig_windows()
    else:
        return dig_mac()

def dig_mac():
    # Repeat dig key sequence 4 times, with a short pause every 2 sequences
    for i in range(4):
        pyautogui.press(DIG_KEY1)
        pyautogui.press(DIG_KEY2)
        pyautogui.press(DIG_KEY1)
        pyautogui.press(DIG_KEY2)
        if i < 3:
            time.sleep(0.1)

    # Walk around to sweep surrounding area and pick up any chest
    walk_pattern(SWEEP_PATTERN)
    
    chest_rarity = check_chest()
    if chest_rarity != ChestRarity.NONE:
        return chest_rarity

    # Double check to be sure there's no chest
    time.sleep(0.1)
    chest_rarity = check_chest()
    return chest_rarity

def dig_windows():
    # Repeat dig key sequence 4 times, with a short pause every 2 sequences
    for i in range(4):
        keyboard.press_and_release(DIG_KEY1)
        keyboard.press_and_release(DIG_KEY2)
        keyboard.press_and_release(DIG_KEY1)
        keyboard.press_and_release(DIG_KEY2)
        if i < 3:
            time.sleep(0.1)

    # Walk around to sweep surrounding area and pick up any chest
    walk_pattern(SWEEP_PATTERN)
    
    chest_rarity = check_chest()
    if chest_rarity != ChestRarity.NONE:
        return chest_rarity

    # Double check to be sure there's no chest
    time.sleep(0.1)
    chest_rarity = check_chest()
    return chest_rarity

def check_chest():
    """
    Check for any type of chest on screen and return its rarity.
    Returns:
        ChestRarity: The rarity of the chest found, or NONE if no chest is found
    """
    # Check in order of rarity (highest to lowest)
    if locate_image_on_screen('legendary_chest'):
        print("Legendary chest FOUND!")
        return ChestRarity.LEGENDARY
    elif locate_image_on_screen('epic_chest'):
        print("Epic chest FOUND!")
        return ChestRarity.EPIC
    elif locate_image_on_screen('common_chest'):
        print("Common chest FOUND!")
        return ChestRarity.COMMON
    elif locate_image_on_screen('rare_chest'):
        print("Rare chest FOUND!")
        return ChestRarity.RARE
    else:
        print("No chest found.")
        return ChestRarity.NONE 