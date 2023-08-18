from Animal import Animal
from Land import Land
class Cat(Animal,Land):
    def __init__(self) :
        Animal.__init__(self, mammals=True,carnivorous=True)
        Land.__init__(self, number_of_legs=4)
       

    def say_hello(self,mode=None):
        if mode is None:
            print("meow")
        if mode==1:
            print("The cat is meow in usual")
        elif mode==2:
            print("when they are in a good mood, they make a purr, purr sound")
        elif mode==3:
            print("and when they are frightened, they make a hiss sound")

    
    
   


    