from flowers import Daisy
from flowers import Rose
from flowers import Alstro
from flowers import BabyBreath
from flowers import Lily
from flowers import Poppy
from arrangements import MothersDay
from arrangements import ValentinesDay






momsFlowers = MothersDay()
valsFlowers = ValentinesDay()



daisy1 = Daisy()
rose1 = Rose("red")
rose2 = Rose("purple")
alstro1 = Alstro()
lily1 = Lily()
poppy1 = Poppy()
baby1 = BabyBreath()

valsFlowers.enhance(rose1)
valsFlowers.enhance(rose2)
valsFlowers.enhance(lily1)
valsFlowers.enhance(alstro1)

momsFlowers.enhance(daisy1)
momsFlowers.enhance(baby1)
momsFlowers.enhance(poppy1)