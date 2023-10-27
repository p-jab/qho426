name = input("Enter your name: ")

if len(name) > 5:
    print("You have a long name")
elif len(name) < 3:
    print("Your name is super-short")
elif name.lower() == "piotr":
    print("That's the best name ever!")
else:
    print("What is your name, mate?")
print("Welcome to Python!")