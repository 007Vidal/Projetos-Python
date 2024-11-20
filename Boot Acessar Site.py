import webbrowser

import pyautogui

from time import sleep

webbrowser.open_new_tab(
    'https://cursoautomacao.netlify.app/?_gl=1*hiebp9*_ga*MTU5MDgwNzMwMy4xNzMxMDE5ODQx*_ga_37GXT4VGQK*MTczMTY5NjAwNi4xOS4xLjE3MzE2OTY5MDQuMC4wLjA.')

sleep(5)

pyautogui.moveTo(x=1254, y=210, duration=1)
sleep(2)

for x in range(1):
    pyautogui.scroll(-1000)
    sleep(1)

pyautogui.click(x=1043, y=276, duration=1)
sleep(1)

pyautogui.typewrite('Almir Malta Vidal')
sleep(1)

pyautogui.click(x=1056, y=312, duration=1)
sleep(2)

ok = pyautogui.locateCenterOnScreen('ok.png')
pyautogui.click(ok[0], ok[1], duration=1)

for x in range(1):
    pyautogui.scroll(2000)
    sleep(2)
    pyautogui.scroll(-2200)
    sleep(2)

pyautogui.click(x=385, y=253, duration=2)
sleep(1)

pyautogui.click(x=193, y=248, duration=2)
sleep(1)
