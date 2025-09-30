from time import sleep
from random import randint
from tkinter import *

class Brainrot:    #    создаю класс персонажей
    def __init__(self, name="Untitled", cost=100, hp=100, damage=20, gold=0):
        self.name=name
        self.cost=cost
        self.hp=hp
        self.damage=damage
        self.gold=gold

BrainrotsList = []    #  список всех персонажей
Inventory = []    # инвентарь
Money = 100
Gold = 0

def License():
    window = Tk()
    window.title("Ліцензійна угода")
    window.geometry("542x100")
    window.resizable(False, False)
    photo = PhotoImage(file="License.ppm")
    image_label = Label(window, image=photo)
    image_label.pack(padx=20, pady=20)
    image_label.image = photo
    window.mainloop()

def CreateCharacters():
    global BrainrotsList
    BrBrPatapim = Brainrot(name="Бр бр патапим", cost=140, damage=40)
    CrocodiloBombordilo = Brainrot(name="Крокодило бомбордило", cost=220, damage=80)
    TralaleiloTralala = Brainrot(name="Тралалейло тралала", cost=80)

    BrainrotsList.append(BrBrPatapim)
    BrainrotsList.append(CrocodiloBombordilo)
    BrainrotsList.append(TralaleiloTralala)

def PrintInventory():
    global Gold
    if Inventory == []:
        print("У вас немає брейнротів")
    else:
        print(f"У вас {Money} грн")
        for x in range(len(Inventory)):
            print(f"{Inventory[x].name}: здоров'я: {Inventory[x].hp}, сила: {Inventory[x].damage}")
        if Gold >= 1:
            GoldBoolInput = int(input("Вимаєте золоте покращення, (1) Використати (2) Вийти: "))
            if GoldBoolInput == 1:
                if len(Inventory) > 1:
                    for x in range(len(Inventory)):
                        if x == len(Inventory)-1:
                            print(f"({x+1}) {Inventory[x].name}:", end=" ")
                        else:
                            print(f"({x+1}) {Inventory[x].name},", end=" ")
                else:
                    print(f"({x+1}) {Inventory[x].name}:", end=" ")
                GoldInput = int(input())
                Gold -= 1
                Inventory[GoldInput-1].gold = 1
                Inventory[GoldInput-1].name = "Золотий " + Inventory[GoldInput-1].name
                Inventory[GoldInput-1].damage = Inventory[GoldInput-1].damage * 2
                Inventory[GoldInput-1].hp = Inventory[GoldInput-1].hp * 2
                print(f"{Inventory[GoldInput-1].name}: здоров'я: {Inventory[GoldInput-1].hp}, сила: {Inventory[GoldInput-1].damage}")
            else:
                pass

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

            if PlayerBattleInput == 1 and EnemyBattleInput == 1:  # Оба атакуют
                BattleEnemyHp -= Inventory[0].damage
                BattlePlayerHp -= BattleEnemyVariable.damage
                print("Обидва атакують і отримують ушкодження")

            elif PlayerBattleInput == 1 and EnemyBattleInput == 2:  # Игрок атакует, враг защищается
                print("Ваш суперник захищається")

            elif PlayerBattleInput == 1 and EnemyBattleInput == 3:  # Игрок атакует, враг контратакует
                BattlePlayerHp -= BattleEnemyVariable.damage
                print("Ви пропускаєте удар")

            elif PlayerBattleInput == 2 and EnemyBattleInput == 1:  # Игрок защищается, враг атакует
                print("Ви захищаєтесь")

            elif PlayerBattleInput == 2 and EnemyBattleInput == 2:  # Оба защищаются
                print("Обидва захищаються, нічого не відбувається")

            elif PlayerBattleInput == 2 and EnemyBattleInput == 3:  # Игрок защищается, враг контратакует
                print("У суперника не вийшло контр-атакувати")

            elif PlayerBattleInput == 3 and EnemyBattleInput == 1:  # Игрок контратакует, враг атакует
                BattleEnemyHp -= Inventory[0].damage
                print("Ваш суперник пропускає удар")

            elif PlayerBattleInput == 3 and EnemyBattleInput == 2:  # Игрок контратакует, враг защищается
                print("Не вийшло — суперник не атакував.")

            elif PlayerBattleInput == 3 and EnemyBattleInput == 3:  # Оба контратакуют
                print("Обидва чекають моменту для контр-атаки, але ніхто не атакує.")
        if BattleEnemyHp <= 0:
            Money += 20
            print(f"Ви перемогли! Ось ваші 20 монет")
        else:
            Inventory.remove(0)
            print("Ви програли! И ваш брейнрот помер")

def MainMenu():
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
    else:
        pass

def Game():
    License()
    CreateCharacters()
    while 1:
        MainMenu()

Game()