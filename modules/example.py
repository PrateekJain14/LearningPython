print(dir())
print(dir(__builtins__))

for i in dir(__builtins__):
    print(i)

import shelve
print(dir())
print(dir(shelve))

# help(shelve)