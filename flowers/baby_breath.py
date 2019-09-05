from . import Flower
from . import Organic

class BabyBreath(Flower, Organic):
    def __init__(self):
        Flower.__init__(self, "purple?")
        self.stem_length = 4
        Organic.__init__(self)