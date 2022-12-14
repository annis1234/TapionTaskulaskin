import tkinter as Tk
from tkinter import ttk, constants, StringVar
from services.plot_service import PLOT_SERVICE, PlotExistsError
from services.user_service import USER_SERVICE

class PlotListView:
    """Koealalistauksesta vastaava näkymä
    """
    
    def __init__(self, root, plots, handle_open_plot, remove_plot):
        """Luokan konstruktori

        Args:
            root: Tkinter-elementti, johon näkymä alustetaan
            plots: lista näytettävistä koealojen nimistä
            handle_open_plot: metodi, jota kutsutaan,
                kun klikataan "Avaa koeala"
            remove_plot: metodi, jota kutsutaan,
                kun klikataan: "Poista koeala"
        """
        self._root = root
        self._plots = plots
        self._frame = None
        self._plot_service = PLOT_SERVICE
        self._handle_open_plot = handle_open_plot
        self._remove_plot = remove_plot
        self._error_variable = None
        self._error_label = None
        self._font = "Comic Sans MS", 15
        self._fg = "green"

        self._initialize()

    def pack(self):
        """Pakkaa näkymän
        """
        self._frame.pack()

    def destroy(self):
        """Tuhoaa näkymän
        """
        self._frame.destroy()

    def _initialize_plot(self, plot):
        plot_frame=ttk.Frame(master=self._frame)

        label=ttk.Label(master=plot_frame, text=plot, font=self._font, foreground=self._fg)
        label.grid(row=0, column=0, sticky=constants.E)

        open_plot_button = Tk.Button(
            master=plot_frame,
            text="Avaa koeala",
            font=self._font,
            foreground=self._fg,
            command=lambda: self._handle_open_plot(plot)
        )

        remove_plot_button = Tk.Button(
            master=plot_frame,
            text="Poista koeala",
            font =self._font,
            foreground=self._fg,
            command=lambda: self._remove_plot(plot)
        )

        open_plot_button.grid(
            row=0,
            column=1,
            padx=3,
            pady=3,
            sticky=constants.EW
        )

        remove_plot_button.grid(
            row=0,
            column=2,
            padx=3,
            pady=3,
            sticky=constants.EW
        )

        plot_frame.pack()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        for plot in self._plots:
            self._initialize_plot(plot)


class HandlePlotsView:

    """Koealatiedostojen lisäämisestä ja poistamisesta vastaava näkymä
    """

    def __init__(self, root, open_plot_handler, handle_logout):
        """Luokan konstruktori
        
        Args:
            root: Tkinter-elementti, jonka sisään näkymä alustetaan
            open_plot_handler: metodi, jota kutsutaan,
                kun klikataan "Avaa koeala"
            handel_logout: metodi, jota kutsutaan,
                kun klikataan "Kirjaudu ulos
            """        
        self._open_plot_handler = open_plot_handler
        self._root = root
        self.plot_entry = None
        self._select_plot_entry = None
        self._frame = None
        self._plot_service = PLOT_SERVICE
        self._handle_logout = handle_logout
        self._user = USER_SERVICE.get_current_user()

        self._plot_list_frame = None
        self._plot_list_view = None

        self._font = "Comic Sans MS", 15
        self._fg = "green"

        self._initialize()
    
    def pack(self):
        """Pakkaa näkymän
        """
        self._frame.place(relx=0.5, rely=0.5 ,anchor="center")

    def destroy(self):
        """Tuhoaa näkymän
        """
        self._frame.destroy()

    def _initialize_plot_list(self):
        if self._plot_list_view:
            self._plot_list_view.destroy()

        plots = self._plot_service.return_plots()

        self._plot_list_view = PlotListView(
            self._plot_list_frame,
            plots,
            self._handle_open_plot,
            self._handle_remove_plot
        )

        self._plot_list_view.pack()

    def _initialize(self):

        self._frame = ttk.Frame(master=self._root)
        self._plot_list_frame = ttk.Frame(master=self._frame)

        self._plot_list_frame.grid(
            padx= 5,
            pady = 5,
            sticky=constants.W)

        self._initialize_plot_list()
        self._initialize_create_plot()

        self._error_variable = StringVar(self._frame)

        self._error_label = ttk.Label(
            master = self._frame,
            textvariable=self._error_variable,
            foreground="red",
            font=("Comic Sans MS",15)
        )

        user = ttk.Label(
            master=self._frame,
            text=f"Käyttäjä: {self._user.username}",
            font=self._font,
            foreground=self._fg
        )

        logout_button = Tk.Button(
            master = self._frame,
            text="Kirjaudu ulos",
            font=self._font,
            foreground=self._fg,
            command=self._handle_logout
        )

        user.grid(padx=5, pady=5)
        logout_button.grid(padx=5, pady=5)

        self._hide_error()

    def _initialize_create_plot(self):
        plot_label = ttk.Label(master=self._frame, text="Koealan nimi:", font=self._font, foreground=self._fg)
        self._plot_entry = ttk.Entry(master=self._frame)

        plot_label.grid(sticky=constants.W, padx=5, pady=5)
        self._plot_entry.grid(padx=5, pady=5)

        create_plot_button = Tk.Button(
            master=self._frame,
            text="Luo koeala",
            font=self._font,
            command = self._handle_add_plot,
            foreground=self._fg)

        create_plot_button.grid(padx=5, pady=5)

    def _handle_add_plot(self):
        
        self._hide_error()

        try:
            self._plot_service.ensure_plot_exists(f"{self._plot_entry.get()}.csv")
            self._plot_service.create_plot(self._plot_entry.get())
        except PlotExistsError:
            self._show_error(f"{self._plot_entry.get()} on jo olemassa!")
        except ValueError:
            self._show_error("Tarkista koealan nimi!")

        self._plot_entry.delete(0, constants.END)
        self._initialize_plot_list()

    def _handle_open_plot(self, plot):
        self._plot_service.select_plot(plot)
        self._open_plot_handler()

    def _handle_remove_plot(self, plot):
        self._plot_service.remove_plot(plot)
        self._initialize_plot_list()


    def _show_error(self, message):
        self._error_variable.set(message)
        self._error_label.grid()

    def _hide_error(self):
        self._error_label.grid_remove()