import pyperclip
from PIL import ImageGrab
import time

def get_clipboard_data():
    try:
        img = ImageGrab.grabclipboard()
        if img:
            return "image", img
    except:
        pass

    text = pyperclip.paste()
    return "text", text


def monitor_clipboard(callback):
    last_data = None

    while True:
        data_type, content = get_clipboard_data()

        if content != last_data:
            last_data = content
            callback(data_type, content)

        time.sleep(1)