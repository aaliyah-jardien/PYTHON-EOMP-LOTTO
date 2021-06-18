# day 02 design & implementation
from tkinter import *
import random

# WINDOW FEATURES
window = Tk()
window.geometry("800x850")
window.title("Lottery Number Generator")
window.config(bg="grey")
# window.resizable(0, 0)

# FRAME
# my_frame = Frame(window, bg="#E5253A")
# my_frame.place(x=0, y=0, width=500, height=500)

# IMAGE
img = PhotoImage(file="images/img-2.png")
canvas = Canvas(window, width=801, height=301, highlightthickness="0")
canvas.create_image(0, 0, anchor=NW, image=img)
canvas.place(x=0, y=100)


# DECLARING MY FUNCTIONS (the variables are also assigned to values)
def lotto_number():

    a = random.randint(1, 49)
    b = random.randint(1, 49)
    c = random.randint(1, 49)
    d = random.randint(1, 49)
    e = random.randint(1, 49)
    f = random.randint(1, 49)

    num1.set(a)
    num1.set(b)
    num1.set(c)
    num1.set(d)
    num1.set(e)
    num1.set(f)
    return


# DEFINING MY VARIABLES
num1 = StringVar()
num2 = StringVar()
num3 = StringVar()
num4 = StringVar()
num5 = StringVar()
num6 = StringVar()

var = StringVar()
var.set("Lotto Numbers Generator")

frame1 = Frame(window)
frame1.pack(side=TOP)

# LABELS
label = Label(window, textvariable=var, font="Arial 48", width=24)
label.pack(side=TOP)
label = Label(window, textvariable="", width=24)
label.pack(side=TOP)
label = Label(window, textvariable="", width=24)
label.pack(side=TOP)

frame2 = Frame(window)
frame2.pack(side=TOP)

# ENTRIES (text boxes)
txtDisplay = Entry(frame2, textvariable=num1, bd=10, insertwidth=1, font="Arial 30", justify="center", width=4, bg="red")
txtDisplay.pack(side=LEFT)
txtDisplay = Entry(frame2, textvariable=num2, bd=10, insertwidth=1, font="Arial 30", justify="center", width=4, bg="orange")
txtDisplay.pack(side=LEFT)
txtDisplay = Entry(frame2, textvariable=num3, bd=10, insertwidth=1, font="Arial 30", justify="center", width=4, bg="yellow")
txtDisplay.pack(side=LEFT)
txtDisplay = Entry(frame2, textvariable=num4, bd=10, insertwidth=1, font="Arial 30", justify="center", width=4, bg="lime")
txtDisplay.pack(side=LEFT)
txtDisplay = Entry(frame2, textvariable=num5, bd=10, insertwidth=1, font="Arial 30", justify="center", width=4, bg="turquoise")
txtDisplay.pack(side=LEFT)
txtDisplay = Entry(frame2, textvariable=num6, bd=10, insertwidth=1, font="Arial 30", justify="center", width=4, bg="purple")
txtDisplay.pack(side=LEFT)

frame3 = Frame(window)
frame3.pack(side=TOP)

# BUTTONS
button1 = Button(frame3, state=DISABLED, text="")
button1.pack(side=TOP)
button1 = Button(frame3, padx=8, width=18, pady=8, font="Arial 26", text="Lotto Number Generator", bg="pink")
button1.pack(side=TOP)

window.mainloop()
