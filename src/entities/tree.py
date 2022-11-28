from math import pi

class Tree():

    def __init__(self, sp: str, d: int, h: int):
        self.sp = sp
        self.d = d
        self.h = h
        self.g = pi*(d/100/2)**2
        self.v = h * self.g * 0.5

    def __str__(self):
        return f"Puulaji: {self.sp}, läpimitta (cm): {self.d}, pituus (cm): {self.h}"
