from tkinter import *
from tkinter import messagebox
from datetime import datetime, timedelta
import rsaidnumber
import re

# WINDOW FEATURES
window = Tk()
window.geometry("900x880")
window.title("Lottery Game Login")
window.config(bg="#E5253A")
window.resizable(0, 0)

# USING OOP TO MAKE A CLASS & FUNCTION

class register:

    # TKINTER FEATURES
    def __init__(self, master):
        # images, labels, entries, buttons
        # IMAGE
        self.img = PhotoImage(file="images/img-1.png")
        self.canvas = Canvas(self.window, width=900, height=400, highlightthickness="0")
        self.canvas.create_image(0, 0, anchor=NW, image=img)
        self.canvas.place(x=-45, y=-105)

        # LABELS
        self.heading = Label(self.window, text="ARE YOU THE NEXT MULTIMILLIONAIRE?", font="arial 28 bold italic", bg="#E5253A", fg="#FFFDFE")
        self.heading.place(x=80, y=305)
        self.register = Label(self.window, text="Register now!!!", font="arial 25 bold", bg="#E5253A", fg="#FFFDFE")
        self.register.place(x=320, y=345)
        self.note = Label(self.window, text="*Please fill out all fields*", font="arial 15", bg="#E5253A", fg="#FFFDFE")
        self.note.place(x=335, y=385)
        self.personal = Label(self.window, text="PERSONAL INFORMATION", font="arial 15 bold", bg="#E5253A", fg="#F9D713")
        self.personal.place(x=90, y=450)
        self.name = Label(self.window, text="Full name :", font="arial 15 bold", bg="#E5253A", fg="#FFFDFE")
        self.name.place(x=90, y=480)
        self.id = Label(self.window, text="RSA ID no :", font="arial 15 bold", bg="#E5253A", fg="#FFFDFE")
        self.id.place(x=90, y=510)
        self.email = Label(self.window, text="Email address :", font="arial 15 bold", bg="#E5253A", fg="#FFFDFE")
        self.email.place(x=90, y=540)
        self.address = Label(self.window, text="YOUR ADDRESS", font="arial 15 bold", bg="#E5253A", fg="#F9D713")
        self.address.place(x=90, y=610)
        self.street = Label(self.window, text="Street :", font="arial 15 bold", bg="#E5253A", fg="#FFFDFE")
        self.street.place(x=90, y=640)
        self.area = Label(self.window, text="Area :", font="arial 15 bold", bg="#E5253A", fg="#FFFDFE")
        self.area.place(x=90, y=670)
        self.city = Label(self.window, text="City :", font="arial 15 bold", bg="#E5253A", fg="#FFFDFE")
        self.city.place(x=90, y=700)
        self.postal_code = Label(self.window, text="Postal Code :", font="arial 15 bold", bg="#E5253A", fg="#FFFDFE")
        self.postal_code.place(x=90, y=730)

        # ENTRIES
        self.name_entry = Entry(self.window, width="30")
        self.name_entry.place(x=450, y=480)
        self.id_entry = Entry(self.window, width="30")
        self.id_entry.place(x=450, y=510)
        self.email_entry = Entry(self.window, width="30")
        self.email_entry.place(x=450, y=540)
        # all the address entries
        self.street_entry = Entry(self.window, width="30")
        self.street_entry.place(x=450, y=640)
        self.area_entry = Entry(self.window, width="30")
        self.area_entry.place(x=450, y=670)
        self.city_entry = Entry(self.window, width="30")
        self.city_entry.place(x=450, y=700)
        self.postal_code_entry = Entry(self.window, width="30")
        self.postal_code_entry.place(x=450, y=730)

        # BUTTONS
        self.clear_btn = Button(self.window, text="Clear", command=clear_func, borderwidth="5", font="arial 15 bold", bg="#F9D713", fg="#FFFDFE")
        self.clear_btn.place(x=150, y=800)
        self.register_btn = Button(self.window, text="Register", command=register, borderwidth="5", font="arial 15 bold", bg="#0C9FD3", fg="#FFFDFE")
        self.register_btn.place(x=350, y=800)
        self.exit_btn = Button(self.window, text="Exit", command=exit_func, borderwidth="5", font="arial 15 bold", bg="#01A66A", fg="#FFFDFE")
        self.exit_btn.place(x=550, y=800)

    # USER VALIDATION FUNCTIONS
    def player_id(self):


    # CLEAR BUTTON FUNCTION
    def clear_func(self):
        self.name_entry.delete(0, END)
        self.id_entry.delete(0, END)
        self.email_entry.delete(0, END)
        self.street_entry.delete(0, END)
        self.area_entry.delete(0, END)
        self.city_entry.delete(0, END)
        self.postal_code_entry.delete(0, END)

    # EXIT BUTTON FUNCTION
    def exit_func(self):
        # self.sure = messagebox.askyesno(title="Alert", message="Are you sure you want to exit this window?")
        # self.if sure:
        #     window.destroy()
        # self.else:
        # return None
        return window.destroy()

window.mainloop()
