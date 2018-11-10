# shopping_list = ["eggs" ,"bread","cake","spam","rice"]
# for item in shopping_list:
#     if item == "spam":
#         continue
#     print("buy "+item)
#------------------------------------------------------------
# shopping_list = ["eggs" ,"bread","cake","spam","rice"]
# for item in shopping_list:
#     if item == "spam":
#         break
#     print("buy "+item)
#------------------------------------------------------------------
meal = ["rice", "eggs", "spam", "burger"]
nasty_food_item=""
for item in meal :
    if item == "spam" :
        nasty_food_item = item
        break

else:
    print("I will have one")

if nasty_food_item :
    print("Spam found")