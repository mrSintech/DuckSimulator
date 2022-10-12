from duck import *

# -=-=-=-=- Implementing Ducks -=-=-=-=- #
rubber_duck = RubberDuck()
rubber_duck.performQuack()
rubber_duck.performFly()

simple_duck = SimpleDuck()
simple_duck.performQuack()
simple_duck.performFly()

mallard_duck = MallardDuck()
mallard_duck.performQuack()
mallard_duck.performFly()

model_duck = ModelDuck()
model_duck.performFly()
model_duck.setFlyBehavior(RocketPoweredFly())
model_duck.performFly()





