
import tkinter as Tk
from tkinter import ttk, constants, StringVar
from services.plot_service import PLOT_SERVICE
from services.user_service import USER_SERVICE
from entities.tree import Tree


class PlotView():

    """Luokka, joka vastaa näkymästä, jossa koealatiedostoon lisätään puita
    """

    def __init__(self, root, handle_show_stand_data_view, show_handle_plots_view):
        """Luokan konstruktori

        Args:
            root: Tkinter-elementti, johon näkymä alustetaan
            handle_show_stand_data_view: metodi, jota kutsutaan,
                kun klikataan "Näytä koealan tiedot"
            show_handle_plots_view: metodi, jota kutsutaan,
                kun klikataan "Takaisin"
        """

        self._root = root
        self._frame = None
        self._plot_service = PLOT_SERVICE
        self._sp_entry = None
        self._d_entry = None
        self._h_entry = None
        self._user = USER_SERVICE.get_current_user()
        self._handle_show_stand_data_view = handle_show_stand_data_view
        self._show_handle_plots_view = show_handle_plots_view
        self._stand_data_frame = None
        self._stand_data_view = None

        self._error_variable = None
        self._error_label = None

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

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._initialize_add_tree()

        self._error_variable = StringVar(self._frame)

        self._error_label = ttk.Label(
            master = self._frame,
            textvariable=self._error_variable,
            foreground="red",
            font=("Comic Sans MS",15)
        )

        clear_plot_button = Tk.Button(
            master=self._frame,
            text="Tyhjennä koeala",
            command=self._handle_clear_plot,
            font=self._font,
            foreground=self._fg)

        show_stand_data_button = Tk.Button(
            master=self._frame,
            text="Näytä koealan tiedot",
            font=self._font,
            foreground=self._fg,
            command=self._handle_show_stand_data_view
        )

        show_handle_plots_view_button = Tk.Button(
            master=self._frame,
            text="Takaisin",
            font=self._font,
            foreground=self._fg,
            command=self._show_handle_plots_view
        )


        clear_plot_button.grid(
            row=9, column=0, sticky=constants.W, padx=5, pady=5)

        show_stand_data_button.grid(
            row=11, column=0, sticky=constants.W, padx=5, pady=5
        )

        show_handle_plots_view_button.grid(
            row=12, column=0, sticky=constants.W, padx=5, pady=5
        )

        self._hide_error()
    
    def _initialize_add_tree(self):

        label = ttk.Label(master=self._frame, text="Syötä puun tiedot:", font=self._font, foreground=self._fg)
        label_sp = ttk.Label(master=self._frame, text="Puulaji:", font=self._font, foreground=self._fg)
        label_d = ttk.Label(master=self._frame, text="Rinnankorkeusläpimitta (cm):", font=self._font, foreground=self._fg)
        label_h = ttk.Label(master=self._frame, text="Pituus (m):", font=self._font, foreground=self._fg)

        self._sp_entry = ttk.Entry(master=self._frame)
        self._h_entry = ttk.Entry(master=self._frame)
        self._d_entry = ttk.Entry(master=self._frame)

        add_tree_button = Tk.Button(
            master=self._frame,
            text="Lisää puu",
            font=self._font,
            foreground=self._fg,
            command=self._handle_add_tree)

        label.grid(columnspan=2, row=1, column=0,
                   sticky=constants.W, padx=5, pady=5)

        label_sp.grid(row=2, column=0)
        self._sp_entry.grid(row=3, column=0)

        label_d.grid(row=4, column=0)
        self._d_entry.grid(row=5, column=0)

        label_h.grid(row=6, column=0)
        self._h_entry.grid(row=7, column=0)

        add_tree_button.grid(
            row=8, column=0, sticky=constants.W, padx=5, pady=5)

    def _handle_add_tree(self):
        self._hide_error()

        tree_sp = self._sp_entry.get()
        tree_h = self._h_entry.get()
        tree_d = self._d_entry.get()
        user = self._user
        tree = Tree(tree_sp, tree_d, tree_h, user)
        
        try:
            self._plot_service.validate_tree(tree)
            self._plot_service.create_tree(tree)
            self._sp_entry.delete(0, constants.END)
            self._h_entry.delete(0, constants.END)
            self._d_entry.delete(0, constants.END)
        except ValueError:
            self._show_error("Tarkista syöttämäsi arvot!")

    def _show_error(self, message):
        self._error_variable.set(message)
        self._error_label.grid()

    def _hide_error(self):
        self._error_label.grid_remove()

    def _handle_clear_plot(self):
        self._plot_service.clear_plot()
