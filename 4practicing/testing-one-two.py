from datetime import date, timedelta
import rsaidnumber

# ID NUMBER IN A CLASS
def id_num(self):
    self.email_entry()
    id_num = rsaidnumber.parse(self.id_entry.get())
    dob = id_num.date_of_birth
    age = (date.today() - dob)//timedelta(days=365.245)

    try:
        if age >= 18:
            print("Status", "Let's Play!")
            # messagebox.showinfo("Status", "Let's Play!")
            # None window.destroy()

        elif age < 18:
            print("You are too young to play. Please try again in the next 'x' years.")
            # messagebox.showinfo("You are too young to play. Please try again in the next 'x' years.")
            # window.destroy()

        # elif len(self.id_ent.get()) != 18:
        #     messagebox.showerror("Error", "Not a valid ID number")
        #     window.destroy()
        except ValueError:
            if self.id_ent.get() != int:
                print("ERROR!, Invalid ID number.")
                # messagebox.showerror("ERROR!, Invalid ID number.")
