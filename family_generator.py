#!/usr/bin/env python3

import random

members = []
relation = ["Pere", "Mere", "Enfants"]
trash = []
pere = []
mere = []
enfants = []
#family = []

def get_members():
    name = ""
    while (name != "end"):
        name = input("Nom du membre de la famille ('end' pour finir): ")
        if (name != "end"):
            members.append(name)

def get_family():
    temp = ""
    for membre in members:
        temp = random.choices(relation)
        temp = str(temp).replace("['", '')
        temp = str(temp).replace("']", '')
        if (temp == 'Pere' or temp == 'Mere'):
            if (temp == 'Pere'):
                pere.append(membre)
            if (temp == 'Mere'):
                mere.append(membre)
            relation.remove(temp)
        if (temp == 'Enfants'):
            enfants.append(membre)


def show_family():
    if (len(pere) == 0 and len(mere) == 0):
        print(", ".join(enfants), "sont orphelins")
        return
    if (len(pere) != 0):
        print("Le père est", "".join(pere))
    else :
        print("Le père est allé cherché du lait")
    if (len(mere) != 0):
        print("La mère est", "".join(mere))
    else :
        print("La mère est partie avec le facteur")
    if (len(enfants) != 0):
        if (len(enfants) == 1):
            print("L'enfant est :", ", ".join(enfants))
            return
        print("Les enfants sont :", ", ".join(enfants))
    else :
        print("Il n'y a pas d'enfants")

get_members()
if (len(members) != 0):
    get_family()
    show_family()