from math import pi

class Tree():
    """Yksittäistä puuta kuvaava luokka

    Attributes:
        tree_sp: Puulaji
        tree_diameter: Puun läpimitta
        tree_heigth: Puun pituus
    """

    def __init__(self, tree_sp: str, tree_diameter: int, tree_height: int, user):
        """Konstruktori, joka luo uuden Tree-olion

        Args:
            tree_sp: Puulaji, luetaan käyttäjältä
            tree_diameter: Puun läpimitta, luetaan käyttäjältä
            tree_height: Puun pituus, luetaan käyttäjältä

        """
        self.tree_sp = tree_sp
        self.tree_diameter = tree_diameter
        self.tree_height = tree_height
        self.user = user

    def get_vol(self):
        return float(self.tree_height) * float(self.get_basal_area()) * 0.5

    def get_basal_area(self):
        return pi*(float(self.tree_diameter)/100/2)**2

    def __str__(self):
        return f"Puulaji: {self.tree_sp}, läpimitta (cm): {self.tree_diameter},\
                pituus (m): {self.tree_height}"
