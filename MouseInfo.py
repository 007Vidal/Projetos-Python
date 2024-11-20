import pyautogui
from time import sleep

pyautogui.press('win')
sleep(1)

pyautogui.typewrite('cmd')
sleep(1)

pyautogui.press('enter')
sleep(1)

pyautogui.typewrite('python')
sleep(1)

pyautogui.press('enter')
sleep(1)

pyautogui.typewrite('from mouseinfo import mouseInfo')
sleep(1)

pyautogui.press('enter')
sleep(1)

pyautogui.typewrite('mouseInfo()')
sleep(1)

pyautogui.press('enter')
