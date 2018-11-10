name = input("Enter your name :")
age = int(input("Enter your age {} :".format(name)))
print(age)

if age >= 18:
    print("You can vote!")
else:
    print("Come back after {} years".format(18-age))



print("Guess the number between 1 and 10")
guess = int(input())
if guess < 5:
    print("Guess a Higher number ")
    guess = int(input())
    if guess == 5:
        print("guessed it correctly")
    else:
        print("Incorrect")
elif guess > 5:
    print("Guess a lower number ")
    guess = int(input())
    if guess == 5:
        print("guessed it correctly")
    else:
        print("Incorrect")
else:
    print("Guessed correctly in first attempt")



