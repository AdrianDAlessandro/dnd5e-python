  
# coding: utf-8

# # Test Driven Development of Character class layout
# 
# This notebook serves two purposes:
# - To develop the program (layout of classes, data structures, etc) for the interactive character sheet
# - To provide an example of test driven development
# 
# ## Objective
# 
# We want to be able to initialise/create a Character object that can return all of the essential information about about the D&D Character. It should also be able to level up and contain methods for all actions in combat.
# 
# ## List of Requirements (Update this over time)
# 1. Initialise a `Character` object
# 2. Initialiase `Character` with some details
#     - A string for each of: `name`, `race`, and `character_class`
#     - An integer for `level`, which defaults to 1
# 3. Make it that `Character` "has a" `Race` and "has a" `CharacterClass`
#     - Each is a class of it's own
#     - Build in the ability to check the string with a `__str__` method
# 4. Further develop the `Race` class
#     - It has subclasses for each race from D&D 5e
#     - The `__str__` method returns the race name
# 5. Further develop the `CharacterClass` class
#     - It has subclasses for each character class from D&D 5e
#     - The `__str__` method returns the character class name
# 6. Initialise a `Player` class which "is a" `Character`
# 7. Initialise a `NonPlayer` class which "is a" `Character`
# 8. Initialise a `Weapon` class
# 9. Initialise a `Spell` class
# 10. Initialise an `Ability` class
#     - `Ability` has the `check()` method and `modifier` and `score` properties
# 11. Each ability (`Strength` etc...) is a subclass of `Ability`
# 12. Each `Ability` subclass has skills
#     - Skills and saving throws are kept in a dictionary called `proficiencies`
#     - `proficiencies` key:value pairs are all `skill : <bool>`
# 13. Initialise a `Background` class
#    - Contains a list of `proficiencies` and a `description` string
# 14. Each `Background` subclass exists and determines skill proficiencies available
#    - Limited by the SRD, can only use Acolyte
# 15. Each `Character` has a list of `Abilities`
#    - The abilities for each character have scores and proficiencies
#    - The proficiencies for each character are determined by the `Race`, `CharacterClass` and `Background`
#    - `Race` and `CharacterClass` each have a list of `proficiencies` (or a list to choose from), just like in `Background`
# 16. Include function to create a custom `Race`, `CharacterClass`, and `Background`
# 17. Be able to return list of options for in-combat. ie list of Actions, Bonus Actions, Movemment
# 18. 

# #### First, import the testing modules:
import pytest
from dnd5e import *

# ## 1. Initialise a `Character` object
def test_Character_can_be_created():
    assert Character()

def test_Character_for_level_default():
    assert 1 == Character("Merret","Halfling","Ranger").level


# ## 3. Make it that `Character` "has a" `Race` and "has a" `CharacterClass`
# - Each is a class of it's own
# - Build in the ability to check the string with a `__str__` method
def test_Character_has_a_Race():
    assert isinstance(Character().race, Race)

def test_Character_has_a_CharacterClass():
    assert isinstance(Character().character_class, CharacterClass)

def test_Character_fields():

    inputs = {
        "name" : "NameA1",
        "race" : "Human",
        "character_class" : "Rogue",
        "ability_scores" : [12] * 6,
        "level" : 8
    }
    field_list = ["name", "race", "character_class", "level"]
    test_character = Character(**inputs) # * operator unpacks tuple (** for dict)
    test_fields = [field for field in dir(test_character)]
    
    for field in field_list:
        inpt = inputs[field]
        if field not in test_fields:
            assert getattr(test_character, field)
        elif str(inpt) != str(getattr(test_character,field)):
            assert str(inpt) == str(getattr(test_character,field))

    # Check the ability scores worked
    for ability, score in zip(test_character.abilities, inputs["ability_scores"]):
        if ability.score != score:
            assert ability.score == score


# ## 4. Further develop the `Race` class
#    - It has subclasses for each race from D&D 5e
#    - The `__str__` method returns the race name
def test_Race_subclasses():

    race_list = [
        "Dwarf", "Elf", "Halfling", "Human", "Dragonborn",
        "Gnome", "HalfElf", "HalfOrc", "Tiefling"
    ]

    subclasses = {cls.__name__ : cls() for cls in Race.__subclasses__()}

    for race in race_list:
        if race not in subclasses:
            assert False, '{0} is not a subclass of Race'.format(race)
        elif str(subclasses[race]) != race:
            assert False, '{0} __str__ method is incorrect'.format(race)
    assert True


# ## 5. Further develop the `CharacterClass` class
#    - It has subclasses for each character class from D&D 5e
#    - The `__str__` method returns the character class name
#    - Each subclass has a flag for if it is a spellcaster
def test_CharacterClass_subclasses():

    class_list = [
        'Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter', 'Monk',
        'Paladin', 'Ranger', 'Rogue', 'Sorcerer', 'Warlock', 'Wizard'
    ]

    subclasses = {cls.__name__ : cls() for cls in CharacterClass.__subclasses__()}

    for cls in class_list:
        # Is a Character Class
        if cls not in subclasses:
            assert False, '{0} is not a subclass of CharacterClass'.format(cls)
        # __str__ method works properly
        elif str(subclasses[cls]) != cls:
            assert False, '{0} __str__ method is incorrect'.format(cls)
        # Has spellcaster boolean
        elif not isinstance(subclasses[cls].spellcaster,bool):
            assert False, '{0}.spellcaster should be boolean'.format(cls)
    assert True


# ## 6. Initialise a `Player` class which "is a" `Character`
def test_Player_is_a_Character():
    assert isinstance(Player(),Character)


# ## 7. Initialise a `NonPlayer` class which "is a" `Character`
def test_NonPlayer_is_a_Character():
    assert isinstance(NonPlayer(),Character)


# ## 8. Initialise a `Weapon` class
def test_Weapon_can_be_created():
    assert Weapon()


# ## 9. Initialise a `Spell` class
def test_Spell_can_be_created():
    assert Spell()


# ## 10. Initialise an `Ability` class
#    - `Ability` has the `check()` method and `modifier` and `score` properties
def test_Ability_fields():

    field_list = ["check", "modifier", "score"]
    test_fields = [field for field in dir(Ability())]
    
    for field in field_list:
        if field not in test_fields:
            assert isinstance(getattr(Ability(),field),int)
    assert True


# ## 11. Each ability (`Strength` etc...) is a subclass of `Ability`
# ## 12. Each `Ability` subclass has skills
#    - Skills and saving throws are kept in a dictionary called `proficiencies`
#    - `proficiencies` key:value pairs are all `skill : <bool>`
def test_Ability_subclasses():

    ability_list = [
        "Strength", "Dexterity", "Constitution",
        "Intelligence", "Wisdom", "Charisma"
    ]

    subclasses = {cls.__name__ : cls() for cls in Ability.__subclasses__()}
    
    for ability in ability_list:
        # Is an Ability
        if ability not in subclasses:
            assert False, '{0} is not a subclass of Ability'.format(ability)
        # Has proficiencies dictionary
        elif not isinstance(subclasses[ability].proficiencies, dict):
            assert False, '{0} does not have proficiencies dict'.format(ability)
        # Values in proficiencies are booleans
        profs = subclasses[ability].proficiencies
        for prof in profs:
            if not isinstance(profs[prof],bool):
                assert False, '{0}.proficiencies[{1}] is not bool'.format(
                    ability, prof)
    assert True


# ## 13. Initialise a `Background` class
#    - Contains a list of `proficiencies` and a `description` string
def test_Background():

    if not isinstance(Background().description,str):
        assert False, "Background has no description string"
    elif not isinstance(Background().proficiencies,list):
        assert False, "Background has no proficiencies list"
    assert True


# ## 14. Each `Background` subclass exists and determines skill proficiencies available
#    - Limited by the SRD, can only use Acolyte
def test_Acolyte():

    subclasses = [cls.__name__ for cls in Background.__subclasses__()]
    
    # Is a Background
    if "Acolyte" not in subclasses:
        assert False, 'Acolyte is not a subclass of Background'
    # Has proficiencies list
    elif not isinstance(Acolyte().proficiencies, list):
        assert False, 'Acolyte does not have proficiencies list'
    # Values in proficiencies are strings
    elif not Acolyte().proficiencies:
        assert False, 'Acolyte.proficiencies is empty'
    for prof in Acolyte().proficiencies:
        if not isinstance(prof, str):
            assert False, 'Acolyte.proficiencies contains a non str'
    assert True


# ## 15. Each `Character` has a `str` method describing it
def test_Character_str():
    assert isinstance(Character().__str__(), str)


# ## 16. Each `Character` has a list of `Abilities`
#    - The abilities for each character have scores and proficiencies
#    - The proficiencies for each character are determined by the user
def test_Character_Abilities():
    assert isinstance(Character().abilities, list), "No abilities list"
    assert all([isinstance(a, Ability) for a in Character().abilities]), "Abilities is not a list of `Ability`s"


# ## 17. Include function to create a custom `Race`, `CharacterClass`, and `Background`

# ## 18. Be able to return list of options for in-combat. ie list of Actions, Bonus Actions, Movemment

