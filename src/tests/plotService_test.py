import unittest
from services.plot_service import plot_service
from entities.tree import Tree


class TestPlot(unittest.TestCase):

    def setUp(self):
        self.plot_service = plot_service
        self.plot_service.clear_plot()

    def test_create(self):
        tree1 = Tree("Mänty", 28, 30)
        self.plot_service.create_tree(tree1)
        trees = self.plot_service.return_trees()

        self.assertEqual(len(trees), 1)
        self.assertEqual(trees[0].tree_sp, "Mänty")

    def test_mean_height(self):
        tree1 = Tree("Mänty", 28, 20)
        tree2 = Tree("Mänty", 28, 30)
        self.plot_service.create_tree(tree1)
        self.plot_service.create_tree(tree2)
        
        self.assertEqual(self.plot_service.mean_height(), 25)

    def test_mean_d(self):
        tree1 = Tree("Mänty", 20, 25)
        tree2 = Tree("Mänty", 30, 25)
        self.plot_service.create_tree(tree1)
        self.plot_service.create_tree(tree2)

        self.assertEqual(self.plot_service.mean_d(), 25)

    def test_v_sum(self):
        tree1 = Tree("Mänty", 20, 20)
        tree2 = Tree("Mänty", 20, 20)
        self.plot_service.create_tree(tree1)
        self.plot_service.create_tree(tree2)

        self.assertEqual(self.plot_service.sum_v(), 0.628)

    def test_main_tree_sp(self):
        tree1 = Tree("Mänty", 20, 20)
        tree2 = Tree("Mänty", 20, 20)
        tree3 = Tree("Kuusi", 25, 30)

        self.plot_service.create_tree(tree1)
        self.plot_service.create_tree(tree2)
        self.plot_service.create_tree(tree3)

        self.assertEqual(self.plot_service.main_tree_sp(), "Mänty")