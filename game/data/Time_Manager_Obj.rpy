init 3 python:
    class PhaseOfDay(Enum):
        EARLY_MORNING = ("Early Morning", "night")
        MORNING = ("Morning", "evening")
        NOON = ("Noon", "day")
        AFTERNOON = ("Afternoon", "day")
        EVENING = ("Sunset", "evening")
        NIGHT = ("Night", "night_light")
        MIDNIGHT = ("Midnight", "night")

    class TimeManager():
        def __init__(self):
            self.current_phase = PhaseOfDay.AFTERNOON

        def advance_phase(self, advance:int):
            phase_list = list(PhaseOfDay)
            current_index = phase_list.index(self.current_phase)
            new_phase = (current_index + advance) % len(phase_list)
            self.current_phase = phase_list[new_phase]

        def get_current_phase_index(self):
            return list(PhaseOfDay).index(self.current_phase)

        def is_in_phase_range(self, time_range):
            phase_list = list(PhaseOfDay)
            return (self.current_phase >= phase_list.index(time_range[0])) and (self.current_phase <= phase_list.index(time_range[1]))
