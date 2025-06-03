import pyautogui
import time

def locate_image_on_screen(template_path, confidence=0.75, grayscale=False):
    try:
        location = pyautogui.locateOnScreen("images/"+ template_path, confidence=confidence, grayscale=grayscale)
        return location
    except Exception as e:
        print(f"Error locating image {template_path}: {e}")
        return None

def click_image(template_path, confidence=0.8, timeout=5):
    """
    Try to find and click an image on screen, retrying until timeout is reached.
    Args:
        template_path (str): Path to the image template
        confidence (float): Confidence threshold for image matching (0-1)
        timeout (float): Maximum time to wait for image in seconds
    Returns:
        bool: True if image was found and clicked, False if timeout was reached
    """
    start_time = time.time()
    while time.time() - start_time < timeout:
        location = locate_image_on_screen(template_path, confidence)
        if location:
            center = pyautogui.center(location)
            pyautogui.click(center)
            print(f"Clicked on {template_path} at {center}")
            return True
        else:
            print(f"Could not find {template_path} on screen. Retrying...")
            time.sleep(0.2)
    
    print(f"Timeout reached after {timeout} seconds. Could not find {template_path}.")
    return False 