import unittest
from repositories.user_repository import user_repository
from entities.user import User

class TestUserRepository(unittest.TestCase):
    def setUp(self):
        user_repository.delete_all()

    def test_create(self):
        user_repository.create(User("Käyttäjä1", "TestiEka12-"))
        users = user_repository.find_all()

        self.assertEqual(len(users), 1)
        self.assertEqual(users[0].username, "Käyttäjä1")

