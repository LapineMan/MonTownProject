#Show character stats
screen Player_Stat_Screen(player):
    modal True
    frame:
        xalign 0.5 yalign 0.4
        padding (80, 50)
        vbox:
            text "{} LV.{}".format(player.name, player.level) xalign 0.5
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
                        text "Magic:"
                        text "Resistance:"
                        text "Speed:"
                    vbox:
                        text "{} / {}".format(player.current_hp, player.max_hp)
                        text "{} / {}".format(player.current_mp, player.max_mp)
                        text "{}".format(player.attack)
                        text "{}".format(player.defense)
                        text "{}".format(player.magic)
                        text "{}".format(player.resistance)
                        text "{}".format(player.speed)
                vbox:
                    text "Battle EXP:"
                    text "{}".format(player.battle_exp) xalign 1.0
                    text "Social EXP:"
                    text "{}".format(player.social_exp) xalign 1.0
                    text "Cooking EXP:"
                    text "{}".format(player.cooking_exp) xalign 1.0
            text ""
            textbutton "Back":
                xalign 0.5
                action Hide("Player_Stat_Screen")
