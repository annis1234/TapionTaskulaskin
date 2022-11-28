from tkinter import Tk
from ui.plot_view import PlotView


class UI:

    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._show_plot_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()
        self._current_view = None

    def _show_plot_view(self):
        self._hide_current_view()
        self._current_view = PlotView(self._root)
        self._current_view.pack()