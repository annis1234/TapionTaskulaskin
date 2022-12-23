from entities.tree import Tree

from repositories.plot_repository import (
    PLOT_REPOSITORY as default_plot_repository)

class PlotExistsError(Exception):
    pass


class PlotService():
    """Koealatiedostojen käsittelystä vastaava luokka
    """

    def __init__(self, plot_repository=default_plot_repository):
        """Luokan konstruktori

        Args:
            plot_repository: Olio, joka hoitaa PlotRepository-luokan tehtävät
            user_repository: Olio, joka hoitaa UserRepository-luokan tehtävät
        """
        self._plot_repository = plot_repository
        self._user = None

    def create_plot(self, plot_filename):
        """Luo uuden koealan csv-tiedostona
        Args:
            plot_filename: tiedoston nimi, luetaan käyttäjältä
        Raises:
            ValueError:
                Virhe ilmenee, jos syötekenttä on tyhjä
        """
        if plot_filename == "":
            raise ValueError
        self._plot_repository.create_plot(plot_filename)

    def select_plot(self, plot_filename):
        """Valitsee koealatiedoston, jota halutaan käsitellä

        Args:
            plot_filename: Valitun tiedoston nimi
        """
        self._plot_repository.select_plot(plot_filename)

    def remove_plot(self, plot_filename):
        """Poistaa koealatiedoston hakemistosta

        Args:
            plot_filename: Poistettavan tiedoston nimi
        """
        self._plot_repository.remove_plot(plot_filename)

    def clear_plot(self):
        """Tyhjentää koealatiedoston
        """
        self._plot_repository.clear_plot()

    def return_plots(self):
        """Palauttaa kaikkien tallennettujen koealatiedostojen nimet

        Returns:
            Palauttaa tiedostojen nimet listana

        """
        return self._plot_repository.return_plots()

    def ensure_plot_exists(self, plot_filename):
        """Tarkastaa, onko nimetty koealatiedosto olemassa
        
        Args:
            plot_filename: Koealatiedoston nimi, luetaan käyttäjältä

        Raises:
            PlotExistsError:
                Virhe ilmenee, jos samanniminen tiedosto on jo luotu

        Returns:
            False, jos samannimistä tiedostoa ei löydy
        """
        if self._plot_repository.ensure_plot_exists(plot_filename):
            raise PlotExistsError
        else:
            return False

    def create_tree(self, tree: Tree):
        """Luo puun ja lisää sen koealalle

        Args:
            Tree-olio, luetaan käyttäjältä
        """
        self._plot_repository.create_tree(tree)

    def validate_tree(self, tree):
        """Tarkastaa käyttäjän syöttämät puunutunnuset

        Args:
            Tree-olio, luetaan käyttäjältä
        
        Returns:
            True, jos arvot ovat oikein
        """
        if not tree.tree_sp.isalpha():
            raise ValueError

        if not tree.tree_diameter.replace(".", "", 1).isdigit() or float(tree.tree_diameter) < 0:
            raise ValueError

        if not tree.tree_height.replace(".", "", 1).isdigit() or float(tree.tree_height) < 1.3:
            raise ValueError

        return True

    def return_trees(self):
        """Hakee kaikki koealalle tallennetut puut

        Returns:
            Palauttaa listan koealalle tallennetuista puista
        """
        trees = self._plot_repository.find_all_trees()
        return trees


PLOT_SERVICE = PlotService()
