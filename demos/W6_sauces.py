def populate(path):
    with open(path, "w") as f:
        while True:
            sauce = input("Enter a sauce you like or \"stop\" ")
            if sauce.lower() == "stop":
                break
            f.write(sauce + "\n")

def reading(path):
    with open(path) as bob:
        print(bob.read())

# name = input("Enter name: ")
# populate(name + ".txt")
reading("robert.txt")