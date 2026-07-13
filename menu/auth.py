from dao.utilisateur_dao import UtilisateurDAO


def connexion():
    print("=== CONNEXION ===")
    login = input("Login : ")
    password = input("Mot de passe : ")

    dao = UtilisateurDAO()
    utilisateur = dao.authentifier(login, password)

    if utilisateur:
        print(f"Bienvenue {utilisateur.prenom} {utilisateur.nom} !")
        return utilisateur
    else:
        print("Login ou mot de passe incorrect")
        return None