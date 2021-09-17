import pyautogui
import time
# pyautogui.PAUSE = 10
pyautogui.FAILSAFE = True

# width, height = pyautogui.size()
# print(width, height)

# yloc = 0
# while yloc <1000:
#     xloc, yloc = pyautogui.position()
#     print(xloc, yloc)

# pyautogui.moveTo(1900,10,duration=0.5)
# pyautogui.click(1900,10)

time.sleep(10)
pyautogui.click()
d = 10
while d < 300:
    pyautogui.dragRel(d, 0, duration=0.1)
    pyautogui.dragRel(0, d, duration=0.1)
    pyautogui.dragRel(-d, 0, duration=0.1)
    pyautogui.dragRel(0, -d, duration=0.1)
    d += 10