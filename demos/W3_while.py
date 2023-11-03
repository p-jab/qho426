#x = int(input("Enter a number: "))
i, j = 1, 1
while i <= 10:
    while j <= 10:
        print(f"{i}x{j}={j*i}")
        j += 1
    i += 1
    j = 1
