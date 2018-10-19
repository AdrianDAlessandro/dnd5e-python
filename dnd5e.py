import random

# In[1]:



# #### Make sure the tests are defined *before* the main code is written:

# In[2]:



# In[3]:




# #### Test failed (because we are yet to define `Character`). "Refactor" the code:

# In[4]:


class Character(object):
    pass


# In[5]:




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

# 2. **Run** the tests

# In[7]:




# 3. **Refactor** - The initial test does not include any inputs to `Character`. Include default values.

# In[8]:


class Character(object):
    
    def __init__(self, name, race, character_class, level=1):
        self.name = name
        self._race = race
        self.character_class = character_class
        self.level = level


# In[9]:




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




# In[12]:



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





# In[15]:


# In[16]:




# In[17]:


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




# In[22]:


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




# In[25]:


# In[26]:


class Player(Character):
    pass


# In[27]:




# In[28]:


# In[29]:


class NonPlayer(Character):
    pass


# In[30]:



# In[31]:


# In[32]:


class Weapon(object):
    pass


# In[33]:




# In[34]:


# In[35]:


class Spell(object):
    pass


# In[36]:




# In[37]:


# In[38]:



class Ability(object):
    
    def __init__(self, score=10):
        self.score = score
        self.modifier = int((score - 10) / 2)
        
    def check(self):
        return random.randint(1,20) + self.modifier
    


# In[39]:




# In[40]:


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




# In[43]:


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




# In[46]:


# In[47]:


class Background(object):
    
    def __init__(self, proficiencies=[], description="Background superclass"):
        self.proficiencies = proficiencies
        self.description = description


# In[48]:




# In[49]:



# In[50]:


class Acolyte(Background):
    
    def __init__(self, description="An Acolyte"):
        proficiencies = ["Insight", "Religion"]
        print(proficiencies)
        super().__init__(proficiencies, description)


# In[51]:




# In[52]:


class Character(object):
    
    def __init__(self, name="Merret", race="Halfling",
                 character_class="Ranger", level=1):
        self.name = name
        self._race = globals()[race.title()]()
        self.character_class = globals()[character_class.title()]()
        self.level = level


# In[53]:




# In[54]:


class Player(Character):
    pass
class NonPlayer(Character):
    pass


# In[58]:


merret = Player("Merret Strongheart",
                   "Halfling",
                   "ranger",
                   #[12, 20, 12, 8, 16, 8],
                   9)


# In[ ]:


print(merret.character_class)


# In[ ]:


print(merret.character_class.spellcaster)


# In[ ]:


print(merret)


# In[ ]:


despair = Player("Despair", "Tiefling", "Sorcerer", #[9, 11, 15, 14, 13, 20], 
                 8)


# In[ ]:


print(despair.character_class.spellcaster)


# In[ ]:


print(despair)
