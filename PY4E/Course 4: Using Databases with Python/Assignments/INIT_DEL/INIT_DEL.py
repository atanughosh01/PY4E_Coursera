"""Progrm to test constructor and destructor in pthon"""
import sys

class PartyAnimal:
    try:
        x = int(input("\nEnter Value of X : "))
    except ValueError as ve:
        print("ValueError Caught : " + str(ve) + "\nEnter Integer Value Next Time.")
        sys.exit()

    def __init__(self):
        print("     INIT Constructor has been called\n")

    def party(self):
        self.x += (self.x * self.x)
        print("So Far", count, "-th term : ", self.x)

    def __del__(self):
        print("     DEL Destructor has been called\n")


print("\n================ CONSTRUCTOR =================")
pa = PartyAnimal()

count = 0
try:
    y = int(input("\nEnter Value of Y : "))
except ValueError as ve:
    print("ValueError Caught : " + str(ve) + "\nEnter Integer Value Next Time.")
    sys.exit()

while count <= y:
    pa.party()
    count += 1

print("\n================ DESTRUCTOR =================")
