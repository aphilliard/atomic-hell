import random
import sys
import os
import math
import time

player_location = 0
game_won = False
combat_order = True
monsters = []
heroes = []
death_words = ["has died.", "has been reduced to a pile of ash!", "is utterly destroyed.", "has become a molten puddle of slag.", "is no more."]
melee_words = ["pounces on", "grapples", "kicks", "bites", "punches", "whallops", "whacks"]
ranged_words = ["shoots", "fires on", "unloads on", "takes aim at", "blasts"]
in_combat = False
random_monster_room = random.randrange(1,6)+2

def display_intro():
    print("You are an intrepid group of survivors, desperately")
    print("clinging to the charred scraps of a post-nuclear")
    print("wasteland.")
    print()
    print("Among your party are:")
    print("Primitive Brute: a mutated human with uncanny strength!")
    print("Scout: a nimble ranger armed with wits, moxie and a lethal crossbow!")
    print("Soldier: a hardended veteran of World War 3.")
    print()
    print("Desperate for food, ammo, or any supplies")
    print("you might find, you have found your way into a crumbling")
    print("ruin.")
    print()
    print("But as you enter, the entrance behind you caves")
    print("in with a crash! There's only one way out now:")
    print("straight ahead! But what dangers may lurk in...")
    print()
    waitforread = input("(press any key)")
    os.system("clear")
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print()
    print("     \u001b[41m...ATOMIC HELL!?\u001b[0m")

def display_monster_description():
    print("You see three frightening forms:")
    print()
    print("An Irradiated Zombie!")
    print("'It no eat my brains!' growls Primitive Brute.")
    print("A Mutant Raccoon!")
    print("'It's a crafty one!' warns Scout.")
    print("A Brain Slug!")
    print("'Don't let it slither its way into your ear!' cries Soldier.")

def determine_turn():
    whoseTurn = random.choice([True, False])
    if whoseTurn == True:
        #print('Player goes first\033[00m')
        combat_order = True
    else:
        #print('Computer goes first\033[00m')
        combat_order = False
    return combat_order

# Create rooms
class room():
    def __init__(self, number, description):
        self.number = number
        self.description = description


def print_rooms():
	for i in range(len(map_rooms)):
		print(map_rooms[i].number)	

map_rooms = [
	room(1, "An empty and nondescript entryway to the ruin."),
	room(2, "A garbage-strewn corridor."),
    room(3, "A foul-smelling hall filled with ankle-deep water."),
    room(4, "The walls here are covered in obscene grafitti."),
    room(5, "Plants have completely taken over this room."),
    room(6, "Dry bones litter the floor here."),
   	room(7, "Rusty cans and refuse are everywhere!"),
   	room(8, "You can see a faint glow in the room to the south."),
   	room(9, "At long last, a way out!")
]

def display_monsters():
    for i in range(len(monsters)):
        print(f"{i} {monsters[i].name} health:{monsters[i].hp} offense:{monsters[i].atk} defense:{monsters[i].ac}")


def display_heroes():
    for i in range(len(heroes)):
        print(f"{i} {heroes[i].name} health:{heroes[i].hp} offense:{heroes[i].atk} defense:{heroes[i].ac}")
            

def roll(modifier):
    return random.randrange(1,20) + modifier

# make a class for generic creatures including both monsters and heroes
class creature():
    def __init__(self, name, ct, atk, ac, hp):
        self.name = name
        self.creatureType = ct 
        self.atk = atk
        self.ac = ac
        self.hp = hp    

    def get_name(self):
        return self.name

# make a list of the creatures' traits: name, ct, atk, ac, hp
creatures = [
            creature('Irradiated Zombie', 'monster', 20, 10, 50),
            creature('Brain Slug', 'monster', 15, 20, 40),
            creature('Mutant Raccoon', 'monster', 10, 25, 30),
            creature('Primitive Brute', 'hero', 20, 10, 50),
            creature('Scout', 'hero', 15, 20, 40),
            creature('Soldier', 'hero', 10, 25, 30)
            ]

# divide creatures into monsters...
for i in range(len(creatures)):
    if creatures[i].creatureType == 'monster':
        monsters.append(creatures[i])
# ...and heroes        
    elif creatures[i].creatureType == 'hero':
        heroes.append(creatures[i])

def room_description():
    print(map_rooms[player_location].description)

def encounter():
    global combat_order
    determine_turn()
    in_combat = True
    display_monster_description()
    while in_combat and monsters:
        while combat_order:

            # get player's choices
            print("\u001b[34;1mYour turn.\n")
            print("These are your targets: \n")
            display_monsters()
            
            # who will player target
            player_target_choice = int(input("Choose target: \n"))
            print(f"You chose to attack {monsters[player_target_choice].name}\n")
                
            # which hero will do the attacking?
            print("These are your heroes: \n")
            display_heroes()
            print(f"Who will attack {monsters[player_target_choice].name}?\n")
            player_character_choice = int(input("Choose attacker: \n"))
            print(f"{heroes[player_character_choice].name} will attack {monsters[player_target_choice].name}.\n")

            # hero kills monster
            tohit = roll(heroes[player_character_choice].atk)
            print(f"{heroes[player_character_choice].name} rolls a {tohit} against {monsters[player_target_choice].name}'s defense score of {monsters[player_target_choice].ac}.\n")
            if tohit > monsters[player_target_choice].ac:
                # print("Hit!")
                if heroes[player_character_choice].name == "Primitive Brute":
                    print(f"{heroes[player_character_choice].name} {random.choice(melee_words)} {monsters[player_target_choice].name}!")
                else:
                    print(f"{heroes[player_character_choice].name} {random.choice(ranged_words)} {monsters[player_target_choice].name}!")
                damageroll = int(random.randrange(1, tohit*2))
                print(f"{heroes[player_character_choice].name} does {damageroll} damage to {monsters[player_target_choice].name}!")
                monsters[player_target_choice].hp = monsters[player_target_choice].hp - damageroll
                if monsters[player_target_choice].hp <= 0:
                    print(f"{heroes[player_character_choice].name} kills {monsters[player_target_choice].name}!\n")
                    print(monsters[player_target_choice].name, random.choice(death_words))
                    monsters.remove(monsters[player_target_choice])
            else:
                print("Miss!")         
            
            # check to see if monsters list is empty
            if not monsters:
                print("Your stalwart band has defeated the loathsome creatures!\033[00m")
                in_combat = False
                break

            # give the player an update on remaining monsters
            print("These monsters remain:")
            display_monsters()
            combat_order = False

        # Computer's turn
        while combat_order == False:
            time.sleep(2)
            print("-------------------------------------")
            print("\n\033[91m\nComputer turn")
            print("Computer has these monsters:\n")
            display_monsters()
            print()
            monster_actor = random.randrange(len(monsters))
            print(f"Computer chooses {monsters[monster_actor].name} to act.\n")
            waitforread = input("(press any key)")
            monster_target = random.randrange(len(heroes))
            print("Computer can choose to target one of these heroes:")
            display_heroes()
            print(f"Computer will target {heroes[monster_target].name}.\n")
            waitforread = input("(press any key)")
            tohit = roll(monsters[monster_actor].atk)
            print(f"{monsters[monster_actor].name} rolls a {tohit} against {heroes[monster_target].name}'s defense score of {heroes[monster_target].ac}")
            if tohit > heroes[monster_target].ac:
                if monsters[monster_actor].name == "Brain Slug" or monsters[monster_actor].name == "Irradiated Zombie":
                    print(f"{monsters[monster_actor].name} {random.choice(melee_words)} {heroes[monster_target].name}!")
                else:
                    print(f"{monsters[monster_actor].name} {random.choice(ranged_words)} {heroes[monster_target].name}!")
                damageroll = int(random.randrange(1, tohit*2)/3)
                print(f"{monsters[monster_actor].name} does {damageroll} damage to {heroes[monster_target].name}!")
                heroes[monster_target].hp = heroes[monster_target].hp - damageroll
                if heroes[monster_target].hp <= 0:
                    print(f"{monsters[monster_actor].name} kills {heroes[monster_target].name}!\n")
                    print(heroes[monster_target].name, random.choice(death_words))
                    heroes.remove(heroes[monster_target])
            else:
                print("Miss!")
            waitforread = input("(press any key)")

            # remove the dead hero from the heroes list            
            print("These heroes remain:")
            display_heroes()
                    
            # check to see if all heroes are dead
            if not heroes:
                print("Your party has fallen prey to the horrors of ATOMIC HELL!\033[00m")
                raise SystemExit
            combat_order = True    

def move_player_south():
    global player_location
    player_location += 1
    if player_location >= 8:
        room_description()
        print("You've escaped!")
        raise SystemExit
    if player_location == random_monster_room:
        encounter()
    return player_location

def move_player_north():
    global player_location
    player_location -= 1
    if player_location <= -1:
    	player_location = 0
    	print("You can't go any farther north.")
		
def handle_player_input(player_input):
    global player_location
    if player_input == "q":
        print("Bye!")
        raise SystemExit		
    elif player_input == "map":
    	print_rooms()
    elif player_input == "s":
    	move_player_south()
    elif player_input == "n":
    	move_player_north()
    else:
    	print("Come again?")			
        
display_intro()
while not game_won:
    print("\u001b[46mROOM:", map_rooms[player_location].number,"\u001b[0m")
    room_description()
    request = input("\u001b[33;1mCOMMANDS: 'q'uit, move 's'outh or 'n'orth?\u001b[0m")
    handle_player_input(request)