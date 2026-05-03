# LAN Clipboard Sync Tool

A Python-based application that enables real-time clipboard sharing between multiple devices connected to the same local network (LAN). This tool does not require an internet connection and works entirely within a WiFi network.

---

## Overview

This project implements a simple client-server architecture for sharing clipboard data across devices. One device acts as the server and continuously monitors clipboard changes. When a change is detected, the updated content is transmitted to all connected client devices using TCP sockets. Clients receive this data and update their local clipboard automatically.

---

## Features

- Real-time clipboard synchronization across devices
- Works over a local network (no internet required)
- Supports multiple clients connected to a single server
- Lightweight and easy to set up
- Uses standard Python libraries and minimal dependencies

---

## Project Structure

```id="struct01"
lan-clipboard-sync/
│
├── server.py        # Starts server and broadcasts clipboard data
├── client.py        # Connects to server and updates clipboard
├── clipboard.py     # Detects clipboard changes
├── requirements.txt
└── README.md
```

---

## Technology Stack

- Python 3
- Socket Programming (TCP)
- threading module for concurrency
- pyperclip for clipboard access

---

## Requirements

- Python 3.7 or higher
- All devices must be connected to the same WiFi network
- Network must allow device-to-device communication (no client isolation)

---

## Installation and Setup

### Step 1: Clone the Repository

Use the following command to download the project to your system:

```bash id="clone01"
git clone https://github.com/your-username/lan-clipboard-sync.git
```

Move into the project directory:

```bash id="clone02"
cd lan-clipboard-sync
```

---

### Step 2: Install Dependencies

Install required Python packages using:

```bash id="install01"
pip install -r requirements.txt
```

---

## How the System Works

- The server listens for incoming client connections on a specific port (default: 5000)
- The clipboard module continuously checks for changes
- When new content is copied, the server broadcasts it to all connected clients
- Each client receives the data and updates its own clipboard

---

## Running the Application

### Step 1: Start the Server

Run the following command on the main device:

```bash id="runserver01"
python server.py
```

Expected output:

```id="runserver02"
Server file started
Server started... Waiting for devices
```

---

## Understanding IP Configuration

### Why IP Address is Required

In a local network, each device is assigned a unique IP address (for example, 192.168.1.5). Clients must know the server’s IP address to establish a connection.

---

### Step 2: Find Server IP Address

On the server device:

#### Windows:

```bash id="ip01"
ipconfig
```

Look for:

```id="ip02"
IPv4 Address: 192.168.x.x
```

---

### Step 3: Configure Client with Server IP

Open `client.py` and update the following line:

```python id="ip03"
SERVER_IP = "192.168.x.x"
```

Replace `192.168.x.x` with the actual IP address of your server.

---

## Important Note About server.py IP

In `server.py`, you will see:

```python id="ip04"
server.bind(("0.0.0.0", 5000))
```

Explanation:

- `0.0.0.0` means the server will listen on all available network interfaces
- This allows any device in the same network to connect using the server's IP
- You do not need to manually change this value

---

## Step 4: Run the Client

On the same or another device, run:

```bash id="runclient01"
python client.py
```

Expected output:

```id="runclient02"
Connected to server
```

---

## Testing the Application

1. Copy any text on the server device
2. The copied text should automatically appear on the client device clipboard
3. If multiple clients are connected, all will receive the updated content

---

## Limitations

- Only text data is supported (no file transfer)
- No encryption is implemented
- Requires manual IP configuration
- Infinite loop issue may occur if bidirectional sync is implemented without safeguards

---

## Security Considerations

This application sends clipboard data as plain text over the network. It should not be used for sensitive information such as passwords or personal data.

---

## Future Improvements

- Automatic device discovery using UDP broadcast
- End-to-end encryption for secure communication
- File transfer capability
- Graphical user interface
- Cross-platform mobile support
- Clipboard sync control (enable/disable toggle)

---

## Author

Divyanshu Pandey

---

## License

This project is open-source and available for educational and personal use.
