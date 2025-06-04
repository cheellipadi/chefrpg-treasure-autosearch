## Instructions
1. Find a treasure spot near a cave entrance/exit.
2. Equip your shovel, save and FORCE QUIT the game. This will be CMD+Q on Mac, and ALT+F4 on windows. (Do not exit via main menu)
3. Run the script after configuration
   
## Configuration

### Change the username

- This tool works by using image recognition. You need to update the [username screenshot](./images/username) to match your own

### Configure params

- Modify the [constants](./utils/constants.py) file.
- It will take some trial and error for the WALK_PATTERN parameter, but it should take fewer than 10 attempts.

## How to run

### Install deps

```
python3 -m venv .venv
. .venv/bin/activate
pip install pyautogui opencv-python pillow numpy
```

### Run script

```
python3 search.py
```

## Logging

For every attempt at finding a treasure chest, it will be logged to the [chest_attempts.csv](./chest_attempts.csv) file.

## FAQs

Q: Why is the script not able to click on a button or detect a certain kind of treasure chest?
A: pyautogui is pixel specific / device sensitive, so if the [images](./images/) folder doesn't contain screenshots specific to your device, it may not work as expected. You can modify these folders to include your own screenshots. Note that the larger the size of this folder, the longer the script will take to run.

Q: Why is it not working properly?
A: For attempts where no chests are found, a screenshot will be taken and saved to the [debug folder](./debug_screenshots/). If you see a chest in any of these screenshots, it means you need to update the screenshots of that particular chest.
