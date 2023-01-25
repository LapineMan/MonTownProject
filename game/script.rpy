# The script of the game goes in this file.
init 0 python:
    import sys
    import renpy.store as store
    import renpy.exports as renpy # we need this so Ren'Py properly handles rollback with classes
    import random
    import json
    import os
    import math
    from abc import ABC, abstractmethod
    from enum import Enum

image red = Solid("#FF0000")

#Check if it is a map transition
label Map_update:
    window hide
    hide screen Character_Select_Screen
    scene black
    python:
        # Reset the selected character
        characterlist.selected = 0
        # Show map screen then wait for answer
        selectedLocation = renpy.call_screen("Map_Screen", world)

        # Update current Location
        world.set_current_location(selectedLocation)

        # Check to what type of location you are moving to and send player to it
        if(world.get_current_location_type() == LocType.TRANSITION):
            renpy.jump("Transition_Label")
        elif(world.get_current_location_type() == LocType.NORMAL):
            renpy.jump("Town_Label")
        elif(world.get_current_location_type() == LocType.SHOP):
            renpy.jump("Shop_Label")
        elif(world.get_current_location_type() == LocType.ADVENTURE):
            renpy.jump("Adventure_Label")
        else:
            # By default returns you to a home label
            renpy.jump("Home_Label")

#Scene used everytime you leave a zone
label Transition_Label:
    $updateScene()
    #Check for event
    "Walking through the path"
    "Nothing interesting happens"
    jump Map_update

#image defines
image right_arrow = im.Flip("gui/arrow.png", horizontal="True")

#Character defines, only used for cutscenes

label start:
    stop music
    scene black
    call hide_screens from _call_hide_screens_1
    menu:
        "Test zone"
        "Start":
            jump init_game
        "Layered Image Test":
            jump Layered_Test
        "Inventory test":
            jump inv_test
        "Quicktest":
            jump char_test

    return

label char_test:
    scene black with fade
    "Start test"
    window hide

    show baphi_face

    pause
    "End Test"
    jump start

label Layered_Test:
    "Start"
    "We Show em"
    scene oven
    show reina
    show chien at left with vpunch
    show charna at right
    "Here they are"
    show reina of_casual ey_mid mo_pout eb_hmm with vpunch
    show charna mo_vhappy eb_hmm ey_closed blush
    show chien ey_mid eb_hmm
    "Cute expressions?"
    show reina of_underwear ey_closed mo_serious eb_angry blush with hpunch
    show charna mo_serious eb_down ey_mid blush sweatdrop of_underwear
    show chien eb_down ey_embarrased
    "hoh...!"
    show reina ey_mid mo_v eb_hmm of_none
    show charna eb_up mo_open ey_closed of_none ta_open
    show chien eb_up ey_pupil mo_angry of_none
    "OH!"
    pause 3.0
    scene oven
    "The end"
    jump start

label init_game:
    "Initializing . . .{nw}"

    # Important Characters
    define cha = Character("Charna", who_color="#808080", image="charna")
    define rei = Character("Reina", who_color="#808080", image="reina")
    define chi = Character("Chien", who_color="#808080", image="chien")
    define lap = Character("Lapin", who_color="#808080", image="lapin")
    define liz = Character("Lizette", who_color="#808080", image="liz")
    define bel = Character("Belial", who_color="#808080", image="belial")
    define bap = Character("? ? ?", who_color="#ea2100", image="baphi")
    define bor = Character("Boris", who_color="#808080", image="boris")
    define b_slime = Character("Mother Slime", who_color="#6ea5b4", image="slimemother")
    define g_slime = Character("Green Slime", who_color="#5ba179", image="GreenSlime")

    #Misc Characters
    define shop = Character("Shopkeeper")

    python:
        # Init Player stuff
        player = Player()
        inventory = Inventory()

        player.skills.append(Skill_Double_Strike())

        # Init Characters
        characterlist = CharacterList()

        # Init World
        world = World()

        # Init Clock
        clock = Clock()

        # c = generate_characters(characterlist.characters)

        # Init event triggers and append first event
        eventTriggers = []
        eventTriggers.append(Event_Trigger("Reina_Boris_Intro", 0, None, None, None))

        # Init quest object
        questLog = QuestLog()

        # Temp variable

        renpy.block_rollback()
    "Finished Initialization"
    menu:
        "QuickTest":
            jump Town_Label
        "Demo":
            jump Game_Start
        "Battle screen test":
            "Starting Battle Test. . ."
            call battle_label(
                {
                    "enemies" : [Slime_Girl(), Slime_Girl()],
                    "background" : "mountain6",
                    "music" : "end_of_road",
                    "flee" : False,
                    "initial_dialogue":["","The slime girl wants to battle!"]
                }
            ) from _call_battle_label
            "Battle ended with [battleEnd]"
            return

label inv_test:
    python:
        inventory = Inventory()
        inventory.add_item(Bandage_1())
        inventory.add_item(Bandage_2())
        inventory.add_item(Bandage_3())
        inventory.add_item(Bandage_1())
        inventory.add_item(Bandage_1())
        inventory.add_item(Bandage_1())
        inventory.add_item(Bandage_1())
        inventory.add_item(Bandage_1())
        inventory.add_item(Bandage_1())
        inventory.add_item(Bandage_1())
        player = Player()
    "Start"
    scene oven
    call screen Inventory_Screen(player, inventory)
    "End"
    jump start

label Adventure_Label:
    $updateScene()
    $check_and_call_for_events(eventTriggers, world.get_current_location(), None, clock.getHrs())
    show screen Character_Select_Screen
    show screen Town_UI(player, inventory, questLog)
    while True:
        menu:
            "Look for battle":
                "Buscar pleito"
                jump battle_label

            "Forage":
                "Buscar objetos"



label waking_up:
    $updateScene(transition="a")
    #check for morning events
    "This is the start of another day..."

label Town_Label:
    #Check for events
    scene black
    python:
        renpy.block_rollback()
        check_and_call_for_events(eventTriggers, world.get_current_location(), None, clock.getHrs())
        renpy.scene()
        #renpy.with_statement(transition)
        showCurrentBG(world, clock)
        characterlist.get_present_characters(world, clock)

    show screen Character_Select_Screen
    show screen Town_UI(player, inventory, questLog)
    with dissolve
    while True:
        pause
    return

label Character_Interaction_Label:
    scene
    python:
        showCurrentBG(world, clock)
        renpy.show("black", at_list = [customTransparent(0.25)])
        renpy.show(characterlist.get_selected_character().fileName)
    hide screen Character_Select_Screen
    with dissolve
    $renpy.show(characterlist.get_selected_character().fileName, at_list = [center])
    #$renpy.with_statement(move)
    while (True):
        menu(screen="choice2"):
            "Talk":
                $check_and_call_for_events(eventTriggers, world.get_current_location(), characterlist.get_selected_character_id(), clock.getHrs())
                $characterlist.say_current_dialogue("talk")
            #"Give item":
            #    $renpy.say("A", "Gift items, will be implemented when I have an inventory")
            #    call screen Inventory_Screen(player, inventory)
            #    "{nw}"
            "Back":
                $renpy.show(characterlist.get_selected_character().fileName, at_list = [center])
                jump Town_Label


label Old_Town_Label:
    #Check for events
    $renpy.block_rollback()
    $check_and_call_for_events(eventTriggers, world.get_current_location(), None, clock.getHrs())
    # Variable
    $looping = True
    show screen Town_UI(player, inventory, questLog)
    while True:
        $updateScene()
        menu(screen="choice2"):

            "Approach" if(not characterlist.present_is_empty()):
                $check_and_call_for_events(eventTriggers, world.get_current_location(), characterlist.get_selected_character_id(), clock.getHrs())
                $characterlist.say_current_dialogue("greeting")
                $looping = True
                while looping:

                    menu(screen="choice2"):
                        "Talk":
                            $characterlist.say_current_dialogue("talk")
                        "Give item":
                            $renpy.say("A", "Gift items, will be implemented when I have an inventory")
                            show screen Inventory_Screen(player, inventory)
                            "{nw}"
                        "Back":
                            $looping = False

            "Investigate Area":
                "A"
    return

label clock_test:
    show screen TimePlace
    while True:
        $updateScene()
        menu:
            "Add hour":
                $clock.passTime(1, 0)
            "Add 5 hours":
                $clock.passTime(5, 0)
            "Add 12 hours":
                $clock.passTime(12, 0)
            "Add min":
                $clock.passTime(0, 1)
            "Add 10 mins":
                $clock.passTime(0, 10)
            "Add 30 mins":
                $clock.passTime(0, 30)
            "Change style":
                $clock.timeMode = not clock.timeMode
            "Return":
                jump start
