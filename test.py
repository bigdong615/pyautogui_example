import pyautogui
import random
import time

txt ="This is a test"

time.sleep(3)

with open('test.txt','r', encoding='utf8') as f:
    lines=f.readlines()

while True:
    pyautogui.typewrite(random.choice(lines),interval=0.15)
    pyautogui.press("enter")
    time.sleep(random.randint(1,3))