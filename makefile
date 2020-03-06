#De momento aparece forbidden IP y termina la instalación del pre-install 
pre-install:
	sudo apt-get update
	sudo apt-get install python3-pip
	sudo apt-get install python3-invoke

install:
	pip install -r requirements.txt
