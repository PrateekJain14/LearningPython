# a key is used to display any element ( contains key value pairs)
fruit = {"orange": "a sweet, citrus fruit",
         "apple": "good for making cider",
         "lemon": "green and sour citrus fruit",
         "grapes": "a small, sweet fruit"}

print(fruit["orange"])

fruit["pear"] = "a small shaped apple"
print(fruit)

del fruit["pear"]
print(fruit)

# fruit.clear() function is used to delete all entries in a dictionary but not dictionary and
# to clear whole diction we can simply use del fruit
fruit.clear()
print(fruit)
print("-"*100)
#---------------------------------------------------------------------------------------------------------------------
fruit = {"orange": "a sweet, citrus fruit",
         "apple": "good for making cider",
         "lemon": "green and sour citrus fruit",
         "grapes": "a small, sweet fruit"}

print(fruit)
while True:
    key = input("Enter fruit name: ")
    if key == "quit":
        break
    if key in fruit:
        description = fruit.get(key)
        print(description)
    else:
        print("{} not found".format(key))