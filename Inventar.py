import json
class Account:
    def __init__(self, name, euro, inventar):
        self.name = name
        self.inventar = inventar
        self.money = euro
        self.items = {
            "star" : 50,
            "shell" : 30,
            "block" : 10
        }
    def einkaufen(self, item):
        if item not in self.items:
            print("dieses item haben wir nicht im sortiment")
            return
        elif self.items[item] > self.money:
            print("Du hast zu wenig coins für dieses item")
            return
        elif len(self.inventar) == 5:
            print(f"Du hast {len(self.inventar)}/5 inventar slots belegt")
        else:
            self.inventar.append(item)
            self.money-=self.items[item]
            print(f"Das Item [{item}] wurde erfolgreich gekauft")
    def verkaufen(self, item):
        if item not in self.inventar:
            print("Du kannst das item nicht verkaufen, hast du nicht. ")
        else:
            self.inventar.remove(item)
            self.money += self.items[item] * 0.9
    def status(self):
        print("=" * 30)
        print(self.name)
        print("-" * 30)
        print(self.inventar)
        print("-" * 30)
        print(self.money)
    def ende(self):
        ausgabe = {"Name" : self.name, "Money" : self.money, "Inventar" : self.inventar}
        return ausgabe
class Account_laden:
    def __init__(self, laden):
        self.laden=laden
    def loadin(self):
        self.laden.append(f"{welcher}.json")

def loading():
    with open("Acounts.json", "r") as c:
        dat = json.load(c)
    loading = input("Willst du einen spielstand laden")
    if loading == "j":
        try:
            with open ("Acounts.json", "r") as c:
                dat = json.load(c)
                welcher = input(f"Wechlen spiel stand willst du laden {dat}")
            try:
                with open(welcher, "r") as f:
                    data = json.load(f)
                    print(data)
                    Player = Account(data["Name"], data["Money"], data["Inventar"])
                    Ich.laden.append(welcher)
                    return Player, welcher
            except FileNotFoundError or json.JSONDecodeError:
                print("Die Datei gibt es nicht")
                username = input("dein Name: ")
                Player = Account(username, 100, [])
                welcher = input("Wie soll deine datei heißen")
                Ich.laden.append(welcher)
                return Player, welcher
        except FileNotFoundError or json.JSONDecodeError:
            print("Die Datei gibt es nicht")
            username = input("dein Name: ")
            Player = Account(username, 100, [])
            welcher = input("Wie soll deine datei heißen")
            Ich.laden.append(welcher)
            return Player, welcher
    elif loading == "n":
        username = input("dein Name: ")
        Player = Account(username, 100, [])
        welcher = input("Wie soll deine datei heißen")
        Ich.laden.append(welcher)
        return Player, welcher
    else:
        print("jetzt erstellst du enen neuen")
        username = input("dein Name: ")
        Player = Account(username, 100, [])
        welcher = input("Wie soll deine datei heißen")
        Ich.laden.append(welcher)
        return Player, welcher

Ich=Account_laden([])
Player, welcher = loading()
while True:
    print("Was willst du machen | kaufen | verkaufen | status | ausgeben |")
    auswahl = input("").lower()
    if auswahl == "kaufen":
        print("welches Item willst du kaufen | star : 50 | shell : 30 | block : 10 |")
        was = input("").lower()
        Player.einkaufen(was)
    elif auswahl == "verkaufen":
        print(f"welches Item willst du verkaufen | star : {Player.items['star'] * 0.9} | shell : {Player.items['shell'] * 0.9} | block : {Player.items['block'] * 0.9} |")
        was = input("").lower()
        Player.verkaufen(was)
    elif auswahl == "status":
        Player.status()
    elif auswahl == "ausgeben":

        Player.ende()
        Ich.loadin()
        with open(f"{welcher}.json", "w") as datei:
            json.dump(Player.ende(), datei)
        with open("Acounts.json", "w") as datei:
            json.dump(Ich.laden, datei)
            print("Dein Acount wurde erfolgreich ausgegeben")
            break
    else:
        print("Die Auswahl gibt es nicht")
