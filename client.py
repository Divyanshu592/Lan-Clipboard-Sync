import socket
import pyperclip

SERVER_IP = "192.168.1.100"  # replace with your laptop IP

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_IP, 5000))

print("Connected to server")

while True:
    data = client.recv(1024).decode()
    print("Received:", data)
    pyperclip.copy(data)