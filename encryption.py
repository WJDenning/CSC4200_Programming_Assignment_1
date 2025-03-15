from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad, unpad
import os

key = b'This is a key123This is a key123'

def encrypt_message(plaintext):
	iv = os.urandom(16)
	cipher = AES.new(key, AES.MODE_CBC, iv)
	ciphertext = cipher.encrypt(pad(plaintext.encode(), AES.block_size))
	return iv + ciphertext

def decrypt_message(ciphertext):
	iv = ciphertext[:16]
	cipher = AES.new(key, AES.MODE_CBC, iv)
	plaintext = unpad(cipher.decrypt(ciphertext[16:]), AES.block_size)
	return plaintext.decode()
