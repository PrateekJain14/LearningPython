# list_1 = []
# list_2 = list()
# # both of them will create an empty list
#
# print("list 1 {}".format(list_1))
# print("list 2 {}".format(list_2))
#
# print(list("the list are equal"))
#-----------------------------------------------------------------
# even = [1, 2, 3, 4]
# another = list(even)
#
# print(another is even)
# another.sort(reverse=True)
# print(even)
#-----------------------------------------------------------------

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7]
number = [even, odd]

print(number)

for i in number:
    print(i)
    for j in i:
        print(j)