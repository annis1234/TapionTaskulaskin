from tkinter import Tk, ttk, constants
from ui.ui import UI

window = Tk()
window.title("Tapion taskulaskin")

window.geometry("300x300")

ui = UI(window)
ui.start()

window.mainloop()
