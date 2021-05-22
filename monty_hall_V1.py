from random import randint, seed
from enum import Enum
import matplotlib.pyplot as plt



class Strategie(Enum):
    CHANGER = 1
    GARDER = 2


# Utilise l'horloge système pour initialiser le générateur de
# nombres pseudo-aléatoires.
seed()


def play_game(strategie):
    '''Simule une partie du jeu Monty Hall.
    Cette fonction simule le choix de la porte par le participant,
    l'élimination d'une mauvaise porte par le présentateur, et le
    choix final. Elle ne retourne que le résultat de la partie, parce
    que nous n'aurons besoin que du résultat pour effectuer nos calculs.
    Args:
        strategie (Strategie): La stratégie du joueur
    Returns:
        bool: Le joueur a-t-il gagné?'''
    portes = [0, 1, 2]

    bonne_porte = randint(0, 2)

    # Choix du joueur
    premier_choix = randint(0, 2)

    # Il nous reste deux portes
    portes.remove(premier_choix)

    # Le présentateur élimine une porte
    if premier_choix == bonne_porte:
        portes.remove(portes[randint(0, 1)])
    else:
        portes = [bonne_porte]

    deuxieme_choix = 0
    # Le deuxieme choix depend de la strategie
    if strategie == Strategie.CHANGER:
        deuxieme_choix = portes[0]
    elif strategie == Strategie.GARDER:
        deuxieme_choix = premier_choix
    else:
        raise ValueError("Stratégie non reconnue!")

    return deuxieme_choix == bonne_porte


def play(strategie, nb_tours):
	return[1 if play_game(strategie) else 0 for i in range(nb_tours)]

result_game=play(Strategie.GARDER, 20)
print ("Voila le resultat sur 20 parties\n",result_game)


print("En changeant de porte, le joueur a gagne {} sur 10000 parties."
      .format(sum(play(Strategie.CHANGER, 10000))))
      
print("En gardant son choix initial, le joueur a gagne {} sur 10000 parties."
      .format(sum(play(Strategie.GARDER, 10000))))

