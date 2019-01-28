#Sci-fi turn-based combat simulator
import os
import math
import random
import time

from operator import itemgetter, attrgetter

global monters
monsters = []
global heroes
heroes = []

randword = ["is killed.", "has been slaughtered.", "is utterly destroyed.", "has been vanquished.", "has died.", "has been reduced to a puddle of gore."]
rangedword = ["blasts", "shoots", "fires at", "opens fire on"]
meleeword = ["punches", "whacks", "bites", "kicks", "grapples"]
dmgword = ["OUCH!", "DAMN!", "OOF!", "That\'s gotta hurt!", "FEEL THE PAIN!"]
lowword = ["Merely a flesh wound.", "Sad.", "Where'd you learn to fight?", "Grazed", "A glancing blow", "I\'ve had worse paper cuts"]

os.system('clear')
print('             \033[1;30;40mCan your intrepid adventurers survive...')
print('                         \033[1;31;40mATOMIC HELL ?!\033[0;37;40m')
print('__________________________________________________________________')
print('A turn-based combat simulator set in a post-apocalyptic wasteland.')
print()
print()
print('Your rag-tag group of survivors includes:')
print('\033[2;36;40mPrimitive Brute\033[0;37;40m: a mutant humanoid with superhuman strength!')
print('\033[2;36;40mScout\033[0;37;40m: a nimble ranger armed with a crossbow and dressed in leather.')
print('\033[2;36;40mSoldier\033[0;37;40m: a veteran equipped with a laser rifle and riot armor.')
print()
print()
print('You venture out into the unwelcoming wastes...')
waitfor = input('PRESS ENTER TO CONTINUE')
os.system('clear')
print('You find yourselves in the crumbling ruins of a once-great city')
print('desperately foraging for scraps on which to survive. Suddenly,')
print('you hear a disturbance behind you! Scout aims her flashlight,')
print('revealing a horrifying sight:')
print()
print('\033[2;32;40mAn Irradiated Zombie!\033[0;37;40m')
print('"It no eat my brain!" grumbles Primitive Brute.')
print('\033[2;32;40mA Mutant Raccoon!\033[0;37;40m')
print('"Its zipgun may look makeshift, but it can be lethal!" warns Scout.')
print('\033[2;32;40mA Brain Slug!\033[0;37;40m')
print('"Don\'t let it slither its way into your ear!" shouts Soldier.')
print()
print('Looks like we\'re in for a fight!')

def roll(modifier):
    return random.randrange(1,20) + modifier

class creature():
    def __init__(self,name, hp, ac, atk, dmg, ini, ct):
        self.name = name
        self.hp = hp
        self.ac = ac
        self.atk = atk
        self.dmg = dmg
        self.ini = ini
        self.creatureType = ct
        self.initiative = roll(ini)
        

    def get_name(self):
        return self.name

    def __repr__(self):
        return '\n{} Name:{} HP:{} Attack:{} Damage{}'.format(self.creatureType, self.name, self.hp, self.atk, self.dmg)

    def attack(self, defender):

        def roll_attack(self, defender):
            attack = roll(self.atk)
            print()
            if (self.name == 'Irradiated Zombie' or self.name == 'Brain Slug' or self.name == 'Primitive Brute'):
                print(self.name, random.choice(meleeword), defender.name)
            else:
                print(self.name, random.choice(rangedword), defender.name)
            print(self.name, "rolls", attack, "against a defense score of", defender.ac)
            if attack >= defender.ac:
                print('That\'s a hit!\033[1;33;40m')
                return True
            else:
                print("\033[1;30;40mMiss.\033[0;37;40m")
                return False

        def roll_damage(self, defender):
            damage = random.randrange(1,self.dmg)
            print(self.name, "deals", damage, "damage!\033[0;37;40m")
            if (self.name == 'Irradiated Zombie' or self.name == 'Primitive Brute') and damage > 20:
                print(f'\033[1;31;40m{random.choice(dmgword)}\033[0;37;40m')
            elif (self.name == 'Mutant Raccoon' or self.name == 'Scout') and damage > 12:
                print(f'\033[1;31;40m{random.choice(dmgword)}\033[0;37;40m')
            elif (self.name == 'Soldier' or self.name == 'Mutant Raccoon') and damage > 16:
                print(f'\033[1;31;40m{random.choice(dmgword)}\033[0;37;40m')
            elif damage < 4:
                print(f'\033[1;32;40m{random.choice(lowword)}\033[0;37;40m')        

            defender.hp = defender.hp - damage
            death_check(defender)

        def death_check(defender):
            if defender.hp <= 0:
                if defender.creatureType == "monster":
                    global monsters
                    print(defender.get_name(), random.choice(randword))
                    global teamMonsters
                    teamMonsters = teamMonsters - 1
                    monsters.remove(defender)
                else:
                    global heroes
                    print(defender.get_name(), random.choice(randword))
                    global teamHeroes
                    teamHeroes = teamHeroes - 1
                    heroes.remove(defender)
                creatures.remove(defender)
                print()

        if roll_attack(self, defender) == True:
            roll_damage(self, defender)

# creature list: name, hp, ac, atk, dmg, ini, ct
creatures = [
            creature('Irradiated Zombie', 45, 15, 10, 25, 1, 'monster'),
            creature('Mutant Raccoon', 25, 20, 20, 15, 1, 'monster'),
            creature('Brain Slug', 35, 25, 15, 20, 1, 'monster'),
            creature('Primitive Brute', 45, 15, 10, 25, 1, 'hero'),
            creature('Scout', 25, 20, 20, 15, 1, 'hero'),
            creature('Soldier', 35, 25, 15, 20, 1, 'hero')
            ]
    
for i in range(len(creatures)):
    if creatures[i].creatureType == 'monster':
        monsters.append(creatures[i])
        
    elif creatures[i].creatureType == 'hero':
        heroes.append(creatures[i])

teamMonsters = len(monsters)
teamHeroes = len(heroes)
turn = 0

# combat loop
while len(monsters) > 0 and len(heroes) > 0:
    waitfor = input('\nPRESS ENTER TO CONTINUE\n')
    print('------------------------------------------')
    print('The combatants:')
    #print('Monsters:')
    for i in range(len(monsters)):
        # print('\033[2;32;40m')
        print('\033[2;32;40m\u25B6', monsters[i].name, "\033[2;33;40mhp:", monsters[i].hp, "\033[0;37;40mdefense:", monsters[i].ac, "offense:", monsters[i].atk, "damage:", monsters[i].dmg)
    #print('\033[2;36;40mHeroes:\033[0;37;40m')
    for i in range(len(heroes)):
        # print('\033[2;36;40m')
        print('\033[2;36;40m\u25B9', heroes[i].name, "\033[2;33;40mhp:", heroes[i].hp, "\033[0;37;40mdefense:", heroes[i].ac, "offense:", heroes[i].atk, "damage:", heroes[i].dmg) 
    turn = turn + 1
    print("Turn:", turn)
    waitfor = input('\nPRESS ENTER TO BEGIN TURN')
    
    #determine combat initiative
    for i in range(len(creatures)):
        creatures[i].initiative = roll(creatures[i].ini)
    combatSequence = sorted(creatures, key = attrgetter('initiative'), reverse = True)

    print('\033[2;32;40mInitiative rolls:\033[0;37;40m')
    for p in range(len(combatSequence)):
        if creatures[p].hp > 0:
            print (creatures[p].name, creatures[p].initiative)
    print()

    for i in range(len(combatSequence)):
        if combatSequence[i].hp > 0:
            if combatSequence[i].creatureType == 'hero':
                try:
                    combatSequence[i].attack(random.choice(monsters))
                except:
                    break
            elif combatSequence[i].creatureType == 'monster':
                try:
                    combatSequence[i].attack(random.choice(heroes))
                except:
                    break

if teamHeroes == 0:
    print("\033[2;32;40mYour party has succumbed to the hazards of the wasteland.\033[0;37;40m")
elif teamMonsters == 0:
     print("\033[2;36;40mYour party has survived another day in the atomic wastes.\033[0;37;40m")
print('Survivors:')
# print(*creatures[0].name, sep='\n')
for i in range(len(creatures)):
    print(creatures[i].name, "hp:", creatures[i].hp)

#End program