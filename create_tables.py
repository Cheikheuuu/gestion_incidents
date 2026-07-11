from database.connexion import Connexion


def create_tables():

    connexion = Connexion.get_instance()

    curseur = connexion.cursor()

    try:

        curseur.execute("""
            CREATE TABLE IF NOT EXISTS utilisateur (
                id INT AUTO_INCREMENT PRIMARY KEY,
                login VARCHAR(50) UNIQUE NOT NULL,
                password VARCHAR(50) NOT NULL,
                nom VARCHAR(50) NOT NULL,
                prenom VARCHAR(50) NOT NULL,
                email VARCHAR(100) NOT NULL,
                role ENUM('UTILISATEUR', 'TECHNICIEN', 'ADMIN') NOT NULL,
                service VARCHAR(50),
                date_creation DATE DEFAULT (CURDATE())
            )
        """)


        curseur.execute("""
            CREATE TABLE IF NOT EXISTS incident (
                id INT AUTO_INCREMENT PRIMARY KEY,
                titre VARCHAR(100) NOT NULL,
                description TEXT NOT NULL,
                priorite ENUM('BASSE', 'MOYENNE', 'HAUTE', 'CRITIQUE') NOT NULL,
                statut ENUM('OUVERT', 'EN_COURS', 'RESOLU', 'FERME') DEFAULT 'OUVERT',
                date_creation DATETIME DEFAULT NOW(),
                utilisateur_id INT NOT NULL,
                FOREIGN KEY (utilisateur_id) REFERENCES utilisateur(id)
            )
        """)


        curseur.execute("""
            CREATE TABLE IF NOT EXISTS intervention (
                id INT AUTO_INCREMENT PRIMARY KEY,
                commentaire TEXT NOT NULL,
                duree_minutes INT DEFAULT 0,
                date_intervention DATETIME DEFAULT NOW(),
                incident_id INT NOT NULL,
                technicien_id INT NOT NULL,
                FOREIGN KEY (incident_id) REFERENCES incident(id),
                FOREIGN KEY (technicien_id) REFERENCES utilisateur(id)
            )
        """)


        connexion.commit()
        print("Tables créées avec succès")

    except Exception as e:

        connexion.rollback()
        print(f"Erreur lors de la création des tables : {e}")

    finally:

        curseur.close()



create_tables()