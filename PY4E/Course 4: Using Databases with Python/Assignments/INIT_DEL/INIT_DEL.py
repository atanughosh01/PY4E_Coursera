"""Progrm to test constructor and destructor in pthon"""

class PartyAnimal:
    x = int(input("Enter Value of X : "))

    def __init__(self):
        print("     INIT Constructor has been called\n")

    def party(self):
        self.x += self.x
        print("So Far", count, "-th term : ", self.x)

    def __del__(self):
        print("     DEL Destructor has been called\n")


print("\n================ CONSTRUCTOR =================")
pa = PartyAnimal()


count = 0
y = int(input("Enter Value of Y : "))
while count <= y:
    pa.party()
    count += 1

print("\nType of pa :", type(pa))
print("\nDIR :", dir(pa))

print("\n================ DESTRUCTOR =================")
