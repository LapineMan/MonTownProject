init 0 python:
    def get_enemy_dialogue(character, type):
        print(character.name)
        data = get_data_from_json("dialogue/enemy/{}_enemy_dialogue.json".format(character.fileName))
        data = data[type]
        return data

    def say_enemy_dialogue(e, speaker, type):
        lines = get_enemy_dialogue(speaker, type)
        lines = renpy.random.choice(lines)
        for l in lines:
            #renpy.show("{} {}".format(speaker.fileName, l[1]))
            renpy.say("{} {}".format(speaker.name, e), l[0])
