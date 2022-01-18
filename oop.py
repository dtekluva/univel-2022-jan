# class Mammalia: # A very useless class here
#     pass

# class HumanKind: # ClASS CREATION 

#     skin = True
#     eyes = True
#     legs = True
#     species = "mammal"

# human_kind = HumanKind() # OBJECT CREATION CLASS INSTANTIATION
# print(human_kind)
# another_name = HumanKind() # OBJECT CREATION CLASS INSTANTIATION
# print(another_name)

# print(human_kind.skin)
# print(human_kind.species)
# print(another_name.skin)
# print(another_name.species)

# import winsound, time

# class HumanKind: # ClASS CREATION 

#     skin = True
#     eyes = True
#     legs = True
#     species = "mammal"

#     def describe(self):
#         print(f"Hello my species is {self.species}")

#     def makenoise(self):
#         print("HELLO !!!!!")
#         winsound.Beep(2000, 500)
#         time.sleep(1)
#         winsound.Beep(1000, 500)
#         time.sleep(1)
#         winsound.Beep(3000, 500)

# varname = HumanKind()
# varname.describe()
# varname.makenoise()

# INSTANCE ATTRIBUTES
import random
import time
import winsound
import guess_game

class Person:
    
    # class attribute
    species = "Hommo-Sapien"
    _class  = "Mammal"

    def __init__(self, name, complexion, height):
        
        self.name = name
        self.complexion = complexion
        self.height = height
        self.voice_freq = random.randint(50, 1500)

    def say_something(self):
        print(f"Hello, my name is {self.name}.\n I am a {self._class}, and my height is {self.height}")
        winsound.Beep(self.voice_freq, 500)
        time.sleep(0.5)
        winsound.Beep(self.voice_freq, 500)
        time.sleep(0.5)
        winsound.Beep(self.voice_freq, 500)

# person1 = Person(name = "Ade", complexion="Brown skin", height="5ft7'")
# person1.say_something()

# person2 = Person(name = "Segun", complexion="Fair skin", height="6ft2'")
# person2.say_something()

print("Hello my name is : ", __name__)

if __name__ == "__main__":
    print("HEY THERE I AM THE MAIN MAN")