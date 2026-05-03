import socket
import threading
from clipboard import monitor_clipboard
clients = []
def handle_client(conn):
    clients.append(conn)
def broadcast(data):
    for client in clients:
        try:
            client.send(data.encode())
        except:
            clients.remove(client)
def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 5000))
    server.listen(5)
    print(" Server started... Waiting for devices")
    while True:
        conn, addr = server.accept()
        print(f"🔗 Connected: {addr}")
        threading.Thread(target=handle_client, args=(conn,), daemon=True).start()
def on_clipboard_change(data):
    print(" Clipboard changed:", data)
    broadcast(data)
if __name__ == "__main__":
    threading.Thread(target=start_server, daemon=True).start()
    monitor_clipboard(on_clipboard_change)