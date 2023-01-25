screen Skill_Screen(subject, targets):

    python:
        tooltip = GetTooltip()

    if tooltip:
        text "[tooltip]":
            color "#FFFFFF"
            outlines [ (absolute(8), "#000", absolute(0), absolute(0)) ]
    modal True
    frame:
        align (0.5, 0.3)
        xysize (640, 360)
        padding(30, 40)
        vbox:
            text "Skill list"
            text "- - -"
            align (0.5,0.5)
            viewport:
                spacing 20
                draggable True
                scrollbars "vertical"
                for i in range(len(subject.skills)):
                    if(subject.skills[i].manaCost <= subject.mp):
                        textbutton "{}".format(subject.skills[i].name):
                            action (ShowTransient("skill_select_screen", skill = subject.skills[i], targets=targets))
                            tooltip "{}: {}".format(subject.skills[i].name, subject.skills[i].description)
                    else:
                        textbutton "{}".format(subject.skills[i].name):
                            action NullAction()
                            tooltip "{}: {}".format(subject.skills[i].name, subject.skills[i].description)

        textbutton "Cancel":
            align (0.5, 0.9)
            action Hide("Skill_Screen")

screen skill_select_screen(skill, targets):
    frame:
        modal True
        xysize (640, 360)
        align (0.5, 0.3)
        vbox:
            text "Select target"
            spacing 30
            align (0.5, 0.5)
            hbox:
                align (0.5, 0.5)
                spacing 80
                box_wrap True
                box_wrap_spacing 40
                for t in targets:
                    if(not t.is_defeated()):
                        textbutton "{} {}".format(t.name, t.tempId) action (Return({"action":2, "skill":skill, "target":t}))
                    else:
                        textbutton "{} {}".format(t.name, t.tempId) action NullAction()

            textbutton "Cancel":
                action (Hide("skill_select_screen"))
                xalign 0.5
