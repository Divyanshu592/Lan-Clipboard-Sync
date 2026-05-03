import socket
import threading
from clipboard import monitor_clipboard
from text_handler import send_text
from image_handler import send_image

clients = []

def handle_client(conn):
    clients.append(conn)
    print(f"Client connected: {conn}")


def broadcast(data_type, content):
    for client in clients:
        try:
            if data_type == "text":
                send_text(client, content)
            elif data_type == "image":
                send_image(client, content)
        except:
            clients.remove(client)


def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 5000))
    server.listen(5)

    print("Server started... Waiting for devices")

    while True:
        conn, addr = server.accept()
        print(f"Connected: {addr}")
        threading.Thread(target=handle_client, args=(conn,), daemon=True).start()


def on_clipboard_change(data_type, content):
    print(f"Clipboard changed: {data_type}")
    broadcast(data_type, content)


if __name__ == "__main__":
    threading.Thread(target=start_server, daemon=True).start()
    monitor_clipboard(on_clipboard_change)