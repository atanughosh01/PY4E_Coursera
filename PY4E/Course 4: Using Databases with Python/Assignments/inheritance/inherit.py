"""Program to test INHERITANCE in python"""

import sys

class PartyAnimal:
    name = " "
    try:
        x = int(input("\nEnter Value of X : "))
    except ValueError as ve:
        print("ValueError Caught : " + str(ve) + "\nEnter Integer Value Next Time.")
        sys.exit()

    def __init__(self, nam):
        print("     INIT Constructor has been called\n")
        self.name = nam
        print(self.name, "constructed")

    def party(self):
        self.x += (self.x * self.x)
        print("So Far", count, "-th term : ", self.x)

    def __del__(self):
        print("     DEL Destructor has been called\n")

class FootballFan(PartyAnimal):
    try:
        points = int(input("\nEnter Points : "))
    except ValueError as ve:
        print("ValueError Caught : " + str(ve) + "\nEnter Integer Value Next Time.")
        sys.exit()

    def __init__(self, nam):
        super().__init__(nam)
        print("    INIT Constructor of SUB-CLASS has been called\n")

    def touchdown(self):
        self.points += 3
        self.party()
        print(self.name, "points", self.points)

print("\n================ CONSTRUCTOR =================")
pa = PartyAnimal("David")
ff = FootballFan("James")

count = 0
try:
    y = int(input("\nEnter Value of Y : "))
except ValueError as ve:
    print("ValueError Caught : " + str(ve) + "\nEnter Integer Value Next Time.")
    sys.exit()

while count <= y:
    pa.party()
    ff.party()
    ff.touchdown()
    count += 1

print("\n================ DESTRUCTOR =================")
