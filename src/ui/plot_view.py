from services.plot_service import plot_service
from entities.tree import Tree
from tkinter import ttk, constants

class PlotView():

    def __init__(self, root):
        self._root = root
        self._frame = None
        self._plot_service = plot_service
        self._sp_entry = None
        self._d_entry = None
        self._h_entry = None
        self._stand_data_frame = None
        self._stand_data_view = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()
    
    def _initialize_header(self):
        header = ttk.Label(master=self._frame, text="Tapion taskulaskin")
        header.grid(columnspan=2, sticky=constants.W, padx=10, pady=10)

  #  def _initialize_stand_data(self):
  #      if self._stand_data_view:
  #          self._stand_data_view.destroy()

   #     self._stand_data_view =StandDataView(self._stand_data_frame)
#
 #       self._stand_data_view.pack()    
    
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

    def _handle_add_tree(self):
        sp = self._sp_entry.get()
        h = self._h_entry.get()
        d = self._d_entry.get()

        tree = Tree(sp, d, h)

        plot_service.create_tree(tree)
        self._sp_entry.delete(0, constants.END)
        self._h_entry.delete(0, constants.END)
        self._d_entry.delete(0, constants.END)

    def _handle_clear_plot(self):
        self._plot_service.clear_plot()
