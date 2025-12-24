import random

number = random.randint(1, 100)
tries = 0
guess = 0

print("welcome to the number guessing game")
print("i am thinking of a number between 1 and 100")

while guess != number:
    guess = input("enter your guess: ")
    if not guess.isdigit():
        print("please enter a valid number")
        continue
    guess = int(guess)
    tries += 1
    if guess < number:
        print("too low")
    elif guess > number:
        print("too high")
    else:
        print(f"congratulations! you guessed it in {tries} tries")
