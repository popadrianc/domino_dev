import random
from random import choice

playernames = ("WIZARD", "BARBARIAN", "ASSASSIN")
mobs = ("Ant", "Spider", "Scorpion", "Farmer", "Necromancer", "Sucubus", "Troll", "Orc", "Skeletron", "Dragon", "Demon", "Devil", "Wolf", "Which", "Werewolves", "Thief", "Vampire")

charname = choice(playernames)
php = random.randint(150,250)
pap = random.randint(10,25)
ename = choice(mobs)
ehp = random.randint(150,250)
eap = random.randint(10,25)
x = 0

def battle(php, pap, ehp, eap, pnm, enm):
    print(f"a very scary {enm} appeared...\n")
    while php >= 0 or ehp >=0:
        print(f"the {pnm} health points are {php}\n")
        print(f"the {enm} has {ehp} health points\n")
        php -= eap
        print(f"the {enm} dealt {eap} points of damage\n")
        print(f"the {pnm} health points are {php}\n")
        ehp -= pap
        print(f"the {pnm} dealt {pap} points of damage\n")
        print(f"the {enm} has {ehp} health points\n")
        if ehp <= 0:
            print("You have won!")
            print("Victory!")
            break
        elif ehp <= 0 & php >=0:
            print("You have Won!")
            print("Victory!")
        elif php <= 0:
            print("You Have Lost!")
            print("Your soul is damned, your god has fell. This will bring you to your death.")
            break
        elif ehp <= 0& php <= 0:
            print("You have died!")
            print("Your soul is damned, your god has fell. This will bring you to your death.")
            break
        elif ehp >= 0 & php >=0:
            continue

battle(php, pap, ehp, eap, charname, ename)