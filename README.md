# palculator

# 231 Lines of code and counting...

palculator is a free & open-source GTK calculator for Windows, Mac and GNU / Linux written in Python.

### To Compile into GNU / Linux executable file on GNU / Linux (and other unix-like OS like macOS and various BSDs):

`git clone https://github.com/yuckdevchan/palculator && cd palculator && sudo pip3 install pyinstaller && pyinstaller --onefile palc.py`

### To Compile into a Microsoft Windows executable file on Microsoft Windows:

Follow this guide on the PyGObject Documentation: https://pygobject.readthedocs.io/en/latest/getting_started.html

Then in the msys2 command prompt, run 

`pip install pyinstaller`

Then change directory into the palculator source code folder and run this command:

`pyinstaller --onefile palc.py`

## Known Issues

- Tiling Window Managers do not play nicely with it
- Resizing is a bit sussy
- There is no divide
- There is no square number button
