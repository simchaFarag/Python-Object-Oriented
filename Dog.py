from typing import Optional
from Animal import Animal
from Land import Land
class Dog(Animal,Land):
    def __init__(self) :
        Animal.__init__(self, mammals=True,carnivorous=True)
        Land.__init__(self, number_of_legs=4)
    
    def say_hello(self,mode=None):
        if mode is None: 
            print("wagging their tails")
        elif mode==1:
            print("The dog is wagging their tails in usual")
        elif mode==2:
            print("The dog  they will bark loudly when  feel comfortable being touched")
        elif mode==3 :
            print("whooping when they frightened and upset")

