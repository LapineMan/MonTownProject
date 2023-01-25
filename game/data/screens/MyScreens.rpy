#Shows current time and location name
screen TimePlace:
    frame:
        padding (30,20)
        vbox:
            text "{}".format(clock.getTime())
            text "{}".format(world.getLocName())
