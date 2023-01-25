# Transforms specific for this screen
transform characterSelectScreenSelected:
    on idle:
        linear 0.1 matrixcolor TintMatrix("#BBBBBB")
    on hover:
        linear 0.1 matrixcolor TintMatrix("#FFFFFF")

transform characterSelectScreenSide:
    on idle:
        linear 0.1 matrixcolor TintMatrix("#888888")
    on hover:
        linear 0.1 matrixcolor TintMatrix("#FFFFFF")

transform unselectedChar:
    zoom 0.85

transform mid_to_left:
    xalign 0.5
    easeout 0.5:
        xalign 0.1

screen Character_Select_Screen:

    python:
        current_character = characterlist.get_selected_character()
        next_character = characterlist.get_next_character()
        prev_character = characterlist.get_prev_character()

#    vbox:
#        text "[characterlist.selected]"

#        text "[current_character.fileName]"


    if(prev_character != None):
        imagebutton idle prev_character.fileName at characterSelectScreenSide, unselectedChar:
            action [
            Function(characterlist.move_prev),
            SetScreenVariable("prev_character", characterlist.get_prev_character()),
            SetScreenVariable("next_character", characterlist.get_next_character()),
            SetScreenVariable("current_character", characterlist.get_selected_character())
            ]
            align(0.075, 1.0)

    if(next_character != None):
        imagebutton idle next_character.fileName at characterSelectScreenSide, unselectedChar:
            action [
            Function(characterlist.move_next),
            SetScreenVariable("prev_character", characterlist.get_prev_character()),
            SetScreenVariable("next_character", characterlist.get_next_character()),
            SetScreenVariable("current_character", characterlist.get_selected_character())
            ]
            align(0.925, 1.0)

    if(current_character !=  None):
        imagebutton idle current_character.fileName at characterSelectScreenSelected:
            sensitive (not renpy.get_screen("say"))
            action [Hide("Town_UI"),Jump("Character_Interaction_Label")]
            align(0.5, 1.0)
