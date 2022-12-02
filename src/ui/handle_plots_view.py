from tkinter import ttk, constants
from services.plot_service import plot_service


class PlotListView:

    def __init__ (self, root, plots):
        self._root = root
        self._plots = plots
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize_plot(self, plot_name):
        plot_frame = ttk.Frame(master=self._frame)
        label = ttk.Label(master=plot_frame, text=plot_name)

        label.grid(row=0, column=0, padx=5, pady=5, sticky=constants.W)

        plot_frame.grid_columnconfigure(0, weight=1)
        plot_frame.pack(fill=constants.X)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        for plot in self._plots:
            self._initialize_plot(plot)



class HandlePlotsView:

    def __init__(self, root, open_plot_handler):
        self._open_plot_handler = open_plot_handler
        self._root = root
        self.plot_entry = None
        self._select_plot_entry = None
        self._frame = None
 #       self._plot_service = plot_service
        self._plot_list_frame = None
        self._plot_list_view = None

        self._initialize()
    
    def pack(self):
        self._frame.place(relx=0.5, rely=0.5 ,anchor="center")

    def destroy(self):
        self._frame.destroy()

    def _initialize_plot_list(self):
        if self._plot_list_view:
            self._plot_list_view.destroy()

            plots = plot_service.return_plots()

            self._plot_list_view = PlotListView(self._plot_list_frame, plots)

            self._plot_list_view.pack()

    def _initialize(self):

        self._frame = ttk.Frame(master=self._root)
        self._plot_list_frame=ttk.Frame(master=self._frame)

        self._initialize_plot_list()
        self._plot_list_frame.grid(row=1, column=0, columnspan=2, sticky=constants.EW)


        plot_label = ttk.Label(master=self._frame, text="Koealan nimi:")
        self._plot_entry = ttk.Entry(master=self._frame)
        plot_label.grid(
            row=1, column=0, sticky=constants.W, padx=10, pady=10)
        self._plot_entry.grid(
            row=2, column=0)

        create_plot_button = ttk.Button(
            master=self._frame,
            text="Luo koeala",
            command = self._handle_add_plot)

        select_plot_label = ttk.Label(master=self._frame, text="Avaa koeala (nimi)")

        self._select_plot_entry = ttk.Entry(master=self._frame)

        select_plot_button = ttk.Button(
            master = self._frame,
            text = "Avaa",
            command = self._handle_open_plot
        )

        create_plot_button.grid(padx=5, pady=5, sticky=constants.EW)
        select_plot_label.grid(padx=5, pady=5, sticky=constants.EW)
        self._select_plot_entry.grid(padx=5, pady=5, sticky=constants.EW)
        select_plot_button.grid(padx=5, pady=5, sticky=constants.EW)
    
    def _handle_add_plot(self):
        plot_service.create_plot(self._plot_entry.get())
        self._initialize_plot_list()
        self._plot_entry.delete(0, constants.END)

    def _handle_open_plot(self):
        plot_service.select_plot(self._select_plot_entry.get())
        self._select_plot_entry.delete(0, constants.END)
        self._open_plot_handler()