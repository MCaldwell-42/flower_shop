from . import Flower
from . import Organic

class Poppy(Flower, Organic):
    def __init__(self):
        Flower.__init__(self, "PURPLE!")
        self.stem_length = 4
        Organic.__init__(self)