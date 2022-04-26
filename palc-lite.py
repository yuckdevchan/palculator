import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
class palc(Gtk.Window):
    def __init__(self):
        super().__init__(title="palculator")
        self.full_query = ""
        ans = ""
        self.display = Gtk.Label()
        self.grid = Gtk.Grid()
        self.grid.attach(self.display, 0, 1, 2, 2)
        self.add(self.grid)
        self.plus = Gtk.Button(label="+")
        self.plus.connect("clicked", self.on_button_clicked)
        self.equals = Gtk.Button(label="=")
        self.equals.connect("clicked", self.on_button_clicked)
        self.seven = Gtk.Button(label="7")
        self.seven.connect("clicked", self.on_button_clicked)
        self.eight = Gtk.Button(label="8")
        self.eight.connect("clicked", self.on_button_clicked)
        self.nine = Gtk.Button(label="9")
        self.nine.connect("clicked", self.on_button_clicked)
        self.four = Gtk.Button(label="4")
        self.four.connect("clicked", self.on_button_clicked)
        self.five = Gtk.Button(label="5")
        self.five.connect("clicked", self.on_button_clicked)
        self.six = Gtk.Button(label="6")
        self.six.connect("clicked", self.on_button_clicked)
        self.one = Gtk.Button(label="1")
        self.one.connect("clicked", self.on_button_clicked)
        self.two = Gtk.Button(label="2")
        self.two.connect("clicked", self.on_button_clicked)
        self.three = Gtk.Button(label="3")
        self.three.connect("clicked", self.on_button_clicked)
        self.backspace = Gtk.Button(label="←")
        self.backspace.connect("clicked", self.on_button_clicked)
        self.reset = Gtk.Button(label="C")
        self.reset.connect("clicked", self.on_button_clicked)
        self.times = Gtk.Button(label="×")
        self.times.connect("clicked", self.on_button_clicked)
        self.zero = Gtk.Button(label="0")
        self.zero.connect("clicked", self.on_button_clicked)
        self.minus = Gtk.Button(label="-")
        self.minus.connect("clicked", self.on_button_clicked)
        self.addtogether = Gtk.Button(label="+")
        self.addtogether.connect("clicked", self.on_button_clicked)
        self.equals = Gtk.Button(label="=")
        self.equals.connect("clicked", self.on_equals_clicked)
        self.point = Gtk.Button(label=".")
        self.point.connect("clicked", self.on_button_clicked)
        self.floaty = Gtk.Button(label="+/-")
        self.floaty.connect("clicked", self.on_button_clicked)
        self.divide = Gtk.Button(label="÷")
        self.divide.connect("clicked", self.on_button_clicked)
        self.grid.attach(self.seven, 0, 3, 1, 1)
        self.grid.attach(self.eight, 1, 3, 1, 1)
        self.grid.attach(self.nine, 2, 3, 1, 1)
        self.grid.attach(self.four, 0, 4, 1, 1)
        self.grid.attach(self.five, 1, 4, 1, 1)
        self.grid.attach(self.six, 2, 4, 1, 1)
        self.grid.attach(self.one, 0, 5, 1, 1)
        self.grid.attach(self.two, 1, 5, 1, 1)
        self.grid.attach(self.three, 2, 5, 1, 1)
        self.grid.attach(self.zero, 1, 6, 1, 1)
        self.grid.attach(self.backspace, 3, 2, 1, 1)
        self.grid.attach(self.reset, 1, 7, 1, 1)
        self.grid.attach(self.times, 3, 3, 1, 1)
        self.grid.attach(self.minus, 3, 4, 1, 1)
        self.grid.attach(self.addtogether, 3, 5, 1, 1)
        self.grid.attach(self.equals, 0, 6, 1, 1)
        self.grid.attach(self.point, 2, 6, 1, 1)
        self.grid.attach(self.floaty, 0, 7, 1, 1)
        self.grid.attach(self.divide, 3, 6, 2, 1)
    def on_button_clicked(self, widget):
        if widget.get_label() == "C":
            self.display.set_markup("")
            self.full_query = ""
            return
        elif widget.get_label() == "←":
            self.full_query = self.full_query[0:-1]
            self.display.set_markup(self.full_query)
            return
        keymap = {"×": "*", "+/-": "*-1", "÷": "/"}
        new_entry = str(widget.get_label())
        if new_entry in keymap:
            new_entry = keymap[new_entry]
        self.full_query = self.full_query + new_entry
        self.display.set_markup(self.full_query)   
    def on_equals_clicked(self, widget):
        ans = eval(self.full_query)
        self.display.set_markup(str(ans))
        self.full_query = str(ans)
def main():
    win = palc()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()
if __name__ == "__main__":
    main()
