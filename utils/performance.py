import time
from .time_helpers import format_elapsed
from .chest_counter import (get_total_chests, chest_counts, ChestRarity)

start_time = time.time()
total_user_input_time = 0

def get_stats():
    global start_time
    time_elapsed = int(time.time() -  start_time - total_user_input_time)  # or use round() for float
    lines = [
        f"📈 STATISTICS:",
        f"Script has run for {format_elapsed(time_elapsed)} seconds (excluding user input)",
        f"total user input time: {total_user_input_time} seconds"
    ]
    total_chests = get_total_chests()

    if total_chests > 0:
        lines.append(f"Chest finding speed: {time_elapsed / total_chests:.2f} seconds taken per chest")

    return "\n".join(lines)
