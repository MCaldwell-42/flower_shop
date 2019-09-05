from . import Arrangement

class MothersDay(Arrangement):

    def __init__(self):
        super().__init__()

    def enhance(self, flower):
        try:
            if flower.organic == True:
                self.flowers.append(flower)
        except AttributeError as ex:
            print(f'{flower} can\'t be added to the arrangement because it isn\'t organic')
