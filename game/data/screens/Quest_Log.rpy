screen Quest_Log(questLog):
    modal True
    default tab = 0
    default emptytext = "No quest selected"
    default selectedName = ""
    default selectedDesc = "No quest selected"
    default checkboxImg = "checkbox"
    python:
        def reset_questlog_screen_selections():
            selectedName = ""
            selectedDesc = "No quest selected"
    frame:
        xsize 0.75
        ysize 0.75
        background "screens/bg_questlog.png"
        xalign 0.5
        yalign 0.5
        padding (30, 40)
        vbox:
            xfill True
            hbox:
                xfill True
                spacing 30
                textbutton "Main Quest":
                    action [SetScreenVariable("tab", 0), SetScreenVariable("selectedDesc", emptytext), SetScreenVariable("selectedName", "")]
                    selected (tab == 0)
                textbutton "Side Quest":
                    action [SetScreenVariable("tab", 1), SetScreenVariable("selectedDesc", emptytext), SetScreenVariable("selectedName", "")]
                    selected (tab == 1)
                textbutton "Special Quest":
                    action [SetScreenVariable("tab", 2), SetScreenVariable("selectedDesc", emptytext), SetScreenVariable("selectedName", "")]
                    selected (tab == 2)
                textbutton "Close Log" action [Hide("Quest_Log")]
            null height 50
            hbox:
                xfill True
                spacing 50
                # Quest List
                viewport:
                    draggable True
                    xsize 0.5
                    # Main Quests
                    if(tab == 0):
                        vbox:
                            xfill True
                            box_wrap True
                            for section in questLog.storyQuests:
                                text "{}".format(section["name"])
                                for quest in section["quests"]:
                                    hbox:
                                        xfill True
                                        textbutton "{}".format(quest["name"]):
                                            selected (selectedName == quest["name"])
                                            yalign 0.5
                                            action [SetScreenVariable("selectedName", quest["name"]), SetScreenVariable("selectedDesc", quest["description"])]
                                        if(quest["status"] == CheckboxStatus.SUCCESS):
                                            $checkboxImg = "checkbox success"
                                        elif(quest["status"] == CheckboxStatus.FAILURE):
                                            $checkboxImg = "checkbox failure"
                                        else:
                                            $checkboxImg = "checkbox"
                                        frame:
                                            background checkboxImg
                                            xysize (45, 45)
                                            yalign 0.5
                                            xalign 1.0

                    # Side Quests
                    elif(tab == 1):
                        vbox:
                            xfill True
                            for section in questLog.sideQuests:
                                text "{}".format(section["name"])
                                for quest in section["quests"]:
                                    hbox:
                                        xfill True
                                        textbutton "{}".format(quest["name"]):
                                            yalign 0.5
                                            action [SetScreenVariable("selectedName", quest["description"])]
                                        text "{}".format(quest["completed"]) yalign 0.5  xalign 1.0

                # Selected Quest description
                viewport:
                    draggable True
                    xsize 1.0
                    xfill True
                    text "{}".format(selectedDesc)
