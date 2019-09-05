from . import Flower

class Rose(Flower):
    def __init__(self, color):
        # if self.color == "red" or "blue" or "purple":
        Flower.__init__(self, color)
        self.stem_length = 7
        # else:
        #     pass