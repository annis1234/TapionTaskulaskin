import string
from entities.user import User

from repositories.user_repository import (
    user_repository as default_user_repository)

class InvalidCredentialsError(Exception):
    pass

class UsernameExistsError(Exception):
    pass

class UserService():
    """Käyttäjätunnusten käsittelystä vastaava luokka
    """

    def __init__(self, user_repository=default_user_repository):
        """Luokan konstruktori

        Args:
            user_repository: Olio, joka hoitaa UserRepository-luokan tehtävät
        """
        self._user_repository = user_repository
        self._user = None

    def create_user(self, username, password, login=True):
        """Luo uuden käyttäjän

        Args:
            username: Käyttäjän käyttätunnus, luetaan käyttäjältä
            password: Käyttäjän salasana, luetaan käyttäjältä
        Returns:
            New user as an User-object
        Raises:
            UsernameExistsError:
                Error occurs in case username already exists
        """

        existing_user = self._user_repository.find_by_username(username)

        if existing_user:
            raise UsernameExistsError("Username already exists")
        user = self._user_repository.create(User(username, password))

        if login:
            self._user = user

        return user

    def get_current_user(self):
        """Return user currently logged in
        """
        return self._user

    def login(self, username, password):
        """Log user in

            Args:
                username: username, read from user
                password: user password, read from user

            Returns:
                Logged in user as an User-object
            Raises:
                InvalidCredentialsError:
                    Error occurs in case of mismatch between username and password

        """

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise InvalidCredentialsError("Invalid username or password")
        self._user = user
        return user

    def logout(self):
        self._user = None

    def get_users(self):
        """Return all users

        Returns:
            All users as a list of User-objects
        """
        return self._user_repository.find_all()

    def validate_password(self, password):
        """Tarkastaa salasanan kelpoisuuden
        Returns:
            False, jos jokin ehdoista ei täyty
        """

        if len(password) < 6:
            return False
        if not any(char.isdigit() for char in password):
            return False
        if not any(char.isupper() for char in password):
            return False
        if not any(char.islower() for char in password):
            return False
        if not any(char in string.punctuation for char in password):
            return False
        return True

USER_SERVICE = UserService()
