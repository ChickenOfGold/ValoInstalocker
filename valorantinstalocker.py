import pyautogui
import keyboard
import pyfiglet
from rich import print
import time


time.sleep(0.5)
title = pyfiglet.figlet_format('Instalock', font='larry3d')
print(f'[yellow]{title}[/yellow]')

title = pyfiglet.figlet_format('      for', font='larry3d')
print(f'[yellow]{title}[/yellow]')
time.sleep(0.2)
title = pyfiglet.figlet_format(' VALORANT', font='larry3d')
print(f'[yellow]{title}[/yellow]')

time.sleep(0.5)
print('      by ChickenOfGold')

print('      Instructions:')
print('      Hold "q" while loading to a game to instalock neon')
print('      Click "esc" to exit the program')

# Start position
start_x = 936
start_y = 808

# End position
end_x = 771
end_y = 924

# Delay between each movement (in seconds)
movement_delay = 0.1

# Click delay (in seconds)
click_delay = 0.2


# Function to move the mouse cursor
def move_mouse():
    # Move the mouse cursor to lock
    pyautogui.moveTo(start_x, start_y)

    pyautogui.click() #lock


    pyautogui.moveTo(end_x, end_y)
    
    pyautogui.click() #pick agent

# Function to handle key press events
def on_press(event):
    if event.name == 'q':
        while keyboard.is_pressed('q'):
            move_mouse()

# Register the key press event handler
keyboard.on_press(on_press)

while 1:
    on_press


keyboard.wait('esc')