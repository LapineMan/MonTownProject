import os
import renpy.store as store
import renpy.exports as renpy # we need this so Ren'Py properly handles rollback with classes
import functions
import random

#Actual Classes

class Mood(store.object):
    NEUTRAL = (1, 'neutral')
    HAPPY = (1.2, 'happy')
    EUPHORIC = (1.5, 'euphoric')
    SAD = (0.80, 'sad')
    ANGRY = (0.60, 'angry')
    DEPRESSED = (0.5, 'depressed')

    @staticmethod
    def getMoodName(mood):
        return mood[1]

class Enemy(store.object):
    def __init__(self, name, fileName):
        self.name = name
        self.fileName = fileName
        self.HP = HP
        self.STR = STR
        self.INT = INT
        self.DEF = DEF
        self.RES = RES

class Plssayer(store.object):
    name = "Ner"

    #Misc stats

    talk_exp = 0
    cooking_exp = 0
    battle_lvl = 1
    battle_exp = 0
    max_battle_exp = 100
    gold = 50
    max_gold = 1000

    #Base stats
    ATK = 8.0
    SPD = 7.0
    INT = 6.0
    DEF = 6.0
    RES = 4.0
    WIL = 10.0

    #Base growths
    ATK_G = 0.8
    SPD_G = 0.7
    INT_G = 0.5
    DEF_G = 0.8
    RES_G = 0.5
    WIL_G = 0.7

    @staticmethod
    def combatLevelUp():
        self.battle_exp -= 100
        self.ATK += self.ATK_G
        self.SPD += self.SPD_G
        self.INT += self.INT_G
        self.DEF += self.DEF_G
        self.RES += self.RES_G
        self.WIL += self.WIL_G
        self.battle_lvl += 1


class NPC(store.object):
    def __init__(self, id, name, fileName, HP, STR, INT, DEF, RES, HPg, STRg, INTg, DEFg, RESg):
        self.id = id
        self.name = name
        self.fileName = fileName
        self.mood = Mood.NEUTRAL
        self.favor = 0
        battle_exp = 0
        self.HP = HP
        self.STR = STR
        self.INT = INT
        self.DEF = DEF
        self.RES = RES
        self.HPg = HPg
        self.STRg = STRg
        self.INTg = INTg
        self.DEFg = DEFg
        self.RESg = RESg
        self.schedule = []

    @staticmethod
    def initSchedules():
        result = []
        for i in CharacterList.characters:
            try:
                file = open(renpy.loader.transfn("data/schedules/{}".format(i.id)),"r")
                data = file.read()
                file.close()
                data = data.split("\n")
                for x in data:
                    x = x.split(",")
                    result.append( (int(x[0]), int(x[1]), int(x[2]), int(x[3]) ) )
                i.schedule = result
            except:
                i.schedule = [(-1, -1, -1, -1)]

class CharacterList(store.object):
    #characters is a list of the character objects
    characters = []
    #presentCharacters is a list of the IDs
    presentCharacters = []
    selected = 0

    @staticmethod
    def presentIsEmpty():
        if(len(CharacterList.presentCharacters) == 0):
            return True
        return False

    @staticmethod
    def getSelectedCharacter():
        return CharacterList.characters[CharacterList.presentCharacters[CharacterList.selected]]

    @staticmethod
    def getRandomIdleChat():
        chara = CharacterList.characters[CharacterList.presentCharacters[CharacterList.selected]]
        data = open(renpy.loader.transfn("dialogue/{}/talk".format(chara.fileName)), "r")
        x = data.read()
        print(x)
        data.close()
        print(x)
        x = x.split(";")
        print(x)
        x = x[0].split("\n")
        while "" in x:
            x.remove("")
        x = x[random.randint(0, len(x)-1)]
        x = x.split('|')
        chara.favor = chara.favor + (1 * chara.mood[0])
        return [chara.name, x, chara.favor]

    @staticmethod
    def getRandomGreeting():
        chara = CharacterList.characters[CharacterList.presentCharacters[CharacterList.selected]]
        data = open(renpy.loader.transfn("dialogue/{}/idle".format(chara.fileName)), "r")
        x = data.read()
        data.close()
        x = x.split(";")
        x = x[0].split("\n")
        while "" in x:
            x.remove("")
        return[chara.name, x]

    #Put the current characters in the presentCharacters list
    @staticmethod
    def getPresentCharacters():
        del CharacterList.presentCharacters[:]
        #Go through the characters
        for index in range(0, len(CharacterList.characters)):
            i = CharacterList.characters[index]
            #Go through the schedules
            for s in i.schedule:
                #Time to check if this character is supposed to be in your location
                if(s[0] == World.currentLoc):
                    if(Clock.getHrs() >= s[1] and Clock.getHrs() <= s[2]):
                        CharacterList.presentCharacters.append(i.id)

    #Initialize a list of characters
    #Type means the character list to load on the data folder
    @staticmethod
    def initCharacters():
        data = open(renpy.loader.transfn("data/characters"), "r")
        tx = data.read()
        data.close()
        tx = tx.split("\n")
        count = 0
        for i in tx:
            dat = i.split(",")
            CharacterList.characters.append(NPC(count, dat[0], dat[1], dat[2], dat[3], dat[4], dat[5], dat[6], dat[7], dat[8], dat[9], dat[10], dat[11]))
            count = count + 1

class World:
    locations = []
    currentLoc = 0

    @staticmethod
    def initWorld():
        print("Initializing World...")
        data = open(renpy.loader.transfn("data/locations"), "r")
        tx = data.read()
        data.close()
        tx = tx.split("\n")
        count = 0
        for i in tx:
            dat = i.split(",")
            World.addLoc(count, dat)
            count = count + 1

        print("done ".format(World.locations))
        print("Initializing Adyacency...")
        World.initAdyacency()

    @staticmethod
    def addLoc(id, data):
        World.locations.append(Location(id, data[0], data[1], data[2]))

    @staticmethod
    def initAdyacency():
        data = open(renpy.loader.transfn("data/adyacency"), "r")
        tx = data.read()
        data.close()
        tx = tx.split("\n")
        count = 0
        print("ch1 {}".format(tx))
        for i in tx:
            dat = i.split(",")
            print("dat {}".format(dat))
            World.locations[count].ady = functions.strToIntArrLocs(dat)
            count = count + 1
            print(count)

    @staticmethod
    def showTravelMenu():
        options = []
        for x in World.locations[World.currentLoc].ady:
            options.append((World.locations[x].name, World.locations[x].id))
        options.append(("Cancel", World.currentLoc))
        return options

    @staticmethod
    def getLocName():
        return World.locations[World.currentLoc].name

    @staticmethod
    def getCurrentType():
        return World.locations[World.currentLoc].getType()

    @staticmethod
    def getShopOwner():
        return World.locations[World.currentLoc].getCharacter()

    @staticmethod
    def changeCurrLocation(n):
        World.currentLoc = n

    @staticmethod
    def getCurrentMap():
        return World.locations[World.currentLoc].getMapID()

    #Get the present characters in your current location

class Location(object):
    def __init__(self, id, name, fileName, mapID):
        self.id = id
        self.name = name
        self.fileName = fileName
        self.mapID = mapID

        self.ady = []
        self.adyW = []

        self.characters = []
        self.enabled = True

    def getMapID(self):
        return self.mapID

#WIP
class ShopLocation(Location):
    def __init__(self, type, id, name, fileName, character, il):
        super(ShopLocation, self).__init__(type, id, name, fileName)
        self.character = character
        self.inventoryList = int(il)

    def getCharacter(self):
        return self.character

class Clock:
    #Just to give default hour
    hrs = 12
    min = 0
    #True to use 12:00 PM format
    #False to use 24:00 format
    timeMode = False

    @staticmethod
    def passTime(hrs, mins):
        mins += Clock.min
        hrs += int(mins/60)
        Clock.min = mins % 60

        hrs += Clock.hrs
        #Sum to days
        #sumDay(int(hrs/24))
        Clock.hrs = hrs % 24

    @staticmethod
    def getTime():
        if(Clock.timeMode):
            return "{:02d} : {:02d} {}".format((Clock.hrs % 12) +1, Clock.min, Clock.getAM())

        else:
            return "{:02d} : {:02d}".format(Clock.hrs +1, Clock.min)

    @staticmethod
    def getMin():
        return Clock.min
    @staticmethod
    def getHrs():
        return Clock.hrs + 1
    @staticmethod
    def getAM():
        if (Clock.hrs > 12):
            return "PM"
        return "AM"

    #Returns a string of the time of day based on the clock
    @staticmethod
    def getDayTime():
        if(Clock.hrs < 6): return "night"
        if(Clock.hrs < 17): return "day"
        if(Clock.hrs < 20): return "late"
        if(Clock.hrs < 24): return "night"
        return "night"
