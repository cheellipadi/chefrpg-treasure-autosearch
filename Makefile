.PHONY: setup run

setup:
	python3 -m venv .venv && . .venv/bin/activate && pip install pyautogui opencv-python pillow numpy

run:
	. .venv/bin/activate && python3 search.py
