from tkinter import Tk, ttk
import os
import webbrowser
from PIL import ImageTk, Image
from ui.UI import UI

WINDOW = Tk()
WINDOW.title("Tapion taskulaskin")

HEADER = ttk.Label(text="Tapion taskulaskin", font=("Comic Sans MS", 25), foreground="green")
HEADER.place(x=20, y=20)

IMG_DIRNAME = os.path.dirname(__file__)
IMG_PATH = os.path.join(IMG_DIRNAME, "..", "images", "tree.png")

IMG = ImageTk.PhotoImage(Image.open(IMG_PATH))
HEADER_IMG = ttk.Label(image=IMG)
HEADER_IMG.place(x=50,y=70)
HEADER_CRED = ttk.Label(text="Kuva: https://pixabay.com/",
                        font=("Comic Sans MS", 10),
                        foreground="green",
                        cursor="hand1")

HEADER_CRED.place(x=50, y=320)
HEADER_CRED.bind("<Button-1>", lambda e: webbrowser.open_new_tab("https://pixabay.com/"))

WINDOW.geometry("900x800")

UI = UI(WINDOW)
UI.start()

WINDOW.mainloop()
