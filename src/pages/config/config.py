from ...prick.toolkit import Clear, Font, Language
from configparser import ConfigParser
from ...prick.fileroutes import FRoutues
from time import sleep
import keyboard

default = {
    "1": False,  #esc
    "72": False, #up
    "75": False, #left
    "80": False, #down
    "77": False, #right
    "28": False, #intro
    "14": False, #back
}

keymap = default.copy()
trans = Language.Translation.Translate_Language
keymapCache = None
selected = 1
optionSelected = 0
option_move = 0
filename = None

class Start:

    options = [
        {
            "name": "Language",
            "variable": "language",
            "type": "select",
            "options": [
                {
                    "name": "English",
                    "default": True,
                    "value": "english"
                },
                {
                    "name": "Español",
                    "default": False,
                    "value": "spanish"
                },
                {
                    "name": "Français",
                    "default": False,
                    "value": "french"
                },
            ]
        },
        {
            "name": "Colors",
            "variable": "color",
            "type": "select",
            "options": [
                {
                    "name": "Yes",
                    "default": True,
                    "value": "y"
                },
                {
                    "name": "No",
                    "default": False,
                    "value": "n"
                },
            ]
        }
    ]

    @staticmethod
    def run():
        Clear.Auto()
        keyboard.on_press(Start.handler)
        Start.loop()

    @staticmethod
    def loop():
        global keymap, keymapCache, selected, optionSelected, option_move, filename
        while True:
            if (keymap != keymapCache):
                filename = Language.Translation.Get_Language()
                filename
                Config_file = FRoutues.config
                Parser = ConfigParser()
                Parser.read(Config_file)
                Clear.Auto()
                if (keymap["1"] and selected == 1):
                    keymap = default.copy()
                    break
                elif (keymap["28"]):
                    keymap = default.copy()
                    selected = 1
                elif (keymap["72"]):   # UP
                    keymap["72"] = False
                    if (not selected):
                        selected = len(Start.options)
                    elif (selected > 1):
                        selected = selected - 1
                elif (keymap["80"]): # DOWN
                    keymap["80"] = False
                    if (not selected):
                        selected = 1
                    elif (selected < len(Start.options)):
                        selected = selected + 1
                elif (keymap["75"]): # LEFT
                    keymap["75"] = False
                    option_move = -1 if optionSelected > 0 else 0
                elif (keymap["77"]): # RIGHT
                    keymap["77"] = False
                    option_move = 1 if optionSelected < len(Start.options[selected-1]["options"])-1 else 0
                print(Font.Color.Text.GREEN+trans(filename, "Config", "title")+Font.Color.Text.RESET)
                print("\n"*2)
                for index, (value) in enumerate(Start.options, 1):
                    option_value = -1
                    default_value = -1
                    setted = Parser["Settings"][value["variable"]]
                    for i, (opcion) in enumerate(value["options"], 1):
                        if (opcion["value"] == setted):
                            option_value = i-1
                        elif (opcion["default"]):
                            default_value = i-1
                    valor_ajuste = ""
                    option_value = default_value if option_value < 0 else option_value
                    option_value = option_value + option_move if selected == index else option_value
                    option_move = 0 if selected == index else option_move
                    optionSelected = option_value if selected == index else optionSelected
                    valor_ajuste = value["options"][option_value]["name"]
                    Parser.set("Settings", value["variable"], value["options"][option_value]["value"])
                    with open(FRoutues.config, 'w') as configfile:
                        Parser.write(configfile)
                    condition = selected and selected == index
                    tcolor = Font.Color.Text
                    title = f"{tcolor.LIGHTBLUE if condition else tcolor.WHITE} {"→" if condition else " "} {value['name']} {"."*(33-len(value["name"]))} "
                    label = f"{tcolor.YELLOW}{"<"if condition else " "} {valor_ajuste} {" "*(10-len(valor_ajuste))} {">"if condition else " "}{tcolor.RESET}"
                    print(f"{title} {label}")
                print("\n"*2)
                print(f"\t{tcolor.LIGHTMAGENTA}[ESC] {tcolor.WHITE}{trans(filename, "Config", "navigation_esc")}{" "*(15-len(trans(filename, "Config", "navigation_esc")))}{tcolor.LIGHTMAGENTA}[ENT] {tcolor.WHITE}{trans(filename, "Config", "navigation_debug")}")
                print(f"\t{tcolor.LIGHTMAGENTA}[↑/↓] {tcolor.WHITE}{trans(filename, "Config", "navigation_1")}{" "*(15-(len(trans(filename, "Config", "navigation_1"))))}{tcolor.LIGHTMAGENTA}[←/→] {tcolor.WHITE}{trans(filename, "Config", "navigation_2")}")
                keymapCache = keymap.copy()
            sleep(0.05)

    @staticmethod
    def handler(event):
        f = keymap.get(f"{event.scan_code}", None)
        if f is not None:
            keymap[f"{event.scan_code}"] = True
