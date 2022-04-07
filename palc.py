# Palculator is a Free & Open-Source GTK-Based calculator written in python

import gi
import sys
import webbrowser

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from gi.repository import Gio


class palc(Gtk.Window):
    def __init__(self):
        super().__init__(title="palculator")

        self.full_query = ""

        ans = ""

        self.display = Gtk.Label()
        grid = Gtk.Grid()

        self.about_button = Gtk.Button("About")
        self.about_button.connect("clicked", self.about_win)

        self.menu_bar =Gtk.MenuBar()
        self.file = Gtk.MenuItem("File")
        self.edit = Gtk.MenuItem("Edit")
        self.view = Gtk.MenuItem("View")
        self.help = Gtk.MenuItem("Help")

        self.filemenu = Gtk.Menu()
        self.quit = Gtk.ImageMenuItem("Quit")
        self.filemenu.append(self.quit)
        self.file.set_submenu(self.filemenu)

        self.viewmenu = Gtk.Menu()
        self.show_display = Gtk.MenuItem("Show Display")
        self.show_numbers = Gtk.MenuItem("Show Numbers")
        self.show_operations = Gtk.MenuItem("Show Operations")
        self.show_menu_bar = Gtk.MenuItem("Show Menubar")
        self.viewmenu.append(self.show_display)
        self.viewmenu.append(self.show_numbers)
        self.viewmenu.append(self.show_operations)
        self.viewmenu.append(self.show_menu_bar)
        self.view.set_submenu(self.viewmenu)

        self.helpmenu = Gtk.Menu()
        self.about = Gtk.MenuItem(label="About")
        self.about.connect("activate", self.about_win)
        self.source_code = Gtk.MenuItem(label="Source on Github")
        self.source_code.connect("activate", self.source_code_clicked)
        self.helpmenu.append(self.about)
        self.helpmenu.append(self.source_code)
        self.help.set_submenu(self.helpmenu)

        self.menu_bar.append(self.file)
        self.menu_bar.append(self.edit)
        self.menu_bar.append(self.view)
        self.menu_bar.append(self.help)

        grid.attach(self.menu_bar, 0, 0, 4, 1)

        grid.attach(self.display, 0, 1, 2, 2)
        grid.attach(self.about_button, 0, 7, 2, 1)

        self.add(grid)

        self.plus = Gtk.Button(label="+", halign=Gtk.Align.START)
        self.plus.connect("clicked", self.on_button_clicked)
        self.add(self.plus)

        self.equals = Gtk.Button(label="=", halign=Gtk.Align.START)
        self.equals.connect("clicked", self.on_button_clicked)
        self.add(self.equals)

        self.seven = Gtk.Button(label="7", halign=Gtk.Align.START)
        self.seven.connect("clicked", self.on_button_clicked)
        self.add(self.seven)

        self.eight = Gtk.Button(label="8", halign=Gtk.Align.START)
        self.eight.connect("clicked", self.on_button_clicked)
        self.add(self.eight)

        self.nine = Gtk.Button(label="9", halign=Gtk.Align.START)
        self.nine.connect("clicked", self.on_button_clicked)
        self.add(self.nine)

        self.four = Gtk.Button(label="4", halign=Gtk.Align.START)
        self.four.connect("clicked", self.on_button_clicked)
        self.add(self.four)

        self.five = Gtk.Button(label="5", halign=Gtk.Align.START)
        self.five.connect("clicked", self.on_button_clicked)
        self.add(self.five)

        self.six = Gtk.Button(label="6", halign=Gtk.Align.START)
        self.six.connect("clicked", self.on_button_clicked)
        self.add(self.six)

        self.one = Gtk.Button(label="1", halign=Gtk.Align.START)
        self.one.connect("clicked", self.on_button_clicked)
        self.add(self.one)

        self.two = Gtk.Button(label="2", halign=Gtk.Align.START)
        self.two.connect("clicked", self.on_button_clicked)
        self.add(self.two)

        self.three = Gtk.Button(label="3", halign=Gtk.Align.START)
        self.three.connect("clicked", self.on_button_clicked)
        self.add(self.three)

        self.backspace = Gtk.Button(label="←", halign=Gtk.Align.START)
        self.backspace.connect("clicked", self.on_button_clicked)
        self.add(self.backspace)

        self.reset = Gtk.Button(label="C", halign=Gtk.Align.END)
        self.reset.connect("clicked", self.on_button_clicked)
        self.add(self.reset)

        self.times = Gtk.Button(label="×", halign=Gtk.Align.END)
        self.times.connect("clicked", self.on_button_clicked)
        self.add(self.times)

        self.zero = Gtk.Button(label="0", halign=Gtk.Align.END)
        self.zero.connect("clicked", self.on_button_clicked)
        self.add(self.zero)

        self.minus = Gtk.Button(label="-", halign=Gtk.Align.END)
        self.minus.connect("clicked", self.on_button_clicked)
        self.add(self.minus)

        self.addtogether = Gtk.Button(label="+", halign=Gtk.Align.END)
        self.addtogether.connect("clicked", self.on_button_clicked)
        self.add(self.addtogether)

        self.equals = Gtk.Button(label="=", halign=Gtk.Align.START)
        self.equals.connect("clicked", self.on_equals_clicked)
        self.add(self.equals)

        self.point = Gtk.Button(label=".", halign=Gtk.Align.START)
        self.point.connect("clicked", self.on_button_clicked)
        self.add(self.point)

        self.floaty = Gtk.Button(label="+/-", halign=Gtk.Align.START)
        self.floaty.connect("clicked", self.on_button_clicked)
        self.add(self.floaty)

        self.divide = Gtk.Button(label="÷", halign=Gtk.Align.START)
        self.divide.connect("clicked", self.on_button_clicked)
        self.add(self.divide)

        self.square = Gtk.Button(label="𝑥²", halign=Gtk.Align.START)
        self.square.connect("clicked", self.on_button_clicked)
        self.add(self.square)

        grid.attach(self.seven, 0, 3, 1, 1)
        grid.attach(self.eight, 1, 3, 1, 1)
        grid.attach(self.nine, 2, 3, 1, 1)
        grid.attach(self.four, 0, 4, 1, 1)
        grid.attach(self.five, 1, 4, 1, 1)
        grid.attach(self.six, 2, 4, 1, 1)
        grid.attach(self.one, 0, 5, 1, 1)
        grid.attach(self.two, 1, 5, 1, 1)
        grid.attach(self.three, 2, 5, 1, 1)
        grid.attach(self.zero, 1, 6, 1, 1)
        grid.attach(self.backspace, 3, 2, 1, 1)
        grid.attach(self.reset, 3, 1, 1, 1)
        grid.attach(self.times, 3, 3, 1, 1)
        grid.attach(self.minus, 3, 4, 1, 1)
        grid.attach(self.addtogether, 3, 5, 1, 1)
        grid.attach(self.equals, 3, 7, 1, 1)
        grid.attach(self.point, 2, 6, 1, 1)
        grid.attach(self.floaty, 0, 6, 1, 1)
        grid.attach(self.divide, 3, 6, 1, 1)

    def source_code_clicked(self, widget):
        webbrowser.open("https://github.com/yuckdevchan/palculator")

    def on_button_clicked(self, widget):
        if widget.get_label() == "C":
            self.display.set_markup("")
            self.full_query = ""
            return
        elif widget.get_label() == "←":
            self.full_query = self.full_query[0:-1]
            self.display.set_markup(self.full_query)
            return

        keymap = {"×":"*", "+/-":"*-1", "𝑥²":"**2", "÷":"/"}
        new_entry = str(widget.get_label())
        if new_entry in keymap:
            new_entry = keymap[new_entry]
        print(widget.get_label()+" was pressed")
        self.full_query = self.full_query + new_entry
        print(self.full_query)
        self.display.set_markup(self.full_query)

    def on_equals_clicked(self, widget):
        ans = eval(self.full_query)
        self.display.set_markup(str(ans))
        print("The answer is " + str(ans))
        self.full_query = str(ans)

    def about_win(self, widget):
        about = Gtk.AboutDialog()
        about.set_program_name("palculator")
        about.set_version("v1.0 Pre-Release 1")
        about.set_copyright("🄯 Copyleft GPL-v2 License")
        about.set_comments("A GTK Python 3 calculator with less than 200 lines of code.")
        about.set_website("https://github.com/yuckdevchan/palculator")

        image = Gtk.Image()
        image.set_from_file("palculator64.png")
        pixbuf = image.get_pixbuf()

        about.set_logo(pixbuf)
        about.run()
        about.destroy()

def main():
    win = palc()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()


if __name__ == "__main__":
    main()
