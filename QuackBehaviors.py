from abc import ABC, abstractmethod
import simpleaudio as sa
# -=-=-=-=-=-=- QuackBehaviors -=-=-=-=-=-=- #
# interface
class QuackBehaviorInterface(ABC):
    file : str
    
    def play_quack(self):
        wav_obj = sa.WaveObject.from_wave_file(self.file)
        play_obj = wav_obj.play()
        # play_obj.wait_done()
    
    @abstractmethod
    def quack(self):
        ...
    
# sets
class SimpleQuack(QuackBehaviorInterface):
    file = "./static/sounds/simplequack.wav"
    
    def quack(self):
        super().play_quack()
        print("Simple Quack played")
        
class SquackQuack(QuackBehaviorInterface):
    file = "./static/sounds/rubberduck.wav"
    
    def quack(self):
        super().play_quack()
        print("Rubber Squack played")
        
class MallardQuack(QuackBehaviorInterface):
    file = "./static/sounds/mallardduck.wav"
    
    def quack(self):
        super().play_quack()
        print("Mallard Squack played")
        
class MuteQuack(QuackBehaviorInterface):
    
    def quack(self):
        print("Mute Quack!")

    