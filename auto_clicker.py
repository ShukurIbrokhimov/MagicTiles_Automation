import time
import win32api
import win32con
import keyboard
import pyautogui

# Pause for 2 seconds to give time to switch to the game window after running the script.
time.sleep(2)

def click(x, y):
    # Move the mouse to the specified (x, y) coordinates.
    win32api.SetCursorPos((x, y))
    # Click the left mouse button.
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)  # Pause the script for 0.01 seconds before releasing the click.
    # Release the left mouse button.
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

# Start an infinite loop that will run until the 's' key is pressed.
while not keyboard.is_pressed('s'):
    # Check the color of the pixel at (1015, 900).
    if pyautogui.pixel(1015, 900)[0] == 0:
        click(1015, 900)  # Click the position if the color is black (RGB value 0, 0, 0).
    # Check the color of the pixel at (1175, 900).
    if pyautogui.pixel(1175, 900)[0] == 0:
        click(1175, 900)  # Click the position if the color is black (RGB value 0, 0, 0).
    # Check the color of the pixel at (1350, 900).
    if pyautogui.pixel(1350, 900)[0] == 0:
        click(1350, 900)  # Click the position if the color is black (RGB value 0, 0, 0).
    # Check the color of the pixel at (1525, 900).
    if pyautogui.pixel(1525, 900)[0] == 0:
        click(1525, 900)  # Click the position if the color is black (RGB value 0, 0, 0).


