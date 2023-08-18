from Animal import Animal
from Land import Land
from Water import Water
class Frog(Animal,Land,Water):
    def __init__(self) :
        Animal.__init__(self, mammals=False,carnivorous=False)
        Land.__init__(self, number_of_legs=2)
        Water.__init__(self,has_gills=False,has_lays_eggs=True)
    def Frog(self):
        return
        
    def say_hello(self,mode=None):
        if mode is None:
            print("kwa")
        if mode==1:
            print("good mood, it will sing quack quack quack on the shore")
        elif mode==2 :
            print("and when frightened, it will plop into the water")


    
    # def get_number_of_legs(self,number_of_legs):
    #     return number_of_legs