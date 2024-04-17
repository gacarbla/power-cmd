class History:
    list = []
    def __init__(self):
        self.list = []
    def add(self, name):
        self.list.append(name)
        if (len(self.list) > 15):
            self.list.pop()