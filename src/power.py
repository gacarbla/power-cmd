from .prick.toolkit import Clear, Font
from .prick.routing import Structure
from .prick.history import History
from .Pages import Routing as Page_Routing
from .Help import Routing as Help_Routing
from .Config import Routing as Config_Routing
import os

tcolor = Font.Color.Text

page_routing = Page_Routing()
help_routing = Help_Routing()
config_routing = Config_Routing()

class Menu:
    def __init__(self):
        self.history = self.History()
        self.Show_Menu(Menu.Structure.home)

    History = History
    Structure = Structure
    emoji_map = {
        "return": "↪️",
        "page": "📄",
        "menu": "📂",
        "help": "❓",
        "config": "⚙️",
        "web": "🌐"
    }

    def Show_Menu(self, menuName):
        self.history.add(menuName)
        Clear.Auto()
        menu = Menu.Structure.E404
        if hasattr(Menu.Structure, menuName):
            menu = getattr(Menu.Structure, menuName)
        meta_items = [(name, value) for name, value in vars(menu).items() if isinstance(value, str) and value.startswith("!")]
        for index, (name, value) in enumerate(meta_items, 1):
            print(value.split(":")[1])
        menu_items = [(name, value) for name, value in vars(menu).items() if isinstance(value, str) and value.startswith("?")]
        for index, (name, value) in enumerate(menu_items, 0):
            parts = value[1:].split(":")
            if len(parts) == 2:
                symbol = tcolor.LIGHTGREEN  +"<"+parts[1]+">"+tcolor.RESET
            else:
                symbol = ""
            emoji = Menu.emoji_map.get(parts[0], None)
            print(f" {emoji} ({index}) {name} {symbol}")
        print("\n")
        typed = input(f" {tcolor.YELLOW}>_{tcolor.RESET} ")
        if typed.lower() != "exit":
            try:
                typed = int(typed)
                if typed < 0 or typed >= len(menu_items):
                    int("a")
                parts = menu_items[typed][1][1:].split(":")
                if parts[0] == "return":
                    if (menu_items[typed][0].lower() != "exit"):
                        self.Show_Menu(self.history.list[-2])
                elif parts[0] == "page":
                    page_routing[parts[1]].run()
                elif parts[0] == "menu":
                    self.Show_Menu(parts[1])
                elif parts[0] == "help":
                    help_routing[parts[1]].run()
                elif parts[0] == "config":
                    config_routing[parts[1]].run()
            except ValueError as e:
                self.Show_Menu(Menu.Structure.notfound)
            except Exception as e:
                Clear.Auto()
                print(tcolor.YELLOW+"<!> ERROR FOUND ON CODE [e02.01]"+"\n"*2+tcolor.RED)
                print(e)
                print("\n"*2+tcolor.RESET)
                print("If you read this while running:\n\tPlease report the error at the GitHub repositorie and help the community.\n\nPress any key to continue.")
                os.system("pause > nul")