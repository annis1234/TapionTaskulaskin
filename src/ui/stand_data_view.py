from tkinter import ttk, constants
from services.plot_service import plot_service

class StandDataView():

    def __init__ (self, root, handle_show_plot_view):
        self._root = root
        self._frame = None
        self._plot_service = plot_service
        self._handle_show_plot_view = handle_show_plot_view
        self._charts_frame = None
        self._charts_view = None

        self._initialize_stand_data()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize_stand_data(self):
        self._frame = ttk.Frame(master=self._root)
        self._charts_frame = ttk.Frame(master=self._frame)

        self._initialize_go_back_button()


        self._charts_frame.grid(
            row=20,
            column=0,
            columnspan=2,
            sticky= constants.EW
     )

        if self._plot_service.return_trees():
            main_tree_sp = ttk.Label(master=self._frame,
            text= f"Pääpuulaji: {self._plot_service.main_tree_sp()}")
            mean_d = ttk.Label(master=self._frame,
            text=f"Keskiläpimitta (cm): {self._plot_service.mean_d():0.2f}")
            mean_h = ttk.Label(master=self._frame,
            text=f"Keskipituus (m): {self._plot_service.mean_height():0.2f}")
            mean_v = ttk.Label(master=self._frame,
            text=f"Keskitilavuus (m3/ha): {self._plot_service.mean_v():0.3f}")

            main_tree_sp.grid(row=12, column=0, sticky=constants.W, padx=5, pady=5)
            mean_d.grid(row=13, column=0, sticky=constants.W, padx=5, pady=5)
            mean_h.grid(row=14, column=0, sticky=constants.W, padx=5, pady=5)
            mean_v.grid(row=15, column=0, sticky=constants.W, padx=5, pady=5)

        else:
            label= ttk.Label(master=self._frame, text="Koeala on tyhjä.")
            label.grid(row=11, column=0, sticky=constants.W, padx=5, pady=5)

    def _initialize_go_back_button(self):
        label = ttk.Button(master=self._frame, text="Takaisin", command=self._handle_show_plot_view)
        label.grid(row=0, column=1, sticky=constants.E)