from pynput.keyboard import Key, Controller, HotKey, Listener
from time import sleep
from ewmh import EWMH

keyboard_con = Controller()
ewmh = EWMH()

window_name = "Chrome"
current_window = ewmh.getActiveWindow()
chrome_window = current_window
all_windows = ewmh.getClientList()
for window in all_windows:
        if ("Chrome" in ewmh.getWmName(window)):
            chrome_window = window
            print("Found window: " + ewmh.getWmName(window))


ewmh.setActiveWindow(chrome_window)
ewmh.display.flush()
sleep(0.1)
# keyboard_con.type("hello")
keyboard_con.tap(Key.space)
# keyboard_con.type("world\n")
sleep(0.1)
ewmh.setActiveWindow(current_window)
ewmh.display.flush()
sleep(1)