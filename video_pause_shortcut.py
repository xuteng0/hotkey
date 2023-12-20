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


# Make sure to clean up the lock file
def clean_up_lock_file():
    try:
        os.remove(lock_file_path)
    except OSError:
        pass


def pause_video(window_name):

    # get the active window
    window_name = "Chrome"
    current_window = ewmh.getActiveWindow()
    all_windows = ewmh.getClientList()

    for window in all_windows:
        window_title = ewmh.getWmName(window)
        if (window_name in window_title):
            ewmh.setActiveWindow(window)
            print("Found window: " + window_title)
            sleep(0.1)
            keyboard_con.press(Key.space)
            sleep(0.1)
            keyboard_con.release(Key.space)
            sleep(0.1)
            # ewmh.setActiveWindow(current_window)
            break

    # flush request
    ewmh.display.flush()


def on_activate(window_name):
    print("Combination pressed!")
    pause_video(window_name)


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

    # Check if the lock file exists
    if os.path.exists(lock_file_path):
        print("Another instance of the script is already running.")
        sys.exit()

    # Create the lock file
    with open(lock_file_path, 'w') as lock_file:
        lock_file.write('locked')

    atexit.register(clean_up_lock_file)

    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
