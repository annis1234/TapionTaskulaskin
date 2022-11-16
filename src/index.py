from plot import Plot
from tree import Tree
from consoleIO import IO
import os

commands = {
    "x" : "x lopeta",
    "1" : "lisää puu",
    "2" : "hae puut",
    "3" : "tyhjennä koeala"
}

class tapionTaskulaskin():

    def __init__(self, io, plot):
        self.plot = plot
        self.io = io

    def start(self):
        self.io.print_string("Tapion taskulaskin")
        self.print_guide()

        while True:
            command = self.io.read_command("Komento: ")

            if command not in commands:
                self.io.print_string("Virheellinen komento")

            if command == "x":
                break

            if command == "1":
                sp = input("Puulaji: ")
                d = input("Läpimitta (cm): ")
                h = input("Pituus (m): ")

                self.plot.create(Tree(sp, d, h))

            if command == "2":
                self.plot.print_trees()

            if command == "3":
                self.plot.clear_plot()

    def print_guide(self):
        print("Tervetuloa! Tämä sovellus kirjoittaa puutunnuksia csv-tiedostoon.\nKomennot:\n1 - Lisää puu\n2 - Tulosta puut\n3 - Tyhjennä tiedosto\nx - Lopeta")

if __name__ == "__main__":

    dirname = os.path.dirname(__file__)
    plot = Plot(os.path.join(dirname, "plot.csv"))
    io = IO()

    laskin = tapionTaskulaskin(io, plot)
    laskin.start()
