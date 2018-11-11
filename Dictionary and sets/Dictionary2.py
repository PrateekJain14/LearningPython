fruit = {"orange": "a sweet, citrus fruit",
         "apple": "good for making cider",
         "lemon": "green and sour citrus fruit",
         "grapes": "a small, sweet fruit"}

# print(fruit)
# while True:
#     key = input("Enter fruit name: ")
#     if key == "quit":
#         break
#     description = fruit.get(key,"{} not found".format(key))
#     print(description)

# my_list = list(fruit.keys())
# my_list.sort()
# for snack in my_list:
#     print(snack +" is "+ fruit[snack])
# print("-"*100)

# fruit_keys = fruit.keys()
# print(fruit_keys)
#
# fruit["tomatos"] = "not nice with ice cream"
# print(fruit_keys)

print(fruit.items())