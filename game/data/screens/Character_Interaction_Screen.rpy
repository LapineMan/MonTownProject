screen Character_Interaction_Screen:
    modal True
    hbox:
        text "[characterlist.selected]"
    frame:
        pos (0.4, 0.1)
        xysize (0.6, 0.8)
        vbox:
            xalign 0.05
            null height 35
            text "Charna":
                size 50
            null height 30
            vbox:
                spacing 25
                xalign 0.5
                if(not renpy.get_screen("say")):
                    textbutton "Talk":
                        action Function(characterlist.say_current_dialogue, "talk")
                    textbutton "Give":
                        action [NullAction()]
