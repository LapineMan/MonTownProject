label baphi_intro_encounter:
    "Whoever or...{p}Whatever she is..."
    "It doesn't seem that she will listen to reason"
    "You prepare youself for an the encounter"
    call battle_label(
        {
            "enemies" : [Baphi_Enemy_Intro()],
            "background" : "bg_woods_1_night",
            "music" : "REPULSIVE - 0000'",
            "canFlee" : False,
            "initial_dialogue":["Baphomet",". . ."],
            "endTheme": None
        }
    ) from _call_battle_label_2
