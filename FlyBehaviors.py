# -=-=-=-=-=-=- FlyBehaviors -=-=-=-=-=-=- #
# interface
from abc import ABC, abstractmethod


class FlyBehaviorInterface(ABC):
    @abstractmethod
    def fly(self):
        ...

# sets 
class FlyWithWings(FlyBehaviorInterface):
    def fly(self):
        print("I'm Flying with wings!")
        
class RocketPoweredFly(FlyBehaviorInterface):
    def fly(self):
        print("I'm flying with a freaking Rocket!")
        
class FlyNoWay(FlyBehaviorInterface):
    def fly(self):
        print("This Duck can't FLY")
        
        
        
        
        
        
        
        
        
        
        
        
        
        