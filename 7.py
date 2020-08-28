#inheritance

from Chef import Chef
from ChineseChef import ChineseChef

myChef = Chef()
myChef.make_chicken()


myChineseChef = ChineseChef()
myChineseChef.make_special_dish()



class Chef:

    def make_chicken(self):
        print("The chef makes a chicken")

    def make_salad(self):
        print("The chef makes a salad")

    def make_special_dish(self):
        print("The chef makes a special dish")



from Chef import Chef

class ChineseChef(Chef): #all functions inside chef class

    def make_special_dish(self):
        print("The chef makes orange chicken")

    def make_fried_rice(self):
        print("The chef makes fried rice")


..

#Python Interpreter
