import pyautogui

import pyperclip

from time import sleep

email = pyautogui.prompt(text='Digite seu e-mail',
                         title='Informaçõs obrigatórias')
senha = pyautogui.password(text='digite sua senha: ',
                           title='dados de login', mask='*')

pyautogui. moveTo(904, 749, duration=1)
pyautogui.click(904, 749, duration=1)
sleep(1)

pyautogui. moveTo(666, 179, duration=1)
pyautogui.click(666, 179, duration=1)
sleep(1)

pyperclip.copy(email)
sleep(1)
pyautogui.hotkey('ctrl', 'v')

pyautogui.press('enter')

pyperclip.copy(senha)
sleep(1)
pyautogui.hotkey('ctrl', 'v')

# Solução do curso

"""
pyautogui.typewrite(email)
pyautogui.press('enter')
pyautogui.typewrite(senha)
"""
