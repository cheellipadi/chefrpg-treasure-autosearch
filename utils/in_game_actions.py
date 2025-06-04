import pyautogui
import time
from .constants import DIG_KEY1, DIG_KEY2
from .movement import walk_pattern
from .images import locate_image_on_screen
from enum import Enum, auto

def dig():
    """
    Press dig keys and check for chests after each keystroke.
    Returns:
        ChestRarity: The rarity of chest found, or NONE if no chest is found
    """
    print(f"Pressing dig key: {DIG_KEY1} and {DIG_KEY2}")
    
    pyautogui.press(DIG_KEY1)
    pyautogui.press(DIG_KEY2)
    pyautogui.press(DIG_KEY1)
    pyautogui.press(DIG_KEY2)
    time.sleep(0.1)
    pyautogui.press(DIG_KEY1)
    pyautogui.press(DIG_KEY2)
    pyautogui.press(DIG_KEY1)
    pyautogui.press(DIG_KEY2)
    chest_rarity = check_chest()
    if chest_rarity != ChestRarity.NONE:
        return chest_rarity
    
    pyautogui.press(DIG_KEY1)
    pyautogui.press(DIG_KEY2)
    time.sleep(0.1)
    
    # Walk around to pick up any chest
    walk_pattern([[0.2,0],[0,-0.2],[-0.4,0],[0,0.4]]);
    chest_rarity = check_chest()
    if chest_rarity != ChestRarity.NONE:
        return chest_rarity
    
    # double check to be sure there's no chest
    time.sleep(0.1)
    chest_rarity = check_chest()
    if chest_rarity != ChestRarity.NONE:
        return chest_rarity
    
    return ChestRarity.NONE


class ChestRarity(Enum):
    NONE = auto()
    COMMON = auto()
    RARE = auto()
    EPIC = auto()
    LEGENDARY = auto()


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