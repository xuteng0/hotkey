import os
import sys
import atexit
from pynput import keyboard
from ewmh import EWMH

ewmh = EWMH()
keyboardController = keyboard.Controller()

# Path to the lock file
lock_file_path = '/tmp/video_pause_shortcut_script_lock'

# Make sure to clean up the lock file
def clean_up_lock_file():
    try:
        os.remove(lock_file_path)
    except OSError:
        pass

def pause_video():

    # get the active window
    window_name = "Chrome"
    current_window = ewmh.getActiveWindow()
    all_windows = ewmh.getClientList()

    for window in all_windows:
        window_title = ewmh.getWmName(window)
        if (window_name in window_title):
            ewmh.setActiveWindow(window)
            print("Found window: " + window_title)
            keyboardController.press(keyboard.Key.space)
            keyboardController.release(keyboard.Key.space)
            ewmh.setActiveWindow(current_window)
            break

    # flush request
    ewmh.display.flush()


def on_activate():
    print("Combination pressed!")
    pause_video()


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
    # Define the key combination
    hotkey = keyboard.HotKey(
        keyboard.HotKey.parse('<ctrl>+<shift>+<space>'), on_activate
    )
    
    try:
        
        # Check if the lock file exists
        if os.path.exists(lock_file_path):
            print("Another instance of the script is already running.")
            sys.exit()

        # Create the lock file
        with open(lock_file_path, 'w') as lock_file:
            lock_file.write('locked')
            
        # atexit.register(clean_up_lock_file)

        with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
            listener.join()

    finally:
        # Clean up the lock file on exit
        clean_up_lock_file()

