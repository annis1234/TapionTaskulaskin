from tkinter import Tk
from ui.ui import UI

window = Tk()
window.title("Tapion taskulaskin")

window.geometry("500x500")

ui = UI(window)
ui.start()

window.mainloop()
