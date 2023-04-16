image chien_eyes_ey_blink:
    "chien_eyes_ey_open"
    choice:
        0.25
    choice:
        2.5
    choice:
        3.5
    choice:
        5.0
    "chien_eyes_ey_mid"
    0.03
    "chien_eyes_ey_closed"
    0.03
    "chien_eyes_ey_mid"
    0.03
    repeat

image chien_tail_ta_hidden:
    customAlpha(0.0)
    "chien_tail_ta_idle"

image chien_tail_ta_slowwag:
    block:
        "chien_tail_ta_2"
        0.15
        "chien_tail_ta_3"
        0.15
        "chien_tail_ta_hidden"
        0.15
        "chien_tail_ta_3"
        0.15
        "chien_tail_ta_4"
        0.15
    repeat

image chien_tail_ta_fastwag:
    block:
        "chien_tail_ta_0"
        0.05
        "chien_tail_ta_1"
        0.05
        "chien_tail_ta_2"
        0.05
        "chien_tail_ta_3"
        0.05
        "chien_tail_ta_hidden"
        0.05
        "chien_tail_ta_3"
        0.05
        "chien_tail_ta_4"
        0.05
    repeat

image chien_tail_ta_wag:
    block:
        "chien_tail_ta_0"
        0.1
        "chien_tail_ta_1"
        0.1
        "chien_tail_ta_2"
        0.1
        "chien_tail_ta_3"
        0.1
        "chien_tail_ta_hidden"
        0.1
        "chien_tail_ta_3"
        0.1
        "chien_tail_ta_4"
        0.1
    repeat

layeredimage chien:
    group tail auto:
        pos(97, 321)
        attribute ta_slowwag
        attribute ta_wag
        attribute ta_fastwag
        attribute ta_none null
        attribute ta_idle default
        #attribute ta_fast_wag
        #attribute ta_up default

    always "chien_body" pos(0, 157)

    group outfit auto:
        pos (4, 270)
        attribute of_leotard default
        attribute of_none null

    group right_arm:
        pos(137, 283)
        attribute right_arm_on default:
            "chien_right_arm"
        attribute right_arm_off null

    group cuff:
        pos(189, 489)
        attribute right_cuff default:
            "chien_righthandcuff"
        attribute cuff_off null

    group cape:
        pos(21, 254)
        attribute cape_on default:
            "chien_cape"
        attribute cape_off null

    always "chien_head" pos(19, 0)

    group hat:
        pos(47, 66)
        attribute hat_on default:
            "chien_hat"
        attribute hat_off null

    group eyebrows auto:
        pos(71, 165)
        attribute eb_mid default

    group eyes auto:
        pos(69, 181)
        attribute ey_blink default

    group mouth auto:
        pos(73, 210)
        attribute mo_smile default

    attribute scowl:
        pos(47, 66)
        "chien_scowl"

    attribute blush:
        pos(79, 200)
        "chien_blush"
