#list
my_list = ["hello brother", "john", 192]
my_list.append(123)
print(my_list)

#touple
welcome = "Welcome to", "india", 1947
bad = "bad company", 1974


print(welcome)

# unpacking of a touple
greeting, country, year = welcome
print(greeting)
print(country)
print(year)
print("*"*50)
#------------------------------------------------------

imelda = "More Mayhem", "Imelda May", 2011, ((1, "Pulling the ring"), (2, "Psycho"), (3, "Mayhem"), (4, "Town waltz"))
title, artist, year, tracks = imelda
print(title)
print(artist)
print(year)
for songs in tracks:
    print("\t",songs)
#---------------------------------------------------------------
imelda = "More Mayhem", "Imelda May", 2011, ([(1, "Pulling the ring"), (2, "Psycho"), (3, "Mayhem"), (4, "Town waltz")])
title, artist, year, tracks = imelda
tracks.append((5, "life"))
print(title)
print(artist)
print(year)
for songs in tracks:
    print("\t",songs)
