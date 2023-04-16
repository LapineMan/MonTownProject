label Town_Label:
    #Check for events
    scene black
    python:
        renpy.block_rollback()
        renpy.scene()
        #renpy.with_statement(transition)
        show_current_background(world, time_manager)
        character_list.set_present_characters(world, time_manager)

    show screen Character_Select_Screen(character_list)
    show screen Town_UI(player, inventory, quest_log, world)
    with dissolve
    while True:
        pause
    return
