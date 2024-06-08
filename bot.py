import time
import win32api
import win32con
import keyboard
import pyautogui

# Import necessary libraries:
# - time: Allows us to work with time-related functions, like pausing the script.
# - win32api: Enables control over the mouse, allowing us to move the cursor.
# - win32con: Provides constants needed for Windows API calls, such as mouse click actions.
# - keyboard: Allows detection of keyboard events to stop the script with a specific key press.
# - pyautogui: Enables control of the mouse and keyboard, and reading pixel colors from the screen.

time.sleep(2)  # Give us a couple of seconds to switch to the game window after running the script.

def click(x, y):
    win32api.SetCursorPos((x, y))  # Move the mouse to the specified (x, y) coordinates.
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)  # Click the left mouse button.
    time.sleep(0.01)  # Pause the script for 0.01 seconds before releasing the click.
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)  # Release the left mouse button.

# Start an infinite loop that will run until the 's' key is pressed.
while not keyboard.is_pressed('s'):
    # Check the color of the pixel at the specified position (x, y).
    if pyautogui.pixel(x, y)[0] == 0:
        click(x, y)  # Click the position if the color is black (RGB value 0, 0, 0).
    if pyautogui.pixel(x, y)[0] == 0:
        click(x, y)  # Check and click again for redundancy.
    if pyautogui.pixel(x, y)[0] == 0:
        click(x, y)  # Check and click again for redundancy.
    if pyautogui.pixel(x, y)[0] == 0:
        click(x, y)  # Check and click again for redundancy.

