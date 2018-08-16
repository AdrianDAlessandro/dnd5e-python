
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
# 17. 

# #### First, import the testing modules:

# In[3]:


# Set the file name for unit testing iwth ipytest
__file__ = "character_scripting.ipynb"

import pytest
import ipytest.magics


# ## 1. Initialise a `Character` object

# #### Make sure the tests are defined *before* the main code is written:

# In[2]:


def test_Character_can_be_created():
    assert Character()


# In[3]:


get_ipython().run_cell_magic('run_pytest', '-v --tb=line', '#')


# #### Test failed (because we are yet to define `Character`). "Refactor" the code:

# In[4]:


class Character(object):
    pass


# In[5]:


get_ipython().run_cell_magic('run_pytest', '', '#')


# ### [This process](https://en.wikipedia.org/wiki/Test-driven_development#Test-driven_development_cycle) should be repeated for each new requirement
# 1. **Write** the test(s)
# ```python
# def test_<test_description>():
#     # Some code (potentially)
#     assert true_statement
# ```
# 2. **Run** the tests
# ```python
# %%run_pytest -v --tb=line
# ```
# 3. **Refactor** (update or write new code - including tests) until all tests pass
# 4. **Repeat** for the next requirement

# ## 2. Initialiase `Character` with some details
# - A string for each of: `name`, `race`, and `character_class`
# - An integer for `level`, which defaults to 1

# 1. **Write** the test(s)

# In[6]:


def test_Character_fields():

    field_list = ["name", "_race", "character_class", "level"]
    inputs = "Merret","Halfling","Ranger", 8
    test_character = Character(*inputs) # * operator unpacks tuple (** for dict)
    test_fields = [field for field in dir(test_character)]
    
    for inpt, field in zip(inputs, field_list):
        if field not in test_fields:
            assert getattr(test_character, field)
        elif inpt != getattr(test_character,field):
            assert inpt == getattr(test_character,field)
    assert True

def test_Character_for_level_default():
    assert 1 == Character("Merret","Halfling","Ranger").level


# 2. **Run** the tests

# In[7]:


get_ipython().run_cell_magic('run_pytest', '-v --tb=line', '#')


# 3. **Refactor** - The initial test does not include any inputs to `Character`. Include default values.

# In[8]:


class Character(object):
    
    def __init__(self, name, race, character_class, level=1):
        self.name = name
        self._race = race
        self.character_class = character_class
        self.level = level


# In[9]:


get_ipython().run_cell_magic('run_pytest', '-v --tb=line', '#')


# 3.1 **Continue Refactoring** - The initial test does not include any inputs to `Character`. Include default values.

# In[10]:


class Character(object):
    
    def __init__(self, name="Merret", race="Halfling",
                 character_class="Ranger", level=1):
        self.name = name
        self._race = race
        self.character_class = character_class
        self.level = level


# In[11]:


get_ipython().run_cell_magic('run_pytest', '-v --tb=line', '#')


# ## 3. Make it that `Character` "has a" `Race` and "has a" `CharacterClass`
# - Each is a class of it's own
# - Build in the ability to check the string with a `__str__` method

# In[12]:


def test_Character_has_a_Race():
    assert isinstance(Character()._race, Race)
def test_Character_has_a_CharacterClass():
    assert isinstance(Character().character_class, CharacterClass)


# In[13]:


class Race(object):
    
    def __init__(self, race):
        self._race = race
    
    def __str__(self):
        return self._race


class CharacterClass(object):
    
    def __init__(self, character_class):
        self.character_class = character_class
    
    def __str__(self):
        return self.character_class


class Character(object):
    
    def __init__(self, name="Merret", race="Halfling",
                 character_class="Ranger", level=1):
        self.name = name
        self._race = Race(race) # Changed Line
        self.character_class = CharacterClass(character_class) # Changed Line
        self.level = level


# In[14]:


get_ipython().run_cell_magic('run_pytest', '-v --tb=line', '#')


# #### The new requirement breaks the `test_Character_fields` test. Refactor the tests to make use of the `__str__` method:

# In[15]:


def test_Character_fields():

    field_list = ["name", "_race", "character_class", "level"]
    inputs = "Merret","Halfling","Ranger", 8
    test_character = Character(*inputs) # * operator unpacks tuple (** for dict)
    test_fields = [field for field in dir(test_character)]
    
    for inpt, field in zip(inputs, field_list):
        if field not in test_fields:
            assert getattr(test_character, field)
        # Refactor here:
        elif str(inpt) != str(getattr(test_character,field)):
            assert str(inpt) == str(getattr(test_character,field))
    assert True


# In[16]:


get_ipython().run_cell_magic('run_pytest', '', '#')


# ## 4. Further develop the `Race` class
#    - It has subclasses for each race from D&D 5e
#    - The `__str__` method returns the race name

# In[17]:


# Is a Race
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


# In[18]:


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


# In[19]:


get_ipython().run_cell_magic('run_pytest', '-v --tb=line', '#')


# #### Must update assignment of `_race` in `Character`

# In[20]:


class Character(object):
    
    def __init__(self, name="Merret", race="Halfling",
                 character_class="Ranger", level=1):
        self.name = name
        self._race = globals()[race.title()]() # Changed Line
        self.character_class = CharacterClass(character_class)
        self.level = level


# In[21]:


get_ipython().run_cell_magic('run_pytest', '', '#')


# ## 5. Further develop the `CharacterClass` class
#    - It has subclasses for each character class from D&D 5e
#    - The `__str__` method returns the character class name
#    - Each subclass has a flag for if it is a spellcaster

# In[22]:


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


# In[23]:


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


# Same problem will occur as when changing Race, so update assignment of
# character_class in Character now
class Character(object):
    
    def __init__(self, name="Merret", race="Halfling",
                 character_class="Ranger", level=1):
        self.name = name
        self._race = globals()[race.title()]()
        self.character_class = globals()[character_class.title()]() # Changed
        self.level = level


# In[24]:


get_ipython().run_cell_magic('run_pytest', '', '#')


# ## 6. Initialise a `Player` class which "is a" `Character`

# In[25]:


def test_Player_is_a_Character():
    assert isinstance(Player(),Character)


# In[26]:


class Player(Character):
    pass


# In[27]:


get_ipython().run_cell_magic('run_pytest', '', '#')


# ## 7. Initialise a `NonPlayer` class which "is a" `Character`

# In[28]:


def test_NonPlayer_is_a_Character():
    assert isinstance(NonPlayer(),Character)


# In[29]:


class NonPlayer(Character):
    pass


# In[30]:


get_ipython().run_cell_magic('run_pytest', '', '#')


# ## 8. Initialise a `Weapon` class

# In[31]:


def test_Weapon_can_be_created():
    assert Weapon()


# In[32]:


class Weapon(object):
    pass


# In[33]:


get_ipython().run_cell_magic('run_pytest', '', '#')


# ## 9. Initialise a `Spell` class

# In[34]:


def test_Spell_can_be_created():
    assert Spell()


# In[35]:


class Spell(object):
    pass


# In[36]:


get_ipython().run_cell_magic('run_pytest', '', '#')


# ## 10. Initialise an `Ability` class
#    - `Ability` has the `check()` method and `modifier` and `score` properties

# In[37]:


def test_Ability_fields():

    field_list = ["check", "modifier", "score"]
    test_fields = [field for field in dir(Ability())]
    
    for field in field_list:
        if field not in test_fields:
            assert isinstance(getattr(Ability(),field),int)
    assert True


# In[38]:


import random

class Ability(object):
    
    def __init__(self, score=10):
        self.score = score
        self.modifier = int((score - 10) / 2)
        
    def check(self):
        return random.randint(1,20) + self.modifier
    


# In[39]:


get_ipython().run_cell_magic('run_pytest', '-v --tb=line', '#')


# ## 11. Each ability (`Strength` etc...) is a subclass of `Ability`

# In[40]:


# Is an Ability
def test_Ability_subclasses():

    ability_list = [
        "Strength", "Dexterity", "Constitution",
        "Intelligence", "Wisdom", "Charisma"
    ]

    subclasses = {cls.__name__ : cls for cls in Ability.__subclasses__()}
    
    for ability in ability_list:
        if ability not in subclasses:
            assert False, '{0} is not a subclass of Ability'.format(ability)
    assert True


# In[41]:


class Strength(Ability):
    pass
class Dexterity(Ability):
    pass
class Constitution(Ability):
    pass
class Intelligence(Ability):
    pass
class Wisdom(Ability):
    pass
class Charisma(Ability):
    pass


# In[42]:


get_ipython().run_cell_magic('run_pytest', '', '#')


# ## 12. Each `Ability` subclass has skills
#    - Skills and saving throws are kept in a dictionary called `proficiencies`
#    - `proficiencies` key:value pairs are all `skill : <bool>`

# In[43]:


# Refactor the previous test
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


# In[44]:


class Strength(Ability):
    
    def __init__(self, score=10, proficiencies=[]):
        skill_list = ["Saving Throws", "Athletics"]
        proficiencies = [prof.title() for prof in proficiencies]
        self.proficiencies = {
            skill:skill in proficiencies for skill in skill_list
        }
        super().__init__(score)
    
class Dexterity(Ability):
    
    def __init__(self, score=10, proficiencies=[]):
        skill_list = [
            "Saving Throws", "Acrobatics",
            "Sleight of Hand", "Stealth"
        ]
        proficiencies = [prof.title() for prof in proficiencies]
        self.proficiencies = {
            skill:skill in proficiencies for skill in skill_list
        }
        super().__init__(score)
    
class Constitution(Ability):
    
    def __init__(self, score=10, proficiencies=[]):
        skill_list = ["Saving Throws"]
        proficiencies = [prof.title() for prof in proficiencies]
        self.proficiencies = {
            skill:skill in proficiencies for skill in skill_list
        }
        super().__init__(score)
    
class Intelligence(Ability):
    
    def __init__(self, score=10, proficiencies=[]):
        skill_list = [
            "Saving Throws", "Arcana", "History",
            "Investigation", "Nature", "Religion"
        ]
        proficiencies = [prof.title() for prof in proficiencies]
        self.proficiencies = {
            skill:skill in proficiencies for skill in skill_list
        }
        super().__init__(score)
    
class Wisdom(Ability):
    
    def __init__(self, score=10, proficiencies=[]):
        skill_list = [
            "Saving Throws", "Animal Handling", "Insight",
            "Medicine", "Perception", "Survival"
        ]
        proficiencies = [prof.title() for prof in proficiencies]
        self.proficiencies = {
            skill:skill in proficiencies for skill in skill_list
        }
        super().__init__(score)
    
class Charisma(Ability):
    
    def __init__(self, score=10, proficiencies=[]):
        skill_list = [
            "Saving Throws", "Deception", "Intimidation",
            "Performance", "Persuasion"
        ]
        proficiencies = [prof.title() for prof in proficiencies]
        self.proficiencies = {
            skill:skill in proficiencies for skill in skill_list
        }
        super().__init__(score)
    


# In[45]:


get_ipython().run_cell_magic('run_pytest', '', '#')


# ## 13. Initialise a `Background` class
#    - Contains a list of `proficiencies` and a `description` string

# In[47]:


def test_Background():

    if not isinstance(Background().description,str):
        assert False, "Background has no description string"
    elif not isinstance(Background().proficiencies,list):
        assert False, "Background has no proficiencies list"
    assert True


# In[4]:


class Background(object):
    
    def __init__(self, proficiencies=[], description="Background superclass"):
        self.proficiencies = proficiencies
        self.description = description


# In[54]:


get_ipython().run_cell_magic('run_pytest', '', '#')


# ## 14. Each `Background` subclass exists and determines skill proficiencies available
#    - Limited by the SRD, can only use Acolyte

# In[40]:


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


# In[43]:


class Acolyte(Background):
    
    def __init__(self, description="An Acolyte"):
        proficiencies = ["Insight", "Religion"]
        print(proficiencies)
        super().__init__(proficiencies, description)


# In[44]:


get_ipython().run_cell_magic('run_pytest', '', '#')


# ## 15. Each `Character` has a list of `Abilities`
#    - The abilities for each character have scores and proficiencies
#    - The proficiencies for each character are determined by the `Race`, `CharacterClass` and `Background`
#    - `Race` and `CharacterClass` each have a list of `proficiencies` (or a list to choose from), just like in `Background`

# In[ ]:


class Character(object):
    
    def __init__(self, name="Merret", race="Halfling",
                 character_class="Ranger", level=1):
        self.name = name
        self._race = globals()[race.title()]()
        self.character_class = globals()[character_class.title()]()
        self.level = level


# In[44]:


get_ipython().run_cell_magic('run_pytest', '', '#')


# ## 16. Include function to create a custom `Race`, `CharacterClass`, and `Background`

# ## Convert Notebook to a Python Script

# In[46]:


get_ipython().system('jupyter nbconvert --to script character_scripting.ipynb')


# In[ ]:


# Main class for Player Characters - "is a" Character
class Player(Character):
    
    def __init__(self, name, race, character_class, ability_scores, level=1):
        super().__init__(name, race, character_class, level)
        self.__spellcaster = str(self._class) in [
            "Bard", "Druid", "Ranger", "Sorceror", "Wizard", "Warlock"]
        self.ability_scores = {
            "Strength" : ability_scores[0],
            "Dexterity" : ability_scores[1],
            "Constitution" : ability_scores[2],
            "Intelligence" : ability_scores[3],
            "Wisdom" : ability_scores[4],
            "Charisma" : ability_scores[5]
        }
        
    def __str__(self):
        return "A level {0} {1} {2} called {3}".format(
            self.level, 
            str(self._race).title(),
            str(self._class),
            self.name.title())
    
    def attack(self):
        pass


# In[ ]:


# Main class for Non-Player Characters - "is a" Character
class NonPlayer(Character):
    pass


# In[ ]:


merret = Player("Merret Strongheart",
                   "Halfling",
                   "ranger",
                   [12, 20, 12, 8, 16, 8],
                   9)


# In[ ]:


print(merret._class)


# In[ ]:


merret._Player__spellcaster


# In[ ]:


print(merret)


# In[ ]:


despair = Player("Despair", "Tiefling", "Sorceror", [9, 11, 15, 14, 13, 20], 8)


# In[ ]:


despair._Player__spellcaster


# In[ ]:


print(despair)

