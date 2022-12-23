from pathlib import Path
import os
from entities.tree import Tree
from config import PLOT_FILE_PATH


class PlotRepository():
    """Koealatiedostoja käsittelevä luokka
    """

    def __init__(self):
        """Luokan konsruktori
        """
        self._plot_filename = None
        self._file_path = None

    def create_plot(self, file_name):
        """Luo uuden koealan csv-tiedostona
        Args:
            file_name: Koealatiedoston nimi, luetaan käyttäjältä
        """
        self._plot_filename = f"{file_name}.csv"
        self._file_path = os.path.join(PLOT_FILE_PATH, self._plot_filename)
        Path(self._file_path).touch()

    def select_plot(self, plot_name):
        """Asettaa käyttäjän valitseman koealatiedoston nimen polkuun
        Args:
            plot_name: Valitun koealan nimi
        """
        self._plot_filename = plot_name
        self._file_path = os.path.join(PLOT_FILE_PATH, self._plot_filename)

    def remove_plot(self, plot_name):
        """Poistaa käyttäjän valitseman koealatiedoston hakemistosta
        Args:
            plot_name: Poistettavan koealan nimi
        """
        self._plot_filename = plot_name
        self._file_path = os.path.join(PLOT_FILE_PATH, self._plot_filename)
        os.remove(self._file_path)

    def ensure_plot_exists(self, plot_name):
        """Tarkistaa, onko koealatiedosto olemassa
        Args:
            plot_name: Koealatiedoston nimi, jonka olemassaolo tarkistetaan

        Returns:
            True, jos tiedosto on olemassa
        """
        plots = os.listdir(PLOT_FILE_PATH)
        return plot_name in plots

    def return_plots(self):
        """Palauttaa kaikkien olemassa olevien koealojen nimet

        Returns:
            Lista data/plots-hakemistossa sijaitsevista tiedostoista,
            poislukien piilotetut tai testejä varten luodut tiedostot
        """
        return [file for file in os.listdir(PLOT_FILE_PATH)
                if not (file.startswith(".") or file.startswith("test_"))]

    def find_all_trees(self):
        """Palauttaa kaikki koealalle tallennetut puut
        """
        return self._read()

    def create_tree(self, tree: Tree):
        """Luo ja lisää uuden puun koealalle
        Args:
            tree: Tree-olio, tiedot luetaan käyttäjältä
        Returns:
            Palauttaa luodun Tree-olion
        """
        trees = self.find_all_trees()
        trees.append(tree)
        self._write(trees)
        return tree

    def _read(self):
        trees = []

        with open(self._file_path, encoding="utf-8") as file:
            for row in file:
                row = row.replace("\n", "")
                parts = row.split(";")
                tree_sp = parts[0]
                tree_diameter = float(parts[1])
                tree_height = float(parts[2])
                user = parts[3]
                trees.append(Tree(tree_sp, tree_diameter, tree_height, user))

        return trees

    def _write(self, trees):

        with open(self._file_path, "w", encoding="utf-8") as file:
            for tree in trees:
                row = f"{tree.tree_sp.lower()};{float(tree.tree_diameter)};{float(tree.tree_height)};{tree.user}"

                file.write(row+"\n")

    def clear_plot(self):
        """Tyhjentää koealan
        """
        open(self._file_path, "w", encoding="utf-8").close()

PLOT_REPOSITORY = PlotRepository()
