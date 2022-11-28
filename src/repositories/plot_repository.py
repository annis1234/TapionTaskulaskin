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

        with open(self._file_path) as file:
            for row in file:
                row = row.replace("\n", "")
                parts = row.split(";")
                sp = parts[0]
                d = float(parts[1])
                h = float(parts[2])
                trees.append(Tree(sp, d, h))

        return trees

    def _write(self, trees):

        with open(self._file_path, "w") as file:
            for tree in trees:
                row = f"{tree.sp};{float(tree.d)};{float(tree.h)}"

                file.write(row+"\n")

    def clear_plot(self):
        open(self._file_path, "w").close()

#    def print_trees(self):
#        trees = self.find_all()
#        for tree in trees:
#            print(tree)

#    def mean_height(self):
#        height_sum = 0
#        trees = self.find_all()
#        for tree in trees:
#            height_sum += tree.h
#        return height_sum/len(trees)

 #   def mean_d(self):
 #       d_sum = 0
 #       trees = self.find_all()
 #       for tree in trees:
 #           d_sum += tree.d
 #       return d_sum/len(trees)

 #   def mean_v(self):
 ##      trees = self.find_all()
  #      for tree in trees:
  #          v_sum += tree.v
  #      return v_sum/len(trees)

  #  def main_tree_sp(self):
  #      trees = self.find_all()
  #      species = []
  #      for tree in trees:
  # species.append(tree.sp)
   #     return max(species, key=species.count)

  #  def g(self):
  #      sum_g = 0
  #      trees = self.find_all()
  #      for tree in trees:
  #
  #      return sum_g


plot_repository = PlotRepository(PLOT_FILE_PATH)
