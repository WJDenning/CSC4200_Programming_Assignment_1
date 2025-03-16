# Client Server Communication
  The client and server for this project communicate through the ip address of the local machine running the program on port 5050
  The client and server communicate through a tcp connection using the python socket library 
  The server listens for a connection and then waits for an encrypted message to be sent and then decrypts it
  The server then sends an encrypted acknowledgement to the client and logs the interaction
  The client then decrypts the acknowledgement and displays it

# Multi-Client support approach
  This project uses pythons threading module to listen to multiple clients at once, each on a separate thread

# Data Encryption
  Message are AES encrypted and decrypted with a key that both the client and server have access to
  Use python pycryptodome libarary for encryption
