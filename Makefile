gui:
	pyuic5 -o bingo_window.py bingo.ui

run: gui
	python3 bingo.py
	
build:
	pyinstaller --clean --noconsole --onefile --icon=icona.ico bingo.py
	
setup:
	sudo apt-get install python3-pip
	pip install pyinstaller
	pip install pyqt5
	pip install pyqt5-tools
	
clean:
	rm -rf __pycache__