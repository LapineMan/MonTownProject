label game_over:
    stop music
    stop sound
    call hide_screens from _call_hide_screens
    scene black with fade
    centered "Game Over"
    stop music
    stop sound
    return

label baphi_game_over:
    stop music
    stop sound
    call hide_screens from _call_hide_screens_2
    scene black with w21
    pause 2
    centered "Game Over"
    stop music
    stop sound
    window hide
    show baphi_face at customXAlign(0.5), customYAlign(0.4), customZoom(0.8) with eyeclosing
    pause 5
    show baphi_face looking with dissolve
    pause 12
    #play music "sounds/music/Adi-Eu.mp3" volume 0.2 fadein 15.0 loop
    $quick_menu = False
    show baphi_face eyes
    pause 5
    show baphi_face twitch
    pause 10
    #play music "<from 26.5>sounds/music/Adi-Eu.mp3" volume 1.25
    show baphi_face -twitch red lines_1 lines_2 lines_3 at h_shake(6)
    pause 6
    scene red
    show black at customAlpha(0.75)
    with wet
    $count = 30
    while count > 0:
        #play music "<from 44>sounds/music/Adi-Eu.mp3" volume 1.5
        pause 0.1
        $count -= 1
    hide black
    show baphi_face at truecenter, red_tint
    #play music "<from 42>sounds/music/Adi-Eu.mp3" volume 2.0
    pause 0.1
    stop music
    $quick_menu = True
    return

label hide_screens:
    hide screen Inventory_Screen
    hide screen Battle_Screen
    hide screen Town_Screen
    return

label secret_baphi_test:
    show baphi at twitch(1.0, 0.13), ominous_zoom, red_tint, darken
    play music "sounds/music/starvation.mp3"
    window hide
    centered "{size=+15}{color=#f00}Why did you stop moving? I am sorry I am sorry please I can't resist it It wasn't my fault please forgive please forgive for what I have done I never wanted this to happen please release please help me it is still after me waiting for me it will take me again and take apart what little remains of me I can't please please please release please end it The hunger I feel it gnawing and ripping my entrails It consumes it hurts so much I need you just this time the pain is unbearable so please give me your carcass please sate this unbearable hunger just end it just end it just end it kill me please kill me please kill me please kill me please kill me please kill me please kill me please kill me please kill me please kill me please kill me please kill me please kill me please kill me please kill me please kill me please kill me please kill me please kill me please kill me please kill me please kill me please kill me please{/color}{/size}"
    jump start
