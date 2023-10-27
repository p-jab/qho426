h = input("Are you happy?\n")
k = input("Do you know it?\n")

if h.lower() == "yes" and k.lower() == "yes":
    print("Clap your hands!")
elif h.upper() == "YES" and k.upper() == "NO":
    print("Appreciate what you have, you ungrateful...")
elif h.upper() == "NO" and k.lower() == "yes":
    print("It will get better, one day!")
else:
    print("Please seek help!")
print("Glad you are here!")
