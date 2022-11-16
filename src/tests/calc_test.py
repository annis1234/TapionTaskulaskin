import unittest
import os
from plot import Plot
from tree import Tree

class TestPlot(unittest.TestCase):

    def setUp(self):
        dirname = os.path.dirname(__file__)
        self.plot = Plot(os.path.join(dirname, "plot.csv"))
        self.plot.clear_plot()

    def test_create(self):
        tree1 = Tree("Mänty", 28, 30)
        self.plot.create(tree1)
        trees = self.plot.find_all()

        self.assertEqual(len(trees), 1)
        self.assertEqual(trees[0].sp, "Mänty")


        
