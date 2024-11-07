def reduction(prix, taux):
    return prix * (1 - taux/100)

def affiche_prix(prix, taux):
    print("Prix: ", prix)
    print("Taux: ", taux)
    print("Prix réduit: ", reduction(prix, taux))

#exemple d'appel de la fonction
affiche_prix(100, 10)
affiche_prix(110, 20)

#passage de paramètres par référence objet  immuable
print("Tentative de passage de paramètres par référence objet immuable")
def reduction(prix, taux):
    prix = prix * (1 - taux/100)    #prix est une variable locale
    print("Prix dans la fonction: ", prix)

def affiche_prix(prix, taux):
    print("Prix: ", prix)
    print("Taux: ", taux)
    reduction(prix, taux)

    print("Prix après réduction: ", prix)

#exemple d'appel de la fonction
affiche_prix(100, 10)
affiche_prix(110, 20)

#passage de paramètres par référence objet mutable
print("Tentative de passage de paramètres par référence objet mutable")
def reduction(liste, taux):
    liste[0] = liste[0] * (1 - taux/100)    #liste est une variable locale
    print("Prix dans la fonction: ", liste[0])

def affiche_prix(liste, taux):
    print("Prix: ", liste[0])
    print("Taux: ", taux)
    reduction(liste, taux)

    print("Prix après réduction: ", liste[0])       #liste est modifiée par la fonction reduction

#exemple d'appel de la fonction
liste = [100, 10]
affiche_prix(liste, 10)
affiche_prix(liste, 20)

