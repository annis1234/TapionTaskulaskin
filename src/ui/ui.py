from ui.plot_view import PlotView
from ui.stand_data_view import StandDataView

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
        self._current_view = PlotView(self._root, self._show_stand_data_view)
        self._current_view.pack()

    def _show_stand_data_view(self):
        self._hide_current_view()
        self._current_view = StandDataView(self._root, self._show_plot_view)
        self._current_view.pack()
