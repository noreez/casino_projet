# CASINO
import time
import random

def intro():
    name = input("Je suis Python. Quel est votre pseudo ?\n")
    print("Hello ", name, ", vous avez 10 €, Très bien ! Installez vous"
                          " à la table de pari.\nJe vous expliquerai "
                          "le principe du jeu :\n"
                          "Je viens de penser à un nombre entre 1 et 10. "
                          "Devinez lequel ?\n"
                          "Att : vous avez le droit à trois essais !\n"
                          "Si vous devinez mon nombre dès le premier coup,"
                          " vous gangez le double de votre mise !\n"
                          "Si vous le devinez au 2è coup, vous gagnez"
                          "exactement votre mise !\n"
                          "Si vous le devinez au 3è coup, vous"
                          " gagnez la moitiè votre mise !\n"
                          "Si vous ne le devinez pas au 3è coup,"
                          " vous perdez votre mise et\n"
                          "vous avez le droit :\n"
                          "\t - de retenter votre chance avec l'argent"
                          " qu'il vous reste pour reconquérir le level perdu\n"
                          "\t - de quitter le jeu.\n"
                          "", sep='')
    return name

def enter_mise(solde):
    text = input("- Le jeu commence, entre votre mise : \n")
    if (text.isdigit() == False):
        print("Je ne comprends pas ! Entrer SVP un nombre entre 1 et 10 €\n")
        enter_mise(solde)
    else:
        mise = int(text)

    if (mise < 1 or mise > 10):
        print("Le montant saisi n'est pas valide. Entrer SVP un montant entre 1 et 10€")
        enter_mise(solde)
    elif (mise > solde):
        print("Erreur, votre mise est plus elevé que votre solde.\n")
        enter_mise(solde)
    return mise

def getnb(level):
    nb_user = input("Alors mon nombre est ?\n")
    if (nb_user.isdigit() == False):
        print(nb_user.isdigit())
        nb_user = int(nb_user)
        print("Je ne comprends pas !\n")
    nb_user = int(nb_user)
    return nb_user

def game(name_user, level, solde, nb_coup, nb_coup_max, nb_python):
    nb_user = getnb(level)
    if (level >= 1):
        if (nb_python == nb_user and level < 3):
            print("Super, vous passez au level", level + 1, "\n")
            return 1
        elif (nb_python == nb_user and level == 3):
            print("gagne")
            return 10
        elif (nb_python > nb_user):
            print("Votre nb est trop petit")
            return 20
        elif (nb_python < nb_user):
            print("Votre nb est trop grand")
            return 20
    return 0

def gameover():
    print("vous avez perdu tout l'argent")
    exit(0)


if  __name__ == '__main__':
    name_user = intro()
    level = 1
    dotation = 10
    solde = dotation
    mise = enter_mise(solde)
    nb_coup = 1
    nb_coup_max = 3
    status = 0
    nb_python = random.randrange(1, level * 10)
    while (nb_coup <= nb_coup_max and level <= 3):
        nb_coup_max += 2 * (level - 1)
        ##if (status == 0):
        ##    game(name_user, level, solde,nb_coup, nb_coup_max, nb_python)

        ##DEBUG
        #print("level", level, "\n"
        #"solde", solde, "\n"
        #"nb_coup_max", nb_coup_max, "\n"
        #"nb_coup", nb_coup, "\n")
        #"nb_python", nb_python
        #status = game(name_user, level, solde, nb_coup, nb_coup_max, nb_python)
        if (status == 1):
            level = level + 1
            nb_coup = 1
            nb_python = random.randrange(1, level * 10)
            if (nb_coup == 1):
                solde += mise * 2
            else:
                solde += mise
        elif (status == 10):
            print("gagne")
            if (nb_coup == 1):
                solde += mise * 2
            else:
                solde += mise
            if (level == 3):
                answer = input("Vous avez gagne,souhaitez vous lancer une nouvelle partie? (O/N)\n")
                if (answer != "o" and answer != "O"):
                    exit(0)
                level = 1
                nb_coup = 1
        elif (nb_coup == nb_coup_max):
            solde -= mise
            level = 1
            nb_coup = 1
            nb_python = random.randrange(1, level * 10)
            answer = input("Souhaitez vous continuer la partie? (O/N)")
            if (solde == 0):
                gameover()
            elif (answer != "o" and answer != "O"):
                exit(0)
        elif (status == 20):
            nb_coup += 1

    ##DEBUG
    #print("level", level, "\n"
    #"solde", solde, "\n"
    #"nb_coup_max", nb_coup_max, "\n"
    #"nb_coup", nb_coup, "\n")
    #"nb_python",nb_python)
    #status = game(name_user, level, solde, nb_coup, nb_coup_max, nb_python)
