x = int(input("Enter number between 1 and 10: "))
mult = 0
if x in range(1,11):
    while mult <= 10:
        print(f"{x}x{mult}={x*mult}")
        mult += 1
else:
    print("Invalid number. You numpty.")

