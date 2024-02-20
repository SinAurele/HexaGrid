# HexaGrid
HexaGris est une bibliothèque de fonctions qui permet de gérer des structures de grille de format Hexagonal pour des jeux par exemple.


# Contexte du projet
Ce projet se fait dans le cadre Du programme de NSI en terminale afin d'être évaluer en P.O.O c'est à dire en programmation orientée objet.

C'est un projet exemple fait par moi-même, le projesseur de la classe de terminale du lycée léonard de Vinci à Amboise (Indre-et-Loire). C'est une sorte de corrigé de ce qui est attendu, au niveau :
* Du code (structure, commantaire, architechture ...)
* De la présentation (powerpoint, documentation)

Il sert d'exemple également sur l'utilisation de solution de travail collaboratif tel que GIT.

Cette documentation sert également de fil de penser, afin de comprendre comment réfléchir sur un projet de A à Z.

# But
Afin de trouver de l'inspiration sur les foncitonnalité, je vais m'inspirer de plusieur jeux utilisant cette structure, tell que The Island, ou encore le challenge 2023 de codding game avec des fourmis qui devais récupérer des ressources.

Le module proposera un objet ``HexaGrid`` qqui permettra les fonctionnalité suivante:
* Creer un grille de la taille souhaitée
* identifier les cases facilement
* définir en chemin entre deux cases
* dessiner un grille en ligen de commade
* dessiner un chemin
* idéalement trouver un chemin entre deux case

Pour le moment : les évolutions possibles seraient:
* Permettre de bloquer des cases et donc empéché "d'aller" sur cette case
* Permettre de faire des objet qui recouvrent plusieurs cases.

# Les objets
Une grille est une liste de case. Le programme de terminale ne prend pas en compte la notion d'héritage. Ce sera donc un objet grille qui contiendre une variable avec une liste de case.

Les cases auront :
* identifiant unique sur la grille
* une liste de case voisines
* une valeur (qui serai utilisée de manière différente en fonction des projets qui l'utiliseront)

On peut imaginer l'utilisation suivante:
```python
grille = HexaGrid(...) #paramètre à définir
grille[0] = val
grille.chemin(6, 4) # retourne la liste des id ou des cases ente la case 6 et 4
grille.display() # affiche la grille
print(grille) # affighe egalement al grille
```

L'affichage d'une grille en mode console ressemblera à :
```
    A   B   C   D   E   F
      G   H   I   J   K
    L   M   N   O   P   Q
```

# Initialisation de la grille
Je viens à me poser plusieurs questions : 
* Comment initialiser une grille, si possible facilement ?
* Comment enregistrer mes données de grille ?

Il serait possible d'enregistrer les données sous la forme d'un tableau. L'exemple ci-dessus pourrait être enregistré sous la forme:
```
[[A,B,C,D,E,F],
 [G,H,I,J,K],
 [L,M,N,O,P,Q]]
```
Avec cette solution, les lignes sont en quinconces. Une solution equivalente serait d'enregitrer le parallélogramme contenant la grille avec des None pour compléter. Cela permettrer en plus, de ficiliter la lecture des voisins.

Pour des raisons pédagogiques, la structure qui sera utilisée sera une structure de graphe simple (non pondéré, non-orienté). Cependant, la structure de tableau pourra être utiliser pour créer et afficher une grille rapdement. Je vais donc créer des foncitonde "conversion".

Une grille contiendra ``_data`` un dictionnaire d'``HexaCell`` qui sera l'objet utilisé pour représentrer une case hexagonale. La clef du dictionnaire sera l'ID de la case.
Une ``HexaCell`` se définie par:
* un ID définie à la création
* une valeur
* un dictionnaire avec les cases voisines. La clé du dictionnaire indiquera la direction:
  * 0 : TOP_LEFT
  * 1 : LEFT
  * 2 : BOTTOM_LEFT
  * 3 : BOTTOM_RIGHT
  * 4 : RIGHT 
  * 5 : TOP_RIGHT

```
   5       0
4    case     1
   3       2
```

*Remarque* : On peut imaginer la possibilité en créant une case de présiser une case voisine dans une certaine direction. Dans ce cas, il faudra prévoir la mise à jour des case adjacentes, ainsi que des exceptions dans le cas ou une cellule est déjà présente dans cette direction ou autre incohérence.

Le projet est maintenant suffisement défini pour passer à la programmation des fonctionnalités principales.
Je vais créer les fichiers python suivants:
* **HexaCell.py** : fichier définisant la classe représentant une case
* **HexaGrid.py** : fichier définisant la classe représentant une grille
* **test.py** : fichier pour tester les fonctionnalités des classes au fur et à mesure.
* **tools.py** : Fichier avec les fonctions classiques pour aider à développer.

# Observation pendant le développement
Au moment de la creation des cases, et surtout de la définition des cases voisines et du maintient de la cohérence, un problème se pose. D'intuition, il semble possible de faire un algorithme récursif, mais il est facile de truver des cases complexes qui serai gérer simplement avec une structure en tableau. Cette solution reste donc envisageable.