import tkinter as Tk
from tkinter import ttk, constants, StringVar
import string
from services.plot_service import PLOT_SERVICE, UsernameExistsError


class CreateUserView:

    def __init__(self, root, handle_show_login_view, handle_create_user):
        self._root = root
        self._handle_create_user = handle_create_user
        self._handle_show_login_view = handle_show_login_view
        self._frame = None
        self._username_entry = None
        self._password_entry = None
        self._error_variable = None
        self._error_label = None

        self._font = "Comic Sans MS", 15
        self._fg = "green"

        self._initialize()

    def pack(self):
        self._frame.place(relx=0.5, rely=0.5 ,anchor="center")

    def destroy(self):
        self._frame.destroy()

    def _create_user_handler(self):
        username = self._username_entry.get()
        password = self._password_entry.get()


        if self._check_password(password) == False:
            return

        try:
            PLOT_SERVICE.create_user(username, password)
            self._handle_create_user()
        except UsernameExistsError:
            self._show_error(f"Käyttäjätunnus {username} on jo käytössä!")

    def _check_password(self, password):
        if len(password) < 8:
            self._show_error("Salasanan täytyy olla yli 8 merkkiä!")
            return False
        elif not any(char.isdigit() for char in password):
            self._show_error("Salasanan täytyy sisältää numero!")
            return False
        elif not any(char.isupper() for char in password):
            self._show_error("Salasanan täytyy sisältää vähintään yksi iso kirjain!")
            return False
        elif not any(char.islower() for char in password):
            self._show_error("Salasanan täytyy sisältää vähitnään yksi pieni kirjain!")
            return False
        elif not any(char in string.punctuation for char in password):
            self._show_error("Salasanan täytyy sisältää vähintään yksi erikoismerkki!")
            return False

    def _show_error(self, message):
        self._error_variable.set(message)
        self._error_label.grid()

    def _hide_error(self):
        self._error_label.grid_remove()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        username_label = ttk.Label(master=self._frame, text="Käyttäjätunnus", font=self._font, foreground=self._fg)
        self._username_entry = ttk.Entry(master=self._frame)

        self._error_variable = StringVar(self._frame)

        self._error_label = ttk.Label(
            master=self._frame,
            textvariable=self._error_variable,
            foreground="red"
        )

        self._error_label.grid(padx=5,pady=5)

        password_label = ttk.Label(master=self._frame, text="Salasana", font=self._font, foreground=self._fg)
        self._password_entry = ttk.Entry(master=self._frame)

        username_label.grid(
            row=1, column=0, sticky=constants.W, padx=10, pady=10)
        self._username_entry.grid(
            row=2, column=0, sticky=constants.W, padx=10, pady=10)

        password_label.grid(
            row=3, column=0, sticky=constants.W, padx=10, pady=10)
        self._password_entry.grid(
            row=4, column=0, sticky=constants.W, padx=10, pady=10)

        create_user_button = Tk.Button(
            master=self._frame,
            text="Luo uusi",
            command=self._create_user_handler,
            font = self._font,
            foreground=self._fg)

        go_back_button = Tk.Button(
            master=self._frame,
            text="Takaisin",
            command = self._handle_show_login_view,
            font = self._font,
            foreground=self._fg)

        create_user_button.grid(padx=5, pady=5, sticky=constants.EW)
        go_back_button.grid(padx=5, pady=5, sticky=constants.EW)

        self._hide_error()
