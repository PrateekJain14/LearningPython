name = input("Enter your name :")
age = int(input("Enter your age {} :".format(name)))

if 18 < age < 31:
    print("Welcome to the trip")
else:
    print("Sorry! you cant come")