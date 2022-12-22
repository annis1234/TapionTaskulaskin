import string
from entities.tree import Tree
from entities.user import User

from repositories.plot_repository import (
    PLOT_REPOSITORY as default_plot_repository)


class PlotService():
    """Sovelluslogiikasta vastaava luokka
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
        """
        if plot_filename == "":
            raise ValueError
        self._plot_repository.create_plot(plot_filename)

    def select_plot(self, plot_filename):
        """Valitsee koealatiedoston, jota halutaan käsitellä

        Args:
            plot_filename: Valitun tiedoston nimi, luetaan käyttäjältä
        """
        self._plot_repository.select_plot(plot_filename)
   
    def remove_plot(self, plot_filename):
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

    def create_tree(self, tree: Tree):
        """Luo puun ja lisää sen koealalle

        Args:
            Tree-olio, luetaan käyttäjältä
        """
        self._plot_repository.create_tree(tree)

    def validate_tree(self, tree):
        if not tree.tree_sp.isalpha():
            raise ValueError

        if not tree.tree_diameter.replace(".", "", 1).isdigit() or float(tree.tree_diameter) < 0:
            raise ValueError

        if not tree.tree_height.replace(".", "", 1).isdigit() or float(tree.tree_height) < 1.3:
            raise ValueError

    def return_trees(self):
        """Hakee kaikki koealalle tallennetut puut

        Returns:
            Palauttaa listan koealalle tallennetuista puista
        """
        trees = self._plot_repository.find_all_trees()
        return trees

    def mean_height(self):
        """Laskee koealan puuston keskipituuden

        Returns:
            Palauttaa koealan puuston keskipituuden
        """
        height_sum = 0
        trees = self.return_trees()
        for tree in trees:
            height_sum += tree.tree_height
        return height_sum/len(trees)

    def mean_diameter(self):
        """Laskee koealan puuston keskiläpimita

        Returns:
            Palauttaa koealan puuston keskiläpimitan
        """
        d_sum = 0
        trees = self.return_trees()
        for tree in trees:
            d_sum += tree.tree_diameter
        return d_sum/len(trees)

    def sum_vol(self):
        """Laskee koealan puuston kokonaistilavuuden

        Returns:
            Palauttaa koealan puuston kokonaistilavuuden
        """
        vol_sum = 0
        trees = self.return_trees()
        for tree in trees:
            vol_sum += tree.get_vol()
        return round(vol_sum, 3) * 50 # jos koealan pinta-ala 200m2

    def main_tree_sp(self):
        """Laskee koelana puuston pääpuulajin

        Returns:
            Palauttaa koealan puuston pääpuulajin
        """
        trees = self.return_trees()
        species = []
        for tree in trees:
            species.append(tree.tree_sp)
        return max(species, key=species.count)

    def return_h(self):
        tree_heights = []
        trees = self._plot_repository.find_all_trees()
        for tree in trees:
            tree_heights.append(tree.tree_height)

        return tree_heights

    def return_d(self):
        tree_diameters = []
        trees =self._plot_repository.find_all_trees()
        for tree in trees:
            tree_diameters.append(tree.tree_diameter)
        return tree_diameters

PLOT_SERVICE = PlotService()
