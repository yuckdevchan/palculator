# Palculator is a Free & Open-Source GTK-Based calculator written in python

import gi
import sys

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from gi.repository import Gio


class palc(Gtk.Window):
    def __init__(self):
        super().__init__(title="palculator")

        # self.register1 = ""
        # self.register2 = ""
        # self.register_op = None

        self.full_query = ""

        ans = ""

        self.display = Gtk.Label()

        menubar = Gtk.MenuBar()
        grid = Gtk.Grid()

        fmi = Gtk.MenuItem.new_with_label("File")

        menu = Gtk.Menu()
        emi = Gtk.MenuItem.new_with_label("Exit")
        menu.append(emi)

        fmi = Gtk.MenuItem.new_with_label("Help")

        menu = Gtk.Menu()
        emi = Gtk.MenuItem.new_with_label("About")
        menu.append(emi)

        fmi.set_submenu(menu)

        menubar.add(fmi)

        grid.attach(menubar, 0, 0, 1, 1)

        grid.attach(self.display, 0, 1, 2, 1)

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

        self.backspace = Gtk.Button(label="¬", halign=Gtk.Align.START)
        self.backspace.connect("clicked", self.on_button_clicked)
        self.add(self.backspace)

        self.reset = Gtk.Button(label="C", halign=Gtk.Align.END)
        self.reset.connect("clicked", self.on_button_clicked)
        self.add(self.reset)

        self.times = Gtk.Button(label="x", halign=Gtk.Align.END)
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

        grid.attach(self.seven, 0, 2, 1, 1)

        grid.attach(self.eight, 1, 2, 1, 1)

        grid.attach(self.nine, 2, 2, 1, 1)

        grid.attach(self.four, 0, 3, 1, 1)

        grid.attach(self.five, 1, 3, 1, 1)

        grid.attach(self.six, 2, 3, 1, 1)

        grid.attach(self.one, 0, 4, 1, 1)

        grid.attach(self.two, 1, 4, 1, 1)

        grid.attach(self.three, 2, 4, 1, 1)

        grid.attach(self.zero, 1, 5, 1, 1)

        grid.attach(self.backspace, 3, 1, 1, 1)

        grid.attach(self.reset, 3, 0, 1, 1)

        grid.attach(self.times, 3, 2, 1, 1)

        grid.attach(self.minus, 3, 3, 1, 1)

        grid.attach(self.addtogether, 3, 4, 1, 1)

        grid.attach(self.equals, 3, 5, 1, 1)

        grid.attach(self.point, 2, 5, 1, 1)

        grid.attach(self.floaty, 0, 5, 1, 1)

    def on_button_clicked(self, widget):
        if widget.get_label() == "C":
            self.display.set_markup("")
            self.full_query = ""
            return
        elif widget.get_label() == "¬":
            self.full_query = self.full_query[0:-1]
            self.display.set_markup(self.full_query)
            return
        
        keymap = {"x":"*", "+/-":"*-1"}
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

    # def on_button_clicked(self, widget):
    #     print(widget.get_label()+" was pressed")
    #
    #     if self.register_op is None and self.register2 == "" and self.register1 == "":
    #         self.register1 = self.register1 + str(widget.get_label())
    #         print("Register 1 is " + self.register1)
    #     elif self.register_op is not None and self.register2 =="" and self.register1 != "":
    #         self.register2 = self.register2 + str(widget.get_label())
    #         print("Register 2 is " + self.register2)
    #     else:
    #         self.register1 = ""
    #         self.register2 = ""
    #         self.register_op = None
    #
    # def on_button_clicked(self, widget):
    #     print(widget.get_label() + " was pressed")
    #
    #     if self.register1 != "" and self.register2 == "":
    #         self.register_op = str(widget.get_label())
    #         print("Operation Register is " + self.register_op)

def main():
    win = palc()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()


if __name__ == "__main__":
    main()
