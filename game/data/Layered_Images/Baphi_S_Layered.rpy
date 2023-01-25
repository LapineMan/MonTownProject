image baphscare_eyes_slow:
    "baphscare_pupils"
    block:
        choice:
            easein 1.5 xoffset 5 yoffset 5
        choice:
            easein 1.5 xoffset -5 yoffset -5
        choice:
            easein 1.5 xoffset 5 yoffset -5
        choice:
            easein 1.5 xoffset -5 yoffset 5
        1.5
        easein 1.5 xoffset 0 yoffset 0
        repeat

image baphscare_eyes_twitch:
    "baphscare_pupils"
    block:
        choice:
            linear 0.01 xoffset 5 yoffset 5
        choice:
            linear 0.01 xoffset -5 yoffset -5
        choice:
            linear 0.01 xoffset 5 yoffset -5
        choice:
            linear 0.01 xoffset -5 yoffset 5

        linear 0.01 xoffset 0 yoffset 0
        repeat

image baph_bg_blinking:
    "baphscare_bg"
    blinking(0.05)

image lines_1_shake:
    "baphscare_lines1"
    fast_shake(20)

image lines_2_shake:
    "baphscare_lines2"
    fast_shake(50)

image lines_3_shake:
    "baphscare_lines3"
    fast_shake(80)


layeredimage baphi_face:
    attribute red:
        "baph_bg_blinking"
        pos(152, 204)

    attribute lines_1:
        "lines_1_shake"
        pos(227, 257)

    attribute lines_2:
        "lines_2_shake"
        pos(244, 286)

    attribute lines_3:
        "lines_3_shake"
        pos(226, 295)

    group eyes:
        pos(256, 352)
        attribute eyes "baphscare_pupils"
        attribute twitch "baphscare_eyes_twitch"
        attribute looking "baphscare_eyes_slow"


    always "baphscare1"
