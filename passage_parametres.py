def reduction(prix, taux):
    return prix * (1 - taux/100)

def affiche_prix(prix, taux):
    print("Prix: ", prix)
    print("Taux: ", taux)
    print("Prix réduit: ", reduction(prix, taux))

#exemple d'appel de la fonction
affiche_prix(100, 10)
affiche_prix(110, 20)

#passage de paramètres par référence
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
