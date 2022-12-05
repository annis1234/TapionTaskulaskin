from tkinter import ttk, constants
from services.plot_service import PLOT_SERVICE

class HandlePlotsView:

    def __init__(self, root, open_plot_handler):
        self._open_plot_handler = open_plot_handler
        self._root = root
        self.plot_entry = None
        self._select_plot_entry = None
        self._frame = None
        self._plot_list_frame = None
        self._plot_list_view = None
        self._plot_service = PLOT_SERVICE

        self._initialize()
    
    def pack(self):
        self._frame.place(relx=0.5, rely=0.5 ,anchor="center")

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):

        self._frame = ttk.Frame(master=self._root)
        self._plot_list_frame=ttk.Frame(master=self._frame)

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

        select_plot_label = ttk.Label(master=self._frame, text="Avaa koeala (nimi):")

        self._select_plot_entry = ttk.Entry(master=self._frame)

        select_plot_button = ttk.Button(
            master = self._frame,
            text = "Avaa koeala",
            command = self._handle_open_plot
        )

        create_plot_button.grid(padx=5, pady=5, sticky=constants.EW)
        select_plot_label.grid(padx=5, pady=5, sticky=constants.EW)
        self._select_plot_entry.grid(padx=5, pady=5, sticky=constants.EW)
        select_plot_button.grid(padx=5, pady=5, sticky=constants.EW)
    
    def _handle_add_plot(self):
        self._plot_service.create_plot(self._plot_entry.get())
        self._plot_entry.delete(0, constants.END)

    def _handle_open_plot(self):
        self._plot_service.select_plot(self._select_plot_entry.get())
        self._select_plot_entry.delete(0, constants.END)
        self._open_plot_handler()