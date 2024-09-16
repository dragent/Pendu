import matplotlib.pyplot as plt

def afficher_pendu(nb_erreurs):
    """
    Affiche le pendu en fonction du nombre d'erreurs.
    """

    plt.figure()  # Crée une nouvelle figure

    # Dessine la potence
    plt.plot([0, 1], [0, 0], 'k')  # Base
    plt.plot([0.5, 0.5], [0, 1], 'k')  # Poteau vertical
    plt.plot([0.5, 1], [1, 1], 'k')  # Barre horizontale

    # Dessine le corps du pendu en fonction du nombre d'erreurs
    if nb_erreurs > 1 :
        plt.plot([1, 1], [1, 0.8], 'k')  # Corde
    if nb_erreurs > 2:  # Tête
        cercle = plt.Circle((1, 0.7), 0.1, color='k', fill=False)
        plt.gca().add_patch(cercle)
    if nb_erreurs >3:  # Corps
        plt.plot([1, 1], [0.6, 0.5], 'k')
    if nb_erreurs > 4:  # Bras gauche
        plt.plot([1, 0.8], [0.55, 0.65], 'k')
    if nb_erreurs > 5:  # Bras droit
        plt.plot([1, 1.2], [0.55, 0.65], 'k')
    if nb_erreurs > 6:  # Jambe gauche
        plt.plot([1, 0.9], [0.5, 0.4], 'k')
    if nb_erreurs > 7:  # Jambe droite
        plt.plot([1, 1.1], [0.5, 0.4], 'k')

    # Paramètres d'affichage
    plt.axis('off')  # Cache les axes
    plt.xlim(-0.2, 1.4)  # Ajuste les limites de l'axe x
    plt.ylim(-0.2, 1.2)  # Ajuste les limites de l'axe y
    plt.show()  # Affiche le pendu