import pyperclip
import time

def monitor_clipboard(callback):
    print("Server file started")
    last = ""

    while True:
        current = pyperclip.paste()
        if current != last:
            last = current
            callback(current)
        time.sleep(1)