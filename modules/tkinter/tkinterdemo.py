try:
    import tkinter
except ImportError:
    import Tkinter as tkinter

print(tkinter.TkVersion)
print(tkinter.TclVersion)
# tkinter._test()

mainWindow = tkinter.Tk()

mainWindow.title("HELLO WORLD")
mainWindow.geometry('640x480')
mainWindow.mainloop()