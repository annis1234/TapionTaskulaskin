import tkinter as Tk
from tkinter import ttk, constants, StringVar
from services.user_service import USER_SERVICE, UsernameExistsError


class CreateUserView:
    """Uuden käyttäjän luomisesta vastaava näkymä
    """

    def __init__(self, root, handle_show_login_view, handle_create_user):
        """Luokan konstruktori

        Args:
            root: Tkinter-ikkuna näkymän alustamiseen
            handle_show_login_view: Metodi, joka hoitaa näkymän vaihtamisen kirjautumisnäkymään siirryttäessä
            handle_create_user: Metodi, jota kutsutaan kun uusi käyttäjä luodaan
        """

        self._root = root
        self._handle_create_user = handle_create_user
        self._handle_show_login_view = handle_show_login_view
        self._frame = None
        self._user_service = USER_SERVICE
        self._username_entry = None
        self._password_entry = None
        self._error_variable = None
        self._error_label = None

        self._font = "Comic Sans MS", 15
        self._fg = "green"

        self._initialize()

    def pack(self):
        """Näyttää näkymän"""
        self._frame.place(relx=0.5, rely=0.5 ,anchor="center")

    def destroy(self):
        """Tuhoaa näkymän"""
        self._frame.destroy()

    def _create_user_handler(self):
        """Käsittelee uuden käyttäjän luomisen
        """
        username = self._username_entry.get()
        password = self._password_entry.get()


        if self._user_service.validate_password(password) == False:
            self._show_error(f"Salasanan on oltava vähintään\n 6 merkkiä pitkä, ja sen tulee sisältää:\n\
            - Yksi pieni kirjain\n\
            - Yksi iso kirjain\n\
            - Yksi numero\n\
            - Yksi erikoismerkki")
            return

        try:
            self._user_service.create_user(username, password)
            self._handle_create_user()
        except UsernameExistsError:
            self._show_error(f"Käyttäjätunnus {username} on jo käytössä!")


    def _show_error(self, message):
        """Näyttää mahdollisen virheviestin"""
        self._error_variable.set(message)
        self._error_label.grid()

    def _hide_error(self):
        """Piilottaa virheviestin"""
        self._error_label.grid_remove()

    def _initialize(self):
        """Alustaa näkymän"""
        self._frame = ttk.Frame(master=self._root)
        username_label = ttk.Label(master=self._frame, text="Käyttäjätunnus", font=self._font, foreground=self._fg)
        self._username_entry = ttk.Entry(master=self._frame)

        self._error_variable = StringVar(self._frame)

        self._error_label = ttk.Label(
            master=self._frame,
            textvariable=self._error_variable,
            font = self._font,
            foreground="red"
        )

        self._error_label.grid(padx=5,pady=5)

        password_label = ttk.Label(master=self._frame, text="Salasana", font=self._font, foreground=self._fg)
        self._password_entry = ttk.Entry(master=self._frame)

        username_label.grid(sticky=constants.W, padx=5, pady=5)
        self._username_entry.grid(sticky=constants.W, padx=5, pady=5)

        password_label.grid(sticky=constants.W, padx=5, pady=5)
        self._password_entry.grid(sticky=constants.W, padx=5, pady=5)

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

        create_user_button.grid(padx=5, pady=5, sticky=constants.E)
        go_back_button.grid(padx=5, pady=5, sticky=constants.E)

        self._hide_error()
