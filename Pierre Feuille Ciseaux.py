import random  
from colorama import Back, Fore, Style, deinit, init
init() # sous windows

points = 0
points_ennemie = 0

print(Fore.BLUE + Style.NORMAL +"Bienvenue dans le Pierre Feuille Ciseaux. Le gagnant l'emporte en 3 manche gagnant !")
while True:
    ennemie = random.randint(1,3)
    

    if points == 3:
        print(f"""
        Bravo tu as gagnés ton adversaire avait {points_ennemie} points !""")
        points_ennemie = 0
        points = 0
        a = input("voulez vous rejouez(o/n)")
        if a == "o":
            continue
        elif a == "n":
            break
        else:
            print("Mettez un choix valide: o/n ")
    if points_ennemie == 3:
            print(f"""Dommage tu as perdu tu avais {points} points ! """)
            points_ennemie = 0
            points = 0
            a = input("voulez vous rejouez(o/n)")
            if a == "o":
                continue
            elif a == "n":
                break
            else:
                print("Mettez un choix valide: o/n ")
    choix = input("Choissez entre Pierre(1) Feuille(2) ou Ciseaux(3) : ")
    if choix == "1":
        choix = "Pierre"

        if ennemie == 1:
            print (f"""
            Enemie : Pierre
            Vous : {choix}
            
            Egalité, Dommage ! 
            
            Vous avez {points} points !
            Votre adversaire à {points_ennemie} points !""")
            continue
        if ennemie == 2: 
            points_ennemie += 1
            print (f"""
            Enemie : Feuille
            Vous : {choix}
            
            Dommage ! c'est perdu ! 
            Vous avez {points} points !
            Votre adversaire à {points_ennemie} points !
            """)
            continue

        if ennemie == 3: 
            points += 1
            print (f"""
            Enemie : Ciseaux
            Vous : {choix}
            
            Bravo ! c'est Gagné ! 
            Vous avez {points} points !
            Votre adversaire à {points_ennemie} points !
            """)
            continue



    if choix == "2":
        choix = "Feuille"
        if ennemie == 1:
            points += 1
            print (f"""
            Enemie : Pierre
            Vous : {choix}
            
            Bravo ! c'est Gagné ! 
            Vous avez {points} points !
            Votre adversaire à {points_ennemie} points !
            """)
            continue
        if ennemie == 2: 
            
            print (f"""
            Enemie : Feuille
            Vous : {choix}
            
            Egalité, Dommage ! 
            
            Vous avez {points} points !
            Votre adversaire à {points_ennemie} points !
            """)
            continue

        if ennemie == 3: 
            points_ennemie += 1
            print (f"""
            Enemie : Ciseaux
            Vous : {choix}
            
            Dommage ! c'est perdu ! 
            Vous avez {points} points !
            Votre adversaire à {points_ennemie} points !
            """)
            continue

    if choix == "3":
        choix = "Ciseaux"
        if ennemie == 1:
            points_ennemie += 1
            print (f"""
            Enemie : Pierre
            Vous : {choix}
            
            Dommage ! c'est perdu ! 
            Vous avez {points} points !
            Votre adversaire à {points_ennemie} points !
            """)
            continue
        if ennemie == 2: 
            points += 1
            print (f"""
            Enemie : Feuille
            Vous : {choix}
            
            Bravo ! c'est Gagné ! 
            Vous avez {points} points !
            Votre adversaire à {points_ennemie} points !
            """)
            continue

        if ennemie == 3: 
            print (f"""
            Enemie : Ciseaux
            Vous : {choix}
            
            Egalité, Dommage ! 
            
            Vous avez {points} points !
            Votre adversaire à {points_ennemie} points !
            """)
            continue
    else: 
        print("Veillez mettre un chiffre valide (1,2,3)")