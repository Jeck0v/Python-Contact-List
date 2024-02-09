class Contact:

  def __init__(self, nom, prenom, numero_telephone, email):
    self.prenom = prenom
    self.nom = nom
    self.numero_telephone = numero_telephone
    self.email = email

  def afficher_contact(self):
    print("Prénom:", self.prenom)
    print("Nom:", self.nom)
    print("Numéro de téléphone:", self.numero_telephone)
    print("Email:", self.email)


class CarnetAdresses:

  def __init__(self):
    self.contacts = []

  def ajouter_contact(self, contact):
    self.contacts.append(contact)
    print("Contact ajouté avec succès.")
    print("========================")

  def afficher_contacts(self):
    if self.contacts:
      print("Liste des contacts:")
      for contact in self.contacts:
        contact.afficher_contact()
        print("========================")
    else:
      print("Le carnet d'adresses est vide.")

  def rechercher_contact(self, nom):
    found = False
    for contact in self.contacts:
      if contact.nom.lower() == nom.lower():
        print("Contact trouvé:")
        contact.afficher_contact()
        found = True
        break
    if not found:
      print("Aucun contact trouvé avec ce nom.")


def main():
  carnet = CarnetAdresses()

  while True:
    print("========================")
    print("Bienvenue dans votre carnet d'adresses.")
    print("1. Ajouter un contact")
    print("2. Afficher tous les contacts")
    print("3. Rechercher un contact")
    print("4. Quitter")
    print("========================")

    choix = input("Que souhaitez-vous faire ? ")

    if choix == "1":
      prenom = input("Prénom: ")
      nom = input("Nom: ")
      numero_telephone = input("Numéro de téléphone: ")
      email = input("Email: ")
      nouveau_contact = Contact(nom, prenom, numero_telephone, email)
      carnet.ajouter_contact(nouveau_contact)

    elif choix == "2":
      carnet.afficher_contacts()

    elif choix == "3":
      nom_recherche = input("Entrez le nom du contact à rechercher: ")
      carnet.rechercher_contact(nom_recherche)

    elif choix == "4":
      print("Merci d'avoir utilisé le carnet d'adresses. Au revoir !")
      break

    else:
      print("Choix invalide. Veuillez choisir une option valide.")


if __name__ == "__main__":
  main()

