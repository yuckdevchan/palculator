# palculator

palculator is a free & open-source [GTK](https://gtk.org) calculator for Windows, Mac and GNU / Linux written in [Python](https://python.org).

### To Compile into GNU / Linux executable file on GNU / Linux (and other unix-like, various BSDs):

- `git clone https://github.com/yuckdevchan/palculator`
- `cd palculator`
- `sudo pip3 install pyinstaller`
- `pyinstaller --onefile palc.py`

### To Compile into a Microsoft Windows executable file on Microsoft Windows:

Follow [this guide](https://pygobject.readthedocs.io/en/latest/getting_started.html#windows-getting-started) on the PyGObject Documentation: 

Then in the msys2 command prompt, run 

- `pacman -Sy mingw-w64-python-pip`
- `pip install pyinstaller`

Then change directory into the palculator source code folder and run this command:

- `pyinstaller palc.py`
- `cd dist`
- `./palc`

### macOS specific:
- You should be on the latest macOS
- Install homebrew at https://brew.sh
- run: brew install pygobject3 gtk+3
- git clone https://github.com/yuckdevchan/palculator
- cd palculator
- python palc.py

## Known Issues

- Tiling Window Managers do not play nicely with it
- Resizing is a bit sussy
- Buttons are offset
- No icons for backspace and positive/negative buttons
