from tkinter import Tk, ttk
from ui.UI import UI
import os
from PIL import ImageTk, Image

WINDOW = Tk()
WINDOW.title("Tapion taskulaskin")

IMG_DIRNAME = os.path.dirname(__file__)
IMG_PATH = os.path.join(IMG_DIRNAME, "..", "images", "tree.png")

BG_IMG = ImageTk.PhotoImage(Image.open(IMG_PATH))
BG = ttk.Label(image=BG_IMG)

BG.place(x=50,y=60)

HEADER = ttk.Label(text="Tapion taskulaskin", font=("Comic Sans MS", 25), foreground="green")
HEADER.place(x=20, y=20)

WINDOW.geometry("700x700")

UI = UI(WINDOW)
UI.start()

WINDOW.mainloop()
