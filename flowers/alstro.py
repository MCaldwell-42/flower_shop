from . import Flower

class Alstro(Flower):
    def __init__(self):
        Flower.__init__(self, "pink")
        self.stem_length = 7