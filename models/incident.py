class Incident:

    def __init__(self, id, titre, description, priorite, statut, date_creation, utilisateur_id):
        self.id = id
        self.titre = titre
        self.description = description
        self.priorite = priorite
        self.statut = statut
        self.date_creation = date_creation
        self.utilisateur_id = utilisateur_id

    def __str__(self):
        return f"[{self.id}] {self.titre} | {self.priorite} | {self.statut}"