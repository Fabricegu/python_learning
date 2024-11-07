def reduction(prix, taux):
    return prix * (1 - taux/100)

def affiche_prix(prix, taux):
    print("Prix: ", prix)
    print("Taux: ", taux)
    print("Prix réduit: ", reduction(prix, taux))

#exemple d'appel de la fonction
affiche_prix(100, 10)
affiche_prix(110, 20)