bike = {"make": "honda", "model": "250 dream", "color": "red", "engine_size": 250}
print(bike["engine_size"])
print(bike["color"])

fruit = {"orange": "a sweet, citrus fruit",
         "apple": "good for making cider",
         "lemon": "green and sour citrus fruit",
         "grapes": "a small, sweet fruit"}
# to add one dictionary into another

bike.update(fruit)
