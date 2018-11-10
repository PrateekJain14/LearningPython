import random

highest = 1000
answer = random.randint(1, highest)

print("Guess a number between 1 and {}".format(highest))
guess = 0

while guess != answer:
    guess = int(input())
    if guess == 0:
        break
    else:
        if guess < answer:
            print("guess higher")
        elif guess > answer:
            print("guess lower")
        else:
            print("Guessed correctly")

