from math import pi

class Tree():

    def __init__(self, tree_sp: str, tree_diameter: int, tree_height: int):
        self.tree_sp = tree_sp
        self.tree_diameter = tree_diameter
        self.tree_height = tree_height
        self.tree_g = pi*(float(tree_diameter)/100/2)**2
        self.tree_vol = float(tree_height) * float(self.tree_g) * 0.5

    def __str__(self):
        return f"Puulaji: {self.tree_sp}, läpimitta (cm): {self.tree_diameter}, pituus (cm): {self.tree_height}"
