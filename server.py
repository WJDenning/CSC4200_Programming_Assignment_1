import socket
import threading
import logging
from encryption import encrypt_message, decrypt_message

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

clients = []

logging.basicConfig(
	level = logging.DEBUG,
	format = '%(asctime)s - %(message)s',
	filename = 'server_logs.txt',
	filemode = 'w'
)

def handle_client(conn, addr):
	print(f"[NEW CONNECTION] {addr} connected.")
	logging.info(f"New connection from {addr}")

	connected = True
	while connected:
		encrypted_msg = conn.recv(1024)
		if not encrypted_msg:
			break

		msg = decrypt_message(encrypted_msg)

		logging.info(f"Received from {addr}: {msg}")
		print(f"[{addr}] {msg}")

		acknowledgement = encrypt_message("Message Received")
		conn.send(acknowledgement)

	conn.close()
	clients.remove(conn)
	logging.info(f"{addr} disconnected.")
	print(f"[CONNECTION CLOSED] {addr} removed.")

def start():
	server.listen(5)
	print(f"[LISTENING] Server is listening on {SERVER}:{PORT}")
	while True:
		conn, addr = server.accept()
		thread = threading.Thread(target=handle_client, args=(conn, addr))
		thread.start()
		clients.append(conn)
		print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

print("[STARTING] server is starting...")
start()
