init 10 python:

    # This class will be in charge of checking if a trigger should be checked

    class EventManager:
        def __init__(self):
            self.triggers = []

        def add_event(self, event_label:str, location:str = None, character:str = None, daytime:str = None, item:str = None):
            trigger = {}

            if(location):
                trigger["location"] = location
            if(character):
                trigger["character"] = character
            if(daytime):
                trigger["daytime"] = daytime
            if(item):
                trigger["item"] = item

            trigger["event_label"] = event_label

            self.triggers.append(trigger)

        def delete_event(self, event_label:str):
            for i in range(len(self.triggers)):

                if(self.triggers[i]["event_label"] == event_label):
                    del self.triggers[i]
                    return True

            return False

        def check_triggers(self, location:str = None, character:str = None, daytime:str = None, item:str = None):
            for t in self.triggers:

                flag = True

                if(location):
                    if(t["locations"] != location):
                        flag = False
                if(character):
                    if(t["character"] != character):
                        flag = False
                if(daytime):
                    if(t["daytime"] != daytime):
                        flag = False
                if(item):
                    if(t["item"] != item):
                        flag = False

            if(flag):
                renpy.notify("Event: {}".format(t["event_label"]))
                renpy.jump(t["event_label"])
