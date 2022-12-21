import unittest
from services.plot_service import PLOT_SERVICE, InvalidCredentialsError, UsernameExistsError
from entities.tree import Tree
from entities.user import User

class TestPlot(unittest.TestCase):

    def setUp(self):
        self._plot_service = PLOT_SERVICE
        self._plot_service.create_plot("test_plot")
        self._plot_service.clear_plot()
        self.user = PLOT_SERVICE.get_current_user()

    def test_create_tree(self):
        tree1 = Tree("Mänty", 28, 30, self.user)
        self._plot_service.create_tree(tree1)
        trees = self._plot_service.return_trees()
        self.assertEqual(len(trees), 1)
        self.assertEqual(trees[0].tree_sp, "Mänty")

    def test_mean_height(self):
        tree1 = Tree("Mänty", 28, 20, self.user)
        tree2 = Tree("Mänty", 28, 30, self.user)
        self._plot_service.create_tree(tree1)
        self._plot_service.create_tree(tree2)
        self.assertEqual(self._plot_service.mean_height(), 25)

    def test_mean_d(self):
        tree1 = Tree("Mänty", 20, 25, self.user)
        tree2 = Tree("Mänty", 30, 25, self.user)
        self._plot_service.create_tree(tree1)
        self._plot_service.create_tree(tree2)
        self.assertEqual(self._plot_service.mean_diameter(), 25)

    def test_v_sum(self):
        tree1 = Tree("Mänty", 20, 20, self.user)
        tree2 = Tree("Mänty", 20, 20, self.user)
        self._plot_service.create_tree(tree1)
        self._plot_service.create_tree(tree2)
        self.assertEqual(self._plot_service.sum_vol(), 0.628)

    def test_main_tree_sp(self):
        tree1 = Tree("Mänty", 20, 20, self.user)
        tree2 = Tree("Mänty", 20, 20, self.user)
        tree3 = Tree("Kuusi", 25, 30, self.user)
        self._plot_service.create_tree(tree1)
        self._plot_service.create_tree(tree2)
        self._plot_service.create_tree(tree3)
        self.assertEqual(self._plot_service.main_tree_sp(), "Mänty")

    def test_handle_two_plots(self):
        self._plot_service.create_plot("test_plot2")
        self._plot_service.select_plot("test_plot2.csv")
        tree1 = Tree("Mänty", 20, 20, self.user)
        self._plot_service.create_tree(tree1)
        self.assertEqual(len(self._plot_service.return_trees()), 1)

        self._plot_service.select_plot("test_plot.csv")
        tree2 = Tree("Kuusi", 25, 25, self.user)
        self._plot_service.create_tree(tree2)

        self.assertEqual(len(self._plot_service.return_trees()), 1)

        self._plot_service.select_plot("test_plot2.csv")
        self._plot_service.clear_plot()

        self.assertEqual(len(self._plot_service.return_trees()), 0)

class TestUser(unittest.TestCase):

    def setUp(self):
        self.plot_service = PLOT_SERVICE

    def test_create_user(self):
        self.plot_service.create_user("Käyttäjä1", "EkaTesti12-")
        users = self.plot_service.get_users()

        self.assertEqual(len(users), 1)
        self.assertEqual(users[0].username, "Käyttäjä1")