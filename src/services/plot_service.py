from entities.tree import Tree

from repositories.plot_repository import (
    plot_repository as default_plot_repository)

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
        trees = self._plot_repository.find_all()
        for tree in trees:
            height_sum += tree.tree_h
        return height_sum/len(trees)

    def mean_d(self):
        d_sum = 0
        trees = self._plot_repository.find_all()
        for tree in trees:
            d_sum += tree.tree_d
        return d_sum/len(trees)

    def sum_v(self):
        v_sum = 0
        trees = self._plot_repository.find_all()
        for tree in trees:
            v_sum += tree.tree_v
        return round(v_sum, 3)

    def main_tree_sp(self):
        trees = self._plot_repository.find_all()
        species = []
        for tree in trees:
            species.append(tree.tree_sp)
        return max(species, key=species.count)

plot_service = PlotService()
