import pyautogui
import time

for i in range(0,60):
    pyautogui.press("volumedown")
    time.sleep(240)
    pyautogui.press("volumeup")
    time.sleep(240)
