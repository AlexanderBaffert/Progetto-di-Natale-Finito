#Progetto di Natale 2023 - Dark Souls 3 remake -
#Baffert,Gibertini e Lupascu
import random
import time
import sys 
from PIL import Image
import climage
import os
import json
import colored

#player classes and stats
# Define the initial stats for each class
class Player:
    def __init__(self,name:str,gender:str,age:int) -> None:
        self.name=name
        self.gender=gender
        self.age=age
        self.nemico=None
        self.armor = []
        self.weapon = None

    def __str__(self) -> str:
        return f"Ciao! Sono {self.name}, il mio genere e' {self.gender} e ho {self.age} anno/i."

    # def add_item(self,item:'Item')->None:
    #     self.inventory.append(item)
class Guerriero(Player):
    def __init__(self, name: str, gender: str, age: int) -> None:
        super().__init__(name, gender, age)
        
        self.vigor=15
        self.vitality=15
        self.strength=15
        self.dexterity=10
        self.faith=5
        self.max_hp = 1500
        self.hp=1500
        self.attack=125
        self.defence=180
        self.dodging = False
        self.defending = False
    def level_vigor(self)->None:
        self.vigor=self.vigor+1
    def level_vitality(self)->None:
        self.vitality=self.vitality+1
    def level_strength(self)->None:
        self.strength=self.strength+1
    def level_dexterity(self)->None:
        self.dexterity=self.dexterity+1

    def level_faith(self)->None:
        self.faith=self.faith+1

    def Attack(self, nemico):
        damage = self.attack * (self.dexterity / 10)
        print(f"{self.name} dealt {damage} damage to {nemico.type}")
        nemico.hp -= damage
        self.dodging = False
        self.defending = False

    def Defence(self):
        print(f"You defence yourself.")
        self.defending = True
        self.dodging = False
    def Dodge(self):
        dodge_chance = random.randint(1, 100)
        if dodge_chance <= 25:
            self.hp = min(self.max_hp, self.hp + 100)
            print(f"{self.name} dodged the attack and healed 100 HP.")
        else:
            print("Hai schivato l'attacco.")
        self.dodging = True
        self.defending = False
        return self.hp
    def Heal(self):
        self.hp = min(self.max_hp, self.hp + 250)
        self.dodging = False
        self.defending = False
        return self.hp
class Chierico(Player):
    def __init__(self, name: str, gender: str, age: int) -> None:
        super().__init__(name, gender, age)
        self.vigor=12
        self.vitality=7
        self.strength=12
        self.dexterity=8
        self.faith=16
        self.max_hp = 1456
        self.hp=1456
        self.attack=77
        self.defence=144
        self.dodging = False
        self.defending = False
    def level_vigor(self)->None:
        self.vigor=self.vigor+1
    def level_vitality(self)->None:
        self.vitality=self.vitality+1
    def level_strength(self)->None:
        self.strength=self.strength+1
    def level_dexterity(self)->None:
        self.dexterity=self.dexterity+1
    def level_faith(self)->None:
        self.vigor=self.faith+1
    def Attack(self, nemico):
        damage = self.attack * (self.dexterity / 10 * (self.faith / 10))
        print(f"{self.name} dealt {damage} damage to {nemico.type}")
        nemico.hp -= damage
        self.dodging = False
        self.defending = False
    def Defence(self):
        print(f"You defence yourself.")
        self.defending = True
        self.dodging = False
    def Dodge(self):
        dodge_chance = random.randint(1, 100)
        if dodge_chance <= 25:
            self.hp = min(self.max_hp, self.hp + 100)
            print(f"{self.name} dodged the attack and healed 100 HP.")
        else:
            print("Hai schivato l'attacco.")
        self.dodging = True
        self.defending = False
        return self.hp
    def Heal(self):
        self.hp = min(self.max_hp, self.hp + 250)
        self.dodging = False
        self.defending = False
        return self.hp
class Mercenario(Player):
    def __init__(self, name: str, gender: str, age: int) -> None:
        super().__init__(name, gender, age)
        self.vigor=10
        self.vitality=10
        self.strength=10
        self.dexterity=15
        self.faith=10
        self.max_hp = 1403
        self.hp=1403
        self.attack=161.5
        self.defence=166
        self.dodging = False
        self.defending = False
    def level_vigor(self)->None:
        self.vigor=self.vigor+1
    def level_vitality(self)->None:
        self.vitality=self.vitality+1
    def level_strength(self)->None:
        self.strength=self.strength+1
    def level_dexterity(self)->None:
        self.dexterity=self.dexterity+1
    def level_faith(self)->None:
        self.vigor=self.faith+1
    def Attack(self, nemico):
        damage = self.attack * 2 * (self.dexterity / 10 )
        print(f"{self.name} dealt {damage} damage to {nemico.type}")
        nemico.hp -= damage
        self.dodging = False
        self.defending = False
    def Defence(self):
        print(f"You defence yourself.")
        self.defending = True
        self.dodging = False
    def Dodge(self):
        dodge_chance = random.randint(1, 100)
        if dodge_chance <= 25:
            self.hp = min(self.max_hp, self.hp + 100)
            print(f"{self.name} dodged the attack and healed 100 HP.")
        else:
            print("Hai schivato l'attacco.")
        self.dodging = True
        self.defending = False
        return self.hp
    def Heal(self):
        self.hp = min(self.max_hp, self.hp + 250)
        self.dodging = False
        self.defending = False
        return self.hp
class Assassino(Player):
    def __init__(self, name: str, gender: str, age: int) -> None:
        super().__init__(name, gender, age)
        self.vigor=10
        self.vitality=10
        self.strength=10
        self.dexterity=14
        self.faith=9
        self.max_hp = 1403
        self.hp=1403
        self.attack=140
        self.defence=94
        self.dodging = False
        self.defending = False
    def level_vigor(self)->None:
        self.vigor=self.vigor+1
    def level_vitality(self)->None:
        self.vitality=self.vitality+1
    def level_strength(self)->None:
        self.strength=self.strength+1
    def level_dexterity(self)->None:
        self.dexterity=self.dexterity+1
    def level_faith(self)->None:
        self.vigor=self.faith+1
    def Attack(self, nemico):
        damage = self.attack * (self.dexterity / 10 * (self.faith / 10))
        print(f"{self.name} dealt {damage} damage to {nemico.type}")
        nemico.hp -= damage
        self.dodging = False
        self.defending = False
    def Defence(self):
        print(f"You defence yourself.")
        self.defending = True
        self.dodging = False
    def Dodge(self):
        dodge_chance = random.randint(1, 100)
        if dodge_chance <= 25:
            self.hp = min(self.max_hp, self.hp + 100)
            print(f"{self.name} dodged the attack and healed 100 HP.")
        else:
            print("Hai schivato l'attacco.")
        self.dodging = True
        self.defending = False
        return self.hp
    def Heal(self):
        self.hp = min(self.max_hp, self.hp + 250)
        self.dodging = False
        self.defending = False
        return self.hp
class Enemy:
    def __init__(self,type:str,hp:int,attack:int,giocatore:Player) -> None:
        self.type=type
        self.hp=hp
        self.attack=attack
        self.giocatore=giocatore

    def Attack(self, player):
        if player.dodging and random.randint(1, 100) <= 80:  # 80% chance to miss if the player is dodging
            print(f"{self.type} missed their attack.")
            return
        if player.defending:
            damage = self.attack - (player.defence/10)
        else:
            damage = self.attack
        damage = max(0, damage)  # Ensure damage is not less than 0
        player.hp -= damage  # The player's HP decreases by the damage
        print(f"{self.type} dealt {damage} damage to {player.name}")
class Item:
    def __init__(self,type:str,attack:int,defence:int) -> None:
        self.type=type
        self.attack=attack
        self.defence=defence
    def __str__(self) -> str:
        return f"Item(type:{self.type}, attack:{self.attack}, defence:{self.defence})"
def award_souls(base_souls):
    # Modify the number of souls gained based on the player's class
    if isinstance(player, Guerriero):
        souls_gained = base_souls * 1.2  # Guerriero gains 20% more souls
    elif isinstance(player, Chierico):
        souls_gained = base_souls * 1.1  # Chierico gains 10% more souls
    elif isinstance(player, Mercenario):
        souls_gained = base_souls  # Mercenario gains the base number of souls
    elif isinstance(player, Assassino):
        souls_gained = base_souls * 0.9  # Assassino gains 10% less souls

    # Update the player's souls
    data['souls'] += souls_gained
def fight(player, enemy):
    while player.hp > 0 and enemy.hp > 0:
        print(f"{player.name} HP: {player.hp}")
        print(f"{enemy.type} HP: {enemy.hp}")
        action = input("Choose an action: a = Attack, p = Defence, h = Heal, d = Dodge: ")

        if action == "a":
            player.Attack(nemico=enemy)
        elif action == "p":
            player.Defence()
        elif action == "h":
            player.Heal()
        elif action == "d":
            print(player.Dodge())
        else:
            print("Invalid action. Please choose a, p, h, or d.")

        if enemy.hp > 0:
            enemy.Attack(player)

        if player.hp <= 0:
            print(f"{player.name} lost the fight!")
            print(f"{colored.fg('red')}Maybe next time{colored.attr('reset')}")

            exit()
        if enemy.hp <= 0:
            print(f"{player.name} won the fight!")
def choose_class(class_name, name, gender, age):
    global player
    while True:
        # Define the classes
        classes = {
            'w': Guerriero,
            'c': Chierico,
            'm': Mercenario,
            'a': Assassino,
        }

        # Check if the class_name is valid
        if class_name not in classes:
            print(f"Invalid class name: {class_name}")
        if class_name in classes:
            # Create a player of the chosen class
            player_class = classes[class_name]
            player = player_class(name, gender, age)

            print(f"You have chosen the {class_name} class.")
            return player
#upgrade sistem
# Initialize player's stats and upgrade costs

def firekeeper():
    read_and_print('firekeeper_logs.txt')

    while data['souls'] >= min(stat['upgrade_cost'] for stat in data['stats'].values()):
        print("Choose your stat to level up")
        print("1. Vigor")
        print("2. Attunement")
        print("3. Endurance")
        print("4. Vitality")
        print("5. Strength")
        print("6. Dexterity")
        print("7. Intelligence")
        print("8. Faith")
        print("9. Luck")
        choice=input("Choose your stat: ")

        if isinstance(player, Guerriero) and choice in ["1", "5"]:
            print(f"You have chosen {get_stat_name(choice)}")
            upgrade_stat(get_stat_name(choice))
        elif isinstance(player, Chierico) and choice in ["2", "8"]:
            print(f"You have chosen {get_stat_name(choice)}")
            upgrade_stat(get_stat_name(choice))
        elif isinstance(player, Mercenario) and choice in ["3", "6"]:
            print(f"You have chosen {get_stat_name(choice)}")
            upgrade_stat(get_stat_name(choice))
        elif isinstance(player, Assassino) and choice in ["4", "7", "9"]:
            print(f"You have chosen {get_stat_name(choice)}")
            upgrade_stat(get_stat_name(choice))
        else:
            print("You have chosen a stat that your class cannot upgrade")
    print("You don't have enough souls to upgrade any more stats.")
def get_stat_name(choice):
    return {
        "1": "Vigor",
        "2": "Attunement",
        "3": "Endurance",
        "4": "Vitality",
        "5": "Strength",
        "6": "Dexterity",
        "7": "Intelligence",
        "8": "Faith",
        "9": "Luck"
    }[choice]
def upgrade_stat(stat_name):
    stat = data['stats'][stat_name]

    if data['souls'] >= stat['upgrade_cost']:
        # Deduct the cost from the player's souls
        data['souls'] -= stat['upgrade_cost']

        # Increase the stat value
        stat['value'] += 1

        # Increase the upgrade cost
        stat['upgrade_cost'] *= 1.1  # Increase cost by 10%

        print(f"You have upgraded {stat_name} to {stat['value']}.")
    else:
        print(f"You don't have enough souls to upgrade {stat_name}.")
#save function
SAVE_FILE_PATH = 'save_file.json'
# Define game_data
game_data = {
    'player_position': [0, 0],
    'inventory': ['sword', 'shield'],
    # Add more game state data as needed
}
def save_game(game_data):
    with open(SAVE_FILE_PATH, 'w') as save_file:
        json.dump(game_data, save_file)
    print("Your game has been saved.")
def load_game():
    try:
        with open(SAVE_FILE_PATH, 'r') as save_file:
            game_data = json.load(save_file)
        print("Game loaded successfully.")
        return game_data
    except FileNotFoundError:
        print(f"No saved game found.")
        return None
def start_game():
    if os.path.exists(SAVE_FILE_PATH):
        load = input("A saved game is available. Would you like to load it? (yes/no): ")
        if load.lower() == 'yes':
            game_data = load_game()
            if game_data is not None:
                # Continue the game with the loaded data
                pass
            else:
                # Start a new game
                pass
    else:
        # Start a new game
        pass
#external file with the text
def print_slow(str):
    for char in str:
        time.sleep(0.01)  # Adjust this value to change the speed of printing
        print(char, end='', flush=True)
def read_and_print(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print_slow(content)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
#countdown function
class CountdownTimer:
    def __init__(self):
        self.stop_countdown = False

    def countdown_timer(self):
        for remaining in range(5, 0, -1):
            sys.stdout.write(f"\rYou have {remaining} seconds to decide your move: ")
            sys.stdout.flush()
            
            if self.stop_countdown:
                break
        else:
            sys.stdout.write("\rYou have 0 seconds to decide your move.                                  \n")
            sys.stdout.flush()

    def stop(self):
        self.stop_countdown = True
data = {
    'souls': 0,
    'inventory': {        
        'items': [None] * 100,  # 100 general inventory slots
    }
}
def choice_2_function():
    print("You have chosen to leave the bonfire")
    read_and_print('progress_3.txt')
    item = 'small lothric banner'
    data['inventory']['items'][0] = item
    print(f"You have obtained {item}.")        
    Vordt=Enemy("Vordt",1328,190,player)
    fight(player,Vordt)
    award_souls(3000)
    #boss soul transposition
    print(f'Now you have {data["souls"]} souls.')
    read_and_print('progress_4.txt')
    mini_boss=Enemy("mini_boss",590,120,player)
    fight(player,mini_boss)
    award_souls(1500)
    #mini boss soul transposition
    print(f'Now you have {data["souls"]} souls.')
    read_and_print('progress_5.txt')
    Abyss_Watchers=Enemy("Abyss Watchers",1548,250,player)
    fight(player,Abyss_Watchers)
    award_souls(18000)
    #boss soul transposition
    print(f'Now you have {data["souls"]} souls.')
    read_and_print('progress_6.txt')
    bridge=input("You have reached the bridge, do you want to cross it?(yes/no): ")
    if bridge=="yes":
        print("The bridge collapsed, you died")
        exit()
    elif bridge=="no":
        print("You have chosen to not cross the bridge")
        read_and_print('progress_6_5.txt')
        High_Lord_Wolnir=Enemy("High Lord Wolnir",15041,50,player)
        fight(player,High_Lord_Wolnir)
        #boss soul transposition
        award_souls(22000)
        print(f'Now you have {data["souls"]} souls.')
        read_and_print('progress_7.txt')
        #mini boss fight --> Giant crocodile
        Giant_Crocodile=Enemy("Giant Crocodile",2495,190,player)
        fight(player,Giant_Crocodile)
        award_souls(1500)
        #mini boss soul transposition
        print(f'Now you have {data["souls"]} souls.')
        read_and_print('progress_8.txt')
        #boss fight 5 --> Aldrich Devourer of Gods
        Aldrich_Devourer_of_Gods=Enemy("Aldrich Devourer of Gods",4727,480,player)
        fight(player,Aldrich_Devourer_of_Gods)
        award_souls(50000)
        #boss soul transposition
        print(f'Now you have {data["souls"]} souls.')
        read_and_print('progress_9.txt') 
        #boss fight 6 --> Yhorm the Giant
        Yhorm_the_Giant=Enemy("Yhorm the Giant",27822,350,player)
        fight(player,Yhorm_the_Giant)
        award_souls(36000)
        #boss soul transposition
        print(f'Now you have {data["souls"]} souls.')
        read_and_print('progress_10.txt')
        #boss fight 7 --> Lothric Younger Prince
        Lothric_Younger_Prince=Enemy("Lothric Younger Prince",10839,460,player)
        fight(player,Lothric_Younger_Prince)
        award_souls(85000)
        #boss soul transposition
        print(f'Now you have {data["souls"]} souls.')
        read_and_print('progress_11.txt')
        #final boss fight --> Soul of Cinder
        Soul_of_Cinder=Enemy("Soul of Cinder",13000,500,player)
        fight(player,Soul_of_Cinder)
        award_souls(100000)
        #boss soul transposition
        print(f'Now you have {data["souls"]} souls.')
        read_and_print("ending.txt")
#main
#start of the game
# start_game()
        #player creation
        #colored text
print(f"{colored.fg('red')}GAME DESIGNED BY Baffert,Gibertini,Lupascu{colored.attr('reset')}")
print(f"{colored.fg('red')}Welcome to Dark Souls 3 Remake{colored.attr('reset')}")
print(f"{colored.fg('red')}Good Luck{colored.attr('reset')}")
read_and_print('logs.txt')
print("Welcome to the game, choose your character")
name=input("Choose your name: ")
gender=input("Choose your gender, m/f: ")
age=input("Choose your age: ")
class_p=input("Choose your class(w=Warrior,c=Cleric,a=Assassin,m=Mercenary): ")
choose_class(class_p, name, gender, age)
print("Choose your burial gift")
#preview of the burial gifts
print("1. Life Ring")
print("2. Divine Blessing")
print("3. Hidden Blessing")
print("4. Black Firebomb")
print("5. Fire Gem")
print("6. Sovereignless Soul")
print("7. Rusted Gold Coin")
print("8. Cracked Red Eye Orb")
print("9. Young White Branch")
print("10. None")
#burial gift choice
gift=input("Choose your burial gift: ")
if gift=="1":
    gift="Life Ring"
    print("You have chosen the Life Ring")
elif gift=="2":
    gift="Divine Blessing"
    print("You have chosen the Divine Blessing")
elif gift=="3":
    gift="Hidden Blessing"
    print("You have chosen the Hidden Blessing")
elif gift=="4":
    gift="Black Firebomb"
    print("You have chosen the Black Firebomb")
elif gift=="5":
    gift="Fire Gem"
    print("You have chosen the Fire Gem")
elif gift=="6":
    gift="Sovereignless Soul"
    print("You have chosen the Sovereignless Soul")
elif gift=="7":
    gift="Rusted Gold Coin"
    print("You have chosen the Rusted Gold Coin")
elif gift=="8":
    gift="Cracked Red Eye Orb"
    print("You have chosen the Cracked Red Eye Orb")
elif gift=="9":
    gift="Young White Branch"
    print("You have chosen the Young White Branch")
elif gift=="10":
    gift="None"
    print("You have chosen the None")
else:
    gift="None"
    print("You have chosen the None")
read_and_print('dialogues.txt')
path=input("Choose your path, r/l:")
if path=="r":
    print("You have chosen the right path")
    read_and_print('right_path.txt')
    #save the game
    save_game(game_data)
    read_and_print('progress_1.txt')
    Gundyr=Enemy("Gundyr",1037,90,player)
    fight(player,Gundyr)
    print("|Heir of fire destroyed|")
    #boss drop
    drop = 'coiled sword'
    data['inventory']['items'][0] = drop
    #boss soul value
    award_souls(3000)
    #boss soul transposition
    print(f'Now you have {data["souls"]} souls.')
    read_and_print('progress_2.txt')
    data['inventory']['items'][0] = None
    print("You touch the bonfire")
    choice_2_function()
elif path=="l":
    print("You have chosen the left path")
    read_and_print('left_path.txt')
    #mini boss class call and fight   
    mini_boss=Enemy("mini_boss",590,35,player)
    fight(player,mini_boss)
    award_souls(1500)
    #mini boss soul transposition
    print(f'Now you have {data["souls"]} souls.')
    print("You go back and take the right path")
    read_and_print('right_path.txt')
    #save the game
    save_game(game_data)
    read_and_print('progress_1.txt')
    Gundyr=Enemy("Gundyr",1037,90,player)
    fight(player,Gundyr)
    print("|Heir of fire destroyed|")
    #boss drop
    drop = 'coiled sword'
    data['inventory']['items'][0] = drop
    #boss soul value
    award_souls(3000)
    #boss soul transposition
    print(f'Now you have {data["souls"]} souls.')
    read_and_print('progress_2.txt')
    data['inventory']['items'][0] = None
    print("You touch the bonfire")
    choice_2_function()