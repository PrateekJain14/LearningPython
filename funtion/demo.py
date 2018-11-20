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


def centre_text(*args):
    text= ""
    for arg in args:
        text += str(arg) + " "
    left_margin= (80-len(text)) // 2
    print(" "*left_margin, text)


centre_text("HELLO WOrLD")
centre_text("Spam", "Eggs", 34, 12)



# PROGRAM TO MAKE OUR OWN PRINT FUNCTION

def centre_text(*args, sep=' ', end='\n', file=None, flush=False):
    text = ""
    for arg in args:
        text += str(arg) + sep
    left_margin= (80-len(text)) // 2
    print(" "*left_margin, text, end=end, file=file, flush=flush)

with open("centeredFile", mode='w') as centered_file:
    centre_text("HELLO WOrLD", file=centered_file)
    centre_text("Spam", "Eggs", 34, 12, file=centered_file)