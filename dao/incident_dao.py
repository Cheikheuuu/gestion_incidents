from database.connexion import Connexion
from models.incident import Incident
from dao.base_dao import BaseDAO


class IncidentDAO(BaseDAO):

    def __init__(self):
        self.connexion = Connexion.get_instance()

    def get_all(self):
        curseur = self.connexion.cursor()
        curseur.execute("SELECT * FROM incident")
        resultats = curseur.fetchall()
        incidents = []
        for r in resultats:
            incidents.append(Incident(r[0], r[1], r[2], r[3], r[4], r[5], r[6]))
        curseur.close()
        return incidents

    def get_by_id(self, id):
        curseur = self.connexion.cursor()
        curseur.execute("SELECT * FROM incident WHERE id = %s", (id,))
        r = curseur.fetchone()
        curseur.close()
        if r:
            return Incident(r[0], r[1], r[2], r[3], r[4], r[5], r[6])
        return None

    def get_by_utilisateur(self, utilisateur_id):
        curseur = self.connexion.cursor()
        curseur.execute("SELECT * FROM incident WHERE utilisateur_id = %s", (utilisateur_id,))
        resultats = curseur.fetchall()
        incidents = []
        for r in resultats:
            incidents.append(Incident(r[0], r[1], r[2], r[3], r[4], r[5], r[6]))
        curseur.close()
        return incidents

    def get_by_statut(self, statut):
        curseur = self.connexion.cursor()
        curseur.execute("SELECT * FROM incident WHERE statut = %s", (statut,))
        resultats = curseur.fetchall()
        incidents = []
        for r in resultats:
            incidents.append(Incident(r[0], r[1], r[2], r[3], r[4], r[5], r[6]))
        curseur.close()
        return incidents

    def ajouter(self, incident):
        curseur = self.connexion.cursor()
        try:
            curseur.execute("""
                INSERT INTO incident (titre, description, priorite, utilisateur_id)
                VALUES (%s, %s, %s, %s)
            """, (incident.titre, incident.description, incident.priorite, incident.utilisateur_id))
            self.connexion.commit()
            print("Incident créé avec succès")
        except Exception as e:
            self.connexion.rollback()
            print(f"Erreur : {e}")
        finally:
            curseur.close()

    def modifier_statut(self, id, nouveau_statut):
        curseur = self.connexion.cursor()
        try:
            curseur.execute("UPDATE incident SET statut = %s WHERE id = %s", (nouveau_statut, id))
            self.connexion.commit()
            print("Statut mis à jour avec succès")
        except Exception as e:
            self.connexion.rollback()
            print(f"Erreur : {e}")
        finally:
            curseur.close()

    def delete_by_id(self, id):
        curseur = self.connexion.cursor()
        try:
            curseur.execute("DELETE FROM incident WHERE id = %s", (id,))
            self.connexion.commit()
            print("Incident supprimé avec succès")
        except Exception as e:
            self.connexion.rollback()
            print(f"Erreur : {e}")
        finally:
            curseur.close()