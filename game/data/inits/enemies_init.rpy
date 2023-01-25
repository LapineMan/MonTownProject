init 2 python:
    class Slime_Girl(Enemy):
        def __init__(self):
            Enemy.__init__(self, "Green Slime", "greenslime", "A slime with higher sentience", ["Common_Herb"], 1.0)
            #                    HP MP ATK DFN MAG RES SPD WIL
            self.set_base_stats([25, 25, 23, 23, 30, 5, 15, 25])
            self.set_base_growths([5, 5, 2, 2, 2, 1, 2, 4])

        def attack(self, target):
            dialogue = get_data_from_json("dialogue/enemy/{}_enemy_dialogue.json".format(self.fileName))
            dialogue = renpy.random.choice(dialogue["attack"])
            for line in dialogue:
                if(line[0] == ""):
                    speaker = self.name
                else:
                    speaker = line[0]
                img = self.fileName + " " +line[1]
                renpy.show("{}".format(img), tag="{}_{}".format(self.fileName, self.tempId))
                renpy.say("{}".format(speaker), "{}".format(line[2]))
                renpy.play("sounds/sfx/squelch.mp3")
                attack(self, player)
                img = img.replace(' ', ' -')
                print(img)
                renpy.show("{}".format(img), tag="{}_{}".format(self.fileName, self.tempId))


    class Baphi_Intro(Enemy):
        def __init__(self):
            Enemy.__init__(self, "Baphomet", "baphi", "A slime with higher sentience", ["Common_Herb"], 1.0)
            #                    HP MP ATK DFN MAG RES SPD WIL
            self.set_base_stats([1000, 600, 25, 25, 80, 20, 15, 25])
            self.set_base_growths([1, 1, 1, 1, 1, 1, 1, 1])

        def attack(self, target):
            dialogue = get_data_from_json("dialogue/enemy/{}_enemy_dialogue.json".format(self.fileName))
            dialogue = renpy.random.choice(dialogue["attack"])
            for line in dialogue:
                if(line[0] == ""):
                    speaker = self.name
                else:
                    speaker = line[0]
                img = self.fileName + " " +line[1]
                renpy.show("{}".format(img), tag="{}_{}".format(self.fileName, self.tempId))
                renpy.say("{}".format(speaker), "{}".format(line[2]))
                attack(self, player)
                img = img.replace(' ', ' -')
                print(img)
                renpy.show("{}".format(img), tag="{}_{}".format(self.fileName, self.tempId))
