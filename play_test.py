from time import sleep
from PIL import Image

import pyautogui

blue_location = pyautogui.locateOnScreen("Images/candy_blue.png", confidence=0.9)

loc = pyautogui.center(blue_location)

pyautogui.moveTo(loc.x, loc.y)   # moves mouse to X of 100, Y of 200.

pyautogui.click(duration=0.1, button='right')

pyautogui.drag(-60, 0, 0, button='right')
pyautogui.move(60, 0)
pyautogui.drag(60, 0, 0, button='right')
pyautogui.move(-60, 0)
pyautogui.drag(0, 60, 0, button='right')
pyautogui.move(0, -60)
pyautogui.drag(0, -60, 0, button='right')
pyautogui.move(0, 60)