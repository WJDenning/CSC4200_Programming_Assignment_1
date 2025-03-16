install: requirements.txt
	pip3 install -r requirements.txt

run:
	python3 client.py
	python3 server.py

clean:
	rm -rf __pycache__
