import pyautogui
import time
import os
from utils import DISPLAY_SCALE_FACTOR

def safe_locate_on_screen(image_path, confidence=0.75, grayscale=False):
    """
    Safely attempt to locate an image on screen with error handling.
    Args:
        image_path (str): Full path to the image file
        confidence (float): Confidence threshold for image matching (0-1)
        grayscale (bool): Whether to use grayscale matching
    Returns:
        tuple: (x, y, width, height) of the match if found, None otherwise
    """
    try:
        return pyautogui.locateOnScreen(image_path, confidence=confidence, grayscale=grayscale)
    except Exception as e:
        print(f"\tError matching image {image_path}: {e}")
        return None

def locate_image_on_screen(templatePath, confidence=0.75, grayscale=False):
    """
    Locate an image or any matching image from a directory of templates on screen.
    Args:
        templatePath (str): Path to either a single image or a directory of template images
        confidence (float): Confidence threshold for image matching (0-1)
        grayscale (bool): Whether to use grayscale matching
    Returns:
        tuple: (x, y, width, height) of the match if found, None otherwise
    """
    template_path = 'images/'+templatePath
    try:
        # Handle directory of template images
        if os.path.isdir(template_path):
            print(f"Matching images in directory: {template_path}")
            files = os.listdir(template_path)
            print(f"\tFound {len(files)} files in directory")
            
            for image_file in files:
                if image_file.lower().endswith(('.png', '.jpg', '.jpeg')):
                    full_path = os.path.join(template_path, image_file)
                    print(f"\tTrying to match image: {image_file}")
                    location = safe_locate_on_screen(full_path, confidence, grayscale)
                    if location:
                        print(f"\tFound match using template: {image_file}")
                        return location
            print("\tNo matches found in any template images")
            return None
        # Handle single image
        else:
            print(f"\tTrying to match single image: {template_path}")
            return safe_locate_on_screen(template_path, confidence, grayscale)
    except Exception as e:
        print(f"\tError accessing path {template_path}: {e}")
        return None

def click_image(template_path, confidence=0.8, timeout=5):
    start_time = time.time()

    while time.time() - start_time < timeout:
        location = locate_image_on_screen(template_path, confidence, grayscale=True)
        if location:
            center = pyautogui.center(location)
            # Adjust for Retina scaling
            adjusted_x = center.x / DISPLAY_SCALE_FACTOR
            adjusted_y = center.y / DISPLAY_SCALE_FACTOR

            pyautogui.moveTo(adjusted_x,adjusted_y)
            pyautogui.mouseDown()
            pyautogui.click()
            time.sleep(0.5) 
            pyautogui.mouseUp()
            time.sleep(0.1)
            print(f"Clicked on {template_path} at ({adjusted_x}, {adjusted_y}) with scale factor {DISPLAY_SCALE_FACTOR}")
            return True
        else:
            print(f"Could not find {template_path} on screen. Retrying...")
            time.sleep(0.2)
    
    print(f"Timeout reached after {timeout} seconds. Could not find {template_path}.")
    return False
