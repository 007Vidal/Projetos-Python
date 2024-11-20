import pyautogui

import webbrowser

from time import sleep

webbrowser.open_new_tab('https://www.google.com')
sleep(2)

pyautogui.hotkey('ctrl', 'shift', 'n')
sleep(6)

pyautogui.typewrite('www.instagram.com')
sleep(2)

pyautogui.press('enter')
sleep(8)

for x in range(4):
    pyautogui.press('tab')
    sleep(1)

pyautogui.press('enter')
sleep(8)

pyautogui.typewrite('email')
sleep(2)

pyautogui.press('tab')
sleep(1)

pyautogui.typewrite('senha')
sleep(1)

pyautogui.press('tab')
sleep(1)

pyautogui.press('enter')
sleep(10)

pyautogui.press('enter')
sleep(10)

pyautogui.click(x=86, y=260, duration=5)
sleep(3)

pyautogui.typewrite('lorena.camposb')
sleep(3)

pyautogui.press('tab')
sleep(0.5)

pyautogui.press('tab')
sleep(0.5)

pyautogui.press('enter')
sleep(0.5)

pyautogui.click(x=490, y=657, duration=2)
sleep(2)

vazio = pyautogui.locateOnScreen('vazio.png')
sleep(1)


if vazio == None:
    sleep(86400)

elif vazio is not None:
    pyautogui.click(x=749, y=572, duration=2)
    sleep(2)
    pyautogui.click(x=826, y=682, duration=2)
    sleep(2)
    pyautogui.typewrite('Dia maravilhoso')
    sleep(2)
    pyautogui.press('enter')
    sleep(4)
    pyautogui.hotkey('alt', 'f4')
    sleep(86400)    
