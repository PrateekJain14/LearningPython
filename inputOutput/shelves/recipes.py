import shelve

# blt = ["bacon", "lettuce", "tomato", "bread"]
# beans_on_toast = ["beans", "bread"]
# scrambled_eggs = ["eggs", "butter", "milk"]
# soup = ["tin of soup"]
# pasta= ["pasta", "cheese"]

with shelve.open("recipes", writeback=True) as recipes:
    # recipes["blt"] = blt
    # recipes["beans_on_toast"] = beans_on_toast
    # recipes["scrambled_eggs"] = scrambled_eggs
    # recipes["pasta"] = pasta
    # recipes["soup"] = soup

    # TO ADD ANYTHING TO LIST

    # temp_list = recipes["blt"]
                              # x = temp_list.index("butter")    (delete an item from list)
                              # del temp_list[x]
    # new = ["butter"]
    # recipes["blt"] = temp_list

    # temp_list = recipes["pasta"]
    # temp_list.append("tomato")
    # recipes["pasta"] = temp_list
    # recipes["soup"].append("croutons")

    for snacks in recipes:
        print(snacks, recipes[snacks])