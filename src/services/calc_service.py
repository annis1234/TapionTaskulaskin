
from repositories.plot_repository import (
    PLOT_REPOSITORY as default_plot_repository)

class CalcService():
    """Koealatunnusten laskemisesta vastaava luokka
    """

    def __init__(self, plot_repository=default_plot_repository):
        """Luokan konstruktori

        Args:
            plot_repository: Olio, joka hoitaa PlotRepository-luokan tehtävät
        """
        self._plot_repository = plot_repository

    def mean_height(self):
        """Laskee koealan puuston keskipituuden

        Returns:
            Palauttaa koealan puuston keskipituuden
        """
        height_sum = 0
        trees = self._plot_repository.find_all_trees()
        for tree in trees:
            height_sum += tree.tree_height
        return height_sum/len(trees)

    def mean_diameter(self):
        """Laskee koealan puuston keskiläpimitan

        Returns:
            Palauttaa koealan puuston keskiläpimitan
        """
        d_sum = 0
        trees = self._plot_repository.find_all_trees()
        for tree in trees:
            d_sum += tree.tree_diameter
        return d_sum/len(trees)

    def sum_vol(self):
        """Laskee koealan puuston kokonaistilavuuden

        Returns:
            Palauttaa koealan puuston kokonaistilavuuden muunnettuna hehtaarikohtaiseksi
        """
        vol_sum = 0
        trees = self._plot_repository.find_all_trees()
        for tree in trees:
            vol_sum += tree.get_vol()
        return round(vol_sum, 3) * 50

    def main_tree_sp(self):
        """Laskee koelana puuston pääpuulajin

        Returns:
            Palauttaa koealan puuston pääpuulajin
        """
        trees = self._plot_repository.find_all_trees()
        species = []
        for tree in trees:
            species.append(tree.tree_sp)
        return max(species, key=species.count)

    def return_h(self):
        """Tallentaa koealan puiden pituudet listaksi

        Returns:
            Palauttaa listan puiden pituuksista
        """
        tree_heights = []
        trees = self._plot_repository.find_all_trees()
        for tree in trees:
            tree_heights.append(tree.tree_height)

        return tree_heights

    def return_d(self):
        """Tallentaa koealan puiden läpimitat listaksi

        Returns:
            Palauttaa listan puiden läpimitoista
        """
        tree_diameters = []
        trees =self._plot_repository.find_all_trees()
        for tree in trees:
            tree_diameters.append(tree.tree_diameter)
        return tree_diameters

CALC_SERVICE = CalcService()
