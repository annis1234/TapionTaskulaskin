from entities.tree import Tree

from repositories.plot_repository import (
    plot_repository as default_plot_repository)

class PlotService():

    def __init__(self, plot_repository=default_plot_repository):
        self._plot_repository = plot_repository

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

    def return_h(self):
        h = []
        trees = self._plot_repository.find_all()
        for tree in trees:
            h.append(tree.tree_h)

        return h
        
    def return_d(self):
        d = []
        trees =self._plot_repository.find_all()
        for tree in trees:
            d.append(tree.tree_d)
        return d

plot_service = PlotService()
