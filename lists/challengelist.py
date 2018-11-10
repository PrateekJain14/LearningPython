menu = []
menu.append(["eggs", "spam", "bacon"])
menu.append(["eggs", "sausage", "bacon"])
menu.append(["eggs", "spam"])
menu.append(["eggs", "bacon", "spam"])
menu.append(["eggs", "bacon", "sausage", "spam"])
menu.append(["spam", "bacon", "sausage", "spam"])
menu.append(["spam", "eggs", "spam", "spam", "bacon", "spam"])
menu.append(["spam", "eggs", "sausage", "spam"])

for meal in menu:
    if "spam" not in meal:
        for ingredients in meal:
            print(ingredients)