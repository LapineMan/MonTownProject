label Shop_Label:
    scene black with fade
    $check_and_call_for_events(eventTriggers, world.get_current_location(), None, clock.getHrs())
    python:
        looping = True
        shopItemList = world.locations[world.get_current_location()].items

        shopTemp = get_NPC_dialogue_json(world.get_current_location_obj().shopkeeper, "greeting")

        renpy.show("{} {}".format("shopkeeper1", "mo_talk"), at_list=[middle_right])
        renpy.with_statement(dissolve)

    while(looping):
        show screen Shop_Screen(player, inventory, shopItemList) with dissolve
        pause 1
        $renpy.show("{} {}".format("shopkeeper1", "mo_happy"), at_list=[middle_right])
        pause
        hide screen Shop_Screen with dissolve
        show shopkeeper1 at center with move
        menu(screen="choice_shop"):
            "Do you want to leave the shop?"
            "yes":
                python:
                    looping = False
                    renpy.show("{} {}".format("shopkeeper1", "mo_talk"))
                "Thanks for your patronage!"
                scene black with fade
            "no":
                show shopkeeper1 at middle_right with move
                pass

    jump Map_update
