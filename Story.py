import UserInterface as UI
import combatsystem as Combat

def Start():
  Village()

def Village():
   UI.DisplayScene(
    "The Village",
     """You wake up to find your home burning in the sunlight and a loud ROAR in the distance. 
You run outside to see your whole village ravaged by fire and a large winged beast flying away. 
You try to find your family but your efforts are worthless as you find out from the town mayor. 
Your mother and sister were trapped under a burning pile of wood and were burnt alive. 
You ask the mayor about your father and the mayor lowers his head. 
In a weak voice he says your father couldn't deal with the news of your mother and sister and has run away leaving you and the rest of the town. 
More buildings collapse as you stand there sobbing but action for your survival must be done.
You are forced to leave to save your life. 
Rocks crumble around you. 
As they fall to the ground, they reveal a doorway.""",
    {
        "Enter the mysterious doorway":DungeonSideEntrance,
        "Leave into the forest":GoblinVillage
    }
  )

def GoblinVillage():
  UI.DisplayScene(
    "The Goblin Village",
    """After wandering the forest for hours, you finally start seeing light up ahead. 
You look up and see smoke rising from a nearby fire. 
You run towards the light, thinking you can finally get some rest with travellers. 
Unfortunatly, as you walk closer you start hearing speach. 
Its not human speach however. 
You cautiously approach the small camp. 
It turns out to be a goblin camp. 
As you try to back away, you acidentally step on a stick. The sound attracts a nearby goblin.""",
    {"Kill em all!!!!!":Ambush}
  )

def Ambush():
    Combat.GoblinFight()
    UI.DisplayScene(
        "The Ambush",
        """You crawl away from the goblin corpses, still mortified at their attempt to attack you. 
You see the city of Engrardo of the Engrado Kingdom""",
        {"Enter Engradoland":Engradoland}
    )

def Engradoland():
    Combat.BanditFight()
    UI.DisplayScene(
        "Engradoland",
        """"todo: Add Engradoland description""",
        {
            "Blacksmith":Blacksmith,
            "Merchant":Merchant,
            "Travel to the Dungeon":DungeonMainEntrance,
        }
    )
  

def DungeonMainEntrance():
    UI.DisplayScene(
        "The Enterance of The Dungeon",
        """"todo: Add description""",
        {
            "Blacksmith":Blacksmith,
            "Merchant":Merchant,
            "Travel to the Dungeon":DungeonMainEntrance,
        }
    )

#def DungeonRoom1():
  #UI.DisplayScene(
   # "Dungeon Room",
   # "As you enter this room you hear the clanking of bones as the skeletons on the ground reanimate themselves",
 # )

def DungeonSideEntrance():
    UI.DisplayScene(
        "The Side Enterance of The Dungeon",
        """"You Enter the Dungeon But Slip and Fall to your Death, You have Died""",
        {
            "Exit":exit
        }
    )

def TreasureRoom():
  print("--- Treasure Room ---")

def ElfVillage():
  print("--- Elf Village ---")

def Market():
  ("--- The Market ---")

def Tavern():
  print("--- The Tavern ---")

def TheWalkup():
  print("--- The Base of The Mountain ---")

def CultistBoss():
  print("--- The Top of The Mountain ---")

def Blacksmith():
  Combat.Player.trade(Combat.blacksmith_bob)  
  print(''' You enter the blacksmith.
  Blacksmith: Ah I see you are in need of some armour and wepons! Here are a selection of the hightest quality in town!
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
      
      

