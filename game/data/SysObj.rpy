init 3 python:
        #Determines time of day in game
    class Clock(store.object):
        def __init__(self):
            #Just to give default hour
            self.hrs = 12
            self.min = 0
            #True to use 12:00 PM format
            #False to use 24:00 format
            self.timeMode = False

        def passTime(self, hrs, mins):
            mins += self.min
            hrs += int(mins/60)
            self.min = mins % 60

            hrs += self.hrs
            #Sum to days
            #sumDay(int(hrs/24))
            self.hrs = hrs % 24

        def getTime(self):
            if(self.timeMode):
                return "{:02d} : {:02d} {}".format((self.hrs % 12) +1, self.min, self.getAM())
            else:
                return "{:02d} : {:02d}".format(self.hrs +1, self.min)

        def getMin(self):
            return self.min
        def getHrs(self):
            return self.hrs + 1
        def getAM(self):
            if (self.hrs > 12):
                return "PM"
            return "AM"

        #Returns a string of the time of day based on the clock
        def getDayTime(self):
            if(self.hrs < 6): return "night"
            if(self.hrs < 17): return "day"
            if(self.hrs < 20): return "late"
            if(self.hrs < 24): return "night"
            return "night"

    class Event_Trigger:
        def __init__(self, labelName, place = None, character = None, timeStart = None, timeEnd = None):
            # Label name to jump to
            self.labelName = labelName
            self.place = place
            self.character = character
            self.timeStart = timeStart
            self.timeEnd = timeEnd

        def is_triggered(self, place=None, character=None, currentTime=None):
            # Check if place matters
            if(self.place != None):
                # Check if player is in that place
                if(self.place != place):
                    return False

            if(self.character != None):
                # Check if player is in that place
                if(self.character != character):
                    return False


            if(self.timeStart != None and self.timeEnd != None):
                if(currentTime < self.timeStart and currentTime >= self.timeEnd):
                    return False

            # It is in time and place
            return True
