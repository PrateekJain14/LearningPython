# def first_fun():
#     print("First Function is made")
#
# # All python function return a value, if we don't specify what needs to be returned then "NONE" is returned
# print(first_fun())


def python_food():
    width = 80
    text = "Spam and Eggs"
    left_margin = (width-len(text)) // 2
    print(" "*left_margin, text)


python_food()


def centre_text(text):
    text= str(text)
    left_margin= (80-len(text)) // 2
    print(" "*left_margin, text)


centre_text("HELLO WOrLD")