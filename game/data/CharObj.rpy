#This file has all the classes that control characters
init 1 python:
    # Base for all, used for the most generic Town NPCs
    class Base_Entity:
        def __init__(self, name, fileName):
            self.name = name
            self.fileName = fileName

        def get_name(self):
            return self.name

        def get_file_name(self):
            return self.name

    # Base for anything that interacts with RPG, also used for generic enemies
    class RPG_Stats():
        def __init__(self):
            self.lvl = 1

            self.attack_type = 0

            # Stats
            self.maxHp = 20
            self.hp = 20
            self.maxMp = 20
            self.mp = 20
            self.atk = 30
            self.dfn = 20
            self.mag = 20
            self.res = 1
            self.spd = 20
            self.wil = 20

            # Stat Growths
            self.hpG = 1
            self.mpG = 1
            self.atkG = 1
            self.dfnG = 1
            self.magG = 1
            self.resG = 1
            self.spdG = 1
            self.wilG = 1

            self.skills = []

            # Extra stuff
            self.statuses = {}
            self.healMultiplier = 1.0
            self.resistances = [0, 0, 0]

            self.isDefending = False
            self.defeatedFlag = False

        def set_base_stats(self, stats):
            self.maxHp = stats[0]
            self.hp = stats[0]
            self.maxMp = stats[1]
            self.mp = stats[1]
            self.atk = stats[2]
            self.dfn = stats[3]
            self.mag = stats[4]
            self.res = stats[5]
            self.spd = stats[6]
            self.wil = stats[7]


        def set_base_growths(self, stats):
            self.hpG = stats[0]
            self.mpG = stats[1]
            self.atkG = stats[2]
            self.dfnG = stats[3]
            self.magG = stats[4]
            self.resG = stats[5]
            self.spdG = stats[6]
            self.wilG = stats[7]


        def heal_hp(self, h_hp):
            # Check  pre_effects()
            self.hp = min(self.hp + int(h_hp * self.healMultiplier), self.maxHp)
            # Check post_effects()


        def heal_mp(self, h_mp):
            # Check  pre_effects()
            self.mp = min(self.mp + int(h_mp * self.healMultiplier), self.maxMp)
            # Check post_effects()O


        def deal_damage(self, dmg, dmg_type=0):
            damage = 0
            # Check  pre_effects()
            if(dmg_type == 0):
                # Physical damage is directly subtracted by the defense
                damage = max(dmg - self.dfn, 1)
            elif(dmg_type == 1):
                # Resistance is the percentage of magic damage reduced, this stat should always be no more than 80
                damage = max(dmg - ((self.res / 100) * dmg))
            else: #True damage case
                # True damage cannot be mitigated, get HP kiddo
                damage = dmg
            # Check  pre_effects()

            if(self.isDefending):
                if(dmg_type == 0):
                    damage -= int(math.ceil(damage * 0.5))
                elif(dmg_type == 1):
                    damage -= int(math.ceil(damage * 0.25))
                else:
                    print("You just attempted to mitigate true damage LOL!")
            self.hp = max(self.hp - int(damage), 0)
            return damage


        def is_defeated(self):
            if(self.hp <= 0):
                print("Unit is defeated")
                return True
            return False


        def give_exp(self, exp):
            # todo: finish
            self.exp += exp


        def lvl_up(self, lvls):
            self.lvl += lvls
            self.maxHp += (self.hpG * lvls)
            self.maxMp += (self.mpG * lvls)
            self.atk += (self.atkG * lvls)
            self.dfn += (self.dfnG * lvls)
            self.mag += (self.magG * lvls)
            self.res += (self.resG * lvls)
            self.spd += (self.spgG * lvls)
            self.wil += (self.wilG * lvls)


        def attack(self, target):
            print("Generic Enemy attack function")
            return 0


        def use_skill(self, target, skill):
            # skill(self, target)
            return



    class Enemy(Base_Entity, RPG_Stats):
        def __init__(self, name, fileName, flavorText, lootTable, expMultiplier):
            Base_Entity.__init__(self, name, fileName)
            RPG_Stats.__init__(self)
            self.imgAttribute = None
            self.tempId = 0
            self.lootTable = lootTable
            self.flavorText = flavorText
            self.expMultiplier = expMultiplier


    #Player character, god please add switch statements
    class Player(RPG_Stats):
        def __init__(self, name="Player"):
            self.name = name
            RPG_Stats.__init__(self)

            self.battleExp = 0
            self.cookingExp = 0
            self.socialExp = 0

            # Wpn
            self.weapon = None

            # Armor
            self.headSlot = None
            self.bodySlot = None
            self.legSlot = None

            # Accessories
            self.accessorySlots = 5
            self.accessories = []

        def equip_gear(self, item, slot=0):
            if slot == 0:
                if self.headSlot is None:
                    self.headSlot = item
                else:
                    # True if Item was removed
                    if not self.remove_gear(item, slot):
                        return False
                    else:
                        return self.equip_gear(item, slot)

            elif slot == 1:
                if self.bodySlot is None:
                    self.bodySlot = item
                else:
                    # True if Item was removed
                    if not self.remove_gear(item, slot):
                        return False
                    else:
                        return self.equip_gear(item, slot)

            else:
                if self.legSlot is None:
                    self.legSlot = item
                else:
                    # True if Item was removed
                    if not self.remove_gear(item, slot):
                        return False
                    else:
                        return self.equip_gear(item, slot)

            # Apply stat changes
            self.maxHp += item.hp
            self.maxMp += item.mp
            self.Atk += item.Atk
            self.Dfn += item.Dfn
            self.Mag += item.Mag
            self.Res += item.Res
            self.Wil += item.Wil

            # Success
            return True

        def remove_gear(self, item, slot=0):
            print("sex")


    class CharacterEntity(Base_Entity, RPG_Stats):
        def __init__(self, name, fileName):
            Base_Entity.__init__(self,name, fileName)
            RPG_Stats.__init__(self)
            self.character = None
            self.characterId = 9999
            self.friendship = 0
            self.maxFriendship = 100
            self.mood = 0
            self.schedule = []


        def add_activity(self, activity):
            self.schedule.append(activity)

        # TODO Remove
        def get_dialogue(self, type):
            data = get_data_from_file("dialogue/{}/{}_{}".format(self.fileName, self.fileName, type))
            data = data.split("\r\n")
            data = renpy.random.choice(data)
            data = data.split(";")
            return data

    class CharacterList(store.object):
        def __init__(self):
            #characters is a list of the character objects
            self.characters = []
            self.characterDict = {}
            #presentCharacters is a list of the IDs
            self.presentCharacters = []
            self.selected = 0
            self.init_main_characters()


        #Initialize a list of characters
        def init_main_characters(self):
            for c in range(len(mainCharacterInits)):
                # Create Character object
                newCharacter = CharacterEntity(mainCharacterInits[c]["name"], mainCharacterInits[c]["fileName"])
                newCharacter.characterId = c
                # Schedule contains a list
                self.init_schedule(mainCharacterInits[c]["schedule"], newCharacter)
                # Add character to list
                self.characters.append(newCharacter)

        def init_schedule(self, schedule, character:CharacterEntity):
            for s in schedule:
                character.schedule.append(Activity(s["place"], s["timeStart"], s["timeEnd"], s["task"]))

        def present_is_empty(self):
            return bool(not self.presentCharacters)

        def get_selected_character_id(self):
            try:
                return self.characters[self.presentCharacters[self.selected]].characterId
            except:
                return None

        # Index Control
        def move_prev(self):
            if(self.selected == 0):
                return
            self.selected -= 1

        def move_next(self):
            if(self.selected == len(self.presentCharacters)-1):
                return
            self.selected += 1

        # Getting character objects
        def get_selected_character(self):
            # If there are no present characters do nothing
            if(len(self.presentCharacters) == 0):
                return None
            return self.characters[self.presentCharacters[self.selected]]

        def get_prev_character(self):
            if(self.selected == 0):
                return None
            return self.characters[self.presentCharacters[self.selected-1]]

        def get_next_character(self):
            if(self.selected >= len(self.presentCharacters)-1):
                return None
            return self.characters[self.presentCharacters[self.selected+1]]

        def say_current_dialogue(self, type:str):
            charName = self.get_selected_character().fileName
            print("Current Character is: {}".format(charName))
            try:
                print("1")
                lines = get_data_from_json("dialogue/{}/{}_dialogue.json".format(charName, charName))
                print("2")
                lines = lines[type]
                print("3")
                lines = renpy.random.choice(lines)
                print("4")
                for l in lines:
                    renpy.show("{} {}".format(charName, l[1]))
                    renpy.say(self.characters[self.selected].character, l[0])
            except:
                renpy.say(self.characters[self.selected].character, ". . .")

            # Not particularly efficient way to reset the character, should optimize
            #renpy.hide(self.characters[self.selected].fileName)
            renpy.show(charName)


        #Put the current characters in the presentCharacters list
        def get_present_characters(self, world, clock):
            del self.presentCharacters[:]
            #Go through the characters
            for i in range(len(self.characters)):
                character = self.characters[i]
                #Go through the schedules
                for s in character.schedule:
                    #Time to check if this character is supposed to be in your location
                    if(s.is_present(world.currentLoc, clock.hrs)):
                        self.presentCharacters.append(character.characterId)
                        break
    class Activity:
        def __init__(self, place=None, hourStart=None, hourEnd=None, task=None):
            self.place = place
            self.hourStart = hourStart
            self.hourEnd = hourEnd
            self.task = task

        def is_present(self, place, hour):
            # If my place is None or the current place matches
            if(self.place != None and self.place != place):
                return False
            # Idf current hour is between clock hour
            if(self.hourStart != None and self.hourEnd != None):
                if(hour >= self.hourStart and hour <= self.hourEnd):
                    return False

            return True
