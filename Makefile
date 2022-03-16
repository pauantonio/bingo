gui:
	pyuic5 -o bingo_window.py bingo.ui
	pyuic5 -o popup_bingo_window.py popup_bingo.ui
	pyuic5 -o popup_linia_window.py popup_linia.ui

run: gui
	python3 bingo.py
	
build:
	pyinstaller --clean --noconsole --onefile --icon=icona.ico bingo.py
	
setup:
	sudo apt-get install python3-pip
	sudo pip3 install pyinstaller
	sudo pip3 install pyqt5
	sudo pip3 install pyqt5-tools
	sudo apt-get install python3-tk
	
clean:
	rm -rf __pycache__
	rm -rf build
	rm -rf dist
