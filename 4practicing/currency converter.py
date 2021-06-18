from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import requests
# from tkinter import messagebox

root = Tk()

# StringVar
results = StringVar()
values1 = StringVar()
values2 = StringVar()

# code to add widgets and style window will go here

information = requests.get('https://v6.exchangerate-api.com/v6/89dcd9e8cc7777ded2575ce1/latest/USD')
information_json = information.json()

conversion_rates = information_json['conversion_rates']

currency = []
for i in conversion_rates.keys():
    currency.append(i)

currency2 = []
for i in conversion_rates.keys():
    currency2.append(i)

currency_cb = ttk.Combobox(root)
currency_cb['values'] = currency
currency_cb['state'] = 'readonly'
currency_cb.set('Select Currency')
currency_cb.place(x=10, y=280)


currency_cb2 = ttk.Combobox(root)
currency_cb2['values'] = currency2
currency_cb2['state'] = 'readonly'
currency_cb2.set('Select Currency')
currency_cb2.place(x=253, y=280)


Label(root, text='Enter Amount:', bg='#00A868').place(x=65, y=330)
ent1 = Entry(root, bg='white')
ent1.place(x=200, y=330)
ent1.focus()
Label(root, text='Converted Amount:', bg='#00A868').place(x=65, y=380)
Label(root, text='', textvariable=results, bg='#00A868').place(x=200, y=380)


def convert(from_currency, to_currency, amount):
    # first convert it into USD if it is not in USD.
    # because our base currency is USD
    if from_currency != 'USD':
        amount = amount / conversion_rates[from_currency]

    amount = round(amount * conversion_rates[to_currency], 4)
    return amount


def perform():
    try:
        amount = float(ent1.get())
        from_curr = currency_cb.get()
        to_curr = currency_cb2.get()

        converted_amount = convert(from_curr, to_curr, amount)

        results.set(converted_amount)
    except ValueError:
        if ent1 != int and ent1 != float:
            messagebox.showerror('Entry not valid', 'Enter numbers only')

    except requests.exceptions.ConnectionError:
        messagebox.showerror('Internet error', 'Internet Bad')
    except KeyError:
        messagebox.showerror('ERROR!!!!!!!!!!!!!!!', 'Select Currency')


# kill program
def kill():
    return root.destroy()


def clear():
    currency_cb.set('Select Currency')
    currency_cb2.set('Select Currency')
    ent1.delete(0, END)
    ent1.focus()
    results.set('')


Button(root, text="CONVERT", borderwidth=3, bg='white', command=perform).place(x=180, y=430)
Button(root, text="EXIT", borderwidth=3, bg='white', command=kill).place(x=281, y=480)
Button(root, text="CLEAR", borderwidth=3, bg='white', command=clear).place(x=100, y=480)


root.mainloop()  # continuously runs program in window
