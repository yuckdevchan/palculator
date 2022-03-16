#Palculator is a Free & Open-Source GTK-Based calculator written in python

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class palc(Gtk.Window):
    def __init__(self):
        super().__init__(title="equals")

        self.button = Gtk.Button(label="=")
        self.button.connect("clicked", self.on_button_clicked)
        self.add(self.button)

    def on_button_clicked(self, widget):
        print("user-press.equals")


win = palc()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
