

label Slime_Steal_Gold:
    scene woods_1_day with fade
    "Slime A" "GOT IT!" with hpunch
    "Slime B" "RUN FOR IT!" with hpunch
    show greenslime ey_dots eb_up mo_mid as s0 at left
    show greenslime as s1 at center
    show greenslime ey_circles mo_vhappy eb_upset as s2 at right
    with moveinbottom

    "Slime C" "APLEASURETOMEETYOUHUMAN!{p}Have a nice day!"
    hide s0
    hide s1
    hide s2
    with moveoutleft

    """
    Huh?

    Got it...?

    You quickly run your hands through your body{p}Did they get something out of the batt-

    No...

    No no no no no

    {b}Your gold pouch{/b}

    {i}Those slimes just ran away with what little savings you had{/i}

    Without even thinking about it{p}As if it was an automatic reaction{p}You go into full sprint to chase the slimes
    """
    scene woods_1_day at running_shake
    "Slime C" "AWAAAAA HE IS COMING AFTER US" with hpunch
    "Slime A" "RUUUN" with hpunch
    #quick footsteps sounds
    #mute music

    scene woods_1_noon with slow_fade
    """
    So tired....

    Your legs are burning{p}Your breath is ragged{p}Your throat feels uncomfortably cold

    But there she is{w}, the one with the gold{p}You have caught up to her
    """
    show greenslime ey_upset eb_upset mo_upset with vpunch
    g_slime """
    Don't you ever give up?!

    For how long are you gonna keep chasing me!

    It doesn't matter! {w}Girls!{w} He's tired! {w}We can take him down here!
    """
    show black at customTransparent(0.5) with dissolve
    centered ".{w=0.5} .{w=0.5} ."
    hide black with dissolve
    show greenslime ey_circles mo_open eb_sad
    g_slime "...girls?{p}You there?"
    """
    You remember the other slimes parting ways mid chase

    In the end they seemingly abandoned this one
    """
    show greenslime ey_upset eb_upset mo_upset with vpunch
    g_slime """
    WHY DO YOU ALWAYS PULL THIS OFF WITH ME!

    GODDAMN IT!

    FINE!

    I'LL BEAT THE HUMAN AND KEEP THE GOLD FOR MYSELF!
    """
    "She looks ready for a last stand"
    # Jump to battle label

label Slime_Intro_Post_Battle_3:
    scene woods_1_noon
    show black at customTransparent(0.5)
    with fade
    #play happy sound

    centered "You got your money back!"
    hide black with dissolve
    """
    That was bothersome

    In front of you lies a defeated slime

    She looks more like a puddle rather than a girl now

    A shape of a what barely looks like a tired face floats in the puddle

    Now that the adrenaline has worn off the exhaustion hits you like a hammer

    Searching for a spot to sit and rest, you remain vigilant of the sentient puddle in front of you
    """
    show greenslime ey_closed mo_open eb_sad at right with moveinright
    g_slime "aweeeeooooo uhhhhhh"
    hide greenslime with moveoutbottom
    with vpunch
    """
    She may be down for good right now

    You find a spot in the shade and sit there to catch your breath
    """
    # play sound wind_blowing
    """
    The breeze gently grazing your skin feels like a caress

    At last some peace

    You take out a water jug and drink what's left of it

    Now that you retrieved your gold pouch you think it is time to go back
    """
    #play sound footsteps
    """
    …

    Should you leave the slime just…

    There?

    She should be fine{w}, right?{p}Not like any animal should be able to harm her…{p}She doesn't even look tasty{w=0.5}.{w=0.6}.{w=0.7}.{w} I think?
    """
    #play sound liquid

    "!" with hpunch

    "You turn around immediately after hearing that"
    show slimemother ey_mid eb_upset mo_serious at center, customBlur(18) with dissolve
    """
    A blue pool appears from behind a tree

    Another slime?

    This time the pool is noticeably larger than the green ones
    """

    "?" "May I know why are you chasing and attacking the small ones?"

    "A voice comes out of the squirming blue blob"

    "?" "Are you perhaps a monster hunter?{p}We do not take kindly to people like you"

    show slimemother at customBlurEase(0.1)

    """
    The blob starts to take form

    It quickly takes a surprisingly accurate humanoid shape

    4 long tentacles emerge from her...{w} dress?

    Now a blue slime woman, barely taller than you, stands there with a stern look on her face
    """

    "Blue Slime" "Not going to answer I take?{p}So you are a rude one too?{p}Aren't you?"

    """
    Is this their boss?

    With your current exhaustion and her size…

    You have to find a way to diffuse the situation {b}now{/b}

    Her tentacles look ready to lunge at you
    """
    menu(screen="choice2"):
        "They started it!":
            show slimemother ey_open mo_open eb_up with vpunch
            """
        	{i}THEY STARTED IT!{/i}{p}You yell in a very annoyed tone

            She can barely keep up with your swift and anger fueled explanation of the events

            She tries to say something but you just don't stop going on and on about the intrincacies of the situation
    		"""

            # End option 1
        "Apologize":
            """
    		Taking a deep breath, you gesture her to calm down

    		Telling her to let you explain the situation
    		"""
            show slimemother ey_mid
            "Blue Slime" "It better be a good explanation…"
            """
    		You calmly go over the succession of events
    		"""
    #End of option 2
    show slimemother ey_closed mo_serious eb_down

    "Blue Slime" "I...{w} see..."

    "You want to make sure she understands that you intended to do things the peaceful way{p}But they weren't interested in negotiations"

    "?" "{b}{i}Get em mama!{/i}{/b}" with hpunch

    show greenslime eb_upset ey_circles at left with moveinleft

    "Green Slime" "That is the man who stole our gold!"

    show slimemother ey_mid eb_upset

    b_slime "I am not your mother… {w} Why do you all insist on…"

    show slimemother ey_open mo_open

    b_slime """
    That's not the important thing here!

    Why are you bothering people in that woman's land in the first place?!

    You are lucky they didn't send a {i}real{/i} monster hunter to kill you!
    """

    "Ouch"

    b_slime "How many times have I told you before?!"

    show greenslime ey_dots eb_up

    "Green Slime" "{size=10}A{/size}"

    show slimemother ey_mid mo_serious

    b_slime "tsk!"

    show slimemother at right with move


    "One of her tentacles extends, going into a nearby brush{p}It picks a couple of leaves and…"

    show slimemother at customXAlign(0.3) with move

    "Shoves them into the green slime"

    show greenslime ey_upset mo_upset at blur_in_and_out, fast_shake(0.1) with vpunch

    "Green Slime" "{b}AAAAAAAAAH BITTERRRRR{/b}"

    "The green slime recoils surprise"

    b_slime "You deserve twice the serving of those"

    show slimemother ey_open eb_mid mo_mid

    show slimemother ey_closed mo_open eb_mid at center with move

    b_slime """
    I apologize for their behavior

    They like to act tough but usually they are good girls"""

    "Green Slime" "{b}BLEGH{/b}" with hpunch

    hide greenslime with moveoutbottom
    with vpunch

    show slimemother ey_mid mo_serious

    b_slime """
    . . .

    Listen

    Would you kindly tell them that you chased them, killed them or whatever they asked of you?

    I will make sure they don't bother that place again, I promise

    So please, make sure they don't come after them
    """

    # Should I plug an optional sex scene here?
    # Like, accept and / or negotiate for sex or something

    """
    The perfect opportunity to leave presents itself

    At this point you just want to finish the quest you were given
    """
    b_slime "Do we have a deal?"

    "You nod"

    show slimemother ey_closed
    b_slime ". . ."

    show slimemother mo_happy

    b_slime """
    Whew

    I am glad

    I am truly sorry about this ordeal, I would love to assist you in some way but
    """

    show slimemother ey_open

    b_slime """
    I have to deal with the three first

    I am indebted to you, if we meet in the future I'll repay the favor somehow
    """

    "Green Slime" "WHAT" with vpunch

    show slimemother ey_mid mo_serious

    b_slime "You shut it"

    show black at customTransparent(0.5) with dissolve

    "With that, your slime trouble has concluded"

    "You should go back to report your success to Reina"

    scene black with wipeleft

    "END"
