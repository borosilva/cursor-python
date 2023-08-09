import pyautogui
import time

def run():
    print('Moviendo Cursor...')
    while True:
        pyautogui.moveTo(500, 500)
        time.sleep(5)
        pyautogui.moveTo(700, 700)
        time.sleep(5)