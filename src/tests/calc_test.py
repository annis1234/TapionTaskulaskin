import unittest
import os
from services.plot_service import plot_service
from entities.tree import Tree

class TestPlot(unittest.TestCase):

    def setUp(self):
        self.plot_service=plot_service
        self.plot_service.clear_plot()

    def test_create(self):
        tree1 = Tree("Mänty", 28, 30)
        self.plot_service.create_tree(tree1)
        trees = self.plot_service.return_trees()

        self.assertEqual(len(trees), 1)
        self.assertEqual(trees[0].sp, "Mänty")


        
