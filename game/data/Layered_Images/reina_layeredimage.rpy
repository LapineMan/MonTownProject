image reina_eyes_ey_blinking:
    "reina_eyes_ey_open"
    choice:
        0.25
    choice:
        2.5
    choice:
        3.5
    choice:
        5.0
    "reina_eyes_ey_mid"
    0.03
    "reina_eyes_ey_closed"
    0.03
    "reina_eyes_ey_mid"
    0.03
    repeat

image reina_eyes_ey_midblinking:
    "reina_eyes_ey_mid"
    choice:
        0.25
    choice:
        2.5
    choice:
        3.5
    choice:
        5.0
    "reina_eyes_ey_closed"
    0.03
    repeat

image reina_mouth_mo_talking:
    "reina_mouth_mo_closed"
    0.075
    "reina_mouth_mo_mid"
    0.075
    "reina_mouth_mo_open"
    0.075
    "reina_mouth_mo_mid"
    0.075
    "reina_mouth_mo_closed"
    repeat 3

image reina_mouth_mo_happytalking:
    "reina_mouth_mo_smile"
    0.075
    "reina_mouth_mo_mid"
    0.075
    "reina_mouth_mo_opensmile"
    0.075
    "reina_mouth_mo_mid"
    0.075
    "reina_mouth_mo_smile"
    repeat 3

image reina_mouth_mo_pouttalking:
    "reina_mouth_mo_mid"
    0.1
    "reina_mouth_mo_pout"
    0.1
    "reina_mouth_mo_mid"
    0.1
    "reina_mouth_mo_pout"
    0.1
    repeat 3

layeredimage reina:
    always "reina_body":
        pos (14, 95)

    always "reina_head":
        pos (23, 0)

    group outfit auto:
        pos(0, 149)
        attribute of_dress default

    group mouth auto:
        pos (89, 100)
        attribute mo_pouttalking
        attribute mo_happytalking
        attribute mo_talking
        attribute mo_smile default

    group eyes auto:
        pos (64, 65)
        attribute ey_midblinking
        attribute ey_blinking default

    group eyebrows auto:
        pos (60, 54)
        attribute eb_mid default

    attribute blush:
        pos (69, 80)

    attribute facemask:
        pos (69, 80)

    attribute angryFx:
        "angryFx"
        pos(120, 50)

    attribute sweatdropFx:
        "sweatdropFx"
        pos(120, 20)

    attribute linesFx:
        "linesFx"
        pos(120, 20)
