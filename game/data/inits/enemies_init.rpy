init 2 python:
    class Slime_Girl(Enemy):
        def __init__(self, level = 1):
            data = get_data_from_json("data/inits/enemy_stats/green_slime.json")
            Enemy.__init__(self, data)

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
