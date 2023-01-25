image angryFx:
    alpha 1.0
    xanchor 0.5
    yanchor 0.5
    rotate 125
    "angry_fx"
    block:
        easein 0.25 zoom 2 rotate 100
        easein 0.25 zoom 1.0  rotate 75
        easein 0.25 zoom 1.5  rotate 50
        easein 0.25 zoom 1.0  rotate 25
        easeout 1.0 alpha 0.0

image sweatdropFx:
    "sweatdrop_fx"
    ease 0.5 yoffset 20
    easein 1.0 alpha 0.0

image linesFx:
    xzoom 1
    "lines1_fx"
    0.1
    "lines2_fx"
    0.1
    "lines1_fx"
    xzoom -1
    0.1
    "lines2_fx"
    0.1
    repeat
