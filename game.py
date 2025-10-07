from time import sleep
from random import randint
from tkinter import *
from notifypy import Notify
import webbrowser
import pyttsx3

noti = Notify()
noti.title = "Дякую!"
noti.message = "Ви самі погодились😉"

engine = pyttsx3.init()
engine.say("Я Черныыыый")
engine.runAndWait()

class Brainrot:    #    создаю класс персонажей
    def __init__(self, name="Untitled", cost=100, hp=100, damage=20, gold=0):
        self.name=name
        self.cost=cost
        self.hp=hp
        self.damage=damage
        self.gold=gold

LicenseAccepted = 0

BrainrotsList = []    #  список всех персонажей
Inventory = []    # инвентарь
Money = 100
Gold = 0

def License():
    def accept():
        global LicenseAccepted
        LicenseAccepted = 1
        window.destroy()
    window = Tk()
    window.title("Ліцензійна угода")
    window.geometry("542x135")
    window.resizable(False, False)
    photo = PhotoImage(file="License.ppm")
    image_label = Label(window, image=photo)
    image_label.pack(padx=20, pady=20)
    image_label.image = photo
    aceeptbutton = Button(window, width = 15, height = 10, text = "Я згоден", command = accept)
    aceeptbutton.pack(side=RIGHT)
    declinebutton = Button(window, width = 15, height = 10, text = "Я не згоден", state = "disabled")
    declinebutton.pack(side=RIGHT)
    window.mainloop()

def CreateCharacters(**kwargs):
    global BrainrotsList
    for key, value in kwargs.items():
        key = Brainrot(value[0], value[1], value[2], value[3])
        BrainrotsList.append(key)

CreateCharacters(brbrpatapim = ("Бр бр патапим", 140, 100, 40), 
                 CrocodiloBombordilo = ("Крокодило бомбордило", 220, 100, 80), 
                 TralaleiloTralala = ("Тралалейло тралала", 80, 100, 20))

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
                if Inventory[GoldInput-1].gold != 2:
                    if Inventory[GoldInput-1].gold == 1:
                        Inventory[GoldInput-1].name = "Алмазний " + Inventory[GoldInput-1].name.replace("Золотий ", "")
                    else:
                        Inventory[GoldInput-1].name = "Золотий " + Inventory[GoldInput-1].name
                    Inventory[GoldInput-1].gold = 1
                    Inventory[GoldInput-1].damage = Inventory[GoldInput-1].damage * 2
                    Inventory[GoldInput-1].hp = Inventory[GoldInput-1].hp * 2
                    print(f"{Inventory[GoldInput-1].name}: здоров'я: {Inventory[GoldInput-1].hp}, сила: {Inventory[GoldInput-1].damage}")
                else:
                    print("Цей брейнрот вже має алмазне покращення")
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
            PlayerBattleInput = int(input("(1) Атака (2) Захист (3) Контр-атака (4) Ризиковий удар: "))
            EnemyBattleInput = randint(1, 4)

            if PlayerBattleInput == 1 and EnemyBattleInput == 1:
                BattleEnemyHp -= Inventory[0].damage
                BattlePlayerHp -= BattleEnemyVariable.damage
                print("Обидва атакують і отримують ушкодження!")

            elif PlayerBattleInput == 1 and EnemyBattleInput == 2:
                print("Суперник захищаєтьcя!")

            elif PlayerBattleInput == 1 and EnemyBattleInput == 3:
                BattlePlayerHp -= BattleEnemyVariable.damage
                print("Ви пропускаєте контр-атаку!")

            elif PlayerBattleInput == 1 and EnemyBattleInput == 4:
                BattlePlayerHp -= BattleEnemyVariable.damage * 1.5
                print("Суперник робить ризикований удар! Ви отримуєте потужний урон!")

            elif PlayerBattleInput == 2 and EnemyBattleInput == 1:
                print("Ви захищаєтесь від атаки!")

            elif PlayerBattleInput == 2 and EnemyBattleInput == 2:
                print("Обидва захищаються, нічого не відбувається.")

            elif PlayerBattleInput == 2 and EnemyBattleInput == 3:
                print("Суперник намагався контр-атакувати, але ви не атакували.")

            elif PlayerBattleInput == 2 and EnemyBattleInput == 4:
                print("Суперник робить ризикований удар, але ви блокуєте частину шкоди!")

            elif PlayerBattleInput == 3 and EnemyBattleInput == 1:
                BattleEnemyHp -= Inventory[0].damage * 1.5
                print("Ви успішно контратакували! Суперник отримує посилений удар!")

            elif PlayerBattleInput == 3 and EnemyBattleInput == 2:
                print("Контр-атака не спрацювала — суперник не атакував.")

            elif PlayerBattleInput == 3 and EnemyBattleInput == 3:
                print("Обидва контратакують — ніхто не атакує.")

            elif PlayerBattleInput == 3 and EnemyBattleInput == 4:
                BattlePlayerHp -= BattleEnemyVariable.damage
                print("Суперник зробив ризикований удар, поки ви чекали моменту!")

            elif PlayerBattleInput == 4 and EnemyBattleInput == 1:
                # 50% шанс, что промахнется
                if randint(1, 2) == 1:
                    BattleEnemyHp -= Inventory[0].damage * 2
                    print("Ваш ризикований удар влучив! Величезна шкода ворогу!")
                else:
                    BattlePlayerHp -= BattleEnemyVariable.damage
                    print("Ви промахнулись і отримали удар у відповідь!")

            elif PlayerBattleInput == 4 and EnemyBattleInput == 2:
                print("Суперник захищаєтьcя — ваш ризикований удар не завдав шкоди.")

            elif PlayerBattleInput == 4 and EnemyBattleInput == 3:
                BattleEnemyHp -= Inventory[0].damage * 2
                print("Ви застали суперника зненацька під час контр-атаки! Потужний удар!")

            elif PlayerBattleInput == 4 and EnemyBattleInput == 4:
                print("Обидва роблять ризиковані удари — промахи з обох сторін!")

        if BattleEnemyHp <= 0:
            Money += 20
            print(f"Ви перемогли! Ось ваші 20 монет")
            engine.say("Ви перемогли! Ось ваші 20 монет")
            engine.runAndWait()
        else:
            Inventory.remove(Inventory[0])
            print("Ви програли! И ваш брейнрот помер")
            engine.say("Ви програли! И ваш брейнрот помер")
            engine.runAndWait()

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
        sleep(1)
        battle()
        sleep(1)
    elif MainMenuInput == "4":
        sleep(1)
        print("Номер карти: 5168 7520 #### 4667")
        sleep(1)
    elif MainMenuInput == "5":
        pass
    elif MainMenuInput == "6":
        webbrowser.open("https://www.youtube.com/watch?v=xvFZjo5PgG0&list=RDxvFZjo5PgG0&start_radio=1")
    else:
        pass

def Game():
    global LicenseAccepted
    License()
    if LicenseAccepted == 1:
        noti.send()
        while 1:
            MainMenu()

Game()