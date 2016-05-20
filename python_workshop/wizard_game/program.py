import random

import models


def print_header():
    print("------------------------------------------")
    print("         Wizard game")
    print("------------------------------------------")
    print()


def game_loop():
    gandolf = models.Wizard("Gandolf", 50)

    print("Dict: {}".format(gandolf.__dict__))

    creatures = [
        models.Bunny(7),
        models.Dragon(100),
        models.Cat(3),
    ]

    # print(gandolf)
    print("A wizard appears: {}".format(gandolf))

    c = random.choice(creatures)
    print("The wizard has spotted a creature: ")
    print(c)
    action = input('what do you want to do? [a]ttack, [r]un away, e[x]it: ')

    while action != 'x':

        if action == 'a':
            if gandolf.attack(c):
                print("The wizard is triumphant!")
            else:
                print("The wizard was defeated, game over")
                break

        action = input('what do you want to do? [a]ttack, [r]un away, e[x]it: ')
        c = random.choice(creatures)
        print("The wizard has spotted a creature: ")
        print(c)


def main():
    print_header()
    game_loop()
    print("Done")


print(__name__)

if __name__ == '__main__':
    main()
