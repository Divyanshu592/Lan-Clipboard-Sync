import socket
import pyperclip
from text_handler import receive_text
from image_handler import receive_image

SERVER_IP = "192.168.1.100"   # CHANGE THIS 
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_IP, PORT))

print("Connected to server")

while True:
    header = client.recv(3)

    if not header:
        break

    size_bytes = client.recv(8)
    size = int.from_bytes(size_bytes, 'big')

    if header == b"TXT":
        text = receive_text(client, size)
        print("Received text:", text)
        pyperclip.copy(text)

    elif header == b"IMG":
        receive_image(client, size)