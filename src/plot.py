from entities.tree import Tree

class Plot():

    def __init__(self, file_path):
        self._file_path = file_path

    def find_all(self):
        return self._read()

    def create(self, tree:Tree):
        trees = self.find_all()
        
        trees.append(tree)

        self._write(trees)

        return tree

    def _read(self):
        trees = []

        with open(self._file_path) as file:
            for row in file:
                row = row.replace("\n", "")
                parts = row.split(";")
                sp = parts[0]
                d = parts[1]
                h = parts[2]
                trees.append(Tree(sp, d, h))

        return trees

    def _write(self, trees):

        with open(self._file_path, "w") as file:
            for tree in trees:
                row = f"{tree.sp};{tree.d};{tree.h}"
                
                file.write(row+"\n")

    def clear_plot(self):
        self._write([])

    def print_trees(self):
        trees = self.find_all()
        for tree in trees:
            print(tree)