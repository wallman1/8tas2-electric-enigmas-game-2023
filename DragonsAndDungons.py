#---------------------------Imports (Systems and Definitions)---------------------------#
import random
import math

#---------------------------Combat System---------------------------#
def show_seperator():
        print("=================================")

def select_dialog(prompt,items):
    while(True):
        index=1
        print(prompt)
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
    print(prompt,": Rolling ", sides, " sided dice.....","Rolled a ", result)
    return result

class goblin(object):
    pass

class skeleton(object):
    pass

class human(object):
    pass

class item(object):
    def __init__(self):
        pass

class weapon(item):
    def __init__(self,name,damage,stamina):
        self.name=name
        self.damage=damage
        self.stamina=stamina

class armour(item):
    def __init__(self,name,resistance,location):
        self.name=name
        self.resistance=resistance
        self.location=location

class character(object):
    def __init__(self,name,type,health,damage):
        
        self.equipped_armour={
            'head': armour("Nothing",0,"head"),
            'torso': armour("Nothing",0,"torso"),
            'left arm': armour("Nothing",0,"left arm"),
            'right arm': armour("Nothing",0,"right arm"),
            'left leg': armour("Nothing",0,"left leg"),
            'right leg': armour("Nothing",0,"right leg")}
        self.name=name
        self.type=type
        self.health=health
        self.inventory=[]
        self.fists=weapon("fists",damage,5)
        self.equipped_weapon=self.fists
    def stats(self):
        return self.name + ": Type="+ self.type + ", ❤️  "+str(self.health)+", ⚔  "+str(self.equipped_weapon.damage)+ ", ⛨  "+str(self.get_total_resistance())
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
        if isinstance(item,weapon):
            self.equipped_weapon=item
            print(self.name, " has equiped weapon: ", item.name)
        elif isinstance(item,armour):
            self.equipped_armour[item.location]=item    
            print(self.name, " has equiped armour: ", item.name, " on ",item.location)

    def give(self,item):
        print(self.name," has been given: ",item.name)
        self.inventory.append(item)

    def give_and_equip(self,item):
        self.give(item)
        self.equip(item)


    def equip_weapon_dialog(self):
        self.equip(select_dialog("Equip item:", self.get_inventory_weapons()))

    def equip_armour_dialog(self):
        self.equip(item=select_dialog("Equip item:", self.get_inventory_armour()))

    def show_outfit(self):
        show_seperator()
        print("Outfit:")
        show_seperator()
        for location in self.equipped_armour.keys():
            print(self.equipped_armour[location].name," on ",location)
        show_seperator()
    
    def show_weapon(self):
        show_seperator()
        print("Weapon:")
        show_seperator()
        print(self.equipped_weapon.name," is selected")
        show_seperator()

    def show_equiped(self):
        self.show_outfit()
        self.show_weapon()

    def equip_outfit(self):
        while True:
            self.show_outfit()
            response = input("do you want to equip armour?(y/n) ")
            if response == 'y':
                self.equip_armour_dialog()
            else:
                return

    def equip_dialog(self):
        while True:
            self.show_equiped()
            response = input("do you want to equip an item?(y/n) ")
            if response == 'y':
                self.equip(select_dialog("Equip item",self.inventory))
            else:
                return

    def show_item_list(self,title,list):
        show_seperator()
        print(title)
        show_seperator()
        for item in list:
            print(item.name)
        show_seperator()

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
        print(self.name," attacked ",target.name," with ", self.equipped_weapon.name)
        sides=6
        attack_damage = int((self.equipped_weapon.damage*roll_dice("\tAttacking",sides))/sides)
        print("\t",self.name," Raw Attack Damage =", attack_damage)
        resistance=target.get_total_resistance()
        print("\t",target.name," Resistance =", resistance)
        armoured_attack_damage=attack_damage-resistance
        if armoured_attack_damage<0:
            armoured_attack_damage=0
        print("\t",target.name, " received armoured Attack Damage =", armoured_attack_damage)            
        target.health-=armoured_attack_damage
        print("\t",target.name," health is at ", target.health)

    def is_dead(self):
        if self.health<=0:
            return True
        return False

    def fight(self,enemies):
        print("A fight has started:")
        show_seperator()
        round=1
        while(True):
            show_seperator()
            print("Round ",round)
            show_seperator()
            round+=1
            print(player.stats())
            #player attacks
            live_enemies=[]
            for enemy in enemies:
                if not enemy.is_dead():
                    print(enemy.stats())
                    live_enemies.append(enemy)
            if len(live_enemies)==0:
                print("you won")
                return True
            player.equip_dialog()
            target=select_dialog("Who will you attack?",live_enemies)
            self.attack(target)
            #then each enemy attacks
            for enemy in live_enemies:
                enemy.attack(player)
                if self.is_dead():
                    print("you died")
                    return False

import Definitions as Def

import System.movementsystem as Move

#---------------------------Imports (Others)---------------------------#
import os



Def.TitleScreen()

print('''Welcome to Dragons And Dungons!

Please Login To continue''') 

Def.login()

Def.village()

Def.gobvillage()