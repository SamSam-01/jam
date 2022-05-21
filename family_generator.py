#!/usr/bin/env python3

import random

members = []
relation = ["Pere", "Mere", "Enfants"]
family_name = ["Simpson", "Griffyn", "Smith", "Vignerand", "D'espine", "Blerd", "Pierrétot"]
mother_left = ["est partie chercher du lait", "est morte dans un accident de voiture", "Est partie avec le facteur", "est partie ce remarier a l'étranger", "a refait sa vie en australie"]
father_left = ["est parti chercher du lait", "est mort percuter par un chauffard", "Est partie avec l'ex-femme de son ex-patron", "est partie ce remarier a l'étranger", "a refait sa vie en argentine"]
just_father = ["un enfant non voulu", "un enfant aimé", "un enfant maltraité", "un enfant adopté", "un enfant intelligent"]
just_mother = ["un enfant non voulu", "un enfant aimé", "un enfant maltraité", "un enfant adopté", "un enfant intelligent"]
just_both = ["un enfant non voulu", "un enfant aimé", "un enfant maltraité", "un enfant adopté", "un enfant intelligent"]
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
        if (len(enfants) == 1):
            print(enfants[0],end = "")
            print(" est orphelin")
            return
        print(", ".join(enfants), "sont orphelins")
        return
    if (len(pere) != 0):
        print("Le père est", "".join(pere))
    else :
        print("Le père ", random.choice(father_left))
    if (len(mere) != 0):
        print("La mère est", "".join(mere))
    else :
        print("La mère ", random.choice(mother_left))
    if (len(enfants) != 0):
        if (len(enfants) == 1):
            print("L'enfant est :", ", ".join(enfants))
            return
        print("Les enfants sont :", ", ".join(enfants))
    else :
        print("Il n'y a pas d'enfants")

def show_family_name():
    print("Dans la famille:", random.choice(family_name))

def link_no_father():
    for enfant in enfants:
        print(enfant, "est", random.choice(just_mother))

def link_no_mother():
    for enfant in enfants:
        print(enfant, "est", random.choice(just_father))

def link_father_and_mother():
    for enfant in enfants:
        print(enfant, "est", random.choice(just_both))

def main():
    get_members()
    if (len(members) != 0):
        get_family()
        print('----------------------------------------------------------')
        show_family_name()
        show_family()
        if (len(pere) == 0 and len(mere) == 0):
            print("Une triste famille, sans héritage ni histoire, peut-être une autre fois ?")
        if (len(pere) == 0):
            link_no_father()
        elif (len(mere) == 0):
            link_no_mother()
        else:
            link_father_and_mother()

main()
