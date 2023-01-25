label Reina_Pre_Intro_Battle_1:
    scene gates_day
    show reina
    with fade
    rei "Got everything you need?"
    show reina mo_open eb_up
    rei """
    Huh?

    Only a set of bandages?

    Is it really the only thing we had...?
    """
    show reina ey_closed mo_v
    "You reassure her that you can handle simple slimes"
    show reina ey_blink mo_happy
    rei """
    Great

    The place you should be heading towards is...

    {b}The Farm{/b}

    The slimes usually appear there at mid day
    """
    show reina ey_closed
    rei "Which means that they should be here anytime soon"
    show reina ey_open
    rei """
    So please, hurry

    May you have success in this, traveler
    """
    scene black with fade

label Slime_Intro_Battle_1:
    show bg_farm_day
    show black at customAlpha(0.75)
    with fade
    centered """
    Just as you get closed to the farm you already hear it

    Screams

    So your best guess is that the so infamous slimes have arrives

    . . .

    Slimes...

    Not very dangerous creatures{p}There are some special cases but{p}9 out of 10 times they are harmless creatures

    Here you hope that you weren't the unlucky winner of that 1 out of 10
    """
    scene black with fade
    show bg_farm_day
    "Green Slime" "WAHAHAHAHA!" with vpunch
    "Green Slime" "So who is going to face me today humans!" with vpunch
    "Green Slime" "Are you all afraid of facing me?!" with vpunch
    show greenslime ey_circles eb_upset mo_open
    "Green Slime" "The queen of slimes!" with vpunch
    "Green Slime" "Surrender all your corn lest you want me to raze the lands!"
    """
    . . .

    A slime that mimics human appareance

    While they are uncommon there is no reason to raise an alarm

    ...{w}Yet...
    """
    play sound "sounds/sfx/footstepsforest1.mp3" volume 0.5
    "You go forward, ready to face your non solid adversary"
    "Green Slime" "Hooo{p}An adversary at last!"
    "Green Slime" "You will serve as an example for everyone!{p}Come on!"
    "Green Slime" "ChaCHAAAAA!"
    scene black with pixellate
    call battle_label(
        {
            "enemies" : [Slime_Girl()],
            "background" : "bg_farm_day",
            "music" : "end_of_road",
            "canFlee" : False,
            "initial_dialogue":["","The slime girl wants to battle!"]
        }
    ) from _call_battle_label_1
    scene bg_farm_day
    show greenslime ey_upset mo_upset eb_upset at center
    with pixellate
    $remove_event_by_name(eventTriggers, "Slime_Intro_Battle_1")
    play music "sounds/music/Windswept.mp3" volume 0.75
    show greenslime with vpunch
    "Green Slime" "Ah-"
    show greenslime ey_closed
    "Green Slime" "That hurt!"
    "Green Slime" "What the hell they got someone who knows to fight!"
    show greenslime ey_circles
    "Green Slime" "Not fair!" with vpunch
    "How is that not fair..."
    "Green Slime" "I...! {w}Uh...!"
    "The slime stops herself form speaking"
    show greenslime ey_closed
    "Green Slime" "You'll see human!"
    "Green Slime" "I will wipe the floor with you{w=0.5}.{w=0.5}.{w=0.5}.{w=0.5}!"
    show greenslime ey_dots eb_up mo_open
    "Green Slime" "Tomorrow!{p}Ahi te ves!"
    menu(screen="choice2"):
        "Wait!":
            "You attempt to talk to her but in just an instant she leaves"
        ". . .":
            "With that said, the slime leaves"
    hide greenslime with moveoutleft
    "What was that..."
    "She is quick for being a literal sentient puddle of..."
    ". . ."
    "What are slimes even made of?{p}Anyway, it doesn't matter"
    "That wasn't that serious...{p}Either the slime seemed to be playing or..."
    "The folk at this place are extremely cowardly..."
    "Well, for today seems that the job is done, you better tell Reina about the slime coming bak tomorrow tho..."
    $eventTriggers.append(Event_Trigger("Post_Intro_Battle_1", 1, 1, None, None))
    jump Adventure_Label

label Post_Intro_Battle_1:
    scene bg_kiosk_day
    show reina ey_mid mo_closed eb_down at right
    show npc_maid at customXAlign(0.65)
    with fade
    rei "..no if we mov… there…"
    "Reina is still where you last saw her, seemingly talking about something important with someone"
    show reina mo_open
    rei "We'll have to redistribute the supplies if that's the case…"
    rei "And…"
    rei "..."
    show reina ey_open mo_vsad eb_up
    rei "huh?!"
    rei "Mr. [player.name]?!{p}Back so soon?!"
    show reina mo_mid
    rei "Ah… may I assume you are done…?{p}You are a bit too…{w} slimy…"
    "With a tired demeanor, you nod your head"
    show reina mo_opensmile
    "Reina's eyes light up at this"
    rei "Really?! Can you-"
    show reina ey_closed mo_smile eb_mid
    rei "Ah, pardon"
    "Reina turns to the person she was talking to"
    show reina ey_open
    rei "Please tell them I'll have an answer tonight, this is quite important, so I have to attent to it right now"
    "Woman" "Yes, mistress"
    hide npc_maid with moveoutleft
    show reina at center with move
    rei "Then"
    rei "Mr [player.name], did you take care of the slimes?"
    show reina mo_mid
    rei "That was very quick!{p}Are you one of the...{w=0.5} was it pros...?"
    "You tell the noble woman that only 1 slime appeared in the fields"
    "You didn't see the supposed other 2"
    "On top of that the slime you faced said she would come back tomorrow"
    show reina mo_closed ey_closed
    rei "Troublesome…{p}Troublesome indeed…"
    rei "That means you are going to have to stay here for a day or two then"
    show reina ey_open
    rei "No objections, I presume?"
    "A place to sleep and rest for beating weak slimes"
    "Sounds good to you"
    show reina mo_smile
    rei "Perfect, you can stay in one of the guest rooms"
    rei "I'll have someone escort you later"
    show reina mo_closed
    rei "Before that...{p}You should go to take a bath..."
    show reina ey_closed mo_smile eb_sad
    rei "I doubt that being covered in slime is nice"
    rei "Ask one of the maids to guide you to a bath"
    rei "They will understand the situation by looking at you{p}Hehe"
    show bg_bathroom_1
    show black at customAlpha(0.7)
    with fade
    play sound "sounds/sfx/water_splash.mp3"
    centered """
    . . .

    How relaxing…

    You haven't had a nice time to relax in the water for a while…

    The slime you fought earlier…

    Didn't seem completely malicious…

    At least her demeanor was closer to a kid having fun…

    Maybe you can reason with it…{p} with her…?

    You ponder how will you approach the slime tomorrow

    Your mind slowly drifts away with the caress of the warm water
    """
    play sound "sounds/sfx/water_drop.mp3"
    centered ". . ."
    hide black with dissolve
    "Butler" "Sir [player.name], are you there?"
    "Butler" "The mistress is waiting for you at her office"
    "Butler" "She has to check you for injuries"
    "Butler" "Please hurry, do not leave the mistress waiting"
    show black at customAlpha(0.65)
    with dissolve
    centered "Ah{p}So this is how the relaxing bath ends"
    play sound "sounds/sfx/water_splash.mp3"
    centered "Getting out of the bath, you reach out for a towel and the spare clothes you were given"
    scene bg_reina_corridor with fade
    scene bg_reina_stairs with fade
    scene bg_reina_livingroom with fade
    scene bg_reina_office with fade
    "Fancy place this is..."
    "Butler" "Mistress?{p}The adventurer is here"
    rei "Ah- good{p}I will take it from here"
    "Butler" "If you'll excuse me..."
    show reina of_doctor facemask at right with moveinright
    rei "[player.name], please take a seat"
    show reina at center with move
    show reina ey_midblinking eb_upset at customYAlign(-0.05), zoomAnim(0.8, 2) with move
    rei "hmm..."
    menu (screen="choice2"):
        rei "Any headaches?"
        "Yes":
            rei "You got a headache..."
        "No":
            rei "Good..."

    "Reina grabs one of your arms{p}She gently presses on a bruise"
    menu (screen="choice2"):
        rei "Do you feel pain?"
        "It stings":
            rei "Ok so you feel this...{p}Noted..."
        "Not at all":
            rei "No pain huh..."
    "Reina pressed her palm on your chest"
    rei "Hmm...{p}Your heart seems to be just fine..."
    rei "What about your stomach?"
    menu (screen="choice2"):
        rei "Do you feel any nausea?"
        "Nope":
            rei "Then it should be fine..."
    rei "Well... you should be fine"
    rei "At least you look fine"
    menu (screen = "choice2"):
        "Why am I having a checkup?":
            rei "Hmm?"
            show reina ey_open eb_mid
            rei "Ah yes{p}I am making sure you are fine after the battle"
            show reina ey_closed at  customYAlign(1.0), zoomAnim(0.75, 1) with move
            rei "You see, some people react badly to the exposure to a slime's...{w} slime..."
            rei "I've seen cases of people getting from mild skin irritation to full on burns on their body"
            rei "And it can be hard to know the reason at times as to why this happens"
            show reina ey_midblinking
            rei "It can be due to allergies to the slime itself...{p}Or what the slime has consumed recently...{p}And sometimes a slime itself can be poisonous!"
            show reina eb_sad
            rei "Slimes are... frightening creatures..."
            show black at customAlpha(0.75) with dissolve
            show greenslime mo_upset ey_circles eb_upset at center, customAlpha(0.75), quickJumps with dissolve
            "Green Slime" "AWAWAWAWAWA" with vpunch
            "Frightening...{p}It is definitely not the word that comes to mind with what you faced"
            hide greenslime
            hide black
            with dissolve
            show reina ey_blinking eb_up
            rei "But...{p}Some species of slime can be useful"
            rei "Namely the stickier ones{p}I've heard that their slime can be used to make adhesives"
            rei "I haven't been able to confirm this though{p}I'd like to someday"
            show reina blush eb_up
            rei "You see, I think I can use them for bandages"
            rei "Getting resources for medical treatment in a place like this is hard!"
            rei "Most things like food and supplies have to be produced here because of the isolation!"
            show reina at quickJump
            rei "And!{p}And..."
            show reina ey_closed at default
            rei ". . ."
            show reina ey_blinking
            rei "My apologies, I am getting ahead of myself"
            rei "Those are things I must resolve in here"
            rei "The important thing for you is the slimes themselves"
            rei "I am going to use some Arnica for the bruises{p}I think that's the only thing you got from that battle"
            "Reina goes to a cabinet full of bottles"
            scene bg_medicines at customZoom(2.0), customYAlign(0.5), slowHPan(25)
            show black at customAlpha(0.6)
            with fade
            centered "She takes some out, looks at a labels, and returns them to the cabinet"
            centered "A minute of her doing this passes by until she finds the one"
            rei "Ah!{p}There is is!"
            scene bg_reina_office
            show reina of_doctor facemask eb_upset ey_midblinking at center, customYAlign(0.0), customZoom(2.0)
            with fade

            rei "Now, please show me the bruises" with vpunch
            "Too close..."

    menu (screen="choice2"):
        "Will you let her apply the arnica herself?"
        "Take off shirt":
            "You decide to take your shirt off"
            "Reina scoops some of the cream from the container and..."
            "Cold!" with vpunch
            show reina ey_closed eb_up
            rei "Forgot to warn you about that hehe..."
            show reina ey_midblinking eb_mid
            rei "Stand still...{p}It should take just a minute..."
            rei "Hmm..."
            rei "You are in good shape...{p}I haven't seen a chest like this in ages..."
            "Her hands delicately go over your chest{p}Gently covering your wounds with the medicine"
            show reina ey_closed blush
            rei ". . ."
            rei ". . . . . . ."
            rei "I..."
            rei "Nevermind..."
            rei "Err..."
            rei "You can put your shirt back on..."
            rei "My apologies...{p}I just realized I am being awkward..."
        "Can't I do it myself?":
            show reina ey_pupil eb_up at quickJump
            rei "Ah!{p}True!"
            rei "My apologies, there's only familiar faces here, so I am not used to...{p}Treating strangers..."
            show reina ey_blinking
            "Reina hands you the bottle"
            rei "Just gently apply this to any bruises you have"
    show reina ey_open eb_mid at default
    rei "You should take a rest now, if they are coming back you should be prepared..."
    show reina at left with move
    "Reina goes over to the door"
    show reina ey_side
    rei "Lead him to his room please"
    show reina ey_blinking
    rei "Take your time to rest, food will be sent to your room in short"
    rei "And again"
    show reina -facemask ey_midblinking mo_smile
    extend ", a pleasure to meet you Mr.[player.name]"
    rei "We will meet again tomorrow"
    scene black with wipeleft
    pause 1.0
    scene bg_reina_guest_room_noon with dissolve
    show black at customAlpha(0.5) with dissolve
    centered """
    Tired

    After a whole morning of walking, and then having to fight you cannot help but feel...

    Tired...

    You want to go out and get to know the place but...
    """
    show bg_reina_guest_room_noon at customBlur(5.0) with dissolve
    "You are... feeling..."
    show bg_reina_guest_room_noon at customBlur(10.0) with dissolve
    "Drow..."
    scene black with eyeopening
    pause
