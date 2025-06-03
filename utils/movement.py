import pyautogui
import time

def walk_pattern(movement_patterns):
    """
    Execute a sequence of movement patterns.
    Args:
        movement_patterns: List of [x, y] pairs where x and y are float durations in seconds.
                         Positive x moves right (D), negative x moves left (A)
                         Positive y moves up (W), negative y moves down (S)
    """
    for x, y in movement_patterns:
        # Determine keys for both directions
        key_x = 'd' if x > 0 else 'a' if x < 0 else None
        key_y = 'w' if y > 0 else 's' if y < 0 else None
        
        # Press all necessary keys
        if key_x:
            print(f"Holding {key_x.upper()} for {abs(x):.2f} seconds")
            pyautogui.keyDown(key_x)
        if key_y:
            print(f"Holding {key_y.upper()} for {abs(y):.2f} seconds")
            pyautogui.keyDown(key_y)
            
        # Handle different duration keys
        if x != 0 and y != 0:
            # If both movements exist, release the shorter duration key first
            shorter_duration = min(abs(x), abs(y))
            longer_duration = max(abs(x), abs(y))
            
            # Wait for shorter duration
            time.sleep(shorter_duration)
            
            # Release the shorter duration key
            if abs(x) == shorter_duration:
                pyautogui.keyUp(key_x)
                print(f"Released {key_x.upper()}")
            else:
                pyautogui.keyUp(key_y)
                print(f"Released {key_y.upper()}")
                
            # Wait for remaining duration
            time.sleep(longer_duration - shorter_duration)
            
            # Release the longer duration key
            if abs(x) == longer_duration:
                pyautogui.keyUp(key_x)
                print(f"Released {key_x.upper()}")
            else:
                pyautogui.keyUp(key_y)
                print(f"Released {key_y.upper()}")
        else:
            # If only one movement exists, just wait for its duration
            duration = abs(x) if x != 0 else abs(y)
            time.sleep(duration)
            
            # Release the key
            if key_x:
                pyautogui.keyUp(key_x)
                print(f"Released {key_x.upper()}")
            if key_y:
                pyautogui.keyUp(key_y)
                print(f"Released {key_y.upper()}")

        time.sleep(0.1)  # small cooldown between movements 