
class Tree():

    def __init__(self, sp:str, d:int, h:int):
        self.sp = sp
        self.d = d
        self.h = h

    def __str__(self):
        return f"Puulaji: {self.sp}, läpimitta: {self.d}, pituus: {self.h}"

