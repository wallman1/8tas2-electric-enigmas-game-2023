import UserInterface as UI 
import combatsystem as Combat
import random

def Start():
  Village()

def Village():
   UI.DisplayScene(
    "The Village",
     """You wake up to find your home burning in the sunlight and a loud ROAR in the distance. 
        You run outside to see your whole village ravaged by fire and a large winged beast 
        flying away. You try to find your family but your efforts are worthless as you find 
        out from the town mayor. Your Mother and Sister were trapped under a burning pile of 
        wood and were burnt. You ask the mayor about your father and the mayor lowers 
        his head. In a weak voice he says your father couldn't deal with the news of your 
        Mother and Sister and has run away leaving you and the rest of the town. More Buildings
        collapse as you stand there sobbing but action for your survival must be done. Rocks are
        falling around you, and as they are, a Doorway is revealed in the Side of the Mountain.

As they fall to the ground, they reveal a doorway.""",
    {
        "Enter the mysterious doorway":DungeonSideEntrance,
        "Leave into the forest":GoblinVillage
    }
  )

def GoblinVillage():
  UI.DisplayScene(
    "The Goblin Village",
    """ After wandering the forest for hours, you finally start seeing light up ahead. 
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
    """ You crawl away from the goblin corpses, still mortified at their attempt to attack you. 
        You see the city of Engrardo of the Engrado Kingdom""",
        
        {"Enter Engradoland":Engradoland}
    )

def Engradoland():
  Combat.BanditFight()
  UI.DisplayScene(
    "Engradoland",
    """At Engradoland, you find yourself a Blacksmith and Merchant. Would you like to visit them or Travel to the Dungeon.  """,
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
            "Travel to the Dungeon":DungeonRoom1,
        }
    )

def DungeonRoom1():
  UI.DisplaySceneWithEvent(
    "Dungeon Room",
    "As you enter the room you hear the clanking of bones as the skeletons on the ground start to reanimate",
    Combat.SkeletonFight,
    "You beat the skeletons",
     {
      'enter the room in front of you':DungeonRoom2,
     }
  )
  
def DungeonRoom2():
   UI.DisplaySceneWithEvent(
      "Dungeon Room",
      "As you enter this room you get covered in spiderwebs as spiders start crawling towards you",
      Combat.SpiderFight,
      "You defeated the spiders.",
      {
         'enter the room in front of you':DungeonRoom3,
         'enter the room to your left':DungeonRoom4,
         'enter the room to your right':DungeonRoom5
      }
   )

def DungeonRoom3():
  UI.DisplaySceneWithEvent(
     "Dungeon Room",
     "As you enter the room you see goblins crowding around a pile of gold",
     Combat.GoblinRoomFight,
     "You defeated the goblins.",
     {
        'enter the room in front of you':DungeonRoom5,
        'enter the room to your left':DungeonRoom4,
        'enter the room to your right':DungeonRoom6
     }
  )

def riddle1():
    while True:
      response = input("What is the answer to the riddle?"),
      if 'candle' in response:
        print("correct, the walls reveal themselves to be doors")
        return
      print("How do you survive? I mean seriously.... Can you even walk and chew gum at the same time?")

def DungeonRoom4():
  UI.DisplaySceneWithEvent(
     "Dungeon Room",
     """As you enter the room you see a riddle on the wall and no clear way out
The riddle reads:
I am tall when I am young, and I am short when I am old. What am I?""",
    riddle1,
    "<sarcasm>Wow, you solved the riddle</sarcasm>. Where to now genius?",
    {
       'enter the room in front of you':DungeonRoom5,
       'enter the room to your left':DungeonRoom6,
    }
  )

def DungeonRoom5():
  UI.DisplaySceneWithEvent(
     "Dungeon Room",
     "As you enter this room you see piles of gold and a sword on the ground",
     Combat.LootRoom,
     "You slyly grab the loot.... Quick lets cheese it!",
     {
        'enter the room in front of you':DungeonRoom6,
        'enter the room to your left':DungeonRoom7,
     }
  )

def DungeonRoom6():
  UI.DisplayScene(
    "Dungeon Room",
    "As you enter the room you feel an uneasy sense of unease because this room is eerily empty",
    {
       'enter the room in front of you':DungeonRoom8,
       'enter the room to your left':DungeonRoom7,
    }
  )

def DungeonRoom7():
   UI.DisplaySceneWithEvent(
      "Dungeon Room",
      "As you enter the room you hear the hissing os spiders behind you and spider webs infront of you",
      Combat.SpiderFight,
      "You smoked the spider. Now what?",
      {
         'enter the room in front of you':DungeonRoom8,
         'enter the room to your left':DungeonRoom6,
      }
   )

def DoNothing():
   pass

def DungeonRoom8():
   UI.DisplayScene(
      "Dungeon Room",
      "As you enter the room you see burn marks covering the walls",
      {
         'walk into the room from where the burn marks came':DragonBoss,
      }
   )

def DragonBoss():
   UI.DisplaySceneWithEvent(
      "The Dragon's Lair",
      "As you walk into the large room with gold and treasure scattered around the room, you see a towering dragon, the same monster that killed your family, as you walk towards it, it awakens",
      Combat.DragonFight,
    """After defeating the vile monster, you see a large purple light around it's neck start to glow and then shatters, which means that the dragon was being controlled by someone
As you are wondering this you see two treasures that peak your intrest""",
    {
       'enter the room wuth the treasures':TreasureRoom,
    }
   )

def DungeonSideEntrance():
    UI.DisplayScene(
        "The Side Enterance of The Dungeon",
        """"You Enter the Dungeon But Slip and Fall to your Death, You have Died""",
        {
            "Exit":exit
        }
    )

def Cave():
  UI.DisplaySceneWithEvent(
        "The Cave",
        """You Enter The Cave and Encounter Lots of Enemies, It is going to be a Long Fight""",
        Combat.SpiderAndSkeletonFight,
        """That was intense. I am going to sit down for a minute while you decide what to do next......
Some skeezy old dude wants me to go on a 'quest'.""",
        {
           "do you accept the stranger's 'quest'":TheWalkup,
        }
    )

def TreasureRoom():
    UI.DisplayScene(
      "The Treasure Room",
      """As you walk through a large stone door, you spot mounds of gold, more than you can ever use! 
Then, lying on the left side of the room is a pure gold totem of the dragon, and on the right side of the room is a dazzaling sword.
You feel intreged towards them. Unfortunatly, the room has started to crumble so you have to choose quickly.""",
        {
            "Totem":ElfVillage,
            "Sword":Cave,
        }
    )

def ElfVillage():
  UI.DisplayScene(
    "The Elf Village",
    """As your hand scrapes the totem, a huge tital wave appears and washes you away. As you start to black you, you see a few sparkling trees in the distance.
As you wake up, you find yourself next to a gushing river. As you get up, you realize that you have been washed up next to a village full of Elves!
As you wander around the village, you see a blacksmith, market and a Casino. Where would you like to visit?""",
    {
        "Blacksmith":Blacksmith,
        "Market":Market,
        "Pasino":Casino,
        "Tavern":Tavern
    }
  
  )

def Market():
  UI.DisplayScene(
     "The Market",
     "As you enter the Bustling market you see a Merchant with items that particularly pique your intrest",
     Combat.Player.trade(Combat.Merchant_Barlie),
     {
        "Blacksmith":Blacksmith,
        "Pasino":Casino,
        "Tavern":Tavern,
        "Back to town":ElfVillage
     }
  )

def Tavern():
  UI.DisplayScene(
     "The Tavern",
    """As you enter the tavern you see many people parting and having a good time but one person stands out, a man in the corner that is covered in a black cloak and is eminating an ominous aura
When you approach the man he starts to tell you that the members of a cult up in the mountains were the people controlling the dragon and he gives you a map to where the cult lives""",
    {
       "You accept the strangers quest":TheWalkup,
       "wait a sec I still need to prepare":ElfVillage
    }
  )

def TheWalkup():
  UI.DisplayScene(
        "The Walk Up",
        '''You start to creep up the mountain awaiting the dragon’s master. The mountain is 
            covered in cobwebs and caves cover it like a wedge of swiss cheese. You hear screeches 
            and the cackles of mutated monkeys. You step on a twig and it snaps.''',
        {
            "CultistBoss":CultistBoss,
        }
    )

def CultistBoss():
  print("THE FINAL BOSSSSSSS!")
  UI.DisplayScene(
    """You rock up to the liar of the great and mighty Cultist BOSS! GET READY TO FIGHT""",
    {
      #Insert the Combat for Cultist Boss
    }
  )

def BlacksmithTrade():
    Combat.Player.trade(Combat.blacksmith_bob)

def Blacksmith():
  while True: 

    UI.DisplayScene(
      "Blacksmith",
      "You walk into the blacksmith to see incredible weapons and armours",
      {
        "Trade":BlacksmithTrade,
        "Market":Market,
        "Pasino":Casino,
        "Tavern":Tavern,
        "Back to town":ElfVillage
      }
  )
 
def ElfBlacksmith():
   UI.DisplayScene(
      "The blacksmith",
      "As you walk into the forge you see an elf forging a new sword",
      Combat.Player.trade(Combat.blacksmith_bog),
      {
         'go back to town':ElfVillage,
         'go to the market':Market,
         'go to tavern':Tavern,
      }
   )

def Merchant():
  UI.DisplayScene(
  "Merchant",
  "The merchant says, well hello there, are you in need of any of my exotic goods?",
  Combat.Player.trade(Combat.Merchant_Charlie),
  {
     "go back to town":Engradoland,
     "go to blacksmith":Blacksmith
  }
  )




def Casino():
  print("the casino is closed righ now")
  return  
  CasinoMultiplier=5
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
        Gold += CasinoMultiplier*Betting
        

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
            ElfVillage()
            break

        else:
            print('''
            Input Not Found Error 404
            ''')


