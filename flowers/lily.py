from . import Flower

class Lily(Flower):
    def __init__(self):
        Flower.__init__(self, "orange")
        self.stem_length = 7