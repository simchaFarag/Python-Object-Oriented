from abc import ABC ,abstractmethod
from typing import Optional
class Animal(ABC ):
    def __init__(self, mammals,carnivorous):
        self.__mammals=mammals
        self.__carnivorous=carnivorous

    @abstractmethod 
    def say_hello(self, mood=None):
       pass

    def is_mammals(self):
        return self.__mammals

    def is_carnivorous(self):
        return self.__carnivorous
    