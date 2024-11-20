# Entender os passos manuais para depois criar o código python;

# Verificar se há um botão com a cor correspondente dentro do circulo daquela cor;

# Importante instalei pip install keyboard

import pyautogui

import keyboard
from time import sleep

sleep(3)

while keyboard.is_pressed('1') == False:
    if pyautogui.pixelMatchesColor(423, 669, (0, 192, 0)):
        pyautogui.press('a')
        sleep(0.05)
    if pyautogui.pixelMatchesColor(480, 669, (237, 0, 12)):
        pyautogui.press('s')
        sleep(0.05)
    if pyautogui.pixelMatchesColor(536, 669, (240, 240, 0)):
        pyautogui.press('j')
        sleep(0.05)
