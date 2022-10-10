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
        print("Flying with wings")
        
class FlyNoWay(FlyBehaviorInterface):
    def fly(self):
        print("dick duck cannot fly")