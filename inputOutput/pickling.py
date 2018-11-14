import pickle

# imelda = ("More Mayhem",
#           "Imelda May",
#           "2011",
#           ((1, "Pulling the rug"),
#            (2, "Psycho"),
#            (3, "Mayhem"),
#            (4, "Kentish town waltz")))
# with open("imelda1.pickle","wb") as pickle_file:
#     pickle.dump(imelda, pickle_file)

# to load the content back

# with open("imelda1.pickle", "rb") as pickleFile:
#     imelda2= pickle.load(pickleFile)
# print(imelda2)
#
# album, artist, year, track_list = imelda2
# print(album)
# print(artist)
# print(year)
# for i in track_list:
#     t_number, t_title = i
#     print(t_number, t_title)

imelda = ("More Mayhem",
          "Imelda May",
          "2011",
          ((1, "Pulling the rug"),
           (2, "Psycho"),
           (3, "Mayhem"),
           (4, "Kentish town waltz")))

even = list(range(0, 20, 2))
odd = list(range(1, 20, 2))
with open("imelda1.pickle","wb") as pickle_file:
    pickle.dump(imelda, pickle_file, protocol=0)
    pickle.dump(even, pickle_file, protocol=0)
    pickle.dump(odd, pickle_file, protocol=0)
    pickle.dump(2998302, pickle_file, protocol=0)

with open("imelda1.pickle", "rb") as pickleFile:
    imelda2 = pickle.load(pickleFile)
    even_list = pickle.load((pickleFile))
    odd_list = pickle.load((pickleFile))
    number = pickle.load(pickleFile)
print(imelda2)

album, artist, year, track_list = imelda2
print(album)
print(artist)
print(year)
for i in track_list:
    t_number, t_title = i
    print(t_number, t_title)

for i in even_list:
    print(i)
for j in odd_list:
    print(j)

print(number)