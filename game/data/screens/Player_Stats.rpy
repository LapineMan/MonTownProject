#Show character stats
screen Player_Stat_Screen(player):
    modal True
    frame:
        xalign 0.5 yalign 0.4
        padding (80, 50)
        vbox:
            text "{} LV.{}".format(player.name, player.lvl) xalign 0.5
            text ""
            hbox:
                spacing 50
                hbox:
                    spacing 20
                    vbox:
                        text "Health:"
                        text "Mana:"
                        text "Attack:"
                        text "Defense:"
                        text "Inteligence:"
                        text "Resistance:"
                        text "Willpower:"
                    vbox:
                        text "{} / {}".format(player.hp, player.maxHp)
                        text "{} / {}".format(player.mp, player.maxMp)
                        text "{}".format(player.atk)
                        text "{}".format(player.dfn)
                        text "{}".format(player.mag)
                        text "{}".format(player.res)
                        text "{}".format(player.wil)
                vbox:
                    text "Battle EXP:"
                    text "{}".format(player.battleExp) xalign 1.0
                    text "Social EXP:"
                    text "{}".format(player.socialExp) xalign 1.0
                    text "Cooking EXP:"
                    text "{}".format(player.cookingExp) xalign 1.0
            text ""
            textbutton "Back":
                xalign 0.5
                action Hide("Player_Stat_Screen")
