from entities.user import User
from database_connection import get_database_connection


def get_user_by_row(row):
    return User(row["username"], row["password"]) if row else None


class UserRepository:
    """Käyttäjätietoja käsittelevästä tietokannasta vastaava luokka
    """

    def __init__(self, connection):
        """Luokan konstruktori

        Args:
            connection: Connection-olio tietokantayhteyden muodostamista varten
        """
        self._connection = connection

    def create(self, user):
        """Luo ja lisää uuden käyttäjän tietokantaan

        Args:
            user: Uusi käyttäjä, joka tallennetaan
        Returns:
            Palauttaa tallennetun käyttäjän

        """
        cursor = self._connection.cursor()
        cursor.execute(
            "insert into users (username, password) values(?,?)",
            (user.username, user.password)
        )
        self._connection.commit()
        return user

    def find_by_username(self, username):
        cursor = self._connection.cursor()
        cursor.execute(
            "select * from users where username =?", (username,)
        )
        row = cursor.fetchone()
        return get_user_by_row(row)

    def find_all(self):
        """Hakee kaikki tallennetut käyttäjät tietokannasta
        Returns:
            Palauttaa listan tietokannan käyttäjistä User-olioina
        """
        cursor=self._connection.cursor()
        cursor.execute("select * from users")
        rows=cursor.fetchall()

        return list(map(get_user_by_row, rows))

    def delete_all(self):
        """Poistaa kaikki käyttäjät tietokannasta
        """
        cursor=self._connection.cursor()
        cursor.execute("delete from users")
        self._connection.commit()

user_repository = UserRepository(get_database_connection())
