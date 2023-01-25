image slimemother_eyes_ey_blinking:
    " slimemother_eyes_ey_open"
    choice:
        0.25
    choice:
        2.5
    choice:
        3.5
    choice:
        5.0
    "slimemother_eyes_ey_mid"
    0.03
    "slimemother_eyes_ey_closed"
    0.1
    "slimemother_eyes_ey_mid"
    0.03
    repeat

layeredimage slimemother:
    always "slimemotherbody"

    group mouth auto:
        attribute mo_happy default
        pos (316, 130)

    group eyes auto:
        attribute ey_blinking default
        pos (300, 90)

    group eyebrows auto:
        attribute eb_mid default
        pos (295, 80)


image greenslime_eyes_ey_blinking:
    "greenslime_eyes_ey_open"
    choice:
        0.25
    choice:
        2.5
    choice:
        3.5
    choice:
        5.0
    "greenslime_eyes_ey_mid"
    0.15
    "greenslime_eyes_ey_closed"
    0.5
    "greenslime_eyes_ey_mid"
    0.15
    repeat

layeredimage greenslime:
    always "greenslimebody"

    group mouth auto:
        attribute mo_open default
        pos (165, 95)

    group eyes auto:
        attribute ey_blinking default
        pos (157, 68)

    group eyebrows auto:
        attribute eb_mid default
        pos (153, 47)
