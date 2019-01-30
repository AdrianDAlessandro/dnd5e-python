import random

class Race(object):

    def __init__(self):
        pass

    def __str__(self):
        return type(self).__name__ # returns the name of the class


class Dwarf(Race):
    pass
class Elf(Race):
    pass
class Halfling(Race):
    pass
class Human(Race):
    pass
class Dragonborn(Race):
    pass
class Gnome(Race):
    pass
class HalfElf(Race):
    pass
class HalfOrc(Race):
    pass
class Tiefling(Race):
    pass


class CharacterClass(object):

    def __init__(self, spellcaster=False):
        self.spellcaster = spellcaster

    def __str__(self):
        return type(self).__name__ # returns the name of the class


class Barbarian(CharacterClass):
    def __init__(self):
        super().__init__()

class Bard(CharacterClass):
    def __init__(self):
        super().__init__(spellcaster=True)

class Cleric(CharacterClass):
    def __init__(self):
        super().__init__(spellcaster=True)

class Druid(CharacterClass):
    def __init__(self):
        super().__init__(spellcaster=True)

class Fighter(CharacterClass):
    def __init__(self):
        super().__init__()

class Monk(CharacterClass):
    def __init__(self):
        super().__init__()

class Paladin(CharacterClass):
    def __init__(self):
        super().__init__(spellcaster=True)

class Ranger(CharacterClass):
    def __init__(self):
        super().__init__(spellcaster=True)

class Rogue(CharacterClass):
    def __init__(self):
        super().__init__()

class Sorcerer(CharacterClass):
    def __init__(self):
        super().__init__(spellcaster=True)

class Warlock(CharacterClass):
    def __init__(self):
        super().__init__(spellcaster=True)

class Wizard(CharacterClass):
    def __init__(self):
        super().__init__(spellcaster=True)


class Weapon(object):
    pass


class Spell(object):
    pass


class Ability(object):

    def __init__(self, score=10, proficiencies=[], skill_list=["Saving Throws"]):
        self.score = score
        self.modifier = int((score - 10) / 2)
        
        proficiencies = [prof.title() for prof in proficiencies]
        self.proficiencies = {
            skill:skill in proficiencies for skill in skill_list
        }

    def check(self):
        return random.randint(1,20) + self.modifier


class Strength(Ability):

    def __init__(self, score=10, proficiencies=[]):
        skill_list = ["Saving Throws", "Athletics"]
        super().__init__(score, proficiencies, skill_list)

class Dexterity(Ability):

    def __init__(self, score=10, proficiencies=[]):
        skill_list = [
            "Saving Throws", "Acrobatics",
            "Sleight of Hand", "Stealth"
        ]
        super().__init__(score, proficiencies, skill_list)

class Constitution(Ability):

    def __init__(self, score=10, proficiencies=[]):
        skill_list = ["Saving Throws"]
        super().__init__(score, proficiencies, skill_list)

class Intelligence(Ability):

    def __init__(self, score=10, proficiencies=[]):
        skill_list = [
            "Saving Throws", "Arcana", "History",
            "Investigation", "Nature", "Religion"
        ]
        super().__init__(score, proficiencies, skill_list)

class Wisdom(Ability):

    def __init__(self, score=10, proficiencies=[]):
        skill_list = [
            "Saving Throws", "Animal Handling", "Insight",
            "Medicine", "Perception", "Survival"
        ]
        super().__init__(score, proficiencies, skill_list)

class Charisma(Ability):

    def __init__(self, score=10, proficiencies=[]):
        skill_list = [
            "Saving Throws", "Deception", "Intimidation",
            "Performance", "Persuasion"
        ]
        super().__init__(score, proficiencies, skill_list)


class Background(object):

    def __init__(self, proficiencies=[], description="Background superclass"):
        self.proficiencies = proficiencies
        self.description = description


class Acolyte(Background):

    def __init__(self, description="An Acolyte"):
        proficiencies = ["Insight", "Religion"]
        print(proficiencies)
        super().__init__(proficiencies, description)


class Character(object):

    def __init__(self, name="Merret", race="Halfling",
                 character_class="Ranger", ability_scores=[10]*6, level=1,
                 proficiencies=[]):
        self.name = name
        self.race = globals()[race.title()]()
        self.character_class = globals()[character_class.title()]()
        self.level = level
        self.abilities = [
            Strength(ability_scores[0], proficiencies=proficiencies),
            Dexterity(ability_scores[1], proficiencies=proficiencies),
            Constitution(ability_scores[2], proficiencies=proficiencies),
            Intelligence(ability_scores[3], proficiencies=proficiencies),
            Wisdom(ability_scores[4], proficiencies=proficiencies),
            Charisma(ability_scores[5], proficiencies=proficiencies)
        ]

    def __str__(self):
        return "A level {0} {1} {2} called {3}".format(
            self.level,
            str(self.race).title(),
            str(self.character_class),
            self.name.title()
        )


class Player(Character):
    pass
class NonPlayer(Character):
    pass


# A couple of test characters:
if __name__ == "__main__":
    merret = Player("Merret Strongheart",
                    "Halfling",
                    "ranger",
                    [12, 20, 12, 8, 16, 8],
                    9)
    print(merret.character_class)
    print(merret.character_class.spellcaster)
    print(merret)

    despair = Player("Despair",
                     "Tiefling",
                     "Sorcerer",
                     [9, 11, 15, 14, 13, 20],
                     8)
    print(despair.character_class.spellcaster)
    print(despair)
