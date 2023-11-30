age = int(input("Enter age: "))
if age < 20:
    charge = 3000
elif age < 29:
    charge = 2200
else:
    charge = 8000

s_driver = input("Do you want to add additional driver? (y/n)")
if "y" in s_driver.lower():
    charge = charge + charge*0.55
    #charge *= 1.55
print(f"Your insurance premium is £{charge:.2f}")