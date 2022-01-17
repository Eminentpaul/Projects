import random

number = random.randint(0, 10)
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input("Guess a number from 0 - 10: "))
    guess_count += 1

    if guess != number:
        print("Oh! No, Try Again!")
    elif guess == number:
        print(f"Wow!!!, You won 'Correct Guessing Value {number}'")
        break
else:
    print("I'm Sorry you failed!")
    print(f"the number is '{number}'")