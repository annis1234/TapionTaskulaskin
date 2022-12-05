from tkinter import Tk, ttk
from ui.UI import UI

WINDOW = Tk()
WINDOW.title("Tapion taskulaskin")


HEADER = ttk.Label(text="Tapion taskulaskin", font=("Comic Sans MS", 25))
HEADER.place(x=20, y=20)

WINDOW.geometry("500x500")

UI = UI(WINDOW)
UI.start()

WINDOW.mainloop()
