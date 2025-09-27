from time import sleep
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

DevMode = 0
BrainrotsList = [BrBrPatapim, CrocodiloBombordilo, TralaleiloTralala]    #  список всех персонажей
Inventory = []    # инвентарь
Money = 100
gold = 1

def DevPrint(DevText):
    global DevMode
    if DevMode == 1:
        print(f"{DevText}")

def PrintInventory():   #   вывод инвентаря
    global gold
    if Inventory == []:
        print("У вас немає брейнротів")
    else:
        print(f"У вас {Money} грн")
        for x in range(len(Inventory)):
            print(f"{Inventory[x].name}: здоров'я: {Inventory[x].hp}, сила: {Inventory[x].damage}")

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

def battle():
    global Money
    global Inventory
    if Inventory == []:
        print("У вас немає брейнротів щоб битися")
    else:
        BattleEnemyVariable = BrainrotsList[randint(0,  len(BrainrotsList)-1)]
        BattleEnemyHp = BattleEnemyVariable.hp
        BattlePlayerHp = Inventory[0].hp
        sleep(1)
        print(f"Ваш суперник: {BattleEnemyVariable.name}, здоров'я: {BattleEnemyVariable.hp}, сила: {BattleEnemyVariable.damage}")
        while BattleEnemyHp > 0 and BattlePlayerHp > 0:
            sleep(1)
            PlayerBattleInput = int(input("(1) Атака (2) Захист (3) Контр-атака: "))
            EnemyBattleInput = randint(1, 3)
            if PlayerBattleInput == 1 and EnemyBattleInput != 2:
                DevPrint("enemy - {BattleEnemyVariable}.damage hp")
                BattleEnemyHp = BattleEnemyHp - Inventory[0].damage
                print(f"{BattleEnemyHp}")
                print(f"Ваш суперник пропускає удар!")

def MainMenu():
    global DevMode
    MainMenuInput = input("(1) Інвентар (2) Магазин (3) Арена (4) Донат (5) Казино: ")
    if MainMenuInput == "1":
        sleep(1)
        PrintInventory()
        sleep(1)
    elif MainMenuInput == "2":
        sleep(1)
        Market()
        sleep(1)
    elif MainMenuInput == "3":
        battle()
    elif MainMenuInput == "4":
        sleep(1)
        print("Номер карти: 5168 7520 #### 4667")
        sleep(1)
    elif MainMenuInput == "5":
        pass
    elif MainMenuInput == "Dev mode on":
        DevMode = 1
        DevPrint("Dev mode activated")
    elif MainMenuInput == "Dev mode off":
        DevPrint("Dev mode deactivated")
        DevMode = 0        
    else:
        pass

while 1:
    MainMenu()
