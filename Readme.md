# Jeu du Pendu

Bienvenue dans le jeu du Pendu, un classique où vous devez deviner un mot en entrant des lettres une par une. Si vous vous trompez trop souvent, le pendu sera complété et vous aurez perdu la partie.

## Fonctionnalités

- **Deviner un mot** : L'utilisateur doit deviner un mot lettre par lettre. Si une lettre est incorrecte, une partie du pendu est dessinée.
- **Affichage graphique** : Le dessin du pendu évolue en fonction du nombre d'erreurs grâce à la bibliothèque `matplotlib`.
- **Sélection aléatoire de mots** : Le mot à deviner est sélectionné aléatoirement parmi une liste prédéfinie.

## Structure du Projet

Le projet est composé de plusieurs modules Python qui coopèrent pour faire fonctionner le jeu.

### Fichiers principaux

1. **Game.py**
    - Contient la logique principale du jeu.
    - Fonction principale : `searchWord(randomWord, hiddenWord)` permet de jouer au jeu en demandant à l'utilisateur de deviner les lettres une par une.
    - La fonction `addLetter()` met à jour le mot caché en fonction des lettres correctement devinées.

2. **PrintPendu.py**
    - Utilise la bibliothèque `matplotlib` pour dessiner le pendu.
    - La fonction `afficher_pendu(nb_erreurs)` affiche graphiquement le pendu en fonction du nombre d'erreurs.

3. **Word.py**
    - Permet de sélectionner un mot aléatoire parmi une liste.
    - Fonction principale : `randomWord(array)` choisit un mot aléatoire dans un tableau.

4. **Pendu.py**
    - Fichier principal qui exécute le jeu.
    - Initialise le mot à deviner et le mot caché, puis lance la fonction `searchWord()` pour démarrer la partie.

## Installation

1. Clonez ce dépôt sur votre machine locale :
    ```bash
    git clone https://github.com/votre-utilisateur/jeu-pendu.git
    ```

2. Installez les dépendances requises (assurez-vous que `matplotlib` et `numpy` sont installés) :
    ```bash
    pip install matplotlib numpy
    ```

## Comment jouer

1. Lancez le script principal `Pendu.py` :
    ```bash
    python Pendu.py
    ```

2. Le jeu vous demandera d'entrer une lettre à chaque tour. Si la lettre est correcte, elle sera révélée dans le mot caché. Si la lettre est incorrecte, une partie du pendu sera dessinée.

3. Continuez à deviner jusqu'à ce que vous trouviez le mot complet ou que vous complétiez le pendu.

## Améliorations possibles

- Ajout d'un compteur d'erreurs pour afficher graphiquement le pendu à chaque erreur.
- Ajout d'une option pour rejouer après avoir gagné ou perdu.
- Extension de la liste de mots pour inclure plus de catégories.

## Contributions

Les contributions sont les bienvenues ! N'hésitez pas à ouvrir une issue ou à soumettre une pull request.

## Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.