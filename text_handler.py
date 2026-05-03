def send_text(client, text):
    data = text.encode()
    length = len(data).to_bytes(8, 'big')
    client.send(b"TXT" + length + data)


def receive_text(sock, size):
    data = b""
    while len(data) < size:
        chunk = sock.recv(4096)
        if not chunk:
            break
        data += chunk
    return data.decode()