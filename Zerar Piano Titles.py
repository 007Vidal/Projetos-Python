# Quais os passos manuais que devo transformar em código?

# Biblioteca instalada pip install pywin32
import pyautogui
import keyboard
import win32api
import win32con
from time import sleep

pyautogui.click(539, 387, duration=1)


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


while keyboard.is_pressed('1') == False:
    if pyautogui.pixelMatchesColor(441, 461, (0, 0, 0)):
        click(441, 461)
    if pyautogui.pixelMatchesColor(509, 458, (0, 0, 0)):
        click(509, 458)
    if pyautogui.pixelMatchesColor(569, 461, (0, 0, 0)):
        click(569, 461)
    if pyautogui.pixelMatchesColor(634, 464, (0, 0, 0)):
        click(634, 464)
