import os
import System.combatsystem as Combat


def TitleScreen():
    os.system("cls")
    print("\033[36m________                                                 ____     ________                                                   ")
    print("\______ \____________     ____   ____   ____   ______   /  _ \    \______ \  __ __  ____    ____   ____  ____   ____   ______")
    print(" |    |  \_  __ \__  \   / ___\ /  _ \ /    \ /  ___/   >  _ </\   |    |  \|  |  \/    \  / ___\_/ __ \/  _ \ /    \ /  ___/")
    print(" |    `   \  | \// __ \_/ /_/  >  <_> )   |  \\___ \    /  <_\ \/   |    `   \  |  /   |  \/ /_/  >  ___(  <_> )   |  \\___ \ ")
    print("/_______  /__|  (____  /\___  / \____/|___|  /____  >  \_____\ \  /_______  /____/|___|  /\___  / \___  >____/|___|  /____  >")
    print("        \/           \//_____/             \/     \/          \/          \/           \//_____/      \/           \/     \/ \033[0m")
    print("")
    login()

def Health():
    global PlayerHealth
    
    if PlayerHealth in range(1, 11):
        print(f"❤️  \033[31m█\033[0m--------- ({PlayerHealth}/100)")

    elif PlayerHealth in range(11, 21):
        print(f"❤️  \033[31m██\033[0m-------- ({PlayerHealth}/100)")

    elif PlayerHealth in range(21, 31):
        print(f"❤️  \033[31m███\033[0m------- ({PlayerHealth}/100)")

    elif PlayerHealth in range(31, 41):
        print(f"❤️  \033[33m████\033[0m------ ({PlayerHealth}/100)")

    elif PlayerHealth in range(41, 51):
        print(f"❤️  \033[33m█████\033[0m----- ({PlayerHealth}/100)")

    elif PlayerHealth in range(51, 61):
        print(f"❤️  \033[33m██████\033[0m---- ({PlayerHealth}/100)")

    elif PlayerHealth in range(61, 71):
        print(f"❤️  \033[33m███████\033[0m--- ({PlayerHealth}/100)")

    elif PlayerHealth in range(71, 81):
        print(f"❤️  \033[32m████████\033[0m-- ({PlayerHealth}/100)")

    elif PlayerHealth in range(81, 91):
        print(f"❤️  \033[32m█████████\033[0m- ({PlayerHealth}/100)")

    elif PlayerHealth in range(91, 101):
        print(f"❤️  \033[32m██████████\033[0m ({PlayerHealth}/100)")

    elif PlayerHealth >= 101:
        print(f"❤️  \033[34m██████████\033[0m ({PlayerHealth}/100)")

    elif PlayerHealth <= 0:
        print(f"❤️  ---------- (0/100)")
        print("Something Something You Died L")
        quit()

def Stamina():
    global PlayerStamina
    
    if PlayerStamina in range(1, 10):
        print(f"🚶 \033[31m█\033[0m--------- ({PlayerStamina}/100)")

    elif PlayerStamina in range(11, 20):
        print(f"🚶 \033[31m██\033[0m-------- ({PlayerStamina}/100)")

    elif PlayerStamina in range(21, 30):
        print(f"🚶 \033[31m███\033[0m------- ({PlayerStamina}/100)")

    elif PlayerStamina in range(31, 40):
        print(f"🚶 \033[33m████\033[0m------ ({PlayerStamina}/100)")

    elif PlayerStamina in range(41, 50):
        print(f"🚶 \033[33m█████\033[0m----- ({PlayerStamina}/100)")

    elif PlayerStamina in range(51, 60):
        print(f"🚶 \033[33m██████\033[0m---- ({PlayerStamina}/100)")

    elif PlayerStamina in range(61, 70):
        print(f"🚶 \033[33m███████\033[0m--- ({PlayerStamina}/100)")

    elif PlayerStamina in range(71, 80):
        print(f"🚶 \033[32m████████\033[0m-- ({PlayerStamina}/100)")

    elif PlayerStamina in range(81, 90):
        print(f"🚶 \033[32m█████████\033[0m- ({PlayerStamina}/100)")

    elif PlayerStamina in range(91, 101):
        print(f"🚶 \033[32m██████████\033[0m ({PlayerStamina}/100)")

    elif PlayerStamina >= 101:
        print(f"🚶 \033[35m██████████\033[0m ({PlayerStamina}/100)")

    elif PlayerStamina <= 0:
        print(f"🚶 ---------- (0/100)")
        print("Something Something You Died L")
        quit()

def login():
  print("Create Your Account")
  User = input("Create Username: ")
  Pass = input("Create Password: ")
  Pass2 = input("Type in your password again: ")

  while Pass != Pass2:
   print("Your Password Does Not Match. Please Try Again!")
  
   User = input("Create Username: ")
   Pass = input("Create Password: ")
   Pass2 = input("Type in your password again: ")

  print("Account Created!")

  print("Login!")

  Username = input("Username: ")
  Password = input("Password: ")

  while User != User or Pass != Password:
    print("Your Username or Password does not match. Please try again")
  
    Username = input("Username: ")
    Password = input("Password: ")

  print("Login Success!")

def character():
  print("Men")

def village():
  print("--- The Village ---")
  print("You wake up to find your home burning in the sunlight and a loud ROAR in the distance. You run outside to see your whole village ravaged by fire and a large winged beast flying away. You try to find your family but your efforts are worthless as you find out from the town mayor. Your Mother and Sister were trapped under a burning pile of wood and were burnt alive. You ask the mayor about your father and the mayor lowers his head. In a weak voice he says your father couldn't deal with the news of your Mother and Sister and has run away leaving you and the rest of the town. More Buildings collapse as you stand there sobbing but action for your survival must be done.")

  LeaveorstayVillage = input("You are forced to leave to save your life, Rocks Crumble around you. As they fall to the ground they Reveal a Doorway, you are left with Two Options, Leave into the forest, or enter this Mysterious Doorway (Doorway) / (Forest) ")

  while True:
    if LeaveorstayVillage == "Doorway":
      print("You Enter the Dungeon But Slip and Fall to your Death, You have Died")
      quit()

    if LeaveorstayVillage == "Forest":
      gobvillage()

def gobvillage():
  print("--- The Goblin Village ---")
  print(''' After wandering the forest for hours, you finally start seeing light up ahead. You look up and see smoke rising from a nearby fire. You run towards the light, thinking you can finally get some rest with travellers. Unfortunatly, as you walk closer you start hearing speach. Its not human speach however.
  You cautiously approach the small camp. It turns out to be a goblin camp. As you try to back away, you acidentally step on a stick. The sound attracts a nearby goblin. ''')


def Ambush():
  print('''You crawl away from the goblin corpses, still mortified at their attempt to attack you. 
  
  As you near the nearly city of Engrardo of the Engrado Kingdom, you hear a stick snap and you find yourself surrounded by a gang of bandits. 
  ''')

  Run = input(str('You have 2 choices, running away (1) or staying to fight (2). '))

def engradoland():
  print("--- Engradoland ---")

def dungeonstart():
  print("--- The Enterance of The Dungeon ---")

def dungeon():
  print("--- The Dungeon ---")

def dungeonroom1():
  print('''You enter the room
you get attacked''')
  ()
  

def treasureroom():
  print("--- Treasure Room ---")

def elfvillage():
  print("--- Elf Village ---")

def market():
  ("--- The Market ---")

def tarvern():
  print("--- The Tavern ---")

def thewalkup():
  print("--- The Base of The Mountain ---")

def cultistboss():
  print("--- The Top of The Mountain ---")

def MiniMap():
    print('''
             ▫️---▫️
             |
    ▫️-\          ▫️
    |  \        / \ 
    ▫️   \       ▫️ ▫️
    |    \      \ /
    ▫️-----\-▫️    ▫️
           \|    |
            ▫️----▫️
    ''')

def Blacksmith():
  print(''' You enter the blacksmith.
  Blacksmith: Ah I see you are in need of some armour and wepons! Here are a selection of the hightest quality in town!
  ''')
  while True:
    inputIwouldliketobuya = input("What sort of Sword Would you Like: (Wooden) / (Copper) / (Iron) / (Diamond) / (Mitheral)")
  
    if inputIwouldliketobuya == "Wooden":
      print('''
      Items:                  Gold:
        Lvl 2 Wooden Sword      2
        Lvl 3 Wooden Sword      4
        Lvl 4 Wooden Sword      8
      
      ''')

    if inputIwouldliketobuya == "Copper":
      print('''
      Items:                  Gold:
        Lvl 1 Copper Sword      16
        Lvl 2 Copper Sword      32
        Lvl 3 Copper Sword      65
        Lvl 4 Copper Sword      120
      ''')

    if inputIwouldliketobuya == "Iron":
      print('''
      Items:                  Gold:
        Lvl 1 Iron Sword        250
        Lvl 2 Iron Sword        300
        Lvl 3 Iron Sword        325
        Lvl 4 Iron Sword        350
      ''')
      
    if inputIwouldliketobuya == "Diamond":
      print('''
      Items:                  Gold:
        Lvl 1 Diamond Sword     400
        Lvl 2 Diamond Sword     450
        Lvl 3 Diamond Sword     500
        Lvl 4 Diamond Sword     550
    ''')

    if inputIwouldliketobuya == "Mitheral":
      print('''
      Items:                  Gold:
        Lvl 1 Mithril Sword     600
        Lvl 2 Mithril Sword     675
        Lvl 3 Mithril Sword     750
        Lvl 4 Mithril Sword     800
      ''')



def Merchant():
  potions = ['Health Potion' , 'Strength potion' , 'Protecton field' , 'Apple' , 'Steak' , 'Stew']
  merchant = input(str("Welcome to the merchant's cavern, would you like to buy something? (Y/N)"))
  while 'Merchant' == Y:
    
    print('''I have a variety of potions and other items in store right now to help you on your journy.
  
    Items:

    Health potion 15 gold (1)
    Strength potion 15 gold (2)
    Protection field 20 gold (3)
    Apple 5 gold (4)
    Steak 5 gold (5)
    Stew 5 gold (6)

    ''')

    Potion = input(str("What would you like to buy? (1) / (2) / (3) / (4) / (5) / (6)  Please input one number"))

    if Potion == 1:
      print("Congratulations, you have obtained a Health Potion that will instantly give you 40 HP!")
      self.give(potions[0])
      
      
