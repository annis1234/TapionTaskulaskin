from entities.tree import Tree
from entities.user import User

from repositories.plot_repository import (
    PLOT_REPOSITORY as default_plot_repository)

from repositories.user_repository import (
    user_repository as default_user_repository)

class InvalidCredentialsError(Exception):
    pass

class UsernameExistsError(Exception):
    pass

class PlotService():

    def __init__(self, plot_repository=default_plot_repository, user_repository=default_user_repository):
        self._plot_repository = plot_repository
        self._user_repository = user_repository

    def create_plot(self, plot_filename):
        self._plot_repository.create_plot(plot_filename)

    def select_plot(self, plot_filename):
        self._plot_repository.select_plot(plot_filename)

    def clear_plot(self):
        self._plot_repository.clear_plot()

    def return_plots(self):
        return self._plot_repository.return_plots()

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

    def create_user(self, username, password, login=True):

        existing_user = self._user_repository.find_by_username(username)

        if existing_user:
            raise UsernameExistsError("Käyttäjätunnus on jo luotu")
        user = self._user_repository.create(User(username, password))

        if login:
            self._user = user

        return user

    def get_current_user(self):
        return self._user


    def login(self, username, password):

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise InvalidCredentialsError("Invalid username or password")
        self._user = user
        return user

    def logout(self):
        self._user = None

    def get_users(self):
        return self._user_repository.find_all()


PLOT_SERVICE = PlotService()
