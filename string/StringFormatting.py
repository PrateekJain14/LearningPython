age= 22
print("my age is " + str(age))
print("my age is {0}".format(age))

print("there are {0} days in {1}, {2}, {3}, {4}, {5}, {6}, {7}".format(31,"january","march","may","july","august","october","december"))
# {0} -> they represent replacement of data at a particular possition


print("""January : {0}
 February : {2}
 march : {0}
 april : {1}
 may : {0}
 june :{1}""".format(31, 30, 28))