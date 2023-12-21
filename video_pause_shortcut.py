import os
import sys
import json
from time import sleep
import atexit
from pynput.keyboard import Key, Controller, HotKey, Listener
from ewmh import EWMH

ewmh = EWMH()
keyboard_con = Controller()
config_file = 'config.json'


# clean up the lock file
def clean_up_lock_file(lock_file_path):
    try:
        os.remove(lock_file_path)
        print("Lock file removed.")
    except OSError:
        pass

#  create lock file
def create_lock_file(lock_file_path):
    with open(lock_file_path, 'w') as lock_file:
        lock_file.write('locked')
    print("Lock file created.")

# check lick file
def check_lock_file(lock_file_path):
    if os.path.exists(lock_file_path):
        print("Another instance of the script is already running.")
        sys.exit()

def on_activate(window_name):
    print("Key Combination Triggered!")
    current_window = ewmh.getActiveWindow()
    chrome_window = current_window
    all_windows = ewmh.getClientList()

    for window in all_windows:
        if (window_name in ewmh.getWmName(window)):
            print("Found window: " + ewmh.getWmName(window))
            chrome_window = window
            break
    
    print("Sending space key to window: " + ewmh.getWmName(chrome_window))
    ewmh.setActiveWindow(chrome_window)
    ewmh.display.flush()
    sleep(0.1)
    keyboard_con.type(" ")
    sleep(0.1)
    print("Window switched back to: " + ewmh.getWmName(current_window))
    ewmh.setActiveWindow(current_window)
    ewmh.display.flush()


def on_press(key):
    try:
        hotkey.press(key)
    except AttributeError:
        pass


def on_release(key):
    try:
        hotkey.release(key)
    except AttributeError:
        pass


if __name__ == "__main__":

    # Load configuration
    with open(config_file, 'r') as file:
        config = json.load(file)
        
    lock_file_path = config['lock_file_path']
    window_name = config['browser_name']

    # Define the key combination
    hotkey = HotKey(
        HotKey.parse(
            '<ctrl>+<shift>+<space>'), lambda: on_activate(window_name)
    )

    check_lock_file(lock_file_path)
    create_lock_file(lock_file_path)
    atexit.register(lambda: clean_up_lock_file(lock_file_path))

    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
