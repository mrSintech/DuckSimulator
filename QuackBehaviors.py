from abc import ABC, abstractmethod
import pygame
# -=-=-=-=-=-=- QuackBehaviors -=-=-=-=-=-=- #
# interface
class QuackBehaviorInterface(ABC):
    @abstractmethod
    def quack(self):
        ...
    
# sets
class SimpleQuack(QuackBehaviorInterface):
    def quack(self):
        file = "./static/sounds/simplequack.wav"
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
        pygame.event.wait()
        print("Simple Quack played")
        
class SquackQuack(QuackBehaviorInterface):
    def quack(self):
        file = "./static/sounds/rubberduck.wav"
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
        pygame.event.wait()
        print("Rubber Squack played")