from database.connexion import Connexion
from models.intervention import Intervention
from dao.base_dao import BaseDAO


class InterventionDAO(BaseDAO):

    def __init__(self):
        self.connexion = Connexion.get_instance()

    def get_all(self):
        curseur = self.connexion.cursor()
        curseur.execute("SELECT * FROM intervention")
        resultats = curseur.fetchall()
        interventions = []
        for r in resultats:
            interventions.append(Intervention(r[0], r[1], r[2], r[3], r[4], r[5]))
        curseur.close()
        return interventions

    def get_by_id(self, id):
        curseur = self.connexion.cursor()
        curseur.execute("SELECT * FROM intervention WHERE id = %s", (id,))
        r = curseur.fetchone()
        curseur.close()
        if r:
            return Intervention(r[0], r[1], r[2], r[3], r[4], r[5])
        return None

    def get_by_incident(self, incident_id):
        curseur = self.connexion.cursor()
        curseur.execute("SELECT * FROM intervention WHERE incident_id = %s", (incident_id,))
        resultats = curseur.fetchall()
        interventions = []
        for r in resultats:
            interventions.append(Intervention(r[0], r[1], r[2], r[3], r[4], r[5]))
        curseur.close()
        return interventions

    def get_by_technicien(self, technicien_id):
        curseur = self.connexion.cursor()
        curseur.execute("SELECT * FROM intervention WHERE technicien_id = %s", (technicien_id,))
        resultats = curseur.fetchall()
        interventions = []
        for r in resultats:
            interventions.append(Intervention(r[0], r[1], r[2], r[3], r[4], r[5]))
        curseur.close()
        return interventions

    def ajouter(self, intervention):
        curseur = self.connexion.cursor()
        try:
            curseur.execute("""
                INSERT INTO intervention (commentaire, duree_minutes, incident_id, technicien_id)
                VALUES (%s, %s, %s, %s)
            """, (intervention.commentaire, intervention.duree_minutes,
                  intervention.incident_id, intervention.technicien_id))
            self.connexion.commit()
            print("Intervention ajoutée avec succès")
        except Exception as e:
            self.connexion.rollback()
            print(f"Erreur : {e}")
        finally:
            curseur.close()

    def delete_by_id(self, id):
        curseur = self.connexion.cursor()
        try:
            curseur.execute("DELETE FROM intervention WHERE id = %s", (id,))
            self.connexion.commit()
            print("Intervention supprimée avec succès")
        except Exception as e:
            self.connexion.rollback()
            print(f"Erreur : {e}")
        finally:
            curseur.close()