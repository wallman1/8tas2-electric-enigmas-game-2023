import os

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


def DisplaySeparator():
    print("+"+"-"*78+"+")

def DisplayTitle(title):
    DisplaySeparator()
    print(f"| {title:76} |")
    DisplaySeparator()

def DisplaySubTitle(title):
    print(f"| {title:76} |")
    DisplaySeparator()


def SelectAction(actions):
    while(True):
        DisplaySeparator()
        index=1
        options=list(actions.keys())
        for option in options:
            print(index,"-",option)
            index+=1
        try:
            option_index = int(input("Selection: "))
            print("You have selected:#", option_index)
            DisplaySeparator()
            action=options[option_index-1]
            print("You have selected:", action)
            actions[action]()
            return
        except:
            print("Stop being an idiot!!!")
            exit()

def DisplayDialog(title,description):
    DisplayTitle(title)
    print(description)

def DisplayScene(title,description,actions):
    DisplayDialog(title,description)
    selection=SelectAction(actions)

def DisplaySceneWithEvent(title,pre_description,event,post_description,actions):
    DisplayDialog(title,pre_description)
    event()
    DisplayDialog(title,post_description)
    selection=SelectAction(actions)


def DisplayStats(name,type, health,max_health,damage,resistance):
    PlayerHealth=health
    bar_count=int(health*10/max_health)
    bars="█"*bar_count
    dashes="-"*(10-bar_count)
    print(f"{name:10}|{type:10}|❤️  [\033[31m{bars}█\033[0m{dashes}]({health:3}/{max_health:3})|🗡️ {damage:3} |🛡️  {resistance:3}")



#DisplayStats("Bob","Human",30,100,20,30)
#DisplayStats("Fred","Gob",30,100,20,30)