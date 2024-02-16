import pyautogui
import time

penis = True
while penis:
    time.sleep(5)
    for i in range(5):
        pyautogui.click()
        time.sleep(5)
        i+=1
    pyautogui.keyDown('f')
    pyautogui.mouseDown(button='right')
    time.sleep(1.61)
    pyautogui.mouseUp(button='right')
    pyautogui.keyUp("f")
    pyautogui.press("1")