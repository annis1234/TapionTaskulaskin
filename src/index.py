from tkinter import Tk
from ui.ui import UI

window = Tk()
window.title("Tapion taskulaskin")

window.geometry("700x700")

ui = UI(window)
ui.start()

window.mainloop()
