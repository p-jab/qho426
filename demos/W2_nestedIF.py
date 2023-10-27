salary = float(input("Enter salary: "))
years = int(input("Enter number of years(whole years): "))

if years > 2:
    if salary < 25000:
        salary *= 1.1
    else:
        salary += 500
elif years == 1:
    salary += 200
else:
    if salary <= 18000:
        print("Oopsie! That's an error! Your salary is £18000")
        salary = 18000
print(f"Your salary from now on will be £{salary:.0f}. Keep up good work")