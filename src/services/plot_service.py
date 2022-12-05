from entities.tree import Tree

from repositories.plot_repository import (
    PLOT_REPOSITORY as default_plot_repository)

class PlotService():

    def __init__(self, plot_repository=default_plot_repository):
        self._plot_repository = plot_repository

    def create_plot(self, plot_filename):
        self._plot_repository.create_plot(plot_filename)

    def select_plot(self, plot_filename):
        self._plot_repository.select_plot(plot_filename)

    def return_plots(self):
        self._plot_repository.return_plots()

    def clear_plot(self):
        self._plot_repository.clear_plot()

    def create_tree(self, tree: Tree):
        self._plot_repository.create(tree)

    def return_trees(self):
        trees = self._plot_repository.find_all()
        return trees

    def mean_height(self):
        height_sum = 0
        trees = self.return_trees()
        for tree in trees:
            height_sum += tree.tree_height
        return height_sum/len(trees)

    def mean_diameter(self):
        d_sum = 0
        trees = self.return_trees()
        for tree in trees:
            d_sum += tree.tree_diameter
        return d_sum/len(trees)

    def sum_vol(self):
        vol_sum = 0
        trees = self.return_trees()
        for tree in trees:
            vol_sum += tree.tree_vol
        return round(vol_sum, 3)

    def main_tree_sp(self):
        trees = self.return_trees()
        species = []
        for tree in trees:
            species.append(tree.tree_sp)
        return max(species, key=species.count)

PLOT_SERVICE = PlotService()
