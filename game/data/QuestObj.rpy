init 8 python:
    class CheckboxStatus(Enum):
        EMPTY = 0
        SUCCESS = 1
        FAILURE = 2

    class QuestLog:
        def __init__(self):
            self.storyQuests = []
            self.sideQuests = []
            self.specialQuests = []

        def get_quest(self, name):
            # Just check all the lists and remove
            for section in self.storyQuests:
                for quest in section["quests"]:
                    if(quest["name"] == name):
                        return quest

            for section in self.sideQuests:
                for quest in section["quests"]:
                    if(quest["name"] == name):
                        return quest

            for section in self.specialQuests:
                for quest in section["quests"]:
                    if(quest["name"] == name):
                        return quest

            return "No quest found"

        def set_quest_status(self, name, status):
            quest = self.get_quest(name)
            quest["status"] = status


        def remove_quest_by_name(self, name):
            # Just check all the lists and remove
            for section in self.storyQuests:
                for quest in section["quests"]:
                    if(quest["name"] == name):
                        section["quests"].remove(quest)

            for section in self.sideQuests:
                for quest in section["quests"]:
                    if(quest["name"] == name):
                        section["quests"].remove(quest)

            for section in self.specialQuests:
                for quest in section["quests"]:
                    if(quest["name"] == name):
                        section["quests"].remove(quest)

            return "Could not remove a quest"

        def add_section(self, type, name):
            if(type == 0):
                self.storyQuests.append(
                    {
                        "name":name,
                        "quests":[]
                    }
                )

        def add_story_quest(self, sec, name, description):
            for section in self.storyQuests:
                print("{} == {}".format(section["name"], sec))
                if(section["name"] == sec):
                    section["quests"].append({
                        "name":name,
                        "description":description,
                        "status":CheckboxStatus.EMPTY
                    })
                    return "Successfully added quest"

        def add_side_quest(self, sec, name, description):
            for section in self.sideQuests:
                if(section["name"] == sec):
                    section["quests"].append({
                        "name":name,
                        "description":description,
                        "status":CheckboxStatus.EMPTY
                    })
