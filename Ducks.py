from abc import abstractmethod, ABC

class FlyBehavior(ABC):
    def fly(self):
        pass

class QuackBehavior(ABC):
    @abstractmethod
    def quack(self):
        ...
    
class SimpleQuack(QuackBehavior):
    def quack(self):
        print("Quack :)")

# Main concrete class for dock
class Duck:
    flyBehavior: FlyBehavior
    quackBehavior: QuackBehavior # Behavior Interface type
    
    def performFly(self):
        ...
        
    def performQuack(self):
        SimpleQuack.quack()
        
    def swim(self):
        print("All docks can Swim")
    

dck = SimpleQuack()
dck.quack()