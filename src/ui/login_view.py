import tkinter as Tk
from tkinter import ttk, StringVar, constants
from services.plot_service import PLOT_SERVICE, InvalidCredentialsError

class LoginView:

    def __init__(self, root, handle_login, handle_show_create_user_view):

        self._root = root
        self._handle_login = handle_login
        self._handle_show_create_user_view = handle_show_create_user_view
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

    def _login_handler(self):
        username = self._username_entry.get()
        password = self._password_entry.get()

        try:
            PLOT_SERVICE.login(username, password)
            self._handle_login()
        except InvalidCredentialsError:
            self._show_error("Väärä käyttäjätunnus tai salasana! :( Yritä uuudestaan!")
    
    def _show_error(self, message):
        self._error_variable.set(message)
        self._error_label.grid()

    def _hide_error(self):
        self._error_label.grid_remove

    def _initialize_password_field(self):
        password_label = ttk.Label(master=self._frame, text="Salasana", font=self._font, foreground=self._fg)
        self._password_entry = ttk.Entry(master=self._frame)
        password_label.grid(padx=5, pady=5, sticky=constants.W)
        self._password_entry.grid(padx=5, pady=5, sticky=constants.E)

    def _initialize_username_field(self):
        username_label = ttk.Label(master=self._frame, text="Käyttäjätunnus", font=self._font, foreground=self._fg)
        self._username_entry = ttk.Entry(master=self._frame)

        username_label.grid(padx=5, pady=5, sticky=constants.W)
        self._username_entry.grid(padx=5, pady=5, sticky=constants.E)

    def _initialize(self):
        self._frame = ttk.Frame(master = self._root)

        self._error_variable = StringVar(self._frame)

        self._error_label = ttk.Label(
            master = self._frame,
            textvariable=self._error_variable,
            foreground="red",
            font=("Comic Sans MS",15)
        )

        self._error_label.grid(padx=5,pady=5)

        self._initialize_username_field()
        self._initialize_password_field()

        login_button = Tk.Button(
            master=self._frame,
            text="Kirjaudu sisään",
            command = self._login_handler,
            font=self._font,
            foreground=self._fg
        )

        create_user_button = Tk.Button(
            master=self._frame,
            text="Uusi käyttäjä",
            command=self._handle_show_create_user_view,
            font=self._font,
            foreground=self._fg
        )

        login_button.grid(padx=5, pady=5, sticky=constants.E)
        create_user_button.grid(padx=5, pady=5, sticky=constants.E)

        self._hide_error()

