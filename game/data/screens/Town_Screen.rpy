#What you should see during the normal locations
screen Town_UI(player, inventory, questLog):

    # Variables to use
    python:
        currTime = clock.getTime()
        currPlace = world.get_current_location_name()

    hbox:
        xalign 0.0
        yalign 0.025
        xfill True

        hbox:
            xfill False
            xalign 0.98
            order_reverse True
            spacing 20

            if(not renpy.get_screen("say")):
                imagebutton auto "gui/map_%s.png" action [ Hide("Town_UI"), Jump("Map_update") ]
                imagebutton auto "gui/profile_%s.png" action ShowTransient("Player_Stat_Screen", player = player)
                imagebutton auto "gui/heart_%s.png" action ShowTransient("Quest_Log", questLog = questLog)
                imagebutton auto "gui/inventory_%s.png" action ShowTransient("Inventory_Screen", player=player, inventory=inventory)
            imagebutton auto "gui/options_%s.png" action ShowMenu('preferences')

#    if(not renpy.get_screen("say")):
