import mysql.connector
from database.config import DB_CONFIG


class Connexion:

    _instance = None

    @staticmethod
    def get_instance():

        if Connexion._instance is None:
            try:

                Connexion._instance = mysql.connector.connect(**DB_CONFIG)
                print("Connexion à la base de données réussie")
            except mysql.connector.Error as e:
                print(f"Erreur de connexion : {e}")

        return Connexion._instance