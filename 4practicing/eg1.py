from tkinter import *

root = Tk()
root.geometry("500x500")
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

class MyLabel(Frame):
    def __init__(self, parent, myborderwidth=0, mybordercolor=None,
                 myborderplace='center', *args, **kwargs):
        Frame.__init__(self, parent, bg=mybordercolor)
        self.propagate(False)
        self.label = Label(self, *args, **kwargs)

        if myborderplace is 'left':
            self.label.pack(side='right')
        elif myborderplace is 'right':
            self.label.pack(side='left')
        else:
            self.label.pack()
            myborderwidth = myborderwidth * 2

        self.config(width=self.label.winfo_reqwidth() + myborderwidth)
        self.config(height=self.label.winfo_reqheight() + myborderwidth)

MyLabel(root, text='Hello World', myborderwidth=2, mybordercolor='black',
        myborderplace='right').grid()

root.mainloop()

Label1 = tk.Label(top, wraplength = 230, font=LabelsFont, fg="white", text="PRETLAK NA VSTUPE",image="", borderwidth=0, compound="center", highlightthickness=0)
Label1.place(x=15,y=90,width=237,height=37)
