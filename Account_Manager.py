import json
import os.path

class Account:
    def __init__(self, name, money, inventory):
        self.name = name
        self.inventory = inventory
        self.money = money
        self.items = {
            "star": 50,
            "shell": 30,
            "block": 10
        }

    def buy(self, item):
        if item not in self.items:
            print("We do not have this item in stock.")
            return
        elif self.items[item] > self.money:
            print("You don't have enough coins for this item.")
            return
        elif len(self.inventory) == 5:
            print(f"Inventory full! {len(self.inventory)}/5 slots used.")
        else:
            self.inventory.append(item)
            self.money -= self.items[item]
            print(f"Item [{item}] bought successfully.")

    def sell(self, item):
        if item not in self.inventory:
            print("You cannot sell what you don't have.")
        else:
            self.inventory.remove(item)
            self.money += self.items[item] * 0.9
            print(f"Item [{item}] sold successfully.")

    def status(self):
        print("=" * 30)
        print(f"Account: {self.name}")
        print("-" * 30)
        print(f"Inventory: {self.inventory}")
        print("-" * 30)
        print(f"Balance: {self.money}")

    def get_data(self):
        output = {"Name": self.name, "Money": self.money, "Inventory": self.inventory}
        return output

class AccountManager:
    def __init__(self, accounts_list):
        self.accounts_list = accounts_list
    
    def add_save(self, filename):
        self.accounts_list.append(f"{filename}.json")

def start_new():
    print("File not found.")
    username = input("Let's start fresh. Enter your name: ")
    player = Account(username, 100, [])
    filename = input("What should your save file be named? ")
    manager.accounts_list.append(filename)
    return player, filename

def loading():
    choice = input("Do you want to load a save game? (y/n): ").lower()
    if choice == "y":
        if os.path.exists("Accounts.json"):
            with open("Accounts.json", "r") as c:
                dat = json.load(c)
                filename = input(f"Which save do you want to load? {dat}: ")
            try:
                with open(filename, "r") as f:
                    data = json.load(f)
                    print("Data loaded successfully.")
                    player = Account(data["Name"], data["Money"], data["Inventory"])
                    manager.accounts_list.append(filename)
                    return player, filename
            except (FileNotFoundError, json.JSONDecodeError):
                return start_new()
        else:
            # Und hier beim Erstellen der Datei auch
            with open("Accounts.json", "w") as f:
                json.dump(manager.accounts_list, f)
                return start_new()
    else:
        username = input("Enter your name: ")
        player = Account(username, 100, [])
        filename = input("What should your save file be named? ")
        manager.accounts_list.append(filename)
        return player, filename

manager = AccountManager([])
player, filename = loading()

while True:
    print("\nActions: | buy | sell | status | save |")
    action = input("Choice: ").lower()
    
    if action == "buy":
        print("Items: | star: 50 | shell: 30 | block: 10 |")
        item = input("Buy what? ").lower()
        player.buy(item)
    elif action == "sell":
        print(f"Sell prices: | star: {player.items['star'] * 0.9} | shell: {player.items['shell'] * 0.9} | block: {player.items['block'] * 0.9} |")
        item = input("Sell what? ").lower()
        player.sell(item)
    elif action == "status":
        player.status()
    elif action == "save":
        player.get_data()
        manager.add_save(filename)
        with open(f"{filename}.json", "w") as f:
            json.dump(player.get_data(), f)
        with open("Accounts.json", "w") as f:
            json.dump(manager.accounts_list, f)
            print("Account saved and exported successfully.")
            break
    else:
        print("Invalid choice.")
