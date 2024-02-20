# HexaGrid
HexaGrid est une bibliothèque de fonctions qui permet de gérer des structures de grille de format Hexagonal pour des jeux par exemple.


# Contexte du projet
Ce projet se fait dans le cadre du programme de NSI en Terminale afin d'être évalué en P.O.O c'est à dire en programmation orientée objet.

C'est un projet exemple fait par moi-même, le projesseur de la classe de terminale du lycée léonard de Vinci à Amboise (Indre-et-Loire). C'est une sorte de corrigé de ce qui est attendu, au niveau :
* Du code (structure, commantaire, architechture ...)
* De la présentation (powerpoint, documentation)

Il sert d'exemple également sur l'utilisation de solution de travail collaboratif tel que GIT.

Cette documentation sert également de fil de penser, afin de comprendre comment réfléchir sur un projet de A à Z.

La liste des projets possibles se trouve sur Capytale avec le code activité suivant : 
[7c77-2854442](https://capytale2.ac-paris.fr/web/c/7c77-2854442)

# But
Afin de trouver de l'inspiration sur les foncitonnalité, je vais m'inspirer de plusieur jeux utilisant cette structure, tell que The Island, ou encore le challenge 2023 de codding game avec des fourmis qui devais récupérer des ressources.

Le module proposera un objet ``HexaGrid`` qqui permettra les fonctionnalité suivante:
* Creer un grille de la taille souhaitée.
* Identifier les cases facilement.
* Définir en chemin entre deux cases.
* Dessiner un grille en ligen de commade.
* Dessiner un chemin.
* Idéalement trouver un chemin entre deux cases.

Pour le moment : les évolutions possibles seraient:
* Permettre de bloquer des cases et donc empéché "d'aller" sur cette case.
* Permettre de faire des objets qui recouvrent plusieurs cases..

# Les objets
Une grille est une liste de cases. Le programme de terminale ne prend pas en compte la notion d'héritage. Ce sera donc un objet grille qui contiendre une variable avec une liste de case.

Les cases auront :
* un identifiant unique sur la grille.
* une liste de case voisines.
* une valeur (qui serai utilisée de manière différente en fonction des projets qui l'utiliseront).

On peut imaginer l'utilisation suivante:
```python
grille = HexaGrid(...) #paramètre à définir
grille[0] = val
grille.chemin(6, 4) # retourne la liste des ids ou des cases ente la case 6 et 4
grille.display() # affiche la grille
print(grille) # affighe egalement la grille
```

L'affichage d'une grille en mode console ressemblera à :
```
    A   B   C   D   E   F
      G   H   I   J   K
    L   M   N   O   P   Q
```

# Initialisation de la grille
Je viens à me poser une première question : "Comment initialiser une grille, si possible facilement ?"