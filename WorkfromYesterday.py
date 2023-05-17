import os
import time
import random

Gold = 1000
CasinoMultiplyer = 4
ShopExit = 1

Weapon = 'Lvl 1 Wooden Sword'
Damage = 10

Armour = 0
Resistance = 0

Health = 100

Inventory = []

Count = 0

class Enemy:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

Goblin = Enemy('Goblin', 30, 7)
TreePeople = Enemy('TreePeople', 32, 4)

EnemiesGoblinVillage = random.randint(2,5)
EnemiesForest = random.randint(7,8)


def FightGoblinVillage():
    global Count, Health, Damage, Gold
    print(f'Enemies Spawned: {EnemiesGoblinVillage}')
    while Count < EnemiesGoblinVillage:
        
        while True:
            Health -= Goblin.damage
            Goblin.health -= Damage
        
            if Health == 0:
                print("You Lose")
                quit()

            elif Goblin.health <= 0:
                Goblin.health = 2
                print('Goblin Defeated +15 Gold')
                Gold += 15
                print('')
                time.sleep(1)
                break

        Count += 1

    Count = 0

def FightCave():
    global Count, Health, Damage, Gold
    print(f'Enemies Spawned: {EnemiesForest}')
    while Count < EnemiesForest:
        
        while True:
            Health -= TreePeople.damage
            TreePeople.health -= Damage
        
            if Health == 0:
                print("You Lose")
                quit()

            elif TreePeople.health <= 0:
                TreePeople.health = 2
                print('TreePerson Defeated +20 Gold')
                print('')
                Gold += 20
                time.sleep(0.5)
                break

        Count += 1

    Count = 0

def DisplayTitleScreen():
    os.system("cls")
    print("\033[36m________                                                 ____     ________                                                   ")
    print("\______ \____________     ____   ____   ____   ______   /  _ \    \______ \  __ __  ____    ____   ____  ____   ____   ______")
    print(" |    |  \_  __ \__  \   / ___\ /  _ \ /    \ /  ___/   >  _ </\   |    |  \|  |  \/    \  / ___\_/ __ \/  _ \ /    \ /  ___/")
    print(" |    `   \  | \// __ \_/ /_/  >  <_> )   |  \\___ \    /  <_\ \/   |    `   \  |  /   |  \/ /_/  >  ___(  <_> )   |  \\___ \ ")
    print("/_______  /__|  (____  /\___  / \____/|___|  /____  >  \_____\ \  /_______  /____/|___|  /\___  / \___  >____/|___|  /____  >")
    print("        \/           \//_____/             \/     \/          \/          \/           \//_____/      \/           \/     \/ \033[0m")
    print("")
    print("Welcome to Dragons And Dungons!")
    print("")
    Village()

def Village():
    print('''
    You wake up to find your home burning in the sunlight and a loud ROAR in the distance. 
    You run outside to see your whole village ravaged by fire and a large winged beast 
    flying away. You try to find your family but your efforts are worthless as you find 
    out from the town mayor. Your Mother and Sister were trapped under a burning pile of 
    wood and were burnt. You ask the mayor about your father and the mayor lowers 
    his head. In a weak voice he says your father couldn't deal with the news of your 
    Mother and Sister and has run away leaving you and the rest of the town. More Buildings
    collapse as you stand there sobbing but action for your survival must be done. Rocks are
    falling around you, and as they are, a Doorway is revealed in the Side of the Mountain.
    ''')

    while True:
        VillageLeave = input('You are left with an Option, Do you Leave into the forest or Enter this mysterious Doorway? (1) Leave / (2) Doorway ')

        if VillageLeave == '1':
            GoblinVillage()
            break

        elif VillageLeave == '2':
            print('''
    You Enter the doorway to find a Long stairway down, you walk down but slip, fall, 
    and Die, laying at the bottom of these stairs.
             ''')
            break

        else:
            print('''
    Input Not Found Error 404
            ''')

def GoblinVillage():
    print('''
    You start running and don’t stop in order to look for help. You see a hedge.You crawl
    through. Intimidated by the pitchforks and the raspy voices of those beyond the bushes.
    You pop your head up above your hiding place unknown to what dangers could present 
    themselves. Green blobs otherwise known as goblins presented themselves. What will you 
    do, this is LIFE AND DEATH.
    ''')

    while True:
        GoblinBattle = input('You are left with Two Options, Run or Fight for You Life, What do you do? (1) Run / (2) Fight ')

        if GoblinBattle == '1':
            Engradoland()
            break

        elif GoblinBattle == '2':
            print('''
            You begin a fight, you will be able to get some loot from them if you win, but
            at the cost of your health.
            ''')

            FightGoblinVillage()

            Engradoland()

        else:
            print('''
            Input Not Found Error 404
            ''')

def Engradoland():
    print('''
    When you come to your senses you look up to see a large city bustling with people. You
    go into a blacksmith shop and get an armour set. When you come out a shady looking guy 
    tells you that you look like a hobo(like WHAT!) and tells you about a dragon on the 
    loose. You recall the night when your village was burnt down. It finally comes to you, 
    the feeling of REVENGE!!! The man talks about the location of a dungeon, the home of 
    the DRAGON!

    But before you go you have shops that you can go to to either earn more gold or buy 
    items with your gold(be warned, you may lose your gold if you try your luck, gamble 
    responsibly).
    ''')

    Casino()

def Casino():
    global Gold
    CasinoNumber = random.randint(1,5)

    print("Welcome to the Casino")
    print("")
    print("If you win you'll get 5 times what you put in, if you lose, we just keep what you bet")
    print("")

    while True:

        Betting = int(input(f"How Much Gold would you Like to Bet? Current Balance: {Gold} "))

        if Betting >= Gold+1:
            print("You don't have that Much Gold")

        else:
            break


    Guess = int(input("Put your Bet on a Number 1-5 "))

    if Guess == CasinoNumber:
        Gold += CasinoMultiplyer*Betting
        

    else:
        print("It'll seem you've lost, maybe next time you'll think twice about going up against the house")
        Gold -= Betting

    print("")
    print(f"The Number was: {CasinoNumber}")
    print("")
    print(f"Current Balence: {Gold}")

    while True:

        CasinoPlayAgain = input('Would you like to Play Again? (1) Yes / (2) Nah ')

        if CasinoPlayAgain == '1':
            Casino()
            break
    
        elif CasinoPlayAgain == '2':
            Shop()
            break

        else:
            print('''
            Input Not Found Error 404
            ''')

def Shop():
    global Gold, Damage, Weapon, Health, Resistance, Armour, ShopExit
    print('''
    Welcome to the Shop, Feel free to Look Around. To Select your Item Put the Group value 
    then the Item Value. i.e Lvl 4 Copper Armour = 210, Lvl 3 Wooden Armour = 16

           Items:                Gold:
    (1)(1)  Lvl 2 Wooden Sword    2
       (2)  Lvl 3 Wooden Sword    4 
       (3)  Lvl 4 Wooden Sword    8
       (4)  Lvl 1 Wooden Armour   10
       (5)  Lvl 2 Wooden Armour   20
       (6)  Lvl 3 Wooden Armour   30
       (7)  Lvl 4 Wooden Armour   40

    (2)(1)  Lvl 1 Copper Sword    16
       (2)  Lvl 2 Copper Sword    32
       (3)  Lvl 3 Copper Sword    65
       (4)  Lvl 4 Copper Sword    120
       (5)  Lvl 1 Copper Armour   50
       (6)  Lvl 2 Copper Armour   75
       (7)  Lvl 3 Copper Armour   100
       (8)  Lvl 4 Copper Armour   125

    (3)(1)  Lvl 1 Iron sword      250
       (2)  Lvl 2 Iron sword      300
       (3)  Lvl 3 Iron sword      325
       (4)  Lvl 4 Iron sword      350
       (5)  Lvl 1 Iron Armour     250
       (6)  Lvl 2 Iron Armour     275
       (7)  Lvl 3 Iron Armour     300
       (8)  Lvl 4 Iron Armour     325
    ''')

    while True:
        ShopBuying = input('So Interested Buyer What would you Like to Buy? (1) Nothing / (#Group Value #Item Value) *Your Item* ')

        if ShopBuying == '1':
            if ShopExit == 1:
                TreasureRoom()
                break

            else:
                TheWalkUp()
                break
            

        elif ShopBuying == '11':
            if 2 <= Gold+1:
                #Add Item
                if 12 >= Damage:
                    Damage = 10
                    Weapon = 'Lvl 2 Wooden Sword'
                    Gold -= 2

                else:
                    print('Lower Level Sword')
            

        elif ShopBuying == '12':
            if 4 <= Gold+1:
                #Add Item
                if 12 >= Damage:
                    Damage = 12
                    Weapon = 'Lvl 3 Wooden Sword'
                    Gold -= 4
                
                else:
                    print('Lower Level Sword')
            

        elif ShopBuying == '13':
            if 8 <= Gold+1:
                #Add Item
                if 14 >= Damage:
                    Damage = 14
                    Weapon = 'Lvl 4 Wooden Sword'
                    Gold -= 8

                else:
                    print('Lower Level Sword')
                
            

        elif ShopBuying == '14':
            if 10 <= Gold+1:
                #Add Item
                if 10 >= Resistance:
                    Resistance = 10
                    Armour = 'Lvl 1 Wooden Armour'
                    Gold -= 10  

                else:    
                    print('Lower Level Sword')

        elif ShopBuying == '15':
            if 20 <= Gold+1:
                #Add Item
                if 12 >= Resistance:
                    Resistance = 12
                    Armour = 'Lvl 2 Wooden Armour'
                    Gold -= 20
                else:
                    print('Lower Level Sword')


        elif ShopBuying == '16':
            if 30 <= Gold+1:
                #Add Item
                if 14 >= Resistance:
                    Resistance = 14
                    Armour = 'Lvl 3 Wooden Armour'
                    Gold -= 30
                else:
                    print('Lower Level Sword')
            

        elif ShopBuying == '17':
            if 40 <= Gold+1:
                #Add Item
                if 16 >= Resistance:
                    Resistance = 16
                    Armour = 'Lvl 4 Wooden Armour'
                    Gold -= 40
                else:
                    print('Lower Level Sword')
    

        elif ShopBuying == '21':
            if 16 <= Gold+1:
                #Add Item
                if 20 >= Damage:
                    Damage = 20
                    Weapon = 'Lvl 1 Copper Sword'
                    Gold -= 16
                else:
                    print('Lower Level Sword')
        

        elif ShopBuying == '22':
            if 32 <= Gold+1:
                #Add Item
                if 25 >= Damage:
                    Damage = 25
                    Weapon = 'Lvl 2 Copper Sword'
                    Gold -= 32
                else:
                    print('Lower Level Sword')

        elif ShopBuying == '23':
            if 65 <= Gold+1:
                #Add Item
                if 30 >= Damage:
                    Damage = 30
                    Weapon = 'Lvl 3 Copper Sword'
                    Gold -= 65
                else:
                    print('Lower Level Sword')

        elif ShopBuying == '24':
            if 120 <= Gold+1:
                #Add Item
                if 35 >= Damage:
                    Damage = 35
                    Weapon = 'Lvl 4 Copper Sword'
                    Gold -= 120
                else:
                    print('Lower Level Sword')

        elif ShopBuying == '25':
            if 50 <= Gold+1:
                #Add Item
                if 20 >= Resistance:
                    Resistance = 20
                    Armour = 'Lvl 1 Copper Armour'
                    Gold -= 50
                else:
                    print('Lower Level Sword')

        elif ShopBuying == '26':
            if 75 <= Gold+1:
                #Add Item
                if 25 >= Resistance:
                    Resistance = 25
                    Armour = 'Lvl 2 Copper Armour'
                    Gold -= 75
                else:
                    print('Lower Level Sword')

        elif ShopBuying == '27':
            if 100 <= Gold+1:
                #Add Item
                if 30 >= Resistance:
                    Resistance = 30
                    Armour = 'Lvl 3 Copper Armour'
                    Gold -= 100
                else:
                    print('Lower Level Sword')

        elif ShopBuying == '28':
            if 125 <= Gold+1:
                #Add Item
                if 35 >= Damage:
                    Damage = 35
                    Weapon = 'Lvl 4 Copper Armour'
                    Gold -= 125
                else:
                    print('Lower Level Sword')


        elif ShopBuying == '31':
            if 250 <= Gold+1:
                #Add Item
                if 50 >= Damage:
                    Damage = 50
                    Weapon = 'Lvl 1 Iron Sword'
                    Gold -= 250
                else:
                    print('Lower Level Sword')

        elif ShopBuying == '32':
            if 300 <= Gold+1:
                #Add Item
                if 60 >= Damage:
                    Damage = 60
                    Weapon = 'Lvl 2 Iron Sword'
                    Gold -= 300
            else:
                    print('Lower Level Sword')

        elif ShopBuying == '33':
            if 325 <= Gold+1:
                #Add Item
                if 70 >= Damage:
                    Damage = 70
                    Weapon = 'Lvl 3 Iron Sword'
                    Gold -= 325
                else:
                    print('Lower Level Sword')

        elif ShopBuying == '34':
            if 350 <= Gold+1:
                #Add Item
                if 80 >= Damage:
                    Damage = 80
                    Weapon = 'Lvl 4 Iron Sword'
                    Gold -= 350 
                else:
                    print('Lower Level Sword')        

        elif ShopBuying == '35':
            if 250 <= Gold+1:
                #Add Item
                if 50 >= Resistance:
                    Resistance = 50
                    Armour = 'Lvl 1 Iron Armour'
                    Gold -= 250
                else:
                    print('Lower Level Sword')

        elif ShopBuying == '36':
            if 275 <= Gold+1:
                #Add Item
                if 60 >= Resistance:
                    Resistance = 6
                    Armour = 'Lvl 2 Iron Armour'
                    Gold -= 275
                else:
                    print('Lower Level Sword')

        elif ShopBuying == '37':
            if 250 <= Gold+1:
                #Add Item
                if 70 >= Resistance:
                    Resistance = 70
                    Armour = 'Lvl 3 Iron Armour'
                    Gold -= 250
                else:
                    print('Lower Level Sword')


        elif ShopBuying == '38':
            if 275 <= Gold+1:
                #Add Item
                if 80 >= Resistance:
                    Resistance = 80
                    Armour = 'Lvl 4 Iron Armour'
                    Gold -= 275
                else:
                    print('Lower Level Sword')

        else:
            print('''
            Input Not Found Error 404
            ''')

def TreasureRoom():
    print('''
    You Leave Engradoland into a Forest where You Enter this strange Temple wondering what treasures it could hold but as you enter, 
    the Doors close around you. You enter slowly but then are amazed by what you see. 
    Before you is a Sword, Forged at the edge on Valhalla, and on the Left is a Totem, 
    made of Silver and Gold Encrustings.
    ''')

    while True:
        TreasureTotemSword = input('Which do you Take? (1) Sword / (2) Totem ')

        if TreasureTotemSword == '1':
            print('''
            You Take the Sword, The Room Shakes and the Sword Fades into Nothing. The Doors
            Open and then the Doors Open, You rush out and see the Open world. You See a
            Forest.
            ''')
            
            Forest()
            break

        elif TreasureTotemSword == '2':
            print('''
            You Take the Totem, The Room Shakes and the Sword Fades into Nothing. The Doors
            Open and then the Doors Open, You rush out and see the Open world. You see a Cave.
            ''')

            Cave()
            break

def Forest():
    global ShopExit
    ShopExit = 2
    print('''
    You wander through the Fores. It's Dark but in the Distance you See a Small Beacon of 
    Light. You Get Closer and You See People. You Run towards them happy and Joyful, it is
    another Town you have found. The Mayor of comes to you Joyfully explaining who they are
    and what they are doing. He explains they are Engradolands Biggest Competition in who
    has the Largest City. He goes on a Little More before shoing you the Shop and Casino.
    ''')
    Casino()

    

def Cave():
    print('''
    You go through the door and all light leaves your eyes and your realise that the door closed behind you.
    ''')
    
def TheWalkUp():
    print('''
    You start to creep up the mountain awaiting the dragon’s master. The mountain is 
    covered in cobwebs and caves cover it like a wedge of swiss cheese. You hear screeches 
    and the cackles of mutated monkeys. You step on a twig and it snaps.


    It's the Final Coun- 
    
    NO MILES, DON't PLAY THAT

    WHY NOT SHABAGEL

    COPYRIGHT REASONS

    WHY DON'T WE LICENCES THE SONG THEN

    BECAUSE THIS IS FOR A SCHOOL ASSIGNMENT

    Wait, why is what we say going into the game

    Ummmmm

    Quick, Turn it off

    I'm Tryi-

    
    Get Ready!!! FOR THE FINAL BOSS BATTLE

    ''')

def Stats():
    if Health in range(1, 10):
        print(f"❤️  \033[31m█\033[0m--------- ({Health}/100)")

    elif Health in range(11, 20):
        print(f"❤️  \033[31m██\033[0m-------- ({Health}/100)")

    elif Health in range(21, 30):
        print(f"❤️  \033[31m███\033[0m------- ({Health}/100)")

    elif Health in range(31, 40):
        print(f"❤️  \033[33m████\033[0m------ ({Health}/100)")

    elif Health in range(41, 50):
        print(f"❤️  \033[33m█████\033[0m----- ({Health}/100)")

    elif Health in range(51, 60):
        print(f"❤️  \033[33m██████\033[0m---- ({Health}/100)")
    elif Health in range(61, 70):
        print(f"❤️  \033[33m███████\033[0m--- ({Health}/100)")

    elif Health in range(71, 80):
        print(f"❤️  \033[32m████████\033[0m-- ({Health}/100)")

    elif Health in range(81, 90):
        print(f"❤️  \033[32m█████████\033[0m- ({Health}/100)")

    elif Health in range(91, 100):
        print(f"❤️  \033[32m██████████\033[0m ({Health}/100)")

    elif Health <= 0:
        print(f"❤️  ---------- (0/100)")
        print("You have Died")
        quit()

    print(f'Weapon: {Weapon} Damage: {Damage}')
    print('')
    print(f'Armour: {Armour} Resistance: {Resistance}')
    print(f'Gold: {Gold}')
    print(f'Inventory: {Inventory}')

DisplayTitleScreen()