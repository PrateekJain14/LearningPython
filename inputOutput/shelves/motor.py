import shelve

with shelve.open("motor") as bike:
    bike["make"] = "Honda"
    bike["model"] = "250 dream"
    bike["color"] = "red"
    bike["engine_size"] = 250

    print(bike["engine_size"])
    print(bike["color"])