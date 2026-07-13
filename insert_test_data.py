from dao.utilisateur_dao import UtilisateurDAO
from dao.incident_dao import IncidentDAO
from dao.intervention_dao import InterventionDAO
from models.utilisateur import Utilisateur
from models.incident import Incident
from models.intervention import Intervention


def insert_test_data():
    dao_utilisateur = UtilisateurDAO()
    dao_incident = IncidentDAO()
    dao_intervention = InterventionDAO()


    dao_utilisateur.ajouter(Utilisateur(None, "admin", "admin123", "Traore", "Cheikh", "admin@entreprise.sn", "ADMIN", "Direction"))
    dao_utilisateur.ajouter(Utilisateur(None, "tech1", "tech123", "Niang", "Khadidiatou", "nkhady@entreprise.sn", "TECHNICIEN", "Informatique"))
    dao_utilisateur.ajouter(Utilisateur(None, "tech2", "tech123", "Gueye", "Marieme", "gmari@entreprise.sn", "TECHNICIEN", "Informatique"))
    dao_utilisateur.ajouter(Utilisateur(None, "user1", "user123", "Diallo", "Mustapha", "dmusta@entreprise.sn", "UTILISATEUR", "Comptabilité"))
    dao_utilisateur.ajouter(Utilisateur(None, "user2", "user123", "Ba", "Fatou", "fba@entreprise.sn", "UTILISATEUR", "RH"))


    dao_incident.ajouter(Incident(None, "PC ne démarre pas", "Mon PC ne s'allume plus depuis ce matin", "HAUTE", "OUVERT", None, 4))
    dao_incident.ajouter(Incident(None, "Connexion internet lente", "La connexion est très lente depuis 2 jours", "MOYENNE", "OUVERT", None, 5))
    dao_incident.ajouter(Incident(None, "Imprimante en panne", "L'imprimante du bureau ne fonctionne plus", "BASSE", "OUVERT", None, 4))


    dao_intervention.ajouter(Intervention(None, "Vérification du matériel en cours", 30, None, 1, 2))
    dao_intervention.ajouter(Intervention(None, "Redémarrage du routeur effectué", 15, None, 2, 3))

    print("Données de test insérées avec succès")


insert_test_data()