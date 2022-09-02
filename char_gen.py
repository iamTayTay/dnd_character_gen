import random
import subprocess

# D&D standard classes in this list
dndclass = ['artificer', 'barbarian', 'bard', 'cleric', 'druid', 'fighter', 
    'monk', 'paladin', 'ranger', 'rogue', 'sorcerer', 'warlock', 'wizard']

extraroll_d6 = ['Charlatan', 'Marine', 'Shipwright', 'Smuggler', 'Far Traveler']

extraroll_d8 = ['City Watch', 'Soldier', 'Archaeologist', 'Athlete',
    'Cloistered Scholar', 'Sage', 'Criminal', 'Feylost', 'Fisher', 'Hermit',
    'House Agent', 'Investigator (SCAG)', 'Knight Of The Order',
    'Mercenary Veteran', 'Spy', 'Urban Bounty Hunter', 'Witchlight Hand']

extraroll_d10 = ['Uthgardt Tribe Member', 'Outlander', 'Folk Hero',
    'Gladiator', 'Haunted One', 'Entertainer', 'Faceless']

extraroll_d20 = ['Courtier', 'Guild Merchant', 'Clan Crafter', 'Guild Artisan']

# Ability Scores determine your stats
ability_scores = {
    'str': '',
    'dex': '',
    'con': '',
    'int': '',
    'wis': '',
    'cha': '',
}

ability_mods = {}

mod_table = {
    '1': '-5', '2': '-4', '3': '-4', '4': '-3', '5': '-3', '6': '-2',
    '7': '-2', '8': '-1', '9': '-1', '10': '+0', '11': '+0', '12': '+1',
    '13': '+1', '14': '+2', '15': '+2', '16': '+3', '17': '+3', '18': '+4',
    '19': '+4', '20': '+5', '21': '+5', '22': '+6', '23': '+6', '24': '+7',
    '25': '+7', '26': '+8', '27': '+8', '28': '+9', '29': '+9', '30': '+10',
}

dictionary = {
    'str': ('Athlete', 'Crusher', 'Heavily Armored',
        'Heavy Armor Master', 'Lightly Armored', 'Moderately Armored', 'Piercer',
        'Resilient', 'Skill Expert', 'Slasher', 'Tavern Brawler', 'Weapon Master'),
    'dex': ('Athlete', 'Gunner', 'Lightly Armored', 'Moderately Armored',
        'Piercer', 'Resilient', 'Skill Expert', 'Slasher', 'Weapon Master'),
    'con': ('Aberrant Dragonmark', 'Chef', 'Crusher', 'Durable', 'Resilient',
        'Skill Expert', 'Tavern Brawler'),
    'int': ('Fey Touched', 'Gift of the Gem Dragon', 'Keen Mind', 'Linguist',
        'Observant', 'Resilient', 'Shadow Touched', 'Skill Expert', 'Telekinetic',
        'Telepathic'),
    'wis': ('Chef', 'Fey Touched', 'Gift of the Gem Dragon', 'Observant',
        'Resilient', 'Shadow Touched', 'Skill Expert', 'Telekinetic', 
        'Telepathic'),
    'cha': ('Actor', 'Fey Touched', 'Gift of the Gem Dragon', 'Resilient',
        'Shadow Touched', 'Skill Expert', 'Telekinetic', 'Telepathic'),
}
featsscore = []
ab_scorelist = ['str', 'dex', 'con', 'int', 'wis', 'cha']

# Pulling standard races, exotic and monstrous races all in seperate lists
with open('dndraces.txt', 'r') as f:
    dndraces = [line.strip() for line in f]

with open('dndexoticrace.txt', 'r') as f:
    dndexotic = [line.strip() for line in f]

with open('dndmonsterrace.txt', 'r') as f:
    dndmonster = [line.strip() for line in f]

# Pulling backgrounds from text file. Extra Roll lists below for BGs that have
# to roll for extra information
with open('dndcommonbgs.txt', 'r') as f:
    dndbackgrounds = [line.strip() for line in f]

# House Agent has another table where you have a house to pick
with open('houseagent.txt', 'r') as f:
    houseagent = [line.strip() for line in f]
houserand = random.choice(houseagent)

# Will prompt if DM wants to randomly assign a feat from these lists
with open('featslist.txt', 'r') as f:
    featslist = [line.strip() for line in f]
featsrand = random.choice(featslist)

with open('combinedspells.txt', 'r') as f:
    spellslist = [line.strip() for line in f]
spellsrand = random.choice(spellslist)

with open('plus1_Cha.txt', 'r') as f:
    plusonecha = [line.strip() for line in f]

with open('plus1_Con.txt', 'r') as f:
    plusonecon = [line.strip() for line in f]

with open('plus1_Dex.txt', 'r') as f:
    plusonedex = [line.strip() for line in f]

with open('plus1_Int.txt', 'r') as f:
    plusoneint = [line.strip() for line in f]

with open('plus1_Str.txt', 'r') as f:
    plusonestr = [line.strip() for line in f]

with open('plus1_Wis.txt', 'r') as f:
    plusonewis = [line.strip() for line in f]

with open('plus2_Cha.txt', 'r') as f:
    plustwocha = [line.strip() for line in f]

with open('plus2_Con.txt', 'r') as f:
    plustwocon = [line.strip() for line in f]

with open('plus2_Dex.txt', 'r') as f:
    plustwodex = [line.strip() for line in f]

with open('plus2_Int.txt', 'r') as f:
    plustwoint = [line.strip() for line in f]

with open('plus2_Str.txt', 'r') as f:
    plustwostr = [line.strip() for line in f]

with open('plus2_Wis.txt', 'r') as f:
    plustwowis = [line.strip() for line in f]

with open('plus_Various.txt', 'r') as f:
    plusvari = [line.strip() for line in f]

# Dice Rolls
def d4rolls():
    d4roll = random.randint(1, 4)
    return d4roll
def d6rolls():
    d6roll = random.randint(1, 6)
    return d6roll
def d8rolls():
    d8roll = random.randint(1, 8)
    return d8roll
def d10rolls():
    d10roll = random.randint(1, 10)
    return d10roll
def d12rolls():
    d12roll = random.randint(1, 12)
    return d12roll
def d20rolls():
    d20roll = random.randint(1, 20)
    return d20roll
def d100rolls():
    d100roll = random.randint(1, 100)
    return d100roll

# Starting prompt: start @ level 1 or 3? Which races to add to pool? Free Spell/ Feat?
level3prompt = input("Would you like to start at first or third level? (1/3)\n")

exoticprompt = "\nWould you like exotic races added to the random pool? (yes/no)\n"
dndeinput = input(exoticprompt)
dndsettoe = True

while dndsettoe:
    if dndeinput == 'yes':
        for exotic in dndexotic:
            dndraces.append(exotic)
        dndraces.sort()
        break
    else:
        dndsettoe = False

monsterprompt = "\nWould you like monstrous races added to the random pool? (yes/no)\n"
dndminput = input(monsterprompt)
dndsettom = True

while dndsettom:
    if dndminput == 'yes':
        for monster in dndmonster:
            dndraces.append(monster)
        dndraces.sort()
        break
    else:
        dndsettom = False

spellsprompt = "\nYou have gained the favor of a god. It has granted you a "
spellsprompt += "single random spell.\nWould you like to accept? (yes/no)\n"
spellinput = input(spellsprompt)
spellsset = True

featssprompt = "\nYou have gained the favor of a god. It has granted you a "
featssprompt += "single random feat.\nWould you like to accept? (yes/no)\n"
featsinput = input(featssprompt)
featsset = True

#Roll for races and classes
print("\nOK! Here is your information:\n")

def dndclassrand():
    dndrandclass = random.choice(dndclass)
    return dndrandclass
dndrandclass = dndclassrand()

def dndbgsrand():
    dndbgs = random.choice(dndbackgrounds)
    return dndbgs
dndbgs = dndbgsrand()

def dndrandrace():
    newdndrace = random.choice(dndraces)
    return newdndrace
dndrace = dndrandrace()

print(f"\nA {dndrace} {dndrandclass.title()} is what you'll be playing.\n")
print(f"Your background is {dndbgs} and your trait rolls are:")

if dndbgs == 'Witchlight Hand':
    print(f"Personality Trait: {d8rolls()}\n"
        f"Ideals: {d8rolls()}\n"
        f"Bonds: {d8rolls()}\n"
        f"Flaws: {d8rolls()}\n")
elif dndbgs == 'Feywild':
    print(f"Personality Trait: {d8rolls()}\n"
        f"Ideals: {d8rolls()}\n"
        f"Bonds: {d8rolls()}\n"
        f"Flaws: {d8rolls()}\n")
elif dndbgs == 'Anthropologist':
    print(f"Personality Trait: {d6rolls()}\n"
        f"Ideals: {d6rolls()}\n"
        f"Bonds: {d6rolls()}\n"
        f"Flaws: {d6rolls()}\n")
elif dndbgs == 'Far Traveler':
    print(f"Personality Trait: {d6rolls()}\n"
        f"Ideals: {d6rolls()}\n"
        f"Bonds: {d6rolls()}\n"
        f"Flaws: {d6rolls()}\n")
else:
    print(f"Personality Trait: {d8rolls()}\n"
        f"Ideals: {d6rolls()}\n"
        f"Bonds: {d6rolls()}\n"
        f"Flaws: {d6rolls()}\n")

if dndbgs in extraroll_d6:
    print(f"There's another table to roll on for your background!\nThat would be a: {d6rolls()}\n") 
elif dndbgs in extraroll_d8:
    print(f"There's another table to roll on for your background!\nThat would be a: {d8rolls()}\n")
elif dndbgs in extraroll_d10:
    print(f"There's another table to roll on for your background!\nThat would be a: {d10rolls()}\n")
elif dndbgs in extraroll_d20:
    print(f"There's another table to roll on for your background!\nThat would be a: {d20rolls()}\n")
elif dndbgs == 'Inheritor':
    print(f"There are two extra tables for you.\n"
        f"First table roll: {d8rolls()}\nSecond table roll: {d10rolls()}\n")

if dndbgs == 'House Agent':
    print(f"Oh, {dndbgs}! I almost forgot. Your house is {houserand}.\n")

while spellsset:
    if spellinput == "yes":
        print(f"You have been granted the spell: {spellsrand}")
        print("You can cast this once per day without expending a spell slot"
            " and you also don't need the required material components.\n")
        break
    else:
        spellsset = False

while featsset:
    if featsinput == "yes":
        print(f"You have been granted the Feat: {featsrand}\n")
        break
    else:
        featsset = False

# Getting ability scores
def ability_numbers():
    roll = [random.randint(1, 6) for x in range(4)]
    roll.sort(reverse = True)
    roll_result = sum(roll[:3])
    return roll_result

#Starts the list for ability score choices for your feat
for key, value in dictionary.items():
    if featsrand in value:
        featsscore.append(key)

#This has the list of ability scores from a feat and randomly picks one
while featsscore:
    for feat in featsscore:
        featsplusone = random.choice(featsscore)
    break
else:
    featsplusone = ''

# Rolling for Ability Score first, then adding it to the ability score dict 
for key, value in ability_scores.items():
    value = ability_numbers()
    if key == featsplusone:
        value = value + 1
    ability_scores[key] = value

if dndrace in plusvari:
    if dndrace == 'Owlin':
        variroll = 1
    else:
        variroll = random.randint(1, 2)
    if variroll == 1:
        variability2 = random.choice(ab_scorelist)
        ab_scorelist.remove(variability2)
        variability1 = random.choice(ab_scorelist)
        for key, value in ability_scores.items():
            if key == variability2:
                value = value + 2
                ability_scores[variability2] = value
            if key == variability1:
                value = value + 1
                ability_scores[variability1] = value
    elif variroll == 2:
        for rolls in range(3):
            variability = random.choice(ab_scorelist)
            ab_scorelist.remove(variability)
            for key, value in ability_scores.items():
                if key == variability:
                    value = value + 1
                    ability_scores[variability] = value
    else:
        for rolls in range(2):
            variability = random.choice(ab_scorelist)
            ab_scorelist.remove(variability)
            for key, value in ability_scores.items():
                if key == variability:
                    value = value + 1
                    ability_scores[variability] = value

for key, value in ability_scores.items():
    if key == 'str':
        if dndrace in plusonestr:
            value = value + 1
        if dndrace in plustwostr:
            value = value + 2
    if key == 'dex':
        if dndrace in plusonedex:
            value = value + 1
        if dndrace in plustwodex:
            value = value + 2
    if key == 'con':
        if dndrace in plusonecon:
            value = value + 1
        if dndrace in plustwocon:
            value = value + 2
    if key == 'int':
        if dndrace in plusoneint:
            value = value + 1
        if dndrace in plustwoint:
            value = value + 2
    if key == 'wis':
        if dndrace in plusonewis:
            value = value + 1
        if dndrace in plustwowis:
            value = value + 2
    if key == 'cha':
        if dndrace in plusonecha:
            value = value + 1
        if dndrace in plustwocha:
            value = value + 2
    if dndrace == 'Human':
        value = value + 1
    if value > 20:
        value = 20
    ability_scores[key] = value

#This is where we get the modifier
for score, mod in mod_table.items():
    for key, value in ability_scores.items():
        if str(value) == score:
            ability_mods[f'{key}_mod'] = mod
            print(f"{key.title()}: {value}  \t/Mod: {mod}.")

sixhp = ['sorcerer', 'wizard']
eighthp = ['artificer', 'bard', 'cleric', 'druid', 'monk', 'rogue', 'warlock']
tenhp = ['fighter', 'paladin', 'ranger']
twelvehp = ['barbarian']

if dndrandclass in sixhp:
    hit_points = 6 + int(ability_mods['con_mod'])
elif dndrandclass in eighthp:
    hit_points = 8 + int(ability_mods['con_mod'])
elif dndrandclass in tenhp:
    hit_points = 10 + int(ability_mods['con_mod'])
elif dndrandclass in twelvehp:
    hit_points = 12 + int(ability_mods['con_mod'])

if featsrand == 'Tough':
    hit_points = hit_points + (int(level3prompt) * 2)

if dndrandclass == 'artificer':
    skill_pro = ['Arcana', 'History', 'Investigation', 'Medicine', 'Nature',
        'Perception', 'Sleight of Hand']
    your_skill_pro = []
    artificer_spec = ['Alchemist', 'Armorer', 'Artillerist', 'Battle Smith']
    
    if level3prompt == '3':
        print(f"Your Artificer Specialist is: {random.choice(artificer_spec)}")
        print(f"Your Hit Points = "
            f"{hit_points + (int(ability_mods['con_mod']) * 2) + d8rolls() + d8rolls()}")
    else:
        print(f"Your Hit Points = {hit_points}")

    print(f"Your Spell Save DC is: {8 + 2 + int(ability_mods['int_mod'])}.")
    print(f"Your Spell Attack modifier is: {2 + int(ability_mods['int_mod'])}.")
    
    def skill_pro_rand():
        skillprorand = random.choice(skill_pro)
        your_skill_pro.append(skillprorand)
        skill_pro.remove(skillprorand)
        return

    skill_pro_rand()
    skill_pro_rand()
    skill_text = "Your first random skill proficiency granted by your class is"
    skill_text += f" {your_skill_pro[0]} and your second is {your_skill_pro[1]}."
    print(skill_text)


elif dndrandclass == 'barbarian':
    skill_pro = ['Animal Handling', 'Athletics', 'Intimidation', 'Nature', 
        'Perception', 'Survival']
    your_skill_pro = []
    primal_path = ['Ancestral Guardian', 'Battlerager', 'Beast', 'Berserker',
        'Storm Herald', 'Totem Warrior', 'Wild Magic', 'Zealot']

    if level3prompt == '3':
        print(f"Your Primal Path is: {random.choice(primal_path)}")
        print(f"Your Hit Points = "
            f"{hit_points + (int(ability_mods['con_mod']) * 2) + d12rolls() + d12rolls()}")
    else:
        print(f"Your Hit Points = {hit_points}")

    def skill_pro_rand():
        skillprorand = random.choice(skill_pro)
        your_skill_pro.append(skillprorand)
        skill_pro.remove(skillprorand)
        return

    skill_pro_rand()
    skill_pro_rand()
    skill_text = "Your first random skill proficiency granted by your class is"
    skill_text += f" {your_skill_pro[0]} and your second is {your_skill_pro[1]}."
    print(skill_text)

elif dndrandclass == 'bard':
    skill_pro = ['Acrobatics', 'Animal Handling', 'Arcana', 'Athletics', 'Deception',
        'History', 'Insight', 'Intimidation', 'Investigation', 'Medicine', 'Nature',
        'Perception', 'Performance', 'Persuasion', 'Religion', 'Sleight of Hand',
        'Stealth', 'Survival']
    your_skill_pro = []
    bard_college = ['Creation', 'Eloquence', 'Glamour', 'Lore', 'Spirits', 'Swords',
        'Valor', 'Whispers']
    if level3prompt == '3':
        print(f"Your Bard College is: {random.choice(bard_college)}")
        print(f"Your Hit Points = "
            f"{hit_points + (int(ability_mods['con_mod']) * 2) + d8rolls() + d8rolls()}")
    else:
        print(f"Your Hit Points = {hit_points}")

    print(f"Your Spell Save DC is: {8 + 2 + int(ability_mods['cha_mod'])}.")
    print(f"Your Spell Attack modifier is: {2 + int(ability_mods['cha_mod'])}.")

    def skill_pro_rand():
        skillprorand = random.choice(skill_pro)
        your_skill_pro.append(skillprorand)
        skill_pro.remove(skillprorand)
        return

    skill_pro_rand()
    skill_pro_rand()
    skill_pro_rand()
    skill_text = "Your first random skill proficiency granted by your class is"
    skill_text += f" {your_skill_pro[0]}, your second is {your_skill_pro[1]}, "
    skill_text += f"and your third is {your_skill_pro[2]}."
    print(skill_text)

elif dndrandclass == 'cleric':
    skill_pro = ['History', 'Insight', 'Medicine', 'Persuasion', 'Religion']
    your_skill_pro = []
    divine_domain = ['Arcana', 'Death', 'Forge', 'Grave', 'Knowledge', 'Life',
        'Light', 'Nature', 'Order', 'Peace', 'Tempest', 'Trickery', 'Twilight',
        'War']

    if level3prompt == '3':
        print(f"Your Divine Domain is: {random.choice(divine_domain)}")
        print(f"Your Hit Points = "
            f"{hit_points + (int(ability_mods['con_mod']) * 2) + d8rolls() + d8rolls()}")
    else:
        print(f"Your Hit Points = {hit_points}")

    print(f"Your Spell Save DC is: {8 + 2 + int(ability_mods['wis_mod'])}.")
    print(f"Your Spell Attack modifier is: {2 + int(ability_mods['wis_mod'])}.")

    def skill_pro_rand():
        skillprorand = random.choice(skill_pro)
        your_skill_pro.append(skillprorand)
        skill_pro.remove(skillprorand)
        return

    skill_pro_rand()
    skill_pro_rand()
    skill_text = "Your first random skill proficiency granted by your class is"
    skill_text += f" {your_skill_pro[0]} and your second is {your_skill_pro[1]}."
    print(skill_text)

elif dndrandclass == 'druid':
    skill_pro = ['Arcana', 'Animal Handling', 'Insight', 'Medicine',
        'Nature', 'Perception', 'Religion', 'Survival']
    your_skill_pro = []
    druid_circle = ['Dreams', 'Land', 'Moon', 'Shepherd', 'Spores', 'Stars', 
        'Wildfire']

    if level3prompt == '3':
        print(f"Your Druid Circle is: {random.choice(druid_circle)}")
        print(f"Your Hit Points = "
            f"{hit_points + (int(ability_mods['con_mod']) * 2) + d8rolls() + d8rolls()}")
    else:
        print(f"Your Hit Points = {hit_points}")

    print(f"Your Spell Save DC is: {8 + 2 + int(ability_mods['wis_mod'])}.")
    print(f"Your Spell Attack modifier is: {2 + int(ability_mods['wis_mod'])}.")

    def skill_pro_rand():
        skillprorand = random.choice(skill_pro)
        your_skill_pro.append(skillprorand)
        skill_pro.remove(skillprorand)
        return

    skill_pro_rand()
    skill_pro_rand()
    skill_text = "Your first random skill proficiency granted by your class is"
    skill_text += f" {your_skill_pro[0]} and your second is {your_skill_pro[1]}."
    print(skill_text)

elif dndrandclass == 'fighter':
    skill_pro = ['Acrobatics', 'Animal Handling', 'Athletics', 'History', 
        'Insight', 'Intimidation', 'Perception', 'Survival']
    your_skill_pro = []
    martial_archetype = ['Arcane Archer', 'Banneret', 'Battle Master', 'Cavalier',
        'Champion', 'Echo Knight', 'Eldritch Knight', 'Psi Warrior', 'Rune Knight',
        'Samurai']

    if level3prompt == '3':
        print(f"Your Martial Archetype is: {random.choice(martial_archetype)}")
        print(f"Your Hit Points = "
            f"{hit_points + (int(ability_mods['con_mod']) * 2) + d10rolls() + d10rolls()}")
    else:
        print(f"Your Hit Points = {hit_points}")

    print("You can choose your own Fighting Style.")

    def skill_pro_rand():
        skillprorand = random.choice(skill_pro)
        your_skill_pro.append(skillprorand)
        skill_pro.remove(skillprorand)
        return

    skill_pro_rand()
    skill_pro_rand()
    skill_text = "Your first random skill proficiency granted by your class is"
    skill_text += f" {your_skill_pro[0]} and your second is {your_skill_pro[1]}."
    print(skill_text)

elif dndrandclass == 'monk':
    skill_pro = ['Acrobatics', 'Athletics', 'History', 'Insight', 'Religion', 
        'Stealth']
    your_skill_pro = []
    monastic_tradition = ['Astral Self', 'Drunken Master', 'Four Elements', 'Kensei',
        'Long Death', 'Mercy', 'Open Hand', 'Shadow', 'Sun Soul', 'Ascendant Dragon']

    if level3prompt == '3':
        print(f"Your Monastic Tradition is: {random.choice(monastic_tradition)}")
        print(f"Your Hit Points = "
            f"{hit_points + (int(ability_mods['con_mod']) * 2) + d8rolls() + d8rolls()}")
    else:
        print(f"Your Hit Points = {hit_points}")

    print(f"Your Ki Save DC is: {8 + 2 + int(ability_mods['wis_mod'])}.")

    def skill_pro_rand():
        skillprorand = random.choice(skill_pro)
        your_skill_pro.append(skillprorand)
        skill_pro.remove(skillprorand)
        return

    skill_pro_rand()
    skill_pro_rand()
    skill_text = "Your first random skill proficiency granted by your class is"
    skill_text += f" {your_skill_pro[0]} and your second is {your_skill_pro[1]}."
    print(skill_text)

elif dndrandclass == 'paladin':
    skill_pro = ['Athletics', 'Insight', 'Intimidation', 'Medicine', 'Persuasion',
        'Religion']
    your_skill_pro = []
    sacred_oath = ['Ancients', 'Conquest', 'Crown', 'Devotion', 'Glory', 
        'Redemption', 'Vengeance', 'Watchers', 'Oathbreaker']

    if level3prompt == '3':
        print(f"Your Sacred Oath is: {random.choice(sacred_oath)}")
        print(f"Your Hit Points = "
            f"{hit_points + (int(ability_mods['con_mod']) * 2) + d10rolls() + d10rolls()}")
        print("You can choose your own Fighting Style.")
    else:
        print(f"Your Hit Points = {hit_points}")

    print(f"Your Spell Save DC is: {8 + 2 + int(ability_mods['cha_mod'])}.")
    print(f"Your Spell Attack modifier is: {2 + int(ability_mods['cha_mod'])}.")

    def skill_pro_rand():
        skillprorand = random.choice(skill_pro)
        your_skill_pro.append(skillprorand)
        skill_pro.remove(skillprorand)
        return

    skill_pro_rand()
    skill_pro_rand()
    skill_text = "Your first random skill proficiency granted by your class is"
    skill_text += f" {your_skill_pro[0]} and your second is {your_skill_pro[1]}."
    print(skill_text)

elif dndrandclass == 'ranger':
    skill_pro = ['Animal Handling', 'Athletics', 'Insight', 'Investigation',
        'Nature', 'Perception', 'Stealth', 'Survival']
    your_skill_pro = []
    ranger_conclave = ['Beast Master', 'Fey Wanderer', 'Gloom Stalker', ' Hunter',
        'Horizon Walker', 'Monster Slayer', 'Swarmkeeper', 'Drakewarden']

    if level3prompt == '3':
        print(f"Your Ranger Conclave is: {random.choice(ranger_conclave)}")
        print(f"Your Hit Points = "
            f"{hit_points + (int(ability_mods['con_mod']) * 2) + d10rolls() + d10rolls()}")
    else:
        print(f"Your Hit Points = {hit_points}")

    print("You can choose your own Favored Enemy and Fighting Style.")
    print(f"Your Spell Save DC is: {8 + 2 + int(ability_mods['wis_mod'])}.")
    print(f"Your Spell Attack modifier is: {2 + int(ability_mods['wis_mod'])}.")

    def skill_pro_rand():
        skillprorand = random.choice(skill_pro)
        your_skill_pro.append(skillprorand)
        skill_pro.remove(skillprorand)
        return

    skill_pro_rand()
    skill_pro_rand()
    skill_pro_rand()
    skill_text = "Your first random skill proficiency granted by your class is"
    skill_text += f" {your_skill_pro[0]} and your second is {your_skill_pro[1]}."
    skill_text += f" Your third is {your_skill_pro[2]}."
    print(skill_text)

elif dndrandclass == 'rogue':
    skill_pro = ['Acrobatics', 'Athletics', 'Deception', 'Insight', 'Intimidation', 
        'Investigation', 'Perception', 'Performance', 'Persuasion',
        'Sleight of Hand', 'Stealth']
    your_skill_pro = []
    roguish_archetype = ['Arcane Trickster', 'Assassin', 'Inquisitive',
        'Mastermind', 'Phantom', 'Scout', 'Soulknife', 'Swashbuckler', 'Thief']

    if level3prompt == '3':
        print(f"Your Roguish Archetype is: {random.choice(roguish_archetype)}")
        print(f"Your Hit Points = "
            f"{hit_points + (int(ability_mods['con_mod']) * 2) + d8rolls() + d8rolls()}")
    else:
        print(f"Your Hit Points = {hit_points}")

    def skill_pro_rand():
        skillprorand = random.choice(skill_pro)
        your_skill_pro.append(skillprorand)
        skill_pro.remove(skillprorand)
        return

    skill_pro_rand()
    skill_pro_rand()
    skill_pro_rand()
    skill_pro_rand()
    skill_text = "Your first random skill proficiency granted by your class is"
    skill_text += f" {your_skill_pro[0]} and your second is {your_skill_pro[1]}."
    skill_text += f" Your third and fourth are {your_skill_pro[2]} and {your_skill_pro[1]}."
    print(skill_text)

elif dndrandclass == 'sorcerer':
    skill_pro = ['Arcana', 'Deception', 'Insight', 'Intimidation', 'Persuasion',
        'Religion']
    your_skill_pro = []
    sorcerous_origin = ['Aberrant Mind', 'Clockwork Soul', 'Draconic Bloodline',
        'Divine Soul', 'Shadow Magic', 'Storm Sorcery', 'Wild Magic']

    if level3prompt == '3':
        print(f"Your Sorcerous Origin is: {random.choice(sorcerous_origin)}")
        print(f"Your Hit Points = "
            f"{hit_points + (int(ability_mods['con_mod']) * 2) + d6rolls() + d6rolls()}")
        print("You can choose your own Metamagic.")
    else:
        print(f"Your Hit Points = {hit_points}")

    print(f"Your Spell Save DC is: {8 + 2 + int(ability_mods['cha_mod'])}.")
    print(f"Your Spell Attack modifier is: {2 + int(ability_mods['cha_mod'])}.")

    def skill_pro_rand():
        skillprorand = random.choice(skill_pro)
        your_skill_pro.append(skillprorand)
        skill_pro.remove(skillprorand)
        return

    skill_pro_rand()
    skill_pro_rand()
    skill_text = "Your first random skill proficiency granted by your class is"
    skill_text += f" {your_skill_pro[0]} and your second is {your_skill_pro[1]}."
    print(skill_text)

elif dndrandclass == 'warlock':
    skill_pro = ['Arcana', 'Deception', 'History', 'Intimidation', 'Investigation',
        'Nature', 'Religion']
    your_skill_pro = []
    otherworldly = ['Archfey', 'Celestial', 'Fathomless', 'Fiend', 'The Genie',
        'Great Old One', 'Hexblade', 'Undead', 'Undying']
    pact_boon = ['Pact of the Blade', 'Pact of the Chain', 'Pact of the Tome',
        'Pact of the Talisman']

    if level3prompt == '3':
        print(f"Your Pact Boon is: {random.choice(pact_boon)}")
        print(f"Your Hit Points = "
            f"{hit_points + (int(ability_mods['con_mod']) * 2) + d8rolls() + d8rolls()}")
        print("You can choose your own Eldritch Invocations.")
    else:
        print(f"Your Hit Points = {hit_points}")

    print(f"Your Otherworldly Patron is: {random.choice(otherworldly)}")
    print(f"Your Spell Save DC is: {8 + 2 + int(ability_mods['cha_mod'])}.")
    print(f"Your Spell Attack modifier is: {2 + int(ability_mods['cha_mod'])}.")

    def skill_pro_rand():
        skillprorand = random.choice(skill_pro)
        your_skill_pro.append(skillprorand)
        skill_pro.remove(skillprorand)
        return

    skill_pro_rand()
    skill_pro_rand()
    skill_text = "Your first random skill proficiency granted by your class is"
    skill_text += f" {your_skill_pro[0]} and your second is {your_skill_pro[1]}."
    print(skill_text)

elif dndrandclass == 'wizard':
    skill_pro = ['Arcana', 'History', 'Insight', 'Investigation', 'Medicine',
        'Religion']
    your_skill_pro = []
    arcane_tradition = ['Abjuration', 'Bladesinging', 'Chronurgy', 'Conjuration',
        'Divination', 'Enchantment', 'Evocation', 'Graviturgy', 'Illusion',
        'Necromancy', 'Order of Scribes', 'Transmutation', 'War Magic']

    if level3prompt == '3':
        print(f"Your Arcane Tradition is: {random.choice(arcane_tradition)}")
        print(f"Your Hit Points = "
            f"{hit_points + (int(ability_mods['con_mod']) * 2) + d6rolls() + d6rolls()}")
    else:
        print(f"Your Hit Points = {hit_points}")

    print(f"Your Spell Save DC is: {8 + 2 + int(ability_mods['int_mod'])}.")
    print(f"Your Spell Attack modifier is: {2 + int(ability_mods['int_mod'])}.")

    def skill_pro_rand():
        skillprorand = random.choice(skill_pro)
        your_skill_pro.append(skillprorand)
        skill_pro.remove(skillprorand)
        return

    skill_pro_rand()
    skill_pro_rand()
    skill_text = "Your first random skill proficiency granted by your class is"
    skill_text += f" {your_skill_pro[0]} and your second is {your_skill_pro[1]}."
    print(skill_text)

if dndrace == 'Eladrin (MToF) Elf':
    fourseasons = ['Autumn', 'Winter', 'Summer', 'Spring']
    season = random.choice(fourseasons)
    print(f"\nYou are associated with the season {season} and your personality "
        f"trait from that table is {d4rolls()} and for the flaw, {d4rolls()}.")
if dndrace == 'Githyanki':
    print("\nIncluding the ones above, you have extra personality tables to roll on.")
    print(f"Personality Trait: {d4rolls()}\n"
    f"Ideals: {d4rolls()}\n"
    f"Bonds: {d4rolls()}\n"
    f"Flaws: {d4rolls()}\n")
if dndrace == 'Githzerai':
    print("\nIncluding the ones above, you have extra personality tables to roll on.")
    print(f"Personality Trait: {d4rolls()}\n"
    f"Ideals: {d4rolls()}\n"
    f"Bonds: {d4rolls()}\n"
    f"Flaws: {d4rolls()}\n")
if dndrace == 'Fairy':
    print(f"\nYou have an extra table for Fey Characteristics.\nYou rolled: {d8rolls()} ")

print("\nGood luck writing your backstory!")