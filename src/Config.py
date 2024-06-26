from .pages.config import config

class Routing:
    def __init__(self):
        self.pages = {
            "config": config.Start()
        }

    def __getitem__(self, key):
        return self.pages.get(key, None)

    def __setitem__(self, key, value):
        self.pages[key] = value