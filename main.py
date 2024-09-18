import random

# Define the Jedi class
class Jedi:
    def __init__(self, name, lightsaber_color, rank, health=100):
        self.name = name
        self.lightsaber_color = lightsaber_color
        self.rank = rank
        self.health = health

    def introduce(self):
        print(f"I am Jedi {self.name}, a {self.rank}. My lightsaber is {self.lightsaber_color}.")

    def lightsaber_attack(self, sith):
        damage = random.randint(10, 30)
        sith.health -= damage
        print(f"{self.name} attacks {sith.name} with a {self.lightsaber_color} lightsaber, dealing {damage} damage!")
        if sith.health <= 0:
            print(f"{sith.name} has been defeated!")
        else:
            print(f"{sith.name} has {sith.health} health remaining.")

    def use_force(self):
        print(f"{self.name} uses the Force to gain an advantage!")

# Define the Sith class
class Sith:
    def __init__(self, name, lightsaber_color, rank, health=100):
        self.name = name
        self.lightsaber_color = lightsaber_color
        self.rank = rank
        self.health = health

    def introduce(self):
        print(f"I am Sith {self.name}, a {self.rank}. My lightsaber is {self.lightsaber_color}.")

    def lightsaber_attack(self, jedi):
        damage = random.randint(10, 30)
        jedi.health -= damage
        print(f"{self.name} attacks {jedi.name} with a {self.lightsaber_color} lightsaber, dealing {damage} damage!")
        if jedi.health <= 0:
            print(f"{jedi.name} has been defeated!")
        else:
            print(f"{jedi.name} has {jedi.health} health remaining.")

    def use_force(self):
        print(f"{self.name} uses the Dark Side of the Force to gain an advantage!")

# Define the Adventure class for random encounters
class Adventure:
    def __init__(self, player_name):
        self.player_name = player_name

    def random_encounter(self):
        encounters = [
            "You found a Jedi temple!",
            "You encountered a Sith Lord!",
            "You found a holocron!",
            "You were ambushed by bounty hunters!"
        ]
        return random.choice(encounters)

# Function to handle a duel between Jedi and Sith
def start_duel(jedi, sith):
    print("\nA duel has begun!")
    while jedi.health > 0 and sith.health > 0:
        jedi.lightsaber_attack(sith)
        if sith.health > 0:
            sith.lightsaber_attack(jedi)
        if jedi.health <= 0:
            print(f"{jedi.name} has been defeated! The Sith reign supreme.")
        elif sith.health <= 0:
            print(f"{sith.name} has been defeated! The Jedi are victorious.")

# Main adventure loop
def start_adventure():
    print("Welcome to the Star Wars Adventure!")
    player_name = input("Enter your name, traveler: ")
    adventure = Adventure(player_name)

    # Create instances of Jedi and Sith
    jedi = Jedi("Obi-Wan Kenobi", "blue", "Master")
    sith = Sith("Darth Vader", "red", "Lord")

    while True:
        print("\nWhat would you like to do?")
        action = input("Explore / Duel / Quit: ").lower()

        if action == "explore":
            encounter = adventure.random_encounter()
            print(f"{player_name} explores the galaxy and: {encounter}")
            if "Jedi" in encounter:
                jedi.introduce()
            elif "Sith" in encounter:
                sith.introduce()

        elif action == "duel":
            start_duel(jedi, sith)

        elif action == "quit":
            print("May the Force be with you. Goodbye!")
            break

        else:
            print("Invalid action, try again.")

# Start the adventure
if __name__ == "__main__":
    start_adventure()
