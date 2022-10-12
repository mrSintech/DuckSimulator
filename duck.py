from abc import abstractmethod, ABC
from tkinter.messagebox import NO
from flyBehaviors import *
from quackBehaviors import *

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
        
    def setQuackBehavior(self, qb):
        self.quackBehavior = qb
        
    def setFlyBehavior(self, fb):
        self.flyBehavior = fb

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
        
class MallardDuck(Duck):
    flyBehavior = FlyWithWings()
    quackBehavior = MallardQuack()
    
    def display(self):
        print("this is a Mallard duck")

class ModelDuck(Duck):
    flyBehavior = FlyNoWay()
    quackBehavior = MuteQuack()
    
    def display(self):
        print("I'm a useless Model Duck")







