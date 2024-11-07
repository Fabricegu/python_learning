# Description: mutable and immutable objects
# Objet immuable
# les addresse mémoire change
prenom = "patric"
print(prenom)
print("emplacement mémoire de prénom: ", id(prenom))
print("type de prénom: ", type(prenom))

prenom += "e"
print(prenom)
print("emplacement mémoire de prénom: ", id(prenom))
print("type de prénom: ", type(prenom))

prenom1 = "julia"
print(prenom1)
print("emplacement mémoire de prénom1: ", id(prenom1))

prenom2 = "robert"
print(prenom2)
print("emplacement mémoire de prénom2: ", id(prenom2))

prenom1 = prenom2
print(prenom1)
print("emplacement mémoire de prénom1: ", id(prenom1))

# objet mutable
# les addresse mémoire ne change pas
liste = [1, 6, 6,4]
print(liste)
print("emplacement mémoire de liste: ", id(liste))

liste.append(5)
print(liste)
print("emplacement mémoire de liste: ", id(liste))

