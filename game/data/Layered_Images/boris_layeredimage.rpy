image boris_eyes_ey_blink:
    "boris_eyes_ey_open"
    choice:
        0.25
    choice:
        2.5
    choice:
        3.5
    choice:
        5.0
    "boris_eyes_ey_mid"
    0.025
    "boris_eyes_ey_closed"
    0.5
    "boris_eyes_ey_mid"
    0.1
    repeat

layeredimage boris:
    always "borisbase" pos(0, 33)

    group eyes auto:
        pos(200, 99)
        attribute ey_blink default

    group eyebrows auto:
        pos(195, 88)
        attribute eb_up default

    attribute hat default:
        pos(103, 0)
