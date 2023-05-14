import UserInterface as UI
import random
import math

def select_dialog(prompt,items):
    while(True):
        index=1
        UI.DisplayTitle(prompt)
        for item in items:
            print(index,"-",item.name)
            index+=1
        try:
            item_index = int(input("Selection: "))
            item=items[item_index-1]
            print("You have selected:", item.name)
            return item
        except:
            print("Stop being an idiot!!!")


def roll_dice(prompt,sides):
    result = random.randrange(1,sides)
    #print(prompt,": Rolling ", sides, " sided dice.....","Rolled a ", result)
    return result

class item(object):
    def __init__(self,name):
        pass

class Weapon(item):
    def __init__(self,name,damage):
        super().__init__(name)
        self.name=name
        self.damage=damage

class Armour(item):
    def __init__(self,name,resistance,location):
        self.name=name
        self.resistance=resistance
        self.location=location

class Character(object):
    def __init__(self,name,type,health):
        
        self.equipped_armour={
            'head': Armour("Nothing",0,"head"),
            'torso': Armour("Nothing",0,"torso"),
            'left arm': Armour("Nothing",0,"left arm"),
            'right arm': Armour("Nothing",0,"right arm"),
            'left leg': Armour("Nothing",0,"left leg"),
            'right leg': Armour("Nothing",0,"right leg")}
        self.name=name
        self.type=type
        self.health=health
        self.max_health=health
        self.inventory=[]
        self.fists=Weapon("Nothing",0)
        self.equipped_weapon=self.fists
    def stats(self):
        UI.DisplayStats(self.name,self.type, self.health,self.max_health,self.equipped_weapon.damage,self.get_total_resistance())

    def get_inventory_weapons(self):
        result=[]
        for item in self.inventory:
            if isinstance(item, weapon):
                result.append(item)
        return result
    def get_inventory_armour(self):
        result=[]
        for item in self.inventory:
            if isinstance(item, armour):
                result.append(item)
        return result

    def equip(self,item):
        if isinstance(item,Weapon):
            self.equipped_weapon=item
            #print(self.name, " has equiped weapon: ", item.name)
        elif isinstance(item,armour):
            self.equipped_armour[item.location]=item    
            #print(self.name, " has equiped armour: ", item.name, " on ",item.location)

    def give(self,item):
        print(self.name," has been given: ",item.name)
        self.inventory.append(item)

    def give_and_equip(self,item):
        self.give(item)
        self.equip(item)

    def show_equiped(self):
        UI.DisplayTitle("Equiped items")
        for location in self.equipped_armour.keys():
            print(f"{location:10}:",self.equipped_armour[location].name)
        location="Weapon"
        print(f"{location:10}:",self.equipped_weapon.name)

    def equip_dialog(self):
        while True:
            response = input("Do you want to equip an item?(y/n) ")
            if response == 'y':
                self.equip(select_dialog("Equip item",self.inventory))
                self.show_equiped()
            else:
                return

    def show_item_list(self,title,list):
        UI.DisplayTitle(title)
        for item in list:
            print(item.name)

    def show_inventory(self):
        self.show_item_list('inventory: ',self.inventory)

    def show_inventory_armours(self):
        self.show_item_list('armour: ',self.get_inventory_armour())

    def show_inventory_weapons(self):
        self.show_item_list('weapons: ',self.get_inventory_weapons())

    def get_total_resistance(self):
        resistance=0
        for location in self.equipped_armour.keys():
            resistance=resistance+self.equipped_armour[location].resistance
        return resistance
        
    def attack(self,target):
        #print(self.name," attacked ",target.name," with ", self.equipped_weapon.name)
        sides=6
        attack_damage = int((self.equipped_weapon.damage*roll_dice("\tAttacking",sides))/sides)
        #print("\t",self.name," Raw Attack Damage =", attack_damage)
        resistance=target.get_total_resistance()
        #print("\t",target.name," Resistance =", resistance)
        armoured_attack_damage=attack_damage-resistance
        if armoured_attack_damage<0:
            armoured_attack_damage=0
        #print("\t",target.name, " received armoured Attack Damage =", armoured_attack_damage)            
        target.health-=armoured_attack_damage
        #print("\t",target.name," health is at ", target.health)
        print(f"{self.name:10} Attacked {target.name:10} | Inflicted Damage : {armoured_attack_damage:3} ")

    def is_dead(self):
        if self.health<=0:
            return True
        return False

    def fight(self,enemies):
        UI.DisplayTitle("A fight has started")
        round=1
        while(True):
            UI.DisplayTitle(f"Round {round}")
            round+=1
            self.stats()
            #player attacks
            live_enemies=[]
            for enemy in enemies:
                if not enemy.is_dead():
                    enemy.stats()
                    live_enemies.append(enemy)
            if len(live_enemies)==0:
                print("you won")
                return True
            self.equip_dialog()
            target=select_dialog("Who will you attack?",live_enemies)
            self.attack(target)
            #then each enemy attacks
            for enemy in live_enemies:
                enemy.attack(self)
                if self.is_dead():
                    print("you died")
                    return False

class Hero(Character):
    def __init__(self,name):
        super().__init__(name,"Human", 100)
        self.give_and_equip(Weapon("Stick",10))

class Goblin(Character):
    def __init__(self,name):
        super().__init__(name,"Goblin", 100)
        self.give_and_equip(Weapon("Club",30))

class Human(Character):
    def __init__(self,name):
        super().__init__(name,"Human", 100)
        self.give_and_equip(Weapon("Level 1 Wooden Sword",10))

class Skeleton(Character):
    def __init__(self,name):
        super().__init__(name,"Skeleton", 100)
        self.give_and_equip(Weapon("Level 1 Wooden Bow",20))
class Spider(Character):
    def __init__(self,name):
        super().__init__(name,"Spider", 100)
        self.give_and_equip(Weapon("Fangs",20))

class Dragon(Character):
    def __init__(self,name):
        super().__init__(name,"Dragon", 100)
        self.give_and_equip(Weapon("Fire Breath",100))

Player = Hero('Grognak')

def GoblinFight():
    Player.fight([Goblin("Brzt")])

def BanditFight():
    Player.fight([Human("Bob"),Human("Gary"),Human("Fred")])

def SkeletonFight():
    Player.fight([Skeleton("Norman"),Skeleton("Harry"),Skeleton("George")])

def SpiderFight():
    Player.fight([Spider("Norman"),Spider("Harry"),Spider("George")])

def DragonFight():
    Player.fight([Dragon("Toothless")])

def test():
    Player.give_and_equip(Weapon("Sword",10))
    GoblinFight()

#test()