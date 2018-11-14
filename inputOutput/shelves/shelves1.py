import shelve

# with shelve.open('shelveTest') as fruit:
#     fruit['orange'] = "a sweet, citrus fruit"
#     fruit['apple'] = "good for making cider"
#     fruit['lemon'] = "a sour, yellow citrus fruit"
#     fruit['grape'] = "a  small, sweet fruit"
#     fruit['lime'] = "a sour, green citrus fruit"
#
#     print(fruit["lemon"])
#     print(fruit["grape"])

# or

fruit = shelve.open('shelveTest')
fruit['orange'] = "a sweet, citrus fruit"
fruit['apple'] = "good for making cider"
fruit['lemon'] = "a sour, yellow citrus fruit"
fruit['grape'] = "a  small, sweet fruit"
fruit['lime'] = "a sour, green citrus fruit"

# print(fruit["lemon"])
# print(fruit["grape"])
# fruit["lime"] = "Great with tequila"
# for snacks in fruit:
#     print(snacks + ": " + fruit[snacks])
# while True:
#     dict_key = input("please enter a key :")
#     if dict_key == "quit":
#         break
#     desc = fruit.get(dict_key, "we don't have {} fruit".format(dict_key))
#     print(desc)
#
# ordered_keys = list(fruit.keys())
# ordered_keys.sort()
# for i in ordered_keys:
#     print(i + ": " + fruit[i])

for j in fruit.values():
    print(j)

print(fruit.values())
fruit.close()