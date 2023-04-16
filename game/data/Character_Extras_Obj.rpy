init 2 python:
    class CharacterList(store.object):
        def __init__(self):
            self.characters = {}
            self.present_characters = []
            self.current_character = 0
            self.init_characters()

        def init_characters(self):
            data = get_data_from_json("data/inits/characters.json")
            for c in data:
                self.characters[c["id"]] = CharacterEntity(c)

        def scroll_characters(self, n):
            self.current_character = (self.current_character + n) % len(self.present_characters)

        def get_current_character(self):
            if(len(self.present_characters) == 0):
                return None
            return self.present_characters[self.current_character]

        def get_next_character(self):
            if(len(self.present_characters) < 2):
                return None
            if(self.current_character == len(self.present_characters) - 1):
                return None
            return self.present_characters[self.current_character + 1]

        def get_prev_character(self):
            if(len(self.present_characters) < 2):
                return None
            if(self.current_character == 0):
                return None
            return self.characters[self.current_character - 1]

        def init_character_schedules(self):
            for c in self.characters:
                character = self.characters[c]
                del character.schedule

                data = get_data_from_json("data/schedules/{}_schedule_{}.json".format(character.character_id, character.schedule_tag))

                for i in range(len(data)):
                    data[i] = tuple(data[i])
                data = tuple(data)

                character.schedule = data

        def set_present_characters(self, world, time_manager):
            current_character = 0
            for c in self.characters:
                character = self.characters[c]

                if(character.schedule == None):
                    continue

                if(character.schedule[time_manager.get_current_phase_index()][0] == world.current_location):
                    self.present_characters.append(character)
