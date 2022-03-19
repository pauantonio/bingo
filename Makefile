.PHONY: resources gui

all: gui
	pyinstaller --clean --noconsole --onefile --icon=resources/icona.ico bingo.py

temp:
	mkdir temp

resources: temp
	pyrcc5 -o temp/resources_rc.py resources/resources.qrc

gui: resources
	pyuic5 -o temp/bingo_window.py gui/bingo.ui
	pyuic5 -o temp/popup_bingo_window.py gui/popup_bingo.ui
	pyuic5 -o temp/popup_linia_window.py gui/popup_linia.ui

run: gui
	python3 bingo.py
	
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
	rm -rf temp
	rm -f bingo.spec
