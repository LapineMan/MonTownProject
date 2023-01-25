import renpy
import classes

#Functions

def sayT(character):
    data = open(renpy.loader.transfn("dialogue/{currentCharacter}.txt"),"r")
    lines = data.readlines()
    for i in lines:
        renpy.say("Etica", i)

def strToIntArrLocs(arr):
    result = []
    count = 0
    print("func {}".format(arr))
    for i in arr:
        result.append(int(arr[count])-1)
        count = count + 1
    print("done {}".format(result))
    return result

def charNameExists(name, characters):
    for i in characters:
        if(name.lower() == i.name.lower()): return True
    return False

def getIntroStatGrowths(boon, bane):
    stats = [classes.Player.ATK, classes.Player.SPD, classes.Player.INT, classes.Player.DEF, classes.Player.RES, classes.Player.WIL]
    sumIntroStats(boon, stats, 2)
    sumIntroStats(bane, stats, -2)
    return stats

def sumIntroStats(i, stats, s):
    if(i==0):
        stats[0] += s
        stats[3] += s
    elif(i==1):
        stats[2] += s
        stats[4] += s
    elif(i==2):
        stats[1] += s
    else:
        stats[5] += s
    return

def checkFor0(arr):
    for i in arr:
        if(i < 0.5):
            i = 0.5

def assignBaseStats(boon, bane):
    #Stats
    stats = [classes.Player.ATK, classes.Player.SPD, classes.Player.INT, classes.Player.DEF, classes.Player.RES, classes.Player.WIL]
    sumIntroStats(boon, stats, 2.0)
    sumIntroStats(bane, stats, -2.0)
    checkFor0(stats)
    #Growths
    growths = [classes.Player.ATK_G, classes.Player.SPD_G, classes.Player.INT_G, classes.Player.DEF_G, classes.Player.RES_G, classes.Player.WIL_G]
    sumIntroStats(boon, stats, 0.4)
    sumIntroStats(bane, stats, -0.4)
    checkFor0(growths)
    #Base stat change
    classes.Player.ATK = stats[0]
    classes.Player.SPD = stats[1]
    classes.Player.INT = stats[2]
    classes.Player.DEF = stats[3]
    classes.Player.RES = stats[4]
    classes.Player.WIL = stats[5]
    #Base growth change
    classes.Player.ATK_G = growths[0]
    classes.Player.SPD_G = growths[1]
    classes.Player.INT_G = growths[2]
    classes.Player.DEF_G = growths[3]
    classes.Player.RES_G = growths[4]
    classes.Player.WIL_G = growths[5]
