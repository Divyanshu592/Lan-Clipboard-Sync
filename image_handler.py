import io

def image_to_bytes(img):
    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    return buffer.getvalue()


def send_image(client, img):
    data = image_to_bytes(img)
    length = len(data).to_bytes(8, 'big')
    client.send(b"IMG" + length + data)


def receive_image(sock, size):
    data = b""
    while len(data) < size:
        chunk = sock.recv(4096)
        if not chunk:
            break
        data += chunk

    with open("received_image.png", "wb") as f:
        f.write(data)

    print("Image received and saved as received_image.png")