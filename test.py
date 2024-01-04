import random, sys, threading, time
class Player:
    def __init__(self,name:str,gender:str,age:int) -> None:
        self.name=name
        self.gender=gender
        self.age=age
        self.inventory=[]
        self.nemico=None

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
        self.max_hp = 550
        self.hp=550
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
    def Dodge(self):
        dodge_chance = random.randint(1, 100)  # Generate a random number between 1 and 100
        if dodge_chance <= 25:  # 25% chance to heal
            self.hp = min(self.max_hp, self.hp + 100)  # Ensure HP does not exceed max_hp
            print(f"{self.name} dodged the attack and healed 100 HP.")        
        else:
            print("Hai schivato l'attacco.")
        self.dodging = True
        return self.hp
    def Heal(self):
        self.hp = min(self.max_hp, self.hp + 100)  # Ensure HP does not exceed max_hp
        return self.hp

class Chierico(Player):
    def __init__(self, name: str, gender: str, age: int) -> None:
        super().__init__(name, gender, age)
        self.vigor=12
        self.vitality=7
        self.strength=12
        self.dexterity=8
        self.faith=16
        self.max_hp = 454
        self.hp=454
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
    def Dodge(self):
        dodge_chance = random.randint(1, 100)
        if dodge_chance <= 25:
            self.hp = min(self.max_hp, self.hp + 100)
            print(f"{self.name} dodged the attack and healed 100 HP.")
        else:
            print("Hai schivato l'attacco.")
        self.dodging = True
        return self.hp
    def Heal(self):
        self.hp = min(self.max_hp, self.hp + 100)
        return self.hp
class Mercenario(Player):
    def __init__(self, name: str, gender: str, age: int) -> None:
        super().__init__(name, gender, age)
        self.vigor=10
        self.vitality=10
        self.strength=10
        self.dexterity=15
        self.faith=10
        self.max_hp = 403
        self.hp=403
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
        damage = self.attack * (self.dexterity / 10 * (self.faith / 10))
        print(f"{self.name} dealt {damage} damage to {nemico.type}")
        nemico.hp -= damage
        self.dodging = False
        self.defending = False
    def Defence(self):
        print(f"You defence yourself.")
        self.defending = True
    def Dodge(self):
        dodge_chance = random.randint(1, 100)
        if dodge_chance <= 25:
            self.hp = min(self.max_hp, self.hp + 100)
            print(f"{self.name} dodged the attack and healed 100 HP.")
        else:
            print("Hai schivato l'attacco.")
        self.dodging = True
        return self.hp
    def Heal(self):
        self.hp = min(self.max_hp, self.hp + 100)
        return self.hp
class Assassino(Player):
    def __init__(self, name: str, gender: str, age: int) -> None:
        super().__init__(name, gender, age)
        self.vigor=10
        self.vitality=10
        self.strength=10
        self.dexterity=14
        self.faith=9
        self.max_hp = 403
        self.hp=403
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
    def Attack(self, enemy):
        damage = self.strength + (self.dexterity / 10)
        if self.weapon:
            damage += self.weapon.attack
        enemy.hp -= damage
        print(f"{self.name} dealt {damage} damage to {enemy.name}")
        self.dodging = False 
        self.defending = False       
    def Defend(self, attack_damage):
        defense = self.vitality
        for armor_piece in self.armor:
            defense += armor_piece.defence * 0.1
        self.hp -= max(0, attack_damage - defense)
        print(f"{self.name} took {max(0, attack_damage - defense)} damage from the attack.")
        self.dodging = False
        self.defending = True
    def Dodge(self):
        dodge_chance = random.randint(1, 100)
        if dodge_chance <= 25:
            self.hp = min(self.max_hp, self.hp + 100)
            print(f"{self.name} dodged the attack and healed 100 HP.")
        else:
            print("Hai schivato l'attacco.")
        self.dodging = True
        return self.hp
    def Heal(self):
        self.hp = min(self.max_hp, self.hp + 100)
        return self.hp
class Enemy:
    def __init__(self,type:str,hp:int,attack:int,souls:int,giocatore:Player) -> None:
        self.type=type
        self.hp=hp
        self.attack=attack
        self.souls=souls
        self.giocatore=giocatore

    def Attack(self, player):
        if player.dodging and random.randint(1, 100) <= 80:  # 80% chance to miss if the player is dodging
            print(f"{self.type} missed their attack.")
            return
        if player.defending:
            damage = self.attack - player.defence
        else:
            damage = self.attack
        damage = max(0, damage)  # Ensure damage is not less than 0
        player.hp -= damage  # The player's HP decreases by the damage
        print(f"{self.type} dealt {damage} damage to {player.name}")
    
player = Assassino("John Doe", "Male", 30)  # Adjust the arguments as needed

# Create an Enemy instance
enemy = Enemy("MiniBoss", 1000, 250, 100, player)  # Adjust the arguments as needed
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
            sys.stdout.write("\rYou have 0 seconds to decide your move. Enemy will attack!                \n")
            sys.stdout.flush()

    def stop(self):
        self.stop_countdown = True
def fight(user, enemy):
    countdown_timer = CountdownTimer()

    while user.hp > 0 and enemy.hp > 0:
        print(f"{user.name} HP: {user.hp}")
        print(f"{enemy.type} HP: {enemy.hp}")

        countdown_timer.stop_countdown = False  # Reset the timer for each round
        countdown_thread = threading.Thread(target=countdown_timer.countdown_timer)
        countdown_thread.start()

        action = input("Choose an action: a = Attack, p = Defence, h = Heal, d = Dodge: ")

        countdown_timer.stop()

        if action == "a":
            user.Attack(enemy)
        elif action == "p":
            user.Defence()
        elif action == "h":
            user.Heal()
        elif action == "d":
            print(user.Dodge())
        else:
            print("Invalid action. Please choose a, p, h, or d. Enemy will attack!")

        if enemy.hp > 0:
            enemy.Attack(user)

        if user.hp <= 0:
            print(f"{user.name} lost the fight!")
            break
        if enemy.hp <= 0:
            print(f"{user.name} won the fight!")
            break
fight(player,enemy)