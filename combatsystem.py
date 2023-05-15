import UserInterface as UI
import random
import math

def select_dialog(prompt,items):
    while(True):
        index=1
        UI.DisplayTitle(prompt)
        for item in items:
            if isinstance(item,Item):
                print(f"{index:2} - {item.name:20} {item.value:5} 🪙")
            else:
                print(f"{index:2} - {item.name:20}")
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

class Item(object):
    def __init__(self,name,value):
        self.name=name
        self.value=value

class Healing(Item):
    def __init__(self,name,value,amount):
        super().__init__(name,value)
        self.amount=amount

class Gold(Item):
    def __init__(self,value):
        super().__init__("Bag of Gold",value)
        self.value=value

class Weapon(Item):
    def __init__(self,name,value,damage):
        super().__init__(name,value)
        self.resistance=0
        self.damage=damage

class Armour(Item):
    def __init__(self,name,value,resistance,location):
        super().__init__(name,value)
        self.resistance=resistance
        self.location=location

class Character(object):
    def __init__(self,name,type,health):
        
        self.equipped={
            'Head': Armour("Nothing",0,0,"Head"),
            'Torso': Armour("Nothing",0,0,"Torso"),
            'Left Arm': Armour("Nothing",0,0,"Left Arm"),
            'Right Arm': Armour("Nothing",0,0,"Right Arm"),
            'Left Leg': Armour("Nothing",0,0,"Left Leg"),
            'Right Leg': Armour("Nothing",0,0,"Right Leg"),
            'Weapon' : Weapon("Nothing",0,0)}
        self.name=name
        self.type=type
        self.health=health
        self.max_health=health
        self.inventory=[]

    def stats(self):
        UI.DisplayStats(self.name,self.type, self.health,self.max_health,self.equipped["Weapon"].damage,self.get_total_resistance())

    def get_inventory_weapons(self):
        result=[]
        for item in self.inventory:
            if isinstance(item, Weapon):
                result.append(item)
        return result
    def get_inventory_armour(self):
        result=[]
        for item in self.inventory:
            if isinstance(item, Armour):
                result.append(item)
        return result

    def equip(self,item):
        if isinstance(item,Weapon):
            self.equipped["Weapon"]=item
        elif isinstance(item,Armour):
            self.equipped[item.location]=item
        elif isinstance(item,Healing):
            self.heal(item.amount)
            self.remove(item.name)

    def unequip(self,item):
        for location in self.equipped.keys():
            if item==self.equipped[location]
                if isinstance(item,Weapon):
                    self.equipped[location]=Weapon("Nothing",0,0)
                elif isinstance(item,Armour):
                    self.equipped[location]=Armour("Nothing",0,0,location)

    def get_gold(self):
        for destination_item in self.inventory:
            if isinstance(destination_item,Gold):
                return destination_item
        destination_item=Gold(0)
        self.inventory.append(destination_item)
        return destination_item

    def add_gold(self,source_item):
        gold=self.get_gold()
        gold.value+=source_item.value

    def give(self,item):
        print(self.name," has been given: ",item.name)
        if isinstance(item,Gold):
            self.add_gold(item)
        else:
            self.inventory.append(item)
        

    def remove(self,target_item_name):
        for inventory_item in self.inventory:
            if target_item_name == inventory_item.name:
                print(f"{target_item_name} removed from {self.name} inventory")
                self.unequip(inventory_item)
                self.inventory.remove(inventory_item)
                return

    def give_and_equip(self,item):
        self.give(item)
        self.equip(item)

    def show_equiped(self):
        UI.DisplayTitle("Equiped items")
        for location in self.equipped.keys():
            print(f"{location:10}:",self.equipped[location].name)

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
        index=1
        for item in list:
            print(f"{index:2} - {item.name:20} {item.value:5} 🪙")
            index+=1

    def DisplayInventory(self):
        self.show_item_list(f"{self.name} inventory:",self.inventory)

    def get_total_resistance(self):
        resistance=0
        for location in self.equipped.keys():
            resistance=resistance+self.equipped[location].resistance
        return resistance
        
    def attack(self,target):
        #print(self.name," attacked ",target.name," with ", self.equipped_weapon.name)
        sides=6
        attack_damage = int((self.equipped["Weapon"].damage*roll_dice("\tAttacking",sides))/sides)
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

    def heal(self,amount):
        self.health = self.health + amount
        if self.health > self.max_health:
            self.health=self.max_health
        print(f"{self.name} healed to {self.health}")

    def is_dead(self):
        if self.health<=0:
            return True
        return False

    def sell(self,target):
        item=select_dialog(f"{self.name} selling to {target.name}",self.inventory)
        if isinstance(item,Gold):
            return
        target_gold=target.get_gold()
        self_gold=self.get_gold()
        if target_gold.value>=item.value:
            print(f"{self.name} sold the the {item.name} to {target.name} for {item.value} gold")
            target.give(item)
            self.remove(item.name)
            target_gold.value-=item.value
            self_gold.value+=item.value
        else:
            print(f"{target.name} does not have enough gold")

    def buy(self,target):
        target.sell(self)

    def trade(self,target):
        while(True):
            self.DisplayInventory()
            target.DisplayInventory()
            UI.DisplayTitle(f"{self.name} is trading with {target.name}")
            index=1
            options=["Buy", "Sell","Stop Trading"]
            for option in options:
                print(f"{index:2} - {option:20}")
                index+=1
            try:
                option_index = int(input("Selection: "))
                option=options[option_index-1]
                print("You have selected:", option)
                if option=="Buy":
                    self.buy(target)
                elif option=="Sell":
                    self.sell(target)
                else:
                    return
            except:
                print("Stop being an idiot!!!")


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
        self.give_and_equip(Weapon("Stick",0,random.randrange(5,15)))
        self.give_and_equip(Armour("leather chestplate",5,2 ,'Torso'))
        self.give_and_equip(Armour("leather helmet",5,1 ,'Head'))
        self.give_and_equip(Armour("leather left leg",5,1 ,'Left Leg'))
        self.give_and_equip(Armour("leather right leg",5,1 ,'Right Leg'))
        self.give(Healing("lvl 1 Health potion",5, 10))
        self.give(Gold(30))
       

class Goblin(Character):
    def __init__(self,name):
        super().__init__(name,"Goblin", random.randrange(40,50))
        self.give_and_equip(Weapon("Club",2,random.randrange(5,10)))

class Human(Character):
    def __init__(self,name):
        super().__init__(name,"Human", random.randrange(50,55))
        self.give_and_equip(Weapon("Level 1 Wooden Sword",5,random.randrange(5,10)))

class Merchant(Character):
    def __init__(self,name):
        super().__init__(name,"Merchant", random.randrange(50,55))
        self.give(Gold(100))

class Blacksmith(Merchant):
    def __init__(self,name):
        super().__init__(name)
        self.give(Weapon("Lvl 1 Wooden Sword",3, 5))
        self.give(Weapon("Lvl 2 Wooden Sword",6, 10))
        self.give(Weapon("Lvl 3 Wooden Sword",9, 15))

        self.give(Weapon("Lvl 1 Metal Sword",13, 20))
        self.give(Weapon("Lvl 2 Metal Sword",16, 25))
        self.give(Weapon("Lvl 3 Metal Sword",19, 30))

        self.give(Weapon("Lvl 1 Diamond Sword",23, 35))
        self.give(Weapon("Lvl 2 Diamond Sword",26, 40))
        self.give(Weapon("Lvl 3 Diamond Sword",29, 45))
        
        self.give(Armour("leather chestplate",5,2 ,'Torso'))
        

class Skeleton(Character):
    def __init__(self,name):
        super().__init__(name,"Skeleton", 100)
        self.give_and_equip(Weapon("Level 1 Wooden Bow",5,20))
class Spider(Character):
    def __init__(self,name):
        super().__init__(name,"Spider", 100)
        self.give_and_equip(Weapon("Fangs",0,20))

class Dragon(Character):
    def __init__(self,name):
        super().__init__(name,"Dragon", 100)
        self.give_and_equip(Weapon("Fire Breath",0,100))

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
    #Player.DisplayInventory()
    Player.give_and_equip(Weapon("Sword",15,random.randrange(10,15)))
    #Player.DisplayInventory()
    Player.remove("Stick")
    Player.give(Gold(100))

    
    Player.trade(blacksmith)

    #Player.show_equiped()
    BanditFight()

Player = Hero('Grognak')
blacksmith_bob=Blacksmith("Blacksmith Bob")

#test()