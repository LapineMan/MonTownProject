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

screen Character_Select_Screen(cList):

    python:
        current_character = cList.get_current_character()
        next_character = cList.get_next_character()
        prev_character = cList.get_prev_character()

#    vbox:
#        text "[characterlist.selected]"

#        text "[current_character.fileName]"


    if(prev_character):
        imagebutton idle prev_character.fileName at characterSelectScreenSide, unselectedChar:
            action [
            Function(cList.scroll_characters, -1),
            SetScreenVariable("prev_character", cList.get_prev_character()),
            SetScreenVariable("next_character", cList.get_next_character()),
            SetScreenVariable("current_character", cList.get_selected_character())
            ]
            align(0.075, 1.0)

    if(next_character):
        imagebutton idle next_character.fileName at characterSelectScreenSide, unselectedChar:
            action [
            Function(cList.scroll_characters, 1),
            SetScreenVariable("prev_character", cList.get_prev_character()),
            SetScreenVariable("next_character", cList.get_next_character()),
            SetScreenVariable("current_character", cList.get_selected_character())
            ]
            align(0.925, 1.0)

    if(current_character):
        imagebutton idle current_character.fileName at characterSelectScreenSelected:
            sensitive (not renpy.get_screen("say"))
            action [Hide("Town_UI"),Jump("Character_Interaction_Label")]
            align(0.5, 1.0)
