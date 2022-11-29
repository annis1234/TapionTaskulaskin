from math import pi

class Tree():

    def __init__(self, tree_sp: str, tree_d: int, tree_h: int):
        self.tree_sp = tree_sp
        self.tree_d = tree_d
        self.tree_h = tree_h
        self.tree_g = pi*(float(tree_d)/100/2)**2
        self.tree_v = float(tree_h) * float(self.tree_g) * 0.5

    def __str__(self):
        return f"Puulaji: {self.tree_sp}, läpimitta (cm): {self.tree_d}, pituus (cm): {self.tree_h}"
