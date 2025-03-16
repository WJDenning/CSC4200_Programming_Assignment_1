install: requirements.txt
	pip3 install -r requirements.txt

runClient:
	python3 client.py

runServer:
	python3 server.py

clean:
	rm -rf __pycache__
