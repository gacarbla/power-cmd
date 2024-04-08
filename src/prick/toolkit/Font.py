from configparser import ConfigParser
from ..fileroutes import FRoutues

class Back:
    def __init__(self):
        Config_file = FRoutues.config
        Parser = ConfigParser()
        Parser.read(Config_file)
        self.enabled = (Parser["Settings"]["Color"] == "y")

        self.BLACK           = "\033[40m" if self.enabled else "\033[49m"
        self.RED             = "\033[41m" if self.enabled else "\033[49m"
        self.GREEN           = "\033[42m" if self.enabled else "\033[49m"
        self.YELLOW          = "\033[43m" if self.enabled else "\033[49m"
        self.BLUE            = "\033[44m" if self.enabled else "\033[49m"
        self.MAGENTA         = "\033[45m" if self.enabled else "\033[49m"
        self.CYAN            = "\033[46m" if self.enabled else "\033[49m"
        self.WHITE           = "\033[47m" if self.enabled else "\033[49m"
        self.RESET           = "\033[49m" if self.enabled else "\033[49m"
        self.LIGHTBLACK      = "\033[100m" if self.enabled else "\033[49m"
        self.LIGHTRED        = "\033[101m" if self.enabled else "\033[49m"
        self.LIGHTGREEN      = "\033[102m" if self.enabled else "\033[49m"
        self.LIGHTYELLOW     = "\033[103m" if self.enabled else "\033[49m"
        self.LIGHTBLUE       = "\033[104m" if self.enabled else "\033[49m"
        self.LIGHTMAGENTA    = "\033[105m" if self.enabled else "\033[49m"
        self.LIGHTCYAN       = "\033[106m" if self.enabled else "\033[49m"
        self.LIGHTWHITE      = "\033[107m" if self.enabled else "\033[49m"

class Text:
    def __init__(self):
        Config_file = FRoutues.config
        Parser = ConfigParser()
        Parser.read(Config_file)
        self.enabled = (Parser["Settings"]["Color"] == "y")

        self.BLACK           = "\033[30m" if self.enabled else "\033[39m"
        self.RED             = "\033[31m" if self.enabled else "\033[39m"
        self.GREEN           = "\033[32m" if self.enabled else "\033[39m"
        self.YELLOW          = "\033[33m" if self.enabled else "\033[39m"
        self.BLUE            = "\033[34m" if self.enabled else "\033[39m"
        self.MAGENTA         = "\033[35m" if self.enabled else "\033[39m"
        self.CYAN            = "\033[36m" if self.enabled else "\033[39m"
        self.WHITE           = "\033[37m" if self.enabled else "\033[39m"
        self.RESET           = "\033[39m" if self.enabled else "\033[39m"
        self.LIGHTBLACK      = "\033[90m" if self.enabled else "\033[39m"
        self.LIGHTRED        = "\033[91m" if self.enabled else "\033[39m"
        self.LIGHTGREEN      = "\033[92m" if self.enabled else "\033[39m"
        self.LIGHTYELLOW     = "\033[93m" if self.enabled else "\033[39m"
        self.LIGHTBLUE       = "\033[94m" if self.enabled else "\033[39m"
        self.LIGHTMAGENTA    = "\033[95m" if self.enabled else "\033[39m"
        self.LIGHTCYAN       = "\033[96m" if self.enabled else "\033[39m"
        self.LIGHTWHITE      = "\033[97m" if self.enabled else "\033[39m"



class Color:
    Back = Back()

    Text = Text()