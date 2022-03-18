# palculator

palculator is a free & open-source GTK calculator for Windows & Linux written in Python.

To Compile into Linux executable file:

`
git clone https://github.com/yuckdevchan/palculator`
(Clones into palculator git repo)
`cd palculator`
(Changes working directory to palculator)
`sudo pip3 install pyinstaller`
(Install pyinstaller with the pip package manager)
`sudo pyinstaller --onefile palc.py`
(Compiles all needed python and GTK libraries and source code into one executable file)
`cd dist`
(Changes working directory to dist)
`sudo chmod +x palc`
(Makes palc executable)
`./palc`
(Executes palc)
