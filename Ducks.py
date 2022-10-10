import abc
from time import sleep
import pygame
from abc import abstractmethod, ABC

from FlyBehaviors import *
from QuackBehaviors import *

pygame.init()
pygame.mixer.init()

# -=-=-=-=- Main Duck classes -=-=-=-=- #
class Duck(ABC):
    flyBehavior: FlyBehaviorInterface
    quackBehavior: QuackBehaviorInterface # Behavior Interface type
    
    def performFly(self):
        if not isinstance(self.flyBehavior, FlyBehaviorInterface):
            raise TypeError("QuackBehavior should be an instance of FlyBehaviorInterface")
            
        self.flyBehavior.fly()
        
    def performQuack(self):
        if not isinstance(self.quackBehavior, QuackBehaviorInterface):
            raise TypeError("QuackBehavior should be an instance of QuackBehaviorInterface")
            
        self.quackBehavior.quack()
        
    @abstractmethod
    def display(self):
        ...
    
    def swim(self):
        print("All docks can Swim")

# Duck types 
class SimpleDuck(Duck):
    flyBehavior = FlyWithWings()
    quackBehavior = SimpleQuack()
    
    def display(self):
        print("this is a simple duck")
        
class RubberDuck(Duck):
    flyBehavior = FlyNoWay()
    quackBehavior = SquackQuack()
    
    def display(self):
        print("this is a rubber duck")
    
    
rubber_duck = RubberDuck()
rubber_duck.performQuack()

sleep(2)

simple_duck = SimpleDuck()
simple_duck.performQuack()


