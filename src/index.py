from tkinter import Tk
from ui.UI import UI

WINDOW = Tk()
WINDOW.title("Tapion taskulaskin")

WINDOW.geometry("500x500")

UI = UI(WINDOW)
UI.start()

WINDOW.mainloop()
