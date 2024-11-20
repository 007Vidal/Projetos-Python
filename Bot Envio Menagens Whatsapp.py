
"""1 - Lista de números;
2 - Enviar individualmente uma mensagem para cada pessoa;
3 - Pausar entre cada envio;

1 - ESCOLHER UM CONTATO;
2 - ENVIAR UMA MENSAGEM PARA ESSE CONTATO;
	http://api.whatsapp.com/send?phone=5577981316999"""

import webbrowser
import pyautogui
from time import sleep

telefones = [5577981316999, 77991398356]

for telefone in telefones:
    webbrowser.open(f'http://api.whatsapp.com/send?phone={telefone}')
    sleep(5)
    pyautogui.click(681, 331, duration=1)
    sleep(5)
    pyautogui.click(548, 699, duration=1)
    sleep(5)
    pyautogui.typewrite(
        'Estou te enviando essa mensagem como teste para minha automação')
    sleep(5)
    pyautogui.press('enter')
    sleep(15)
