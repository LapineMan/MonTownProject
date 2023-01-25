import enum

class Week(enum.Enum):
    MON = 0
    TUE = 1
    WEN = 2
    THU = 3
    FRI = 4
    SAT = 5
    SUN = 6

class State(enum.Enum):
    NORMAL = 0
    WORKING = 1
    SLEEPING = 2
    BREAK = 3


class Schedule:
    def __init__(self):
        self.schedule = {
            Week.MON:[(0,0,State.SLEEPING), (7,0,0), (9,1,2), (12,3,3), (1,1,1), (6,3,0), (8,2,0), (10,0,2)],
            Week.TUE:[1],
            Week.WEN:[2, 3],
            Week.THU:[4, 5],
            Week.FRI:[6, 7],
            Week.SAT:[8, 9],
            Week.SUN:[10]
        }

class Activity:
    def __init__(self, hour, locationId, state):
        self.hour = hour
        self.locationId = locationId
        self.state = state


currWeekDay = Week.MON
c = Schedule()
print(c.schedule[currWeekDay])
