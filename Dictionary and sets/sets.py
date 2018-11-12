# TWO WAYS OF DECLARING A SET
farm = {"hen", "sheep", "cow"}
print(farm)
for animal in farm:
    print(animal)

print("-"*50)

wild = set(["lion", "tiger", "panther"])
print(wild)
for animal in wild:
    print(animal)

farm.add("horse")
wild.add("horse")

print(farm)

even = set(range(0, 40, 2))
print(even)
print(len(even))

squares = (1, 4, 9, 16, 25)
square_tuple = set(squares)
print(square_tuple)
print(len(square_tuple))

print(even.union(square_tuple))
print(len(even.union(square_tuple)))

print("="*50)
print(even.intersection(square_tuple))
print(even & square_tuple)

even =  set(range(0, 40, 2))
print(sorted(even))
squares = (1, 4, 9, 16, 25)
square_tuple = set(squares)
print(sorted(square_tuple))

print("SUB")
print(sorted(even.difference(square_tuple)))
print(sorted(even - square_tuple))

print("="*66)
print(sorted(even))
even.difference_update(square_tuple)
print(even)


# symmetric difference of all sets i.e all elements except the element that comes in their intersection

even = set(range(0, 40, 2))
square_tuple = (1, 4, 9, 16, 25)
squares = set(square_tuple)
print(sorted(even.symmetric_difference(squares)))

print(sorted(squares.symmetric_difference(even)))

# there are two ways of removing items from sets 1) discard  2) remove-> be sure that element is present in that set

squares.remove(4)
squares.discard(8)
squares.discard(9)
print(squares)

# check subset or superset

even = set(range(0, 40, 2))
square_tuple = (4, 6, 16)
squares = set(square_tuple)
if squares.issubset(even):
    print("square is subset of even")

if even.issuperset(squares):
    print("even is superset of squares")


# Frozen set -> can be changed i.e no add, subtract, union , intersection etc
even = frozenset(range(0, 100, 2))