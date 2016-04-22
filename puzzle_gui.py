import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

class PuzzleGUI:

    def __init__(self):
        self.build_interface()
        self.register_handlers()
        return

    def build_interface(self):
        self.title = Gtk.Label("PUZZLE")
        self.title.set_margin_top(5)
        self.title.set_margin_bottom(10)
        self.title.set_name("game_name")
        self.title.show()


        self.buttons = []
        self.grid = Gtk.Grid()

        for i in range(4):
            for j in range(4):
                button = Gtk.Button(str(i * 4 + j + 1))
                button.set_size_request(40, 40)
                button.show()
                self.buttons.append(button)
                self.grid.attach(button, j, i, 1, 1)
                self.grid.show()
        

 
        self.label = Gtk.Label("Click a button")
        self.label.set_margin_top(15)
        self.label.set_margin_bottom(10)
        self.label.set_name("title")
        self.label.show()

        # self.grid2 = Gtk.Grid()
        self.newGame_button = Gtk.Button("New Game")
        self.newGame_button.show()
        self.quit_button = Gtk.Button("Quit")
        self.quit_button.show()
        # self.grid2.attach(self.newGame_button)
        # self.grid2.attach(self.quit_button)
        # self.grid.show()


       
        self.container = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        self.container.set_border_width(20)
        self.container.pack_start(self.title, True, True, 0)
        self.container.pack_start(self.grid, True, True, 0)
        self.container.pack_start(self.label, False, False, 0)
        self.container.pack_start(self.newGame_button, False, False, 0)
        self.container.pack_start(self.quit_button, False, False, 0)
        self.container.show()

    
        self.window = Gtk.Window(Gtk.WindowType.TOPLEVEL, title="Puzzle")
        self.window.add(self.container)
        self.window.show()

        
        style_provider = Gtk.CssProvider()
        style_provider.load_from_path('style.css')
        screen = Gdk.Screen.get_default()
        style_context = Gtk.StyleContext()
        style_context.add_provider_for_screen(screen, style_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

        return

    def register_handlers(self):
        self.window.connect('delete-event', self.delete_event_handler)
        self.window.connect('destroy', self.destroy_handler)
        self.newGame_button.connect('clicked', self.newGame_handler)
        self.quit_button.connect('clicked', self.destroy_handler)

        for i in range(len(self.buttons)):
            button = self.buttons[i]
            button.connect('clicked', self.button_handler, i)
            self.grid.show()

        return


    def run(self):
        Gtk.main()
        return

    def delete_event_handler(self, widget, event, data=None):
        return False

    def destroy_handler(self, widget, data=None):
        Gtk.main_quit()
        return

    def button_handler(self, widget, data=None):
        self.label.set_text("#" + str(data + 1) + " clicked")
        for i in range(len(self.buttons)):
            button = self.buttons[i]
            Gtk.Widget.show(button)

        button = self.buttons[data]
        Gtk.Widget.hide(button)

        return

    def newGame_handler(self, widget, data=None):
        self.label.set_text("New Game clicked")
        return
    
