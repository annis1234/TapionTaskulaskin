import tkinter as Tk
from tkinter import ttk, constants
from services.plot_service import PLOT_SERVICE


class PlotListView:

    def __init__(self, root, plots):
        self._root = root
        self._plots = plots
        self._frame = None
        self._plot_service = PLOT_SERVICE
#        self._handle_open_plot = handle_open_plot

        self._font = "Comic Sans MS", 15
        self._fg = "green"

        self._initialize()


    def pack(self):
        self._frame.place(relx=0.5, rely=0, anchor="n")

    def destroy(self):
        self._frame.destroy()

    def _initialize_plot(self, plot):
        plot_frame=ttk.Frame(master=self._frame)
        label=ttk.Label(master=plot_frame, text=plot, font=self._font, foreground=self._fg)

        open_plot_button = Tk.Button(
            master=plot_frame,
            text="Avaa koeala",
            font=("Comic Sans MS", 10),
            foreground=self._fg,
#            command=lambda:self._handle_open_plot(plot)
        )

        label.grid(row=0, column=0, sticky=constants.E)

        open_plot_button.grid(row=0,column=1, pady=5, sticky=constants.EW)

        plot_frame.pack(fill=constants.X)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        for plot in self._plots:
            self._initialize_plot(plot)


class HandlePlotsView:

    def __init__(self, root, open_plot_handler, handle_logout):
        self._open_plot_handler = open_plot_handler
        self._root = root
        self.plot_entry = None
        self._select_plot_entry = None
        self._frame = None
        self._plot_service = PLOT_SERVICE
        self._handle_logout = handle_logout
        self._user = PLOT_SERVICE.get_current_user()

        self._plot_list_frame = None
        self._plot_list_view = None

        self._font = "Comic Sans MS", 15
        self._fg = "green"

        self._initialize()
    
    def pack(self):
        self._frame.place(relx=0.5, rely=1, anchor="s")

    def destroy(self):
        self._frame.destroy()

    def _initialize_plot_list(self):
        if self._plot_list_view:
            self._plot_list_view.destroy()

        plots = self._plot_service.return_plots()

        self._plot_list_view = PlotListView(
            self._plot_list_frame,
            plots,
 #           self._handle_open_plot
        )

        self._plot_list_view.pack()

    def _initialize(self):

        self._frame = ttk.Frame(master=self._root)

        self._initialize_plot_list()
        self._initialize_create_plot()
        self._initialize_select_plot()

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

        user.grid(padx=5, pady=5, sticky=constants.W)
        logout_button.grid(padx=5, pady=5, sticky=constants.W)


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

        create_plot_button.grid(padx=5, pady=5, sticky=constants.EW)

    def _initialize_select_plot(self):
        select_plot_label = ttk.Label(master=self._frame, text="Avaa koeala (nimi):", font=self._font, foreground=self._fg)
        self._select_plot_entry = ttk.Entry(master=self._frame)

        select_plot_button = Tk.Button(
            master = self._frame,
            text = "Avaa koeala",
            font=self._font,
            command = self._handle_open_plot,
            foreground=self._fg
        )

        select_plot_label.grid(padx=5, pady=5, sticky=constants.EW)
        self._select_plot_entry.grid(padx=5, pady=5, sticky=constants.EW)
        select_plot_button.grid(padx=5, pady=5, sticky=constants.EW)
    
    def _handle_add_plot(self):
        self._plot_service.create_plot(self._plot_entry.get())
        self._plot_entry.delete(0, constants.END)
        self._initialize_plot_list()

    def _handle_open_plot(self):
        self._plot_service.select_plot(self._select_plot_entry.get())
        self._select_plot_entry.delete(0, constants.END)
        self._open_plot_handler()