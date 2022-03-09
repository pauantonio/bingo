gui:
	pyuic5 -o bingo_window.py bingo.ui

run: gui
	python3 bingo.py
	
build:
	pyinstaller --noconsole --onefile bingo.py --clean
	
setup:
	pip install pyinstaller
	pip install pyqt5
	
clean:
	rm -rf __pycache__
