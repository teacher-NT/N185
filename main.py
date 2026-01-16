import os
os.system("cls")

from abc import ABC, abstractmethod

class Player(ABC):
    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def kick(self):
        pass

    @abstractmethod
    def jump(self):
        pass


class Ronaldo(Player):
    def run(self):
        print("Running...")
    def kick(self):
        print("Kicking...")
    def jump(self):
        print("Jumping...")
    
class Messi(Player):
    def run(self):
        print("Running...")
    def kick(self):
        print("Kicking...")
    def jump(self):
        print("Jumping...")

    def pas(self):
        print("Passing...")

r1 = Ronaldo()
m1 = Messi()
r1.run()
m1.pas()