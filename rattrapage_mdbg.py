# -*- coding: utf-8 -*-

print('Exercice 1')
def nbre_poule_lapin(tetes, pattes):
    # Définir le coefficient tetes et pattes par animal
    coef_tetes_poule = 1
    coef_tetes_lapin = 1
    coef_pattes_poule = 2
    coef_pattes_lapin = 4

    # Utiliser une boucle for pour itérer sur les différentes possibilités
    for nb_poules in range(tetes+1):
        nb_lapins = tetes - nb_poules
        if (coef_pattes_poule * nb_poules + coef_pattes_lapin * nb_lapins) == pattes:
            return nb_poules, nb_lapins

    # Retourner None si aucune solution n'est trouvée
    return None, None

total_tetes = 35
total_pattes = 94

# Appel de la fonction pour trouver le nombre de poules et de lapins
resultat_poules, resultat_lapins = nbre_poule_lapin(total_tetes, total_pattes)

# Affichage des résultats
if resultat_poules is not None and resultat_lapins is not None:
    print("Nombre de poules:", resultat_poules)
    print("Nombre de lapins:", resultat_lapins)
else:
    print("Aucune solution trouvée.")

print('Exercice 2')
import sqlite3
def read_file(path = "./dataset2.txt"):
  with open(path, 'r') as data:
    chaine = data.read()
    # Connexion à une base de données SQLite en mémoire
    conn = sqlite3.connect('coordonnees')
    cursor = conn.cursor()

    # Création de la table
    cursor.execute('''CREATE TABLE IF NOT EXISTS donnees (
                        abscisse INTEGER,
                        ordonnee INTEGER
                    )''')

    # Extraction des données de la chaîne et insertion dans la table SQLite
    points = chaine.split(';')
    abscisses = []
    ordonnees = []
    for point in points:
        if ',' in point:
            abscisse, ordonnee = point.split(',')
            if abscisse != 'Null' and ordonnee != 'Null' :
              cursor.execute("INSERT INTO donnees VALUES (?, ?)", (int(abscisse), int(ordonnee)))
              abscisses.append(int(abscisse))
              ordonnees.append(int(ordonnee))

    # Fermeture de la connexion à la base de données
    conn.close()

    return abscisses, ordonnees

# Test de la fonction
abscisses, ordonnees = read_file()

# Affichage des résultats
print("Abscisses:", abscisses)
print("Ordonnées:", ordonnees)

print('Exercice 3')
def test(A, B):

    # On vérifie si les deux chaînes ont la même longueur
    if len(A) != len(B):
        return False

    # On concaténe la première chaîne avec elle-même pour former une chaîne plus grande
    A_double = A + A

    # On vérifier si la deuxième chaîne est une sous-chaîne de la chaîne concaténée
    return B in A_double

if __name__ == "__main__":
    print(test('', 'cdeab'))  # False
    print(test('abcde', 'cdeab'))  # True
    print(test('abcde', 'abced'))  # False
    print(test('cdefgh', 'efghcd'))  # True
