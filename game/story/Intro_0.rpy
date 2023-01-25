#Set up Player stats and name
label Game_Start:
    scene black with fade
    centered "Game Start:{w} Now{w=0.5}.{w=0.5}.{w=0.5}.{w=1}"
    stop music
    play sound "sounds/sfx/footstepsforest1.mp3" volume 0.5
    play music "sounds/sfx/SunnyDay.mp3" volume 0.6 loop
    scene forestsky at left_to_right_vslow
    show black at customAlpha(0.75)
    with Fade(1.0, 0, 5.0)

    centered """
    Almost there...\n{p}At least that is what you tell yourself

    Having to wake up so early to work has never been any fun\n{p}Even less when not even the sun has woken up either

    You have been walking through a forest for couple of hours now\n{p}What hour could it be right now...?\n{p}Around 9 am?\n{p}You hope it is, you want to arrive before the sun is in it's full 'power'

    What a hassle honestly\n{p}But regardless of your complaints\n{p}You needed the job\n{p}And you took it

    Well{w}, {b}jobs{/b}\n{p}Your second job is quite close from your first destination, and it pays quite well\n{p}If all goes according to your plan you could finish the small job first and then the bigger one after\n{p}With the payments of both you could live carefree for a month or two\n{p}That is what you hope at least
    """
    play sound "sounds/sfx/footstepsforest1.mp3" volume 0.5
    centered "As for the jobs you have accepted...{p}The first one that should be easier..."
    centered """
    {size=+25}Slime hunting{/size}\n{p}{i}'Looking for a warrior capable of dealing with slimes'{/i}\n{p}{i}'Amount: 3 Slimes as of the report's creation'{/i}\n{p}{i}Payment: 80 gold{/i}
    """
    centered "Doesn't seem to be hard{p}Slimes for the most part are pushovers...{p}{i}For the most part{/i}"
    centered "You hope that this isn't that big of a deal"
    centered "The second job is far more interesting..."
    centered "{size=+25}Rescue Mission{/size}\n{p}{i}'We need an experienced warrior for a rescue'{/i}\n{p}{i}'Must be skilled in survival, combat and have experience with dealing with magic'{/i}\n{p}{i}'Highly recommended to have good predisposition towards working with demi-humans'{/i}\n{p}{i}Payment: 1,000 gold{/i}\n{p}{i}Further details given on arrival{/i}"
    centered "This one is much more interesting\n{p}The payment is what enticed you\n{p}Apparently no one took this job because of the demi-human requirement\n{p}Relations between humans and demi-humans are very shaky at moment\n{p}That leaves many jobs open for people like you, who are either friendly or at the very least neutral towards demis"
    scene black with Fade(1.0, 0.0, 1.0)
    # Set some variables
    python:
        world.set_current_location(5)
        updateScene()
        eventTriggers.append(Event_Trigger("Map_Intro", 5, None, None, None))
        world.disable_all()
        world.enable_locations([0, 1])
    jump Town_Label

label title_card:
    stop music fadeout 3.0
    scene titlecard with Fade(3.0, 1.0, 3.0)
    pause 5.0
    jump Town_Label

label Map_Intro:
    """
    You find yourself at the entrance of the fief

    Click the map icon to open up the map and select the location you want to move to
    """
    $remove_event_by_name(eventTriggers, "Map_Intro")
    jump Town_Label

label Reina_Boris_Intro:
    play music "sounds/music/Windswept.mp3" volume 0.75
    scene gates_day at up_down_zoom_out with Fade(1.0, 1.0, 1.0)
    pause 3.0
    play sound "sounds/sfx/footstepsforest1.mp3"
    """
    Hmm...{p}This place looks quite luxurious for being in the middle of nowhere

    You scan the area that surrounds you, looking at the mansion that sits in front of you{p}

    It is surrounded by a beautiful garden

    The entire place looks pristine as a matter of fact

    Whoever hired you must be rich{p}Let's hope that your payment reflects that

    You manage to spot a shop...{p}A farm not too far from here...{p}And what looks like a central area with various small houses

    Looking at the people that come and go you manage to guess what their jobs may be

    Farmers{w}, gardeners{w}, builders...

    With the arrangement of jobs you see here you can see how this place has mantained itself so well preserved
    """
    show gates_day at darken with dissolve
    centered ". . .\n{p}. . .\n{p}. . ."

    "Wasn't someone supposed to recieve you?"
    "Should you go inside the mansion or..."
    scene gates_day
    "?" "You there" with vpunch
    show boris ey_mid eb_upset with vpunch
    bor "Aren't you supposed to be doing something?!" with vpunch
    bor "Don't you stand there spacing out!"
    bor "Get to work!" with vpunch
    "A big angry man storms towards you"
    show boris:
        xalign 0.5
        yalign 0.0
        zoom 1.5
    bor "Are you listening to me?!" with vpunch
    bor "I am talking to you!" with vpunch
    bor "Are you deaf or what?!" with vpunch
    show black at customAlpha(0.5) with dissolve
    "You've known about this person's existance for a minute and you already want to throw him off a cliff"
    "You should let him know that you aren't an employee here"
    menu:
        "So how will you answer to him?"
        "Answer indignantly":
            "Getting annoyed, you raise your voice and answer with..."
            menu:
                "Getting annoyed, you raise your voice and answer with..."
                "A firm response":
                    hide black with dissolve
                    "You puff out your chest and tell the man that you don't know who he is or what he is talking about"
                    "You just arrived and your first interaction with a person here is his rude outburst"
                    bor ". . . !"
                    "The man looks like he is about to say something{p} then stops for a second"
                    bor "Alright then-!{p}And who are you supposed to be then?!"
                    bor "What is your business here?!"
                    "He is getting worked up again"
                "An aggressive response":
                    hide black with dissolve
                    show boris with vpunch:
                        zoom 1.0
                    bor "wha-!"
                    "You push the man back and tell him to back off"
                    bor "How dare you!" with vpunch
                    "The man starts looking for something on his pocket"
                    bor "If that is what you want it will be my pleasure to put you in your place-!"

        "Answer calmly":
            hide black with dissolve
            "With visible annoyance, you take a deep breath and step back"
            show boris ey_mid eb_down at default
            "Trying to contain your frustration, you explain him that he may be mistaking you for someone else"
            "You are the mercenary that accepted the job of helping out with the monsters in the farm"
            "He looks at you with a puzzled expression, some anger still painted on his face"
            "For a second he looks like he is going to say something, but falls silent again"

    "After a couple of awkward seconds go by, a voice calls to both of you"
    $rei.name = "Woman"
    rei """
    Boris?

    What is happening over there?

    I can hear your ruckus from the inside of the mansion
    """
    show reina eb_upset mo_closed at right with moveinright
    rei """
    You are making quite the spectacle for everyone

    Haven't I told you before to keep your temper in check?
    """
    show boris ey_pupil eb_up
    bor "Mistress! {w} I...!" with vpunch
    bor "You see-! I was dealing with-!" with vpunch
    bor "This man! You see-!" with vpunch
    bor "He-!" with vpunch
    bor ". . ."
    show boris ey_closed eb_sad
    rei ". . ."
    show reina ey_mid mo_closed
    rei ". . ."
    "The young lady turns her gaze towards you"
    show boris at center, customXAlign(0.25)
    show reina eb_down at customXAlign(0.65)
    with move
    rei "Hmm..."
    show reina mo_mid
    rei """
    I don't recognize you...

    Are you a visitor...?

    At least I don't remember you working in here... {w}right...?
    """
    show black at customAlpha(0.65) with dissolve
    centered "What follows was a quick explanation of who you are{p}And what you came for"
    hide black
    show boris ey_mid
    show reina ey_open eb_up mo_open
    with fade
    rei """
    Ah!

    The request I sent to the guild!

    I completely forgot about that!
    """
    show reina ey_mid mo_mid
    rei "My apologies!"
    show boris eb_upset
    bor "A request to the guild?{p}Without telling me!?{p}Mistress, you know you shouldn't-"
    show reina ey_mid eb_upset mo_closed at customXAlign(0.6) with move
    show boris ey_open eb_up at customXAlign(0.2) with move
    rei "Shush it!"
    rei "I don't want to hear it!"
    rei "If I asked you first we would be waiting for someone to arrive for another month!"
    rei "Safety goes first for our people"
    rei "Now let me handle it{p}Go and finish whatever tasks you have today"
    show boris ey_closed eb_sad
    bor "but-"
    show reina ey_closed eb_sad
    rei "Boris{p}Please{p}Just go"
    rei "I am sure you are needed somewhere else right now"
    bor ". . ."
    show boris ey_mid
    "The man looks at you both and sighs"
    bor "Yes mistress..."
    hide boris with moveoutleft
    "And with a crestfallen look, the man leaves"
    show reina ey_closed at center with move
    rei "Geez Boris, why do you have to be like this..."
    ". . ."
    show reina eb_sad mo_smile
    rei "My apologies Mr...{p}hmmm"
    show reina mo_vsad eb_down
    rei "Ah{w}, may I know your name?"
    show black at customAlpha(0.65) with dissolve
    $temp0 = False
    #Choosing a name
    while(not temp0):
        $temp1 = renpy.input("My name is...").strip()
        $temp2 = compare_names(temp1, characterlist.characters)
        if(not temp2):
            "Cannot use that name"
        $player.name = temp1
        #confirm name
        menu:
            "Is your name [player.name]?"
            "Yes":
                $temp0 = True
            "No":
                $temp0 = False

    python:
        temp0 = None
        temp1 = None
        temp2 = None

    show reina eb_up ey_blinking mo_smile
    hide black with dissolve
    rei """
    Mr [player.name]!{p}A pleasure to meet you

    I am sorry for what happened

    Dear Boris is not a bad person

    He is just easily stressed out

    And with some recent events he has been on edge
    """
    show reina mo_opensmile
    rei """
    I'm glad you could arrive safely

    A pleasure to meet you, my name is {b}Reina{/b}{p}Your employer
    """
    show reina mo_smile
    rei """
    You came here to deal with our slime problem, right?

    Will you please accompany me?{p}I'll fill you on the details
    """
    play sound "sounds/sfx/footstepsforest1.mp3"
    scene bg_kiosk_day
    show reina
    show black at customAlpha(0.75)
    with fade
    centered "Reina's mannerisms are calm and gentle{p}\nThe way she conducts and expresses herself seem to indicate that she is a noble of some sort{p}\nBut why is this place isolated in the middle of the forest?"
    centered "It looks like a small thriving community but still..."
    show reina mo_mid eb_up
    rei "Hello?{p}Do I have your attention?"
    hide black with dissolve
    show reina mo_smile eb_mid
    rei "There we go{p}Taking in the scenary?"
    show reina ey_closed
    rei "Enjoy it to your heart's content"
    show reina ey_open
    rei "But first I must fill you in with the details"
    "You nod"
    show reina mo_opensmile
    rei "Great"
    show reina mo_mid eb_upset
    rei "Now, to the matter in hand..."
    show reina mo_vsad
    rei """
    A group of slimes arrived not too long ago{p}2 months back if memory serves me right

    At first the farmers just reported sightings of them in the surrounding area, but then the slimes started coming into the land
    """
    show reina mo_closed
    rei "Every other day they come into the farm and start consuming our crops"
    rei "One of our farmers attempted to chase them off but..."
    show reina ey_closed eb_sad
    rei """
    But he ended up getting beaten up...{p}And it took us a whole day to wash off the slime off him

    Our farmers are terrified to go into the fields for fear of encountering the monsters
    """
    show reina ey_closed eb_down
    rei "And I fear that one of our farmers could end up severely injured by the slimes..."
    show reina ey_blinking
    rei "So please, if you could get rid of the slimes we would be ever so grateful"
    $temp0 = True
    while temp0:
        menu:
            rei "Do you have any questions?"
            "About the payment":
                "You inquire about your payment, and if it is really appropiate for the task"
                show reina mo_smile eb_up
                rei "Yes, about that, I will pay 50 gold for the job once it's done"
                rei "I will also offer any medical aid that I can provide while you are here"
                show reina ey_blinking mo_closed eb_down
            "About the slimes":
                "You ask her about the group of slimes, any more details on said group?"
                show reina ey_closed mo_vsad
                rei "Hmmm"
                rei "From what we could tell it is not a group of more than 3 slimes"
                rei "They seem to cycle every day"
                rei "I am sorry, we don't know much about the situation"
                rei "As soon as one of them appears our farmers flee immediately"
                show reina ey_blinking mo_closed eb_down
            "No more questions":
                "You tell her that you don't have any more questions"
                $temp0 = False

    show reina mo_smile eb_up
    rei """
    Perfect, please start as soon as possible, they usually come in the afternoon{p}So you will have to wait a couple of hours before they come

    I pray that everything will be fine in your task, traveler
    """
    show reina mo_closed
    rei """
    . . .

    Say, aren't you going a little bit... lightweight?

    Don't you have any weapon...?
    """
    "You don't have any weapons...?"
    "You explain her that you broke the one you had when travelling here{p}(A small lie)"
    show reina ey_closed mo_vsad
    rei "That is troublesome indeed..."
    rei ". . ."
    show reina ey_blinking mo_closed
    rei "I'll give you 10 gold, it should be enough to get a weapon from this place's store"
    rei "We usually don't have conflicts here, so our weapons aren't at the caliber you would find at an average town"
    rei "For that I apologize"
    "Reina hands you 10 gold"
    rei "The store is over there, I think you can get a club with this"
    show reina mo_smile
    rei "Now go Mr.[player.name], I wish you the best of luck{p}If you need something I'll be around"
    "The young noble gently bows at you and leaves"
    "You better go to the shop"
    python:
        questLog.add_section(0, "Your first job")
        questLog.add_story_quest("Your first job", "Gear up", "Go to the shop and buy a supplies before going to your first job")
        inventory.gold += 10
        world.currentLoc = 1
        world.locations[3].locState = LocState.BLOCKED
        world.locations[4].locState = LocState.BLOCKED
        # Add items to shop
        world.locations[2].add_item("bandage_1")
        # Add event
        eventTriggers.append(Event_Trigger("Shop_Intro_1", 2, None, None, None))
        eventTriggers.append(Event_Trigger("Reina_Intro_Item_Bought", 1, 1, None, None))
        remove_event_by_name(eventTriggers, "Reina_Boris_Intro")
        characterlist.characters[1].schedule.clear()
    #$characterlist.selected = 1
        characterlist.characters[1].schedule.append(Activity(1, 1, None, None))
    jump Town_Label

label Trigger_Test:
    "Chien ate your breakfast, you died"
    $remove_event_by_name(eventTriggers, "Trigger_Test")
    jump game_over

label Reina_Intro_Item_Bought:
    show reina mo_smile eb_up
    rei "Did you get what you needed?"
    if(inventory.search_item("bandage_1") != None):
        show reina mo_vsad eb_mid
        rei "A single set of bandages..."
        rei "Against a slime it should be enough...{p}Right?"
        "You assure her that it should be fine"
        show reina mo_smile
        rei "Very well then"
        rei "Now that you are ready you should go to the farm area{p}That place is where the slimes usually appear"
        rei "I'll tell the farmers to let you through"
        show reina mo_opensmile ey_closed
        rei "My best wishes on this quest adventurer"
        rei "Don't forget to come back once you are finished today"
        python:
            world.locations[3].locState = LocState.NORMAL
            remove_event_by_name(eventTriggers, "Reina_Intro_Item_Bought")
            eventTriggers.append(Event_Trigger("Slime_Intro_Battle_1", place = 3))
    else:
        show reina mo_closed
        rei "hm?"
        rei "You got nothing...?"
        show reina ey_mid eb_mid
        rei "I cannot have you go into this without some precautions{p}Get some supplies before we proceed"
        show reina mo_smile
        rei "Don't worry{w}, I will cover the cost of them"
        rei "Now go{w}, prepare"

    jump Town_Label

label Shop_Intro_1:
    scene black
    show shopkeeper1 eb_up mo_vhappy
    shop """
        Greetings!{p}How may I serve you?

        hmm...?
    """
    show shopkeeper1 eb_hmm mo_closed ey_mid
    shop ". . . ?"
    show shopkeeper1 ey_blink mo_open eb_up
    shop "I haven't seen you before{p}Are you a visitor?"
    centered "You give the woman a quick explanation of who are you and that Reina sent you here"
    show shopkeeper1 ey_mid mo_closed eb_mid
    shop "Hmm{p}I see I see"
    show shopkeeper1 mo_vhappy ey_closed eb_up
    shop """
    Well then, a pleasure to meet you [player.name]

    I hope you can resolve our problem, those slimes are a pain in the-
    """
    show shopkeeper1 mo_closed eb_mid
    shop """
    . . .

    My my, excuse my manners

    But you get the idea, slimes seem to just exist to cause havoc in the land
    """
    show shopkeeper1 mo_vhappy2 ey_blink eb_up
    shop "So please stock up in what you need!"
    $remove_event_by_name(eventTriggers, "Shop_Intro_1")
    jump Shop_Label
