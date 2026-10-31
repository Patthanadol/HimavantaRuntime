import random

name = None

player = [
    ["hp", 100],
    ["maxhp", 100],
    ["mana", 2000],
    ["maxmana", 2000]]

heal_mana_cost = 100
ult_mana_cost = 300


def get_stat(stat_name):
    for i in player:
        if i[0] == stat_name:
            return i[1]
    return None


def set_stat(stat_name, value):
    for i in player:
        if i[0] == stat_name:
            i[1] = value
            return True
    return False


def resetPlayer():
    set_stat("hp", 100)
    set_stat("maxhp", 100)
    set_stat("mana", 2000)
    set_stat("maxmana", 2000)

def att():
    return random.randint(10, 20)
    

def ult():
    if not useMana(ult_mana_cost):
        return None
    return random.randint(30, 40)


def heal():
    if not useMana(heal_mana_cost):
        return False

    hp = get_stat("hp")
    maxhp = get_stat("maxhp")

    hp = min(hp + random.randint(20, 30), maxhp)
    set_stat("hp", hp)
    return True


def useMana(cost):
    if get_stat("mana") < cost:
        return False

    set_stat("mana", get_stat("mana") - cost)
    return True

def isGameOver():
    return get_stat("hp") <= 0