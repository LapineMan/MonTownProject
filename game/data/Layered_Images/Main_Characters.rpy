image charna_eyes_ey_blink:
    "charna_eyes_ey_open"
    choice:
        0.25
    choice:
        2.5
    choice:
        3.5
    choice:
        5.0
    "charna_eyes_ey_mid"
    0.03
    "charna_eyes_ey_closed"
    0.03
    "charna_eyes_ey_mid"
    0.03
    repeat

image charna_mouth_mo_talk:
    "charna_mouth_mo_vhappy"
    0.1
    "charna_mouth_mo_happy"
    0.1
    repeat 3

layeredimage charna:
    always "charnabody":
        pos(55, 78)

    group outfit auto:
        pos(114, 162)
        attribute of_casual default
        attribute of_none null

    group tail auto:
        pos(15, 229)
        attribute ta_closed default

    always "charnahead":
        pos(132, 17)

    group eyebrows auto:
        pos(177, 73)
        attribute eb_neutral default

    group eyes auto:
        pos(169, 94)
        attribute ey_blink default

    group mouth auto:
        pos(186, 134)
        attribute mo_talk
        attribute mo_happy default

    attribute sweatdrop pos(179, 118)
    attribute blush pos(179, 118)


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

layeredimage chien:
    always "chienbody" pos(34, 190)

    group outfit auto:
        pos (92, 267)
        attribute of_casual default
        attribute of_none null

    always "chienhead" pos(78, 0)

    group eyebrows auto:
        pos(137, 177)
        attribute eb_neutral default

    group eyes auto:
        pos(134, 198)
        attribute ey_blink default

    group mouth auto:
        pos(140, 225)
        attribute mo_neutral default

    attribute sweatdrop pos(203, 222)
    attribute blush pos(141, 214)
    attribute scowl pos(136, 190)


layeredimage liz:
    always "lizbody" pos(0, 124)

    group clothes auto:
        pos (128, 214)
        attribute cl_casual default
        attribute of_none null

    always "lizhead" pos(194, 0)

    group eyes auto:
        pos(221, 134)
        attribute ey_open default

    group eyebrows auto:
        pos(223, 126)
        attribute eb_mid default

    group mouth auto:
        pos(256, 167)
        attribute mo_happy default

image lapin_eyes_ey_blink:
    "lapin_eyes_ey_open"
    choice:
        0.25
    choice:
        2.5
    choice:
        3.5
    choice:
        5.0
    "lapin_eyes_ey_mid"
    0.03
    "lapin_eyes_ey_closed"
    0.03
    "lapin_eyes_ey_mid"
    0.03
    repeat

layeredimage lapin:
    always "lapinbase" pos(2, 215)

    group outfit auto:
        pos(0, 290)
        attribute of_casual default

    always "lapinhead" pos(53, 0)

    group eyebrows auto:
        pos(112, 182)
        attribute eb_neutral default

    group eyes auto:
        pos(116, 209)
        attribute ey_blink default

    group blush auto:
        pos(128,234)

    attribute sweatdrop pos(128, 241)
