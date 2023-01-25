screen Battle_Screen:
    $hbox_hsize = 200
    $hbox_vsize = 540
    $global_padding = 25
    vbox:
        hbox:
            xfill True
            ysize hbox_vsize
            # Self status
            frame:
                background color((0, 0, 10, 180))
                yalign 0.5
                xsize 280
                ysize 720
                vbox:
                    xsize hbox_hsize
                    yalign 0.3
                    xalign 0.5
                    spacing global_padding
                    vbox:
                        text "[player.name]"
                        text "[player.lvl]"
                        text "HP: [player.hp] / [player.maxHp]"
                        bar value player.hp range player.maxHp xalign 0.0 yalign 0.0 xmaximum 200
                        text "MP: [player.mp] / [player.maxMp]"
                        bar value player.mp range player.maxMp xalign 0.0 yalign 0.0 xmaximum 200


            # Scene
            # Enemy status
            frame:
                background color((0, 0, 10, 180))
                xalign 1.0
                xsize 280
                ysize 720
                vbox:
                    xsize hbox_hsize
                    yalign 0.1
                    xalign 0.5
                    spacing global_padding
                    for e in enemies:
                        vbox:
                            text "[e.name] [e.tempId]"
                            text "[e.lvl]"
                            text "HP:[e.hp] / [e.maxHp]"
                            bar value e.hp range e.maxHp xalign 0.0 yalign 0.0

screen target_select_screen:
    frame:
        modal True
        xsize 750 ysize 250
        align (0.5, 0.5)
        vbox:
            spacing 30
            align (0.5, 0.5)
            hbox:
                align (0.5, 0.5)
                spacing 80
                box_wrap True
                box_wrap_spacing 40
                for e in enemies:
                    if not e.is_defeated():
                        textbutton "{} {}".format(e.name, e.tempId) action Return({"target":[e], "action":1})
                    else:
                        textbutton "{} {}".format(e.name, e.tempId) action NullAction()

            textbutton "Back":
                action (Hide("target_select_screen"))
                xalign 0.5

screen Choose_Battle_Action:
#   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #
#   Action list:
#       Run 8
#
#   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #
    $global_padding = 25
    modal True
    if(True):
    # if(not renpy.get_screen("say")):
        frame:
            yalign 1.0
            ysize 200
            hbox:
                xfill True
                yalign 0.5
                xalign 0.5
                vbox:
                    xalign 0.5
                    spacing global_padding
                    textbutton "Attack":
                        action (ShowTransient("target_select_screen", enemies=enemies))
                    textbutton "Skills":
                        action (ShowTransient("Skill_Screen", subject = player, targets = enemies))
                    #textbutton "Magic WIP" action NullAction()

                vbox:
                    xalign 0.5
                    spacing global_padding
                    #textbutton "Talk WIP" action (NullAction())
                    textbutton "Defend" action (Return({"action":5}))
                    textbutton "Wait" action (Return({"action":6}))

                vbox:
                    xalign 0.5
                    spacing global_padding
                    textbutton "Item" action (ShowTransient("Inventory_Screen", player = player, inventory = inventory))
                    textbutton "Flee" action (Return({"action":8}))
