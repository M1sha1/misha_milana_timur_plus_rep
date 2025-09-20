#from time import sleep
from random import randint
class Brainrot:    #    создаю класс персонажей
    def __init__(self, name="Untitled", cost=100, hp=100, damage=20):
        self.name=name
        self.cost=cost
        self.hp=hp
        self.damage=damage

#   тут создаю всех персонажей
BrBrPatapim = Brainrot(name="Бр бр патапим", cost=140, damage=40)
CrocodiloBombordilo = Brainrot(name="Крокодило бомбордило", cost=220, damage=80)
TralaleiloTralala = Brainrot(name="Тралалейло тралала", cost=80)

BrainrotsList = [BrBrPatapim, CrocodiloBombordilo, TralaleiloTralala]    #  список всех персонажей
Inventory = []    # инвентарь
Money = 100
gold = 1

def PrintInventory():   #   вывод инвентаря
    global gold
    if Inventory == []:
        print("У вас немає брейнротів")
    else:
        print(f"У вас {Money} грн")
        for x in range(len(Inventory)):
            print(f"{Inventory[x].name}: здоров'я: {Inventory[x].hp}, сила: {Inventory[x].damage}")
#        if gold == 1:
#            if int(input(f"({len(Inventory)+1}) Перетворити персонажа на золотого ({len(Inventory)+2}) Вихід: ")) == len(Inventory)+1:
#                for x in range(len(Inventory)):
#                    print(f"({x + 1}) {Inventory[x].name}")
#                Inventory[int(input("Якого персонажа ви хочете перетворити на золотого?: "))-1].hp*10
#                Inventory[int(input("Якого персонажа ви хочете перетворити на золотого?: "))-1].damage*10
#                gold=gold-1

def Market():
    global Money
    print(f"У вас {Money} грн, в ассортименті є:")
    MarketAssortiment = randint(1,2)
    MarketCycleForVariableSaveList=[]
    for x in range(MarketAssortiment):
        MarketCycleForVariable = randint(0, len(BrainrotsList)-1)
        MarketCycleForVariableSaveList.append(MarketCycleForVariable)
        print(f"({x+1}) {BrainrotsList[MarketCycleForVariable].name}: коштує {BrainrotsList[MarketCycleForVariable].cost} грн, здоров'я: {BrainrotsList[MarketCycleForVariable].hp}, сила: {BrainrotsList[MarketCycleForVariable].damage}", end=" ")
        sleep(1)
    MarketChoise=0
    print(f"({MarketAssortiment+1}) Вихід: ", end="")
    while MarketChoise == 0 or MarketChoise > MarketAssortiment+1:
        MarketChoise=int(input())
        if MarketChoise == MarketAssortiment+1:
            pass
        elif MarketChoise == 1:
            if BrainrotsList[MarketCycleForVariableSaveList[0]].cost <= Money:
                Money -= BrainrotsList[MarketCycleForVariableSaveList[0]].cost
                print(f"Куплен {BrainrotsList[MarketCycleForVariableSaveList[0]].name}")
                Inventory.insert(0, BrainrotsList[MarketCycleForVariableSaveList[0]])
                MarketCycleForVariableSaveList.clear()
            else:
                print("У вас невисточає грошей")
        elif MarketAssortiment == 2 and MarketChoise == 2:
            if BrainrotsList[MarketCycleForVariableSaveList[1]].cost <= Money:
                Money -= BrainrotsList[MarketCycleForVariableSaveList[1]].cost
                print(f"Куплен {BrainrotsList[MarketCycleForVariableSaveList[1]].name}")
                Inventory.insert(0, BrainrotsList[MarketCycleForVariableSaveList[1]])
                MarketCycleForVariableSaveList.clear()
            else:
                print("У вас невисточає грошей")

def MainMenu():
    MainMenuInput=int(input("(1) Інвентар (2) Магазин (3) Арена (4) Донат (5) Казино: "))
    if MainMenuInput == 1:
        sleep(1)
        PrintInventory()
        sleep(1)
    elif MainMenuInput == 2:
        sleep(1)
        Market()
        sleep(1)
    elif MainMenuInput == 3:
        pass
    elif MainMenuInput == 4:
        sleep(1)
        print("Номер карти: 5168 7520 #### 4667")
        sleep(1)
    elif MainMenuInput == 5:
        pass
    else:
        pass

while 1:
    MainMenu()
