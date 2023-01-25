label battle_label(battle_params = {"enemies": [Slime_Girl()], "background":"mountain6", "music":"end_of_road", "canFlee":True}):
    python:
        # Setup Data
        enemies = battle_params["enemies"]
        inventory.is_in_battle = True
        battleEnd = None
        turn = 0

        for i in range(len(enemies)):
            enemies[i].tempId = i

        # Set turn order
        order = (enemies + [player])
        order_by_speed(order)

        # Setup the visuals
        renpy.music.play("sounds/music/{}.mp3".format(battle_params["music"]), loop = True)
        renpy.scene()
        renpy.show("{}".format(battle_params["background"]))
        renpy.with_statement(fade)

        renpy.show_screen("Battle_Screen", player, enemies, order, turn)
        renpy.with_statement(dissolve)
        show_characters_by_order(enemies)

    # Battle start dialogue
    if("initial_dialogue" in battle_params):
        $renpy.say("{}".format(battle_params["initial_dialogue"][0]),"{}".format(battle_params["initial_dialogue"][1]))
    else:
        "Battle Start"

    while not battleEnd:
        python:
            # Reset some values
            # PrePhase
            for e in order:
                if(Status_Effect_Type.PHASE_START in e.statuses):
                    for s in e.statuses[Status_Effect_Type.PHASE_START].keys():
                        s.effect(e)

            # Follow the order
            for e in order:
                #Check if battle is over
                e.isDefending = False

                # Pre turn debuff
                if(Status_Effect_Type.TURN_START in e.statuses):
                    for s in e.statuses[Status_Effect_Type.TURN_START].keys():
                        s.effect(e)

                if(player.is_defeated()):
                    endType = "Defeat"
                    break
                if(is_everyone_defeated(enemies)):
                    battleEnd = "Victory"
                    break
                # Player action
                if(e == player):
                    _window_hide()
                    # Check for event

                    # Choose action
                    actionInfo = renpy.call_screen("Choose_Battle_Action")

                    # Attack
                    if(actionInfo["action"] == 1):
                        if(actionInfo["target"] == None):
                            attack_action(player, enemies)
                        else:
                            attack_action(player, actionInfo["target"])

                    # Skill
                    elif(actionInfo["action"] == 2):
                        actionInfo["skill"].use(player, [actionInfo["target"]])

                    # Defend
                    elif(actionInfo["action"] == 5):
                        player.isDefending = True
                        renpy.say("Defending","You brace yourself for incoming attacks")

                    # Wait
                    elif(actionInfo["action"] == 6):
                        renpy.say("","You wait to see what the enemy will do")

                    # Item
                    elif(actionInfo["action"] == 7):
                        actionInfo["item"].use_item(player)

                    # Escape
                    elif(actionInfo["action"] == 8):
                        renpy.say("", "You attempt an escape!")
                        if(battle_params["canFlee"]):
                            # Function to decide if flee was successful
                            if(flee_check(player, enemies)):
                                battleEnd = "Escaped"
                                break
                            else:
                                renpy.say("", "But you couldn't!")
                        else:
                            renpy.say("", "But you cannot flee from this battle!")
                    else:
                        renpy.say("","Nothing Happens")
                        pass



                # Enemy Action
                else:
                    # If defeated, skip
                    if(e.is_defeated()):
                        continue

                    e.attack(player)

                # Check post turn shenanigans
                # Post Turn Effects
                if(Status_Effect_Type.TURN_END in e.statuses):
                    for s in e.statuses[Status_Effect_Type.TURN_END].keys():
                        s.effect(e)
                check_defeated(enemies)

        $turn += 1
    python:
        # Post battle adjustments
        del order
        for i in enemies:
            del i
        inventory.is_in_battle = False

    stop music fadeout 0.1
    if("endTheme" not in battle_params):
        play sound "sounds/music/battle_end.mp3"
    elif(battle_params["endTheme"] != None):
        $renpy.sound.play("sounds/music/{}.mp3".format(battle_params["endTheme"]))
    hide screen Battle_Screen with dissolve
    "Battle ended as [battleEnd]"
    stop music
    stop sound
    return
