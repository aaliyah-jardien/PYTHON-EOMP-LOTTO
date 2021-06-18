# IMPORTING
import multiprocessing
from playsound import playsound
from tkinter import *

# WINDOW FEATURES
window = Tk()
window.title("Playing sound")
window.geometry("300x200")
window.config(bg="red")

p = multiprocessing.Process(target=playsound, args=('aaliyah.mp3',))


# FUNCTIONS
def play_music():
    p.start()


def stop_music():
    p.terminate()
    window.destroy()


# ADDING BUTTONS
play_btn = Button(window, text="Play", command=play_music)
play_btn.place(x=20, y=50)

stop_btn = Button(window, text="Stop", command=stop_music)
stop_btn.place(x=20, y=100)


window.mainloop()
