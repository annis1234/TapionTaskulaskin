from tkinter import ttk, constants
from services.plot_service import plot_service
from entities.tree import Tree
from ui.stand_data_view import StandDataView


class PlotView():

    def __init__(self, root, handle_show_stand_data_view, show_handle_plots_view):
        self._root = root
        self._frame = None
        self._plot_service = plot_service
        self._sp_entry = None
        self._d_entry = None
        self._h_entry = None
        self._handle_show_stand_data_view = handle_show_stand_data_view
        self._show_handle_plots_view = show_handle_plots_view
        self._stand_data_frame = None
        self._stand_data_view = None

        self._initialize()

    def pack(self):
        self._frame.place(relx=0.5, rely=0.5 ,anchor="center")

    def destroy(self):
        self._frame.destroy()

    def _initialize_header(self):
        header = ttk.Label(master=self._frame, text="Tapion taskulaskin")
        header.grid(columnspan=2, sticky=constants.W, padx=10, pady=10)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self._initialize_header()

        label = ttk.Label(master=self._frame, text="Syötä puun tiedot:")
        label_sp = ttk.Label(master=self._frame, text="Puulaji:")
        label_d = ttk.Label(master=self._frame, text="Läpimitta (cm):")
        label_h = ttk.Label(master=self._frame, text="Pituus (m):")

        add_tree_button = ttk.Button(
            master=self._frame,
            text="Lisää puu",
            command=self._handle_add_tree)

        clear_plot_button = ttk.Button(
            master=self._frame,
            text="Tyhjennä koeala",
            command=self._handle_clear_plot)

        show_stand_data_button = ttk.Button(
            master=self._frame,
            text="Näytä koealan tiedot",
            command=self._handle_show_stand_data_view
        )

        show_handle_plots_view_button = ttk.Button(
            master=self._frame,
            text="Takaisin",
            command=self._show_handle_plots_view
        )

        self._sp_entry = ttk.Entry(master=self._frame)
        self._h_entry = ttk.Entry(master=self._frame)
        self._d_entry = ttk.Entry(master=self._frame)

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
        clear_plot_button.grid(
            row=9, column=0, sticky=constants.W, padx=5, pady=5)

        show_stand_data_button.grid(
            row=11, column=0, sticky=constants.W, padx=5, pady=5
        )

        show_handle_plots_view_button.grid(
            row=12, column=0, sticky=constants.W, padx=5, pady=5
        )

    def _handle_add_tree(self):
        tree_sp = self._sp_entry.get()
        tree_h = self._h_entry.get()
        tree_d = self._d_entry.get()

        tree = Tree(tree_sp, tree_d, tree_h)

        plot_service.create_tree(tree)
        self._sp_entry.delete(0, constants.END)
        self._h_entry.delete(0, constants.END)
        self._d_entry.delete(0, constants.END)

    def _handle_clear_plot(self):
        self._plot_service.clear_plot()
