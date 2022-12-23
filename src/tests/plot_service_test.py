import unittest
from services.plot_service import PLOT_SERVICE
from services.user_service import USER_SERVICE, InvalidCredentialsError, UsernameExistsError
from services.calc_service import CALC_SERVICE
from entities.tree import Tree

class TestPlot(unittest.TestCase):

    def setUp(self):
        self._plot_service = PLOT_SERVICE
        self._calc_service = CALC_SERVICE
        self._plot_service.create_plot("test_plot")
        self._plot_service.clear_plot()
        self._user = None

    def test_create_tree(self):
        tree1 = Tree("Mänty", 28, 30, self._user)
        self._plot_service.create_tree(tree1)
        trees = self._plot_service.return_trees()
        self.assertEqual(len(trees), 1)
        self.assertEqual(trees[0].tree_sp, "mänty")

    def test_create_tree_with_invalid_values(self):
        self.assertRaises(ValueError, lambda: self._plot_service.validate_tree(Tree("222", 25, 27, self._user)))
        self.assertRaises(ValueError, lambda: self._plot_service.validate_tree(Tree("Mänty", "ff", 27, self._user)))
        self.assertRaises(ValueError, lambda: self._plot_service.validate_tree(Tree("Mänty", "25", "kk", self._user)))

    def test_create_plot_with_invalid_name(self):
        self.assertRaises(ValueError, lambda: self._plot_service.create_plot(""))

    def test_mean_height(self):
        tree1 = Tree("Mänty", 28, 20, self._user)
        tree2 = Tree("Mänty", 28, 30, self._user)
        self._plot_service.create_tree(tree1)
        self._plot_service.create_tree(tree2)
        self.assertEqual(self._calc_service.mean_height(), 25)

    def test_mean_d(self):
        tree1 = Tree("Mänty", 20, 25, self._user)
        tree2 = Tree("Mänty", 30, 25, self._user)
        self._plot_service.create_tree(tree1)
        self._plot_service.create_tree(tree2)
        self.assertEqual(self._calc_service.mean_diameter(), 25)

    def test_v_sum(self):
        tree1 = Tree("Mänty", 20, 20, self._user)
        tree2 = Tree("Mänty", 20, 20, self._user)
        self._plot_service.create_tree(tree1)
        self._plot_service.create_tree(tree2)
        self.assertEqual(self._calc_service.sum_vol(), 0.628*50)

    def test_main_tree_sp(self):
        tree1 = Tree("Mänty", 20, 20, self._user)
        tree2 = Tree("Mänty", 20, 20, self._user)
        tree3 = Tree("Kuusi", 25, 30, self._user)
        self._plot_service.create_tree(tree1)
        self._plot_service.create_tree(tree2)
        self._plot_service.create_tree(tree3)
        self.assertEqual(self._calc_service.main_tree_sp(), "mänty")

    def test_handle_two_plots(self):
        self._plot_service.create_plot("test_plot2")

        self._plot_service.select_plot("test_plot2.csv")
        tree1 = Tree("Mänty", 20, 20, self._user)
        self._plot_service.create_tree(tree1)
        self.assertEqual(len(self._plot_service.return_trees()), 1)

        self._plot_service.select_plot("test_plot.csv")
        tree2 = Tree("Kuusi", 25, 25, self._user)
        self._plot_service.create_tree(tree2)

        self.assertEqual(len(self._plot_service.return_trees()), 1)

        self._plot_service.select_plot("test_plot2.csv")
        self._plot_service.clear_plot()

        self.assertEqual(len(self._plot_service.return_trees()), 0)

    def test_remove_plot(self):
        self._plot_service.remove_plot("test_plot2.csv")
        self.assertEqual(self._plot_service.ensure_plot_exists("test_plot2.csv"), False)


class TestUser(unittest.TestCase):

    def setUp(self):
        self._user_service = USER_SERVICE

    def test_create_user(self):
        self._user_service.create_user("Käyttäjä1", "EkaTesti12-")
        users = self._user_service.get_users()

        self.assertEqual(len(users), 1)
        self.assertEqual(users[0].username, "Käyttäjä1")
    
    def test_login(self):
        user = self._user_service.login("Käyttäjä1", "EkaTesti12-")
        self.assertEqual(user.username, "Käyttäjä1")

    def test_get_current_user(self):
        user = self._user_service.get_current_user()
        self.assertEqual(user.username, "Käyttäjä1")

    def test_logout(self):
        self._user_service.logout()
        self.assertEqual(self._user_service.get_current_user(), None)

    def test_invalid_login(self):
        self.assertRaises(InvalidCredentialsError, lambda: self._user_service.login("Käyttäjä1", "VaaraSalasana1-"))

    def test_username_exists(self):
        self.assertRaises(UsernameExistsError, lambda: self._user_service.create_user("Käyttäjä1", "TokaTesti12-"))

    def test_validate_password(self):
        self.assertEqual(self._user_service.validate_password("Sal1-"), False)
        self.assertEqual(self._user_service.validate_password("Salasana-"), False)
        self.assertEqual(self._user_service.validate_password("salasana1-"), False)
        self.assertEqual(self._user_service.validate_password("SALASANA1-"), False)
        self.assertEqual(self._user_service.validate_password("Salasana1"), False)
        self.assertEqual(self._user_service.validate_password("Salasana1-"), True)