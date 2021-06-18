# Aaliyah Jardien, Class 2
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

# IMAGE
img = PhotoImage(file="images/img-1.png")
canvas = Canvas(window, width=900, height=400, highlightthickness="0")
canvas.create_image(0, 0, anchor=NW, image=img)
canvas.place(x=-45, y=-105)

# LABELS
heading = Label(window, text="ARE YOU THE NEXT MULTIMILLIONAIRE?", font="arial 28 bold italic", bg="#E5253A", fg="#FFFDFE")
heading.place(x=80, y=305)

register = Label(window, text="Register now!!!", font="arial 25 bold", bg="#E5253A", fg="#FFFDFE")
register.place(x=320, y=345)

note = Label(window, text="*Please fill out all fields*", font="arial 15", bg="#E5253A", fg="#FFFDFE")
note.place(x=335, y=385)

personal = Label(window, text="PERSONAL INFORMATION", font="arial 15 bold", bg="#E5253A", fg="#F9D713")
personal.place(x=90, y=450)

name = Label(window, text="Full name :", font="arial 15 bold", bg="#E5253A", fg="#FFFDFE")
name.place(x=90, y=480)

id = Label(window, text="RSA ID no :", font="arial 15 bold", bg="#E5253A", fg="#FFFDFE")
id.place(x=90, y=510)

email = Label(window, text="Email address :", font="arial 15 bold", bg="#E5253A", fg="#FFFDFE")
email.place(x=90, y=540)

address = Label(window, text="YOUR ADDRESS", font="arial 15 bold", bg="#E5253A", fg="#F9D713")
address.place(x=90, y=610)

street = Label(window, text="Street :", font="arial 15 bold", bg="#E5253A", fg="#FFFDFE")
street.place(x=90, y=640)

area = Label(window, text="Area :", font="arial 15 bold", bg="#E5253A", fg="#FFFDFE")
area.place(x=90, y=670)

city = Label(window, text="City :", font="arial 15 bold", bg="#E5253A", fg="#FFFDFE")
city.place(x=90, y=700)

postal_code = Label(window, text="Postal Code :", font="arial 15 bold", bg="#E5253A", fg="#FFFDFE")
postal_code.place(x=90, y=730)

# ENTRIES
name_entry = Entry(window, width="30")
name_entry.place(x=450, y=480)

id_entry = Entry(window, width="30")
id_entry.place(x=450, y=510)

email_entry = Entry(window, width="30")
email_entry.place(x=450, y=540)

# all the address entries
street_entry = Entry(window, width="30")
street_entry.place(x=450, y=640)

area_entry = Entry(window, width="30")
area_entry.place(x=450, y=670)

city_entry = Entry(window, width="30")
city_entry.place(x=450, y=700)

postal_code_entry = Entry(window, width="30")
postal_code_entry.place(x=450, y=730)


# FUNCTIONS
# email validation
def register():
    id_numb()
    register2()

    ex = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
    # email_entry = input('user email: ')

    # email validation
    for i in range(len(email_entry.get())):
        if re.search(ex, email_entry.get()):
            with open("text_file2.txt", "a") as f:
                f.write(email_entry.get())
                f.write('\n')

        else:
            f.write('invalid')


# age validation
# ID NUMBER IN A CLASS
def id_numb():

    # self.email_entry()
    id_num = rsaidnumber.parse(id_entry.get())
    dob = id_num.date_of_birth
    age = (datetime.today() - dob) // timedelta(days=365.245)

    try:
        if age >= 18:
            messagebox.showinfo("Let's Play!")
            window.destroy()

        elif age < 18:
            years = str(int(dob)-18)
            messagebox.showinfo("You are too young to play. Please try again in the next" + str(years) + "years.")
            window.destroy()

        # elif len(self.id_ent.get()) != 18:
        #     messagebox.showerror("Error", "Not a valid ID number")
        #     window.destroy()
    except ValueError:
        # if self.id_ent.get() != int:
        messagebox.showerror("ERROR!, Invalid ID number.")


# submit button function & storing it in the text file
def register2():

    answers = ""
    my_file = open("text_file2.txt", 'a')
    answers += "Full name : " + name_entry.get()
    answers += '\n'
    answers += "RSA ID no : " + id_entry.get()
    answers += '\n'
    answers += "Email address : " + email_entry.get()
    answers += '\n'
    answers += "Street : " + street_entry.get()
    answers += '\n'
    answers += "Area : " + area_entry.get()
    answers += '\n'
    answers += "City, Postal : " + city_entry.get()
    answers += '\n'
    answers += "Postal : " + postal_code_entry.get()
    answers += '\n'

    my_file.write(answers)


# clear button
def clear_func():
    name_entry.delete(0, END)
    id_entry.delete(0, END)
    email_entry.delete(0, END)
    street_entry.delete(0, END)
    area_entry.delete(0, END)
    city_entry.delete(0, END)
    postal_code_entry.delete(0, END)


# exit button
def exit_func():
    sure = messagebox.askyesno(title="Alert", message="Are you sure you want to exit this window?")
    if sure:
        window.destroy()
    else:
        return None


# BUTTONS
clear_btn = Button(window, text="Clear", command=clear_func, borderwidth="5", font="arial 15 bold", bg="#F9D713", fg="#FFFDFE")
clear_btn.place(x=150, y=800)

register_btn = Button(window, text="Register", command=register, borderwidth="5", font="arial 15 bold", bg="#0C9FD3", fg="#FFFDFE")
register_btn.place(x=350, y=800)

exit_btn = Button(window, text="Exit", command=exit_func, borderwidth="5", font="arial 15 bold", bg="#01A66A", fg="#FFFDFE")
exit_btn.place(x=550, y=800)

window.mainloop()

# blue #0C9FD3
# green #01A66A
# yellow #F9D713
