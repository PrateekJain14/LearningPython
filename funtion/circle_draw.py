import tkinter
import math


def parabola(page, size):   # page = canvas
    for x in range(size):
        y = x * x / size
        plot(page, x, y)
        plot(page, -x, y)

def cicle(page, rad, g, h):
    page.create_oval(g + rad, h + rad, g - rad, h - rad, outline='red', width=2)

    # OR

    # for x in range(100 * g, 100 * (g+rad)):
    #     x = x / 100
    #     y = h + (math.sqrt(rad ** 2 - ((x - g)**2)))
    #     plot(page, x, y)
    #     plot(page, x, 2 * h - y)
    #     plot(page, 2 * g - x, y)
    #     plot(page, 2 * g - x, 2 * h - y)



def draw_axis(page):
    page.update()
    x_origin = page.winfo_width() // 2
    y_origin = page.winfo_height() // 2
    page.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))
    page.create_line(-x_origin, 0, x_origin, 0, fill="black")
    page.create_line(0, -y_origin, 0, y_origin,  fill="black")


def plot(page, x, y):
    page.create_line(x, -y, x+1, -y+1, fill="red")


mainWindow = tkinter.Tk()
mainWindow.title("PARABOLA")
mainWindow.geometry('640x480')

canvas = tkinter.Canvas(mainWindow, width=640, height=480)
canvas.grid(row=0, column=0)


draw_axis(canvas)

parabola(canvas, 100)
parabola(canvas, 200)
cicle(canvas, 100, 100, 100)
cicle(canvas, 100, 100, -100)
cicle(canvas, 100, -100, 100)
cicle(canvas, 100, -100, -100)
cicle(canvas, 10, 30, 30)
cicle(canvas, 10, 30, -30)
cicle(canvas, 10, -30, -30)
cicle(canvas, 10, -30, 30)
cicle(canvas, 30, 0, 0)

mainWindow.mainloop()
