import socket
import threading
from kivy.app import App
from kivy.uix.label import Label

SERVER_IP = "192.168.1.100"   # change this
PORT = 5000


class MobileClient(App):
    def build(self):
        self.label = Label(text="Connecting...")
        threading.Thread(target=self.connect_server, daemon=True).start()
        return self.label

    def connect_server(self):
        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect((SERVER_IP, PORT))

            self.update("Connected to server")

            while True:
                header = client.recv(3)

                if not header:
                    break

                size_bytes = client.recv(8)
                size = int.from_bytes(size_bytes, 'big')

                data = b""
                while len(data) < size:
                    chunk = client.recv(4096)
                    data += chunk

                if header == b"TXT":
                    text = data.decode()
                    self.update(f"Text: {text}")

                elif header == b"IMG":
                    with open("received_image.png", "wb") as f:
                        f.write(data)
                    self.update("Image received")

        except Exception as e:
            self.update(f"Error: {e}")

    def update(self, msg):
        self.label.text = msg


MobileClient().run()