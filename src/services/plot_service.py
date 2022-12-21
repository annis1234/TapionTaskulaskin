import string
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
    """Sovelluslogiikasta vastaava luokka
    """

    def __init__(self, plot_repository=default_plot_repository,
                    user_repository=default_user_repository):
        """Luokan konstruktori

        Args:
            plot_repository: Olio, joka hoitaa PlotRepository-luokan tehtävät
            user_repository: Olio, joka hoitaa UserRepository-luokan tehtävät
        """
        self._plot_repository = plot_repository
        self._user_repository = user_repository
        self._user = None

    def create_plot(self, plot_filename):
        """Luo uuden koealan csv-tiedostona
        Args:
            plot_filename: tiedoston nimi, luetaan käyttäjältä
        """
        self._plot_repository.create_plot(plot_filename)

    def select_plot(self, plot_filename):
        """Valitsee koealatiedoston, jota halutaan käsitellä

        Args:
            plot_filename: Valitun tiedoston nimi, luetaan käyttäjältä
        """
        self._plot_repository.select_plot(plot_filename)

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
            vol_sum += tree.tree_vol
        return round(vol_sum, 3)

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

    def create_user(self, username, password, login=True):
        """Luo uuden käyttäjän

        Args:
            username: Käyttäjän käyttätunnus, luetaan käyttäjältä
            password: Käyttäjän salasana, luetaan käyttäjältä
        Returns:
            New user as an User-object
        Raises:
            UsernameExistsError:
                Error occurs in case username already exists
        """

        existing_user = self._user_repository.find_by_username(username)

        if existing_user:
            raise UsernameExistsError("Username already exists")
        user = self._user_repository.create(User(username, password))

        if login:
            self._user = user

        return user

    def get_current_user(self):
        """Return user currently logged in
        """
        return self._user

    def login(self, username, password):
        """Log user in

            Args:
                username: username, read from user
                password: user password, read from user

            Returns:
                Logged in user as an User-object
            Raises:
                InvalidCredentialsError:
                    Error occurs in case of mismatch between username and password

        """

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise InvalidCredentialsError("Invalid username or password")
        self._user = user
        return user

    def logout(self):
        self._user = None

    def get_users(self):
        """Return all users

        Returns:
            All users as a list of User-objects
        """
        return self._user_repository.find_all()

    def validate_password(self, password):
        """Tarkastaa salasanan kelpoisuuden
        Returns:
            False, jos jokin ehdoista ei täyty
        """

        if len(password) < 6:
            return False
        if not any(char.isdigit() for char in password):
            return False
        if not any(char.isupper() for char in password):
            return False
        if not any(char.islower() for char in password):
            return False
        if not any(char in string.punctuation for char in password):
            return False
        return True

PLOT_SERVICE = PlotService()
