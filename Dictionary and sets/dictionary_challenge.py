

location = {0: "You are sitting in front of computer learning python",
            1: "You are standing at the end of the road",
            2: "You are at the top of the hill",
            3: "You are inside a building",
            4: "You are in a valley",
            5: "You are in the forest" }

exits = {0: {"Q": 0},
         1: {"W": 2, "E": 3, "N": 5, "S":4, "Q": 0},
         2: {"N": 5, "Q": 0},
         3: {"W": 1, "Q": 0},
         4: {"N": 1, "W": 2, "Q": 0},
         5: {"W": 2, "S": 1, "Q": 0}}

vocab = { "EAST":  "E",
          "WEST":  "W",
          "NORTH": "N",
          "SOUTH": "S",
          "QUIT":  "Q"}
loc = 1

while True:
    availableExits = ",".join(exits[loc].keys())
    print(location[loc])

    if loc == 0:
        break
    direction = input("Available exits are " + availableExits +" ").upper()
    if len(direction) > 1:
        words = direction.split()
        for word in words:
            if word in vocab:
                direction = vocab[word]
    if direction in exits[loc]:
        loc = exits[loc][direction]
    else:
        print("you cant go in that direction")
