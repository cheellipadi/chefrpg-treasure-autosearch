import csv
from datetime import datetime
from .chest_counter import increment_chest

def log_attempt(attempt_number, chest_rarity):
    increment_chest(chest_rarity)

    """
    Log an attempt and its result to a CSV file.
    Args:
        attempt_number (int): The attempt number
        chest_rarity (ChestRarity): The rarity of chest found
    """
    filename = 'chest_attempts.csv'
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Create file with headers if it doesn't exist
    try:
        with open(filename, 'x', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Timestamp', 'Attempt', 'Chest Rarity'])
    except FileExistsError:
        pass
    
    # Append the new attempt
    with open(filename, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([timestamp, attempt_number, chest_rarity.name]) 