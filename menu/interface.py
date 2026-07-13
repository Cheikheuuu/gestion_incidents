from dao.utilisateur_dao import UtilisateurDAO
from dao.incident_dao import IncidentDAO
from dao.intervention_dao import InterventionDAO
from models.utilisateur import Utilisateur
from models.incident import Incident
from models.intervention import Intervention


def menu_utilisateur(utilisateur_connecte):
    dao_incident = IncidentDAO()
    while True:
        print("\n=== MENU UTILISATEUR ===")
        print("1. Créer un incident")
        print("2. Mes incidents")
        print("3. Filtrer par statut")
        print("4. Filtrer par priorité")
        print("0. Déconnexion")
        choix = input("Votre choix : ")

        if choix == "1":
            titre = input("Titre : ")
            description = input("Description : ")
            print("Priorité : BASSE / MOYENNE / HAUTE / CRITIQUE")
            priorite = input("Priorité : ").upper()
            incident = Incident(None, titre, description, priorite, "OUVERT", None, utilisateur_connecte.id)
            dao_incident.ajouter(incident)

        elif choix == "2":
            incidents = dao_incident.get_by_utilisateur(utilisateur_connecte.id)
            print("\n=== MES INCIDENTS ===")
            for i in incidents:
                print(i)

        elif choix == "3":
            print("Statut : OUVERT / EN_COURS / RESOLU / FERME")
            statut = input("Statut : ").upper()
            incidents = dao_incident.get_by_statut(statut)
            for i in incidents:
                if i.utilisateur_id == utilisateur_connecte.id:
                    print(i)

        elif choix == "4":
            print("Priorité : BASSE / MOYENNE / HAUTE / CRITIQUE")
            priorite = input("Priorité : ").upper()
            incidents = dao_incident.get_by_utilisateur(utilisateur_connecte.id)
            for i in incidents:
                if i.priorite == priorite:
                    print(i)

        elif choix == "0":
            print("Déconnexion...")
            break


def menu_technicien(utilisateur_connecte):
    dao_incident = IncidentDAO()
    dao_intervention = InterventionDAO()
    while True:
        print("\n=== MENU TECHNICIEN ===")
        print("1. Voir incidents ouverts")
        print("2. Prendre en charge un incident")
        print("3. Ajouter une intervention")
        print("4. Résoudre un incident")
        print("5. Fermer un incident")
        print("6. Mes incidents traités")
        print("0. Déconnexion")
        choix = input("Votre choix : ")

        if choix == "1":
            incidents = dao_incident.get_by_statut("OUVERT")
            incidents += dao_incident.get_by_statut("EN_COURS")
            print("\n=== INCIDENTS OUVERTS / EN COURS ===")
            for i in incidents:
                print(i)

        elif choix == "2":
            id_incident = int(input("ID de l'incident : "))
            dao_incident.modifier_statut(id_incident, "EN_COURS")

        elif choix == "3":
            id_incident = int(input("ID de l'incident : "))
            commentaire = input("Commentaire : ")
            duree = int(input("Durée en minutes : "))
            intervention = Intervention(None, commentaire, duree, None, id_incident, utilisateur_connecte.id)
            dao_intervention.ajouter(intervention)

        elif choix == "4":
            id_incident = int(input("ID de l'incident : "))
            dao_incident.modifier_statut(id_incident, "RESOLU")

        elif choix == "5":
            id_incident = int(input("ID de l'incident : "))
            dao_incident.modifier_statut(id_incident, "FERME")

        elif choix == "6":
            interventions = dao_intervention.get_by_technicien(utilisateur_connecte.id)
            print("\n=== MES INTERVENTIONS ===")
            for i in interventions:
                print(i)

        elif choix == "0":
            print("Déconnexion...")
            break


def menu_admin(utilisateur_connecte):
    dao_utilisateur = UtilisateurDAO()
    dao_incident = IncidentDAO()
    dao_intervention = InterventionDAO()
    while True:
        print("\n=== MENU ADMIN ===")
        print("1. Liste des utilisateurs")
        print("2. Ajouter un utilisateur")
        print("3. Modifier un utilisateur")
        print("4. Supprimer un utilisateur")
        print("5. Rechercher un utilisateur")
        print("6. Tous les incidents")
        print("7. Statistiques")
        print("0. Déconnexion")
        choix = input("Votre choix : ")

        if choix == "1":
            utilisateurs = dao_utilisateur.get_all()
            print("\n=== LISTE DES UTILISATEURS ===")
            for u in utilisateurs:
                print(u)

        elif choix == "2":
            login = input("Login : ")
            password = input("Mot de passe : ")
            nom = input("Nom : ")
            prenom = input("Prénom : ")
            email = input("Email : ")
            print("Rôle : UTILISATEUR / TECHNICIEN / ADMIN")
            role = input("Rôle : ").upper()
            service = input("Service : ")
            u = Utilisateur(None, login, password, nom, prenom, email, role, service)
            dao_utilisateur.ajouter(u)

        elif choix == "3":
            id_u = int(input("ID de l'utilisateur : "))
            u = dao_utilisateur.get_by_id(id_u)
            if u:
                u.login = input(f"Login ({u.login}) : ") or u.login
                u.nom = input(f"Nom ({u.nom}) : ") or u.nom
                u.prenom = input(f"Prénom ({u.prenom}) : ") or u.prenom
                u.email = input(f"Email ({u.email}) : ") or u.email
                u.role = input(f"Rôle ({u.role}) : ").upper() or u.role
                u.service = input(f"Service ({u.service}) : ") or u.service
                dao_utilisateur.modifier(u)
            else:
                print("Utilisateur introuvable")

        elif choix == "4":
            id_u = int(input("ID de l'utilisateur : "))
            dao_utilisateur.delete_by_id(id_u)

        elif choix == "5":
            mot_cle = input("Rechercher (nom, login, service) : ")
            utilisateurs = dao_utilisateur.rechercher(mot_cle)
            for u in utilisateurs:
                print(u)

        elif choix == "6":
            incidents = dao_incident.get_all()
            print("\n=== TOUS LES INCIDENTS ===")
            for i in incidents:
                print(i)

        elif choix == "7":
            print("\n=== STATISTIQUES ===")
            for statut in ["OUVERT", "EN_COURS", "RESOLU", "FERME"]:
                incidents = dao_incident.get_by_statut(statut)
                print(f"{statut} : {len(incidents)} incident(s)")

        elif choix == "0":
            print("Déconnexion...")
            break