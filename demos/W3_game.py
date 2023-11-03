import random #Taking definitions from package "random" into my scope
secret = random.randint(1,20)
print("Welcome to my Guess-Game. I am thinking of a number between 1 and 20")

for attempt in range(5):
    print(f"Attempt nr {attempt+1}")
    guess = int(input("Take a guess: "))
    if guess == secret:
        print("Congrats! You have won, bro!")
        break
    elif guess > secret:
        print("Too high!")
    else:
        print("Too low!")
if guess != secret:
    print(f"Game over! Loser! My number was {secret}")