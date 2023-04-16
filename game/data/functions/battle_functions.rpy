init 20 python:

    # Visual Stuff
    def play_enemy_hit_anim(target):
        expressions = get_data_from_json("dialogue/enemy/{}_enemy_dialogue.json".format(target.fileName))["hurt"]
        show_enemy(target, attributes = expressions, atList = [hit_shake])
        return expressions

    # check if an enemy has been defeated
    def check_defeated(enemies):
        for e in enemies:
            if(e.is_defeated() and not e.defeatedFlag):
                dialogue = get_data_from_json("dialogue/enemy/{}_enemy_dialogue.json".format(e.fileName))
                defeatedExpression = dialogue["defeated"]
                dialogue = renpy.random.choice(dialogue["defeat"])
                for line in dialogue:
                    if(line[0] == ""):
                        speaker = e.name
                    else:
                        speaker = line[0]
                    img = e.fileName + " " +line[1]
                    renpy.show("{}".format(img), tag="{}_{}".format(e.fileName, e.tempId))
                    renpy.say("{}".format(speaker), "{}".format(line[2]))
                    img = revert_expressions(img)
                    show_enemy(e, attributes = img)
                    renpy.show("{}".format(img), tag="{}_{}".format(e.fileName, e.tempId))
                e.defeatedFlag = True
                show_enemy(e, attributes = defeatedExpression, atList = [darken])

    # This is if I ever want to add flee conditions
    def flee_check(player, enemies):
        return True

    # check if all enemies have been defeated
    def is_everyone_defeated(enemies):
        for e in enemies:
            if(not e.is_defeated()):
                return False
        return True

    # Simple attack action functionality
    def attack(attacker, target, multiplier = 1.0):
        isEnemy = not isinstance(target, Player)

        if isEnemy : expressions = play_enemy_hit_anim(target)

        dmgDealt = target.deal_damage(int(attacker.atk * multiplier), attacker.attack_type)
        if not isEnemy : renpy.with_statement(vpunch)
        if(isinstance(attacker, Player)):
            if(attacker.weapon == None):
                renpy.sound.play("sounds/sfx/punch1.mp3", relative_volume = 1.2)
            else:
                renpy.sound.play("sounds/sfx/{}.mp3".format(attacker.weapon["hit_sound"]), relative_volume = 1.2)

        renpy.say(None,"{} received {} damage".format(target.name, dmgDealt))
        if(isEnemy):
            expressions = revert_expressions(expressions)
            print(expressions)
            show_enemy(target, attributes = expressions)

        return dmgDealt


    # Used for the simple attack action, no skill nor specials
    def attack_action(attacker:RpgStats, targets:[RpgStats]):
        for t in targets:
            attack(attacker, t)


    # Get turn order for battle
    def order_by_speed(array):
        array.sort(key=lambda entity: entity.spd, reverse=True)
