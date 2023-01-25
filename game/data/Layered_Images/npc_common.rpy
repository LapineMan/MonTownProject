image shopkeeper1_eyes_ey_blink:
    "shopkeeper1_eyes_ey_open"
    choice:
        0.25
    choice:
        2.5
    choice:
        3.5
    choice:
        5.0
    "shopkeeper1_eyes_ey_mid"
    0.03
    "shopkeeper1_eyes_ey_closed"
    0.03
    "shopkeeper1_eyes_ey_mid"
    0.03
    repeat

image shopkeeper1_mouth_mo_talk:
    "shopkeeper1_mouth_mo_happy"
    0.1
    "shopkeeper1_mouth_mo_vhappy"
    0.1
    "shopkeeper1_mouth_mo_vhappy2"
    0.1
    repeat 3

layeredimage shopkeeper1:
    always "shopkeeper1_body" pos(0, 109)
    always "shopkeeper1_head" pos(177, 0)
    group eyes auto:
        pos(213, 91)
        attribute ey_blink default

    group mouth auto:
        pos(220, 115)
        attribute mo_talk
        attribute mo_happy default

    group eyebrows auto:
        pos(210, 73)
        attribute eb_mid default

    attribute scowl pos(218, 95)
    attribute sweatdrop pos(276, 119)
