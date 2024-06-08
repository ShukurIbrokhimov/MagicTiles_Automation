import time
import win32api
import win32con
import keyboard
import pyautogui


time.sleep(2)

def click(x, y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01) # This pauses the script for 0.001 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while not keyboard.is_pressed('s'):

    if pyautogui.pixel(1015, 900)[0] == 0:
        click(1015, 900)
    if pyautogui.pixel(1175, 900)[0] == 0:
        click(1175, 900)
    if pyautogui.pixel(1350, 900)[0] == 0:
        click(1350, 900)
    if pyautogui.pixel(1525, 900)[0] == 0:
        click(1525, 900)

print(1)