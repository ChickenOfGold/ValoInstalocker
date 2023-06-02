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
print('      Hold "q" while loading to a game to instalock Neon')
print('      Hold "w" while loading to a game to instalock Omen')
print('      Hold "e" while loading to a game to instalock Brimstone')
print('      Hold "s" while loading to a game to instalock Sage')
print('      Click "esc" to exit the program')


# Lock button
lock_x = 936
lock_y = 808

movement_delay = 0.1
click_delay = 0.2


# Function to move the mouse cursor
def move_neon():
    # Move the mouse cursor to lock
    pyautogui.moveTo(lock_x, lock_y)
    pyautogui.click()  # Lock

    # Move the mouse cursor to Neon
    pyautogui.moveTo(771, 924)
    pyautogui.click()  # Pick agent


# Function to handle key press events for Neon
def neon(event):
    if event.name == 'q':
        while keyboard.is_pressed('q'):
            move_neon()


def move_omen():
    # Move the mouse cursor to lock
    pyautogui.moveTo(lock_x, lock_y)
    pyautogui.click()  # Lock

    # Move the mouse cursor to Omen
    pyautogui.moveTo(883, 916)
    pyautogui.click()  # Pick agent


# Function to handle key press events for W
def omen(event):
    if event.name == 'w':
        move_omen()


def move_brim():
    # Move the mouse cursor to lock
    pyautogui.moveTo(lock_x, lock_y)
    pyautogui.click()  # Lock

    # Move the mouse cursor to Brimstone
    pyautogui.moveTo(521, 930)
    pyautogui.click()  # Pick agent


def brim(event):
    if event.name == 'e':
        move_omen()


def move_sage():
    # Move the mouse cursor to lock
    pyautogui.moveTo(lock_x, lock_y)
    pyautogui.click()  # Lock

    # Move the mouse cursor to Sage
    pyautogui.moveTo(1044, 924)
    pyautogui.click()  # Pick agent

def sage(event):
    if event.name == 's':
        move_omen()

# Register the key press event handlers
keyboard.on_press(neon)
keyboard.on_press(omen)
keyboard.on_press(brim)
keyboard.on_press(sage)

while True:
    pass

keyboard.wait('esc')
