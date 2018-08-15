
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
#    - Contains a list of `proficiencies` and a description string
# 14. Each `Character` has a list of `Abilities`
#    - The abilities for each character have scores and proficiencies
#    - The proficiencies for each character are determined by the `Race`, `CharacterClass` and `Background`
#    - `Race` and `CharacterClass` each have a list of `proficiencies` (or a list to choose from), just like in `Background`
# 15. Include function to create a custom `Race` and a `CharacterClass`
# 16. 

# #### First, import the testing modules:

# In[1]:


# Set the file name for unit testing iwth ipytest
__file__ = "character_scripting.ipynb"

import pytest
import ipytest.magics


# ## 1. Initialise a `Character` object

# #### Make sure the tests are defined *before* the main code is written:

# In[7]:


get_ipython().run_cell_magic('run_pytest', '-v --tb=line', '\ndef test_Character_can_be_created():\n    assert Character()')


# #### Test failed (because we are yet to define `Character`). "Refactor" the code:

# In[8]:


get_ipython().run_cell_magic('run_pytest', '', '\nclass Character(object):\n    pass')


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

# In[9]:


get_ipython().run_cell_magic('run_pytest', '-v --tb=line', '\ndef test_Character_fields():\n\n    field_list = ["name", "_race", "character_class", "level"]\n    inputs = "Merret","Halfling","Ranger", 8\n    test_character = Character(*inputs) # * operator unpacks tuple (** for dict)\n    test_fields = [field for field in dir(test_character)]\n    \n    for inpt, field in zip(inputs, field_list):\n        if field not in test_fields:\n            assert getattr(test_character, field)\n        elif inpt != getattr(test_character,field):\n            assert inpt == getattr(test_character,field)\n    assert True\n\ndef test_Character_for_level_default():\n    assert 1 == Character("Merret","Halfling","Ranger").level')


# 2. **Run** the tests

# In[10]:


get_ipython().run_cell_magic('run_pytest', '-v --tb=line', '\nclass Character(object):\n    \n    def __init__(self, name, race, character_class, level=1):\n        self.name = name\n        self._race = race\n        self.character_class = character_class\n        self.level = level')


# 3. **Refactor** - The initial test does not include any inputs to `Character`. Include default values.

# In[11]:


get_ipython().run_cell_magic('run_pytest', '-v --tb=line', '\nclass Character(object):\n    \n    def __init__(self, name="Merret", race="Halfling",\n                 character_class="Ranger", level=1):\n        self.name = name\n        self._race = race\n        self.character_class = character_class\n        self.level = level')


# ## 3. Make it that `Character` "has a" `Race` and "has a" `CharacterClass`
# - Each is a class of it's own
# - Build in the ability to check the string with a `__str__` method

# In[12]:


def test_Character_has_a_Race():
    assert isinstance(Character()._race, Race)
def test_Character_has_a_CharacterClass():
    assert isinstance(Character().character_class, CharacterClass)


# In[13]:


get_ipython().run_cell_magic('run_pytest', '-v --tb=line', '\nclass Race(object):\n    \n    def __init__(self, race):\n        self._race = race\n    \n    def __str__(self):\n        return self._race\n\n\nclass CharacterClass(object):\n    \n    def __init__(self, character_class):\n        self.character_class = character_class\n    \n    def __str__(self):\n        return self.character_class\n\n\nclass Character(object):\n    \n    def __init__(self, name="Merret", race="Halfling",\n                 character_class="Ranger", level=1):\n        self.name = name\n        self._race = Race(race) # Changed Line\n        self.character_class = CharacterClass(character_class) # Changed Line\n        self.level = level')


# #### The new requirement breaks the `test_Character_fields` test. Refactor the tests to make use of the `__str__` method:

# In[14]:


get_ipython().run_cell_magic('run_pytest', '', '\ndef test_Character_fields():\n\n    field_list = ["name", "_race", "character_class", "level"]\n    inputs = "Merret","Halfling","Ranger", 8\n    test_character = Character(*inputs) # * operator unpacks tuple (** for dict)\n    test_fields = [field for field in dir(test_character)]\n    \n    for inpt, field in zip(inputs, field_list):\n        if field not in test_fields:\n            assert getattr(test_character, field)\n        # Refactor here:\n        elif str(inpt) != str(getattr(test_character,field)):\n            assert str(inpt) == str(getattr(test_character,field))\n    assert True')


# ## 4. Further develop the `Race` class
#    - It has subclasses for each race from D&D 5e
#    - The `__str__` method returns the race name

# In[89]:


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


# In[91]:


get_ipython().run_cell_magic('run_pytest', '-v --tb=line', '\nclass Race(object):\n    \n    def __init__(self):\n        pass\n    \n    def __str__(self):\n        return type(self).__name__ # returns the name of the class\n\n    \nclass Dwarf(Race):\n    pass\nclass Elf(Race):\n    pass\nclass Halfling(Race):\n    pass\nclass Human(Race):\n    pass\nclass Dragonborn(Race):\n    pass\nclass Gnome(Race):\n    pass\nclass HalfElf(Race):\n    pass\nclass HalfOrc(Race):\n    pass\nclass Tiefling(Race):\n    pass')


# #### Must update assignment of `_race` in `Character`

# In[17]:


get_ipython().run_cell_magic('run_pytest', '', '\nclass Character(object):\n    \n    def __init__(self, name="Merret", race="Halfling",\n                 character_class="Ranger", level=1):\n        self.name = name\n        self._race = globals()[race.title()]() # Changed Line\n        self.character_class = CharacterClass(character_class)\n        self.level = level')


# ## 5. Further develop the `CharacterClass` class
#    - It has subclasses for each character class from D&D 5e
#    - The `__str__` method returns the character class name
#    - Each subclass has a flag for if it is a spellcaster

# In[105]:


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


# In[86]:


get_ipython().run_cell_magic('run_pytest', '', '\nclass CharacterClass(object):\n    \n    def __init__(self, spellcaster=False):\n        self.spellcaster = spellcaster\n    \n    def __str__(self):\n        return type(self).__name__ # returns the name of the class\n\n    \nclass Barbarian(CharacterClass):\n    def __init__(self):\n        super().__init__()\n\nclass Bard(CharacterClass):\n    def __init__(self):\n        super().__init__(spellcaster=True)\n\nclass Cleric(CharacterClass):\n    def __init__(self):\n        super().__init__(spellcaster=True)\n\nclass Druid(CharacterClass):\n    def __init__(self):\n        super().__init__(spellcaster=True)\n\nclass Fighter(CharacterClass):\n    def __init__(self):\n        super().__init__()\n\nclass Monk(CharacterClass):\n    def __init__(self):\n        super().__init__()\n\nclass Paladin(CharacterClass):\n    def __init__(self):\n        super().__init__(spellcaster=True)\n\nclass Ranger(CharacterClass):\n    def __init__(self):\n        super().__init__(spellcaster=True)\n\nclass Rogue(CharacterClass):\n    def __init__(self):\n        super().__init__()\n\nclass Sorcerer(CharacterClass):\n    def __init__(self):\n        super().__init__(spellcaster=True)\n\nclass Warlock(CharacterClass):\n    def __init__(self):\n        super().__init__(spellcaster=True)\n\nclass Wizard(CharacterClass):\n    def __init__(self):\n        super().__init__(spellcaster=True)\n\n\n# Same problem will occur as when changing Race, so update assignment of\n# character_class in Character now\nclass Character(object):\n    \n    def __init__(self, name="Merret", race="Halfling",\n                 character_class="Ranger", level=1):\n        self.name = name\n        self._race = globals()[race.title()]()\n        self.character_class = globals()[character_class.title()]() # Changed\n        self.level = level')


# ## 6. Initialise a `Player` class which "is a" `Character`

# In[92]:


def test_Player_is_a_Character():
    assert isinstance(Player(),Character)


# In[93]:


get_ipython().run_cell_magic('run_pytest', '', '\nclass Player(Character):\n    pass')


# ## 7. Initialise a `NonPlayer` class which "is a" `Character`

# In[22]:


def test_NonPlayer_is_a_Character():
    assert isinstance(NonPlayer(),Character)


# In[94]:


get_ipython().run_cell_magic('run_pytest', '', '\nclass NonPlayer(Character):\n    pass')


# ## 8. Initialise a `Weapon` class

# In[24]:


def test_Weapon_can_be_created():
    assert Weapon()


# In[25]:


get_ipython().run_cell_magic('run_pytest', '', '\nclass Weapon(object):\n    pass')


# ## 9. Initialise a `Spell` class

# In[26]:


def test_Spell_can_be_created():
    assert Spell()


# In[27]:


get_ipython().run_cell_magic('run_pytest', '', '\nclass Spell(object):\n    pass')


# ## 10. Initialise an `Ability` class
#    - `Ability` has the `check()` method and `modifier` and `score` properties

# In[95]:


def test_Ability_fields():

    field_list = ["check", "modifier", "score"]
    test_fields = [field for field in dir(Ability())]
    
    for field in field_list:
        if field not in test_fields:
            assert isinstance(getattr(Ability(),field),int)
    assert True


# In[96]:


get_ipython().run_cell_magic('run_pytest', '-v --tb=line', '\nimport random\n\nclass Ability(object):\n    \n    def __init__(self, score=10):\n        self.score = score\n        self.modifier = int((score - 10) / 2)\n        \n    def check(self):\n        return random.randint(1,20) + self.modifier\n    ')


# ## 11. Each ability (`Strength` etc...) is a subclass of `Ability`

# In[102]:


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


# In[103]:


get_ipython().run_cell_magic('run_pytest', '', '\nclass Strength(Ability):\n    pass\nclass Dexterity(Ability):\n    pass\nclass Constitution(Ability):\n    pass\nclass Intelligence(Ability):\n    pass\nclass Wisdom(Ability):\n    pass\nclass Charisma(Ability):\n    pass')


# ## 12. Each `Ability` subclass has skills
#    - Skills and saving throws are kept in a dictionary called `proficiencies`
#    - `proficiencies` key:value pairs are all `skill : <bool>`

# In[154]:


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
        elif not isinstance(subclasses[ability].proficiencies,dict):
            assert False, '{0} does not have proficiencies dict'.format(ability)
        # Values in proficiencies are booleans
        profs = subclasses[ability].proficiencies
        for prof in profs:
            if not isinstance(profs[prof],bool):
                assert False, '{0}.proficiencies[{1}] is not bool'.format(
                    ability, prof)
    assert True


# In[155]:


get_ipython().run_cell_magic('run_pytest', '', '\nclass Strength(Ability):\n    \n    def __init__(self, score=10, proficiencies=[]):\n        skill_list = ["Saving Throws", "Athletics"]\n        proficiencies = [prof.title() for prof in proficiencies]\n        self.proficiencies = {\n            skill:skill in proficiencies for skill in skill_list\n        }\n        super().__init__(score)\n    \nclass Dexterity(Ability):\n    \n    def __init__(self, score=10, proficiencies=[]):\n        skill_list = [\n            "Saving Throws", "Acrobatics",\n            "Sleight of Hand", "Stealth"\n        ]\n        proficiencies = [prof.title() for prof in proficiencies]\n        self.proficiencies = {\n            skill:skill in proficiencies for skill in skill_list\n        }\n        super().__init__(score)\n    \nclass Constitution(Ability):\n    \n    def __init__(self, score=10, proficiencies=[]):\n        skill_list = ["Saving Throws"]\n        proficiencies = [prof.title() for prof in proficiencies]\n        self.proficiencies = {\n            skill:skill in proficiencies for skill in skill_list\n        }\n        super().__init__(score)\n    \nclass Intelligence(Ability):\n    \n    def __init__(self, score=10, proficiencies=[]):\n        skill_list = [\n            "Saving Throws", "Arcana", "History",\n            "Investigation", "Nature", "Religion"\n        ]\n        proficiencies = [prof.title() for prof in proficiencies]\n        self.proficiencies = {\n            skill:skill in proficiencies for skill in skill_list\n        }\n        super().__init__(score)\n    \nclass Wisdom(Ability):\n    \n    def __init__(self, score=10, proficiencies=[]):\n        skill_list = [\n            "Saving Throws", "Animal Handling", "Insight",\n            "Medicine", "Perception", "Survival"\n        ]\n        proficiencies = [prof.title() for prof in proficiencies]\n        self.proficiencies = {\n            skill:skill in proficiencies for skill in skill_list\n        }\n        super().__init__(score)\n    \nclass Charisma(Ability):\n    \n    def __init__(self, score=10, proficiencies=[]):\n        skill_list = [\n            "Saving Throws", "Deception", "Intimidation",\n            "Performance", "Persuasion"\n        ]\n        proficiencies = [prof.title() for prof in proficiencies]\n        self.proficiencies = {\n            skill:skill in proficiencies for skill in skill_list\n        }\n        super().__init__(score)\n    ')


# ## 13. Initialise a `Background` class
#    - Contains a list of `proficiencies` and a description string

# ## 14. Each `Character` has a list of `Abilities`
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


# ## 15. Include function to create a custom `Race` and a `CharacterClass`

# ## Convert Notebook to a Python Script

# In[ ]:


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

