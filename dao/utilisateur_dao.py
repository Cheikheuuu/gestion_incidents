from database.connexion import Connexion
from models.utilisateur import Utilisateur
from dao.base_dao import BaseDAO


class UtilisateurDAO(BaseDAO):

    def __init__(self):
        self.connexion = Connexion.get_instance()

    def get_all(self):
        curseur = self.connexion.cursor()
        curseur.execute("SELECT * FROM utilisateur")
        resultats = curseur.fetchall()
        utilisateurs = []
        for r in resultats:
            utilisateurs.append(Utilisateur(r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7], r[8]))
        curseur.close()
        return utilisateurs

    def get_by_id(self, id):
        curseur = self.connexion.cursor()
        curseur.execute("SELECT * FROM utilisateur WHERE id = %s", (id,))
        r = curseur.fetchone()
        curseur.close()
        if r:
            return Utilisateur(r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7], r[8])
        return None

    def get_by_login(self, login):
        curseur = self.connexion.cursor()
        curseur.execute("SELECT * FROM utilisateur WHERE login = %s", (login,))
        r = curseur.fetchone()
        curseur.close()
        if r:
            return Utilisateur(r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7], r[8])
        return None

    def ajouter(self, utilisateur):
        curseur = self.connexion.cursor()
        try:
            curseur.execute("""
                INSERT INTO utilisateur (login, password, nom, prenom, email, role, service)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, (utilisateur.login, utilisateur.password, utilisateur.nom,
                  utilisateur.prenom, utilisateur.email, utilisateur.role, utilisateur.service))
            self.connexion.commit()
            print("Utilisateur ajouté avec succès")
        except Exception as e:
            self.connexion.rollback()
            print(f"Erreur : {e}")
        finally:
            curseur.close()

    def modifier(self, utilisateur):
        curseur = self.connexion.cursor()
        try:
            curseur.execute("""
                UPDATE utilisateur
                SET login=%s, nom=%s, prenom=%s, email=%s, role=%s, service=%s
                WHERE id=%s
            """, (utilisateur.login, utilisateur.nom, utilisateur.prenom,
                  utilisateur.email, utilisateur.role, utilisateur.service, utilisateur.id))
            self.connexion.commit()
            print("Utilisateur modifié avec succès")
        except Exception as e:
            self.connexion.rollback()
            print(f"Erreur : {e}")
        finally:
            curseur.close()

    def delete_by_id(self, id):
        curseur = self.connexion.cursor()
        try:
            curseur.execute("DELETE FROM utilisateur WHERE id = %s", (id,))
            self.connexion.commit()
            print("Utilisateur supprimé avec succès")
        except Exception as e:
            self.connexion.rollback()
            print(f"Erreur : {e}")
        finally:
            curseur.close()

    def authentifier(self, login, password):
        curseur = self.connexion.cursor()
        curseur.execute("SELECT * FROM utilisateur WHERE login = %s AND password = %s", (login, password))
        r = curseur.fetchone()
        curseur.close()
        if r:
            return Utilisateur(r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7], r[8])
        return None

    def rechercher(self, mot_cle):
        curseur = self.connexion.cursor()
        curseur.execute("""
            SELECT * FROM utilisateur
            WHERE nom LIKE %s OR login LIKE %s OR service LIKE %s
        """, (f"%{mot_cle}%", f"%{mot_cle}%", f"%{mot_cle}%"))
        resultats = curseur.fetchall()
        utilisateurs = []
        for r in resultats:
            utilisateurs.append(Utilisateur(r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7], r[8]))
        curseur.close()
        return utilisateurs