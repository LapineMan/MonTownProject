#Transforms
transform main_menu_stars_anim:
    xalign 0.5
    yalign 0.5
    linear 180.0 rotate 360
    repeat
# shitpost
transform awesomeTint:
    linear 0.5 matrixcolor TintMatrix("#DFFF00")
    linear 0.5 matrixcolor TintMatrix("#FFBF00")
    linear 0.5 matrixcolor TintMatrix("#FF7F50")
    linear 0.5 matrixcolor TintMatrix("#DE3163")
    linear 0.5 matrixcolor TintMatrix("#9FE2BF")
    linear 0.5 matrixcolor TintMatrix("#40E0D0")
    linear 0.5 matrixcolor TintMatrix("#6495ED")
    linear 0.5 matrixcolor TintMatrix("#CCCCFF")
    repeat

# Story
transform slowHPan(n):
    xalign 0.0
    easein n xalign 1.0

transform quickJump(n):
    easein 0.2 yoffset -n
    easeout 0.2 yoffset 0

transform quickJumps(n):
    easein 0.2 yoffset -n
    easeout 0.2 yoffset 0
    repeat

# Transitions
define slow_fade = Fade(1.5, 1.0, 1.5)

# Customs
transform cameraZoomAnim(a = (0.5, 0.5), t = 1, z = 1):
    align a
    linear t zoom z


transform customTransparent(n):
    matrixcolor Matrix([ 1.0, 0.0, 0.0, 0.0,
                         0.0, 1.0, 0.0, 0.0,
                         0.0, 0.0, 1.0, 0.0,
                         0.0, 0.0, 0.0, n,])

transform flip:
    xzoom -1

transform customXZoom(n):
    xzoom n

transform customYAlign(n):
    yalign n

transform customXAlign(n):
    yalign 1.0
    xalign n

transform zoomAnim(m, n):
    ease m zoom n

transform customZoom(n):
    zoom n

transform customBlurEase(n):
    easeout 1.0 blur n

transform customAlpha(n):
    alpha n

transform customBlur(n):
    blur n

#General Tints
transform red_tint:
    matrixcolor TintMatrix("#F00")

transform night_darken:
    matrixcolor Matrix([ 0.50, 0.0, 0.0, 0.0,
                         0.0, 0.50, 0.0, 0.0,
                         0.0, 0.0, 0.70, 0.0,
                         0.0, 0.0, 0.0, 1.0,])

transform night_dark_tint:
    matrixcolor TintMatrix("#2d87ff")

transform noon_orange_tint:
    matrixcolor TintMatrix("#ffd9b4")

transform day_light_tint:
    matrixcolor TintMatrix("#ffffee")


# Misc
transform blinking(speed):
    alpha 1.0
    speed
    alpha 0.0
    speed
    repeat

transform h_shake(n):
    ease 0.025 yoffset n
    ease 0.025 yoffset 0
    ease 0.025 yoffset -n
    repeat

transform fast_shake(n):
    ease 0.025 xoffset n
    ease 0.025 xoffset 0
    ease 0.025 xoffset -n
    repeat

transform blur_in_and_out:
    ease 1 blur 5
    ease 1 blur 0
    repeat

transform evenly_order_h(position):
    xalign position
    yalign 1.0


transform running_shake():
    zoom 1.30
    xalign 0.5
    block:
        easeout 0.15 yalign 1.0
        easein 0.15 yalign 0.8
        repeat


transform twitch(xcord, ycord):
    xalign xcord
    yalign ycord
    linear 0.05 xalign (xcord + 0.005) yalign (ycord + 0.005)
    xalign xcord
    yalign ycord
    linear 0.05 xalign (xcord - 0.005) yalign (ycord + 0.005)
    repeat


transform ominous_zoom:
    zoom 7

transform face_zoom:
    linear 0.3 zoom 2.5 yalign 0.0

transform up_down_zoom_out:
    zoom 1.5
    xalign 0.5
    ease 10.0 yalign 1.0
    ease 10.0 zoom 1.0

transform darken:
    matrixcolor Matrix([ 0.45, 0.0, 0.0, 0.0,
                         0.0, 0.45, 0.0, 0.0,
                         0.0, 0.0, 0.5, 0.0,
                         0.0, 0.0, 0.0, 1.0,])

transform Map_Button_Highlight:
    matrixcolor Matrix([ 1.45, 0.0, 0.0, 0.0,
                         0.0, 1.45, 0.0, 0.0,
                         0.0, 0.0, 1.5, 0.0,
                         0.0, 0.0, 0.0, 1.0,])

transform normal_color:
    matrixcolor Matrix([ 1.0, 0.0, 0.0, 0.0,
                         0.0, 1.0, 0.0, 0.0,
                         0.0, 0.0, 1.0, 0.0,
                         0.0, 0.0, 0.0, 1.0,])

transform shake_test:
    zoom 1.2
    ease 0.25 xalign 1.0
    ease 0.25 xalign 0.0
    repeat

transform hit_shake:
    block:
        linear 0.01 yoffset 25
        linear 0.01 yoffset -25
        linear 0.01 yoffset 0
        repeat 5

transform middle_right:
    yalign 1.0
    xalign 0.80

transform left_to_right_vslow:
    zoom 1.2
    xalign 0.0
    ease 45.0 xalign 1.0

transform inv_eff: # too lazy to make another version of each item, we just use ATL to make hovered items super bright
    zoom 0.5 xanchor 0.5 yanchor 0.5
    on idle:
        linear 0.2 alpha 1.0
    on hover:
        linear 0.2 alpha 2.5

transform arrow_btn_eff:
    yanchor 0.5 xanchor 0.5
    on idle:
        linear 0.05 zoom 0.8 alpha 0.8
    on hover:
        linear 0.05 zoom 0.9 alpha 1.0
