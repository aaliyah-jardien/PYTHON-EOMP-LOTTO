# validating an entry widget as an integer
from tkinter import *

# WINDOW FEATURES
window = Tk()
window.title("tk")
window.geometry("400x300")
window.config(bg="purple")
window.resizable(0, 0)

# FUNCTION
def number():
    try:
        int(entry.get())
        answer.config(text="THIS IS A NUMBER! CONGRATS!!")
    except ValueError:
        answer.config(text="This is NOT a number, you doughnut!")

# LABEL
label = Label(window, text=" Enter a number: ", font="poppins 15 bold", bg="aqua")
label.place(x=120, y=30)

# ENTRY
entry = Entry(window, width=30)
entry.place(x=120, y=80)

# BUTTON
button = Button(window, text="Submit", command=number, font="poppins 10 bold", bg="aqua", border=10)
button.place(x=150, y=150)

# OUTPUT
answer = Label(window, text="", width="30")
answer.place(x=120, y=200)

window.mainloop()
