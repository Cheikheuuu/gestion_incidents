from menu.auth import connexion
from menu.interface import menu_utilisateur, menu_technicien, menu_admin


def main():
    print("=== SYSTEME DE GESTION DES INCIDENTS ===")
    while True:
        utilisateur = connexion()

        if utilisateur is None:
            choix = input("Réessayer ? (o/n) : ")
            if choix.lower() != "o":
                print("Au revoir !")
                break
        else:
            if utilisateur.role == "UTILISATEUR":
                menu_utilisateur(utilisateur)
            elif utilisateur.role == "TECHNICIEN":
                menu_technicien(utilisateur)
            elif utilisateur.role == "ADMIN":
                menu_admin(utilisateur)


main()