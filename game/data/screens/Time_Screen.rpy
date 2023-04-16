#Shows current time and location name
screen Time_Screen(t_manager, w_manager):
    default phase = t_manager.current_phase.value[0]
    default place = w_manager.get_current_location().name
    frame:
        padding (30,20)
        vbox:
            text "[phase]"
            text "[place]"
