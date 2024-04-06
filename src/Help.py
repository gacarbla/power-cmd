from .help import Config

class Routing:
    def __init__(self):
        self.pages = {
            "Config": Config.Start()
        }

    def __getitem__(self, key):
        return self.pages.get(key, None)

    def __setitem__(self, key, value):
        self.pages[key] = value