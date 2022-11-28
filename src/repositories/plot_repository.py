from pathlib import Path
from entities.tree import Tree
from config import PLOT_FILE_PATH


class PlotRepository():

    def __init__(self, file_path):
        self._file_path = file_path

    def find_all(self):
        return self._read()

    def create(self, tree: Tree):
        trees = self.find_all()
        trees.append(tree)
        self._write(trees)
        return tree

    def _ensure_file_exists(self):
        Path(self._file_path).touch()

    def _read(self):
        trees = []

        self._ensure_file_exists()

        with open(self._file_path, encoding="utf-8") as file:
            for row in file:
                row = row.replace("\n", "")
                parts = row.split(";")
                tree_sp = parts[0]
                tree_d = float(parts[1])
                tree_h = float(parts[2])
                trees.append(Tree(tree_sp, tree_d, tree_h))

        return trees

    def _write(self, trees):

        with open(self._file_path, "w", encoding="utf-8") as file:
            for tree in trees:
                row = f"{tree.tree_sp};{float(tree.tree_d)};{float(tree.tree_h)}"

                file.write(row+"\n")

    def clear_plot(self):
        open(self._file_path, "w").close()

plot_repository = PlotRepository(PLOT_FILE_PATH)
