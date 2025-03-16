import socket
from encryption import encrypt_message, decrypt_message

HOST = socket.gethostbyname(socket.gethostname())
PORT = 5050
ADDR = (HOST, PORT)

def start_client():
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client.connect(ADDR)

	print(f"Connected to server at {HOST}:{PORT}, type your message.")
	print("Type 'exit' to disconnect.")

	while True:
		message = input("> ")
		if message.lower() == "exit":
			break
		encrypted_message = encrypt_message(message)
		client.send(encrypted_message)

		encrypted_acknowledgement = client.recv(1024)
		acknowledgement = decrypt_message(encrypted_acknowledgement)
		print(f"Server: {acknowledgement}")

	client.close()
	print("Disconnected from the server.")

start_client()
