from abc import ABC, abstractmethod

class Shape(ABC): 
    def __init__(self,name):
        self.name = name

    @abstractmethod
    def area(self):
        pass
