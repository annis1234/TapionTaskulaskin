import unittest
from repositories.plot_repository import PLOT_REPOSITORY
from entities.tree import Tree

class TestPlotRepository(unittest.TestCase):

    def setUp(self):
        self._plot_repository = PLOT_REPOSITORY

    def test_create_plot(self):
        self._plot_repository.create_plot("test_plot1")
        self.assertEqual(self._plot_repository.ensure_plot_exists("test_plot1.csv"), True)

    def test_remove_plot(self):
        self._plot_repository.remove_plot("test_plot1.csv")
        self.assertEqual(self._plot_repository.ensure_plot_exists("test_plot1.csv"), False)
