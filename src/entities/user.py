class User:
    """Sovelluksen kyttäjää kuvaava luokka

        username: Käyttäjän käyttäjätunnus
        password: Käyttäjän salasana
    """
    def __init__(self, username, password):
        """Konstruktori, joka luo uuden käyttäjän

        Args:
            username: Käyttäjän käyttäjätunnus
            password: Käyttäjän salasana
        """
        self.username = username
        self.password = password
