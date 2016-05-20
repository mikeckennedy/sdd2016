import random


class Wizard:
    def __init__(self, name, level):
        self.level = level
        self.name = name
        self.__modifier = len(name)

    def __str__(self):
        return "This is the wizard {} of level {}".format(self.name, self.level)

    def attack(self, creature):
        creature_throw = creature.level * random.randint(0, 12)
        my_throw = self.level * random.randint(0, 12)

        return my_throw >= creature_throw


class Creature:
    def __init__(self, level):
        self.level = level

    def __str__(self):
        return "A {} of level {}".format(type(self), self.level)

        # @classmethod
        # def test(cls):
        #     return True


class Bunny(Creature):
    pass


class Cat(Creature):
    pass


class Dragon(Creature):
    pass
