from . import Flower
from . import Organic

class Daisy(Flower, Organic):
    def __init__(self):
        Flower.__init__(self, "white")
        self.stem_length = 4
        Organic.__init__(self)

