from ui.plot_view import PlotView
from ui.stand_data_view import StandDataView
from ui.handle_plots_view import HandlePlotsView
from ui.login_view import LoginView
from ui.create_user_view import CreateUserView

class UI:

    """Käyttöliittymän näkymien vaihtavmisesta vastaava luokka
    """

    def __init__(self, root):
        """Luokan konstruktori

        Args:
            root: Tkinter-ikkuna, johon näkymä alustetaan
        """
        self._root = root
        self._current_view = None

    def start(self):
        """Näyttää ohjelman käynnistyessä näytettävän näkymän
        """
        self._show_login_view()

    def _hide_current_view(self):
        """Piilottaa näkymän
        """ 
        if self._current_view:
            self._current_view.destroy()
        self._current_view = None
    
    def _show_login_view(self):
        """Näyttää kirjautumisnäkymän
        """
        self._hide_current_view()
        self._current_view = LoginView(self._root, self._show_handle_plots_view, self._show_create_user_view)
        self._current_view.pack()

    def _show_create_user_view(self):
        """Näyttää näkymän, jossa luodaan uusi käyttäjä
        """
        self._hide_current_view()
        self._current_view = CreateUserView(self._root, self._show_login_view, self._show_handle_plots_view)
        self._current_view.pack()

    def _show_plot_view(self):
        """Näyttää näkymän, jonka kautta koealatiedostoon lisätään puita
        """
        self._hide_current_view()
        self._current_view = PlotView(self._root, self._show_stand_data_view, self._show_handle_plots_view)
        self._current_view.pack()

    def _show_stand_data_view(self):
        """Näyttää koealan puustotiedot esittävän näkymän
        """
        self._hide_current_view()
        self._current_view = StandDataView(self._root, self._show_plot_view)
        self._current_view.pack()

    def _show_handle_plots_view(self):
        """Näyttää näkymän, jossa luodaan tai poistetaan koealatiedostoja
        """
        self._hide_current_view()
        self._current_view = HandlePlotsView(self._root, self._show_plot_view, self._show_login_view)
        self._current_view.pack()
