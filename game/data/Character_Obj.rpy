#This file has all the classes that control characters
init 1:
    define MAX_FRIENDSHIP = 100
    define MID_FRIENDSHIP = 50

init 1 python:
    class DamageType(Enum):
        PHYSICAL = 0
        MAGIC = 1
        TRUE = 2
        MENTAL = 3

    class Moods(Enum):
        NEUTRAL = 0
        HAPPY = 1
        SAD = 2
        ANGRY = 3

    class Activity(Enum):
        IDLE = ("idle")
        WORKING = ("working")
        LEISURE = ("leisure")
        RESTING = ("resting")
        SLEEPING = ("sleeping")

    # Base for all, used for the most generic Town NPCs
    class Entity:
        def __init__(self, data):
            self.name = data.get("name")
            self.character_id = data.get("id")
            self.image_attribute = None
            self.file_name = data.get("file_name")
            if(data.get("rpg")):
                self.rpg_stats = RPG_Stats(data.get("rpg"))

    # Base for anything that interacts with RPG, also used for generic enemies
    class RpgStats():
        def __init__(self, data):
            # Current stats
            self.level = 1
            self.max_hp = data.get("max_hp")
            self.max_mp = data.get("max_mp")

            # Base stats
            self.current_hp = self.max_hp
            self.current_mp = self.max_mp
            self.attack = data.get("attack")
            self.defense = data.get("defense")
            self.magic = data.get("magic")
            self.resistance = data.get("resistance")
            self.speed = data.get("speed")

            # Stat Growths
            self.hp_growth = data.get("hp_growth")
            self.mp_growth = data.get("mp_growth")
            self.attack_growth = data.get("attack_growth")
            self.defense_growth = data.get("defense_growth")
            self.magic_growth = data.get("magic_growth")
            self.resistance_growth = data.get("resistance_growth")
            self.speed_growth = data.get("speed_growth")

            # Extra stuff
            self.statuses = {}

            self.is_defending = False
            self.defeated_flag = False

        def heal_hp(self, hp):
            # Check effects
            heal_amount = hp
            if(self.statuses.get("hp_heal")):
                for s in self.statuses["hp_heal"]:
                    # Self reference is to remove the effect if necessary
                    heal_amount = s.apply(self, heal_amount)

            # Apply heal
            self.current_hp = min(self.current_hp + heal_amount, self.max_hp)

        def heal_mp(self, mp):
            # Check effects
            heal_amount = mp
            if(self.statuses.get("mp_heal")):
                for s in self.statuses["mp_heal"]:
                    # Self reference is to remove the effect if necessary
                    heal_amount = s.apply(self, heal_amount)

            self.current_mp = min(self.current_mp + heal_amount, self.max_mp)


        def deal_damage(self, dmg, type):
            damage = 0

            # Calculate
            if(type == DAMAGE_TYPE.PHYSICAL):
                # Physical damage is directly subtracted by the defense
                damage = int(max(dmg - self.defense, self.attack * 0.25))
            elif(type == DAMAGE_TYPE.MAGIC):
                # Resistance is the percentage of magic damage reduced, this stat should always be no more than 80
                damage = max(dmg - ((self.resistance / 100) * dmg))
            elif(type == DAMAGE_TYPE.TRUE):
                # True damage cannot be mitigated, get HP kiddo
                damage = dmg

            if(self.statuses.get("deal_damage")):
                for s in self.statuses["deal_damage"]:
                    # Self reference is to remove the effect if necessary
                    damage = s.apply(self, damage)

            if(self.isDefending):
                if(dmg_type == 0):
                    damage -= int(math.ceil(damage * 0.5))
                elif(dmg_type == 1):
                    damage -= int(math.ceil(damage * 0.25))
                else:
                    print("> Tried to mitigate true damage")

            # Apply
            self.hp = max(self.hp - int(damage), 0)
            return damage


        def is_defeated(self):
            if(self.hp <= 0):
                print("Unit is defeated")
                self.defeated_flag = True
            return self.defeated_flag

        def lvl_up(self, lvls):
            self.lvl += lvls
            self.max_hp += (self.hp_growth * lvls)
            self.max_hp += (self.mp_growth * lvls)
            self.attack += (self.attack_growth * lvls)
            self.defense += (self.defense_growth * lvls)
            self.magic += (self.magic_growth * lvls)
            self.resistance += (self.resistance_growth * lvls)
            self.speed += (self.speed_growth * lvls)

        def attack(self, target, type = DamageType.PHYSICAL, damage = None):
            if(damage == None):
                if(type == DamageType.PHYSICAL):
                    damage = self.attack
                if(type == DamageType.MAGIC):
                    damage = self.magic

            if(self.statuses.get("attack")):
                for s in self.statuses["attack"]:
                    # Self reference is to remove the effect if necessary
                    damage = s.apply(self, damage)

            target.deal_damage(damage, type)
            return


        def use_skill(self, target, skill):
            # skill(self, target)
            return


    class Enemy(Entity, RpgStats):
        def __init__(self, data):
            Entity.__init__(self, data)
            RPG_Stats.__init__(self, data.get("rpg"))
            self.temp_id = 0
            self.loot_table = data.get("loot_table")
            self.flavor_text = data.get("flavor_text")
            self.experience = data.get("exp")


    #Player character, god please add switch statements
    class Player(RpgStats):
        def __init__(self, name="Player"):
            data = get_data_from_json("data/inits/player_init.json")
            RpgStats.__init__(self, data["rpg"])
            self.name = name
            self.battle_exp = 0
            self.cooking_exp = 0
            self.social_exp = 0

            self.skills = []

            # Wpn
            self.weapon = None

            # Armor
            self.head_slot = None
            self.body_slot = None
            self.leg_slot = None

            # Accessories
            self.max_accessory_slots = 5
            self.accessories = []

    class CharacterEntity(Entity):
        def __init__(self, data):
            Entity.__init__(self, data)
            self.character = Character(data.get("name"), who_color = data.get("color"))
            self.character_id = data.get("id")
            self.friendship = 0
            # Mood attributes
            temp = data.get("predisposition")
            self.predisposition = (getattr(Moods, temp[0]), temp[1])
            self.mood = Moods.NEUTRAL
            # Schedule attributes
            self.schedule_tag = "default"
            self.schedule = None

        def add_friendship(self, amount):
            self.friendship = min(MAX_FRIENDSHIP, self.friendship + amount)
            return self.friendship

        def sub_friendship(self, amount):
            self.friendship = max(0, self.friendship - amount)
            return self.friendship
