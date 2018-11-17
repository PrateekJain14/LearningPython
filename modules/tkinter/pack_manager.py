# import tkinter
#
# mainWindow = tkinter.Tk()
#
# mainWindow.title("FIRST GUI BASED PROGRAM")
# mainWindow.geometry('640x480')
#
# label = tkinter.Label(mainWindow, text="HelloWorld")
# label.pack(side='top')
# canvas = tkinter.Canvas(mainWindow, relief='raised', borderwidth=1)
# # canvas.pack(side='left', fill=tkinter.X, expand=True)
# # canvas.pack(side='left', fill=tkinter.BOTH, expand=True)
# canvas.pack(side='left')
#
# button1 = tkinter.Button(mainWindow, text="B1")
# button2 = tkinter.Button(mainWindow, text="B2")
# button3 = tkinter.Button(mainWindow, text="B3")
# button1.pack(side='left', anchor="n")
# button2.pack(side='left', anchor="s")
# button3.pack(side='left', anchor="e")
#
# mainWindow.mainloop()


# NEXT EXAMPLE

import tkinter

mainWindow = tkinter.Tk()

mainWindow.title("FIRST GUI BASED PROGRAM")
mainWindow.geometry('640x480')
label = tkinter.Label(mainWindow, text="HelloWorld")
label.pack(side='top')

leftFrame = tkinter.Frame(mainWindow)
leftFrame.pack(side='left', anchor='n', fill=tkinter.Y, expand=False)

canvas = tkinter.Canvas(leftFrame, relief='raised', borderwidth=1)
canvas.pack(side='left', anchor='n')

rightFrame = tkinter.Frame(mainWindow)
rightFrame.pack(side='right', anchor='n', expand=True)
button1 = tkinter.Button(rightFrame, text="B1")
button2 = tkinter.Button(rightFrame, text="B2")
button3 = tkinter.Button(rightFrame, text="B3")
button1.pack(side='top')
button2.pack(side='top')
button3.pack(side='top')

mainWindow.mainloop()