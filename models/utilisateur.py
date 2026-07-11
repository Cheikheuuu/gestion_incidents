class Utilisateur:

    def __init__(self, id, login, password, nom, prenom, email, role, service, date_creation=None):
        self.id = id
        self.login = login
        self.password = password
        self.nom = nom
        self.prenom = prenom
        self.email = email
        self.role = role
        self.service = service
        self.date_creation = date_creation

    def __str__(self):
        return f"[{self.id}] {self.prenom} {self.nom} | {self.role} | {self.service}"