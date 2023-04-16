init 0 python:
#Functions
    def show_enemy(entity, attributes = None, atList = []):
        imgToShow = entity.fileName
        if(entity.imgAttribute != None): imgToShow += " {}".format(entity.imgAttribute)
        if(attributes != None): imgToShow += " {}".format(attributes)
        print("imgToShow: " + imgToShow)
        renpy.show(imgToShow, tag="{}_{}".format(entity.fileName, entity.tempId), at_list=atList)

    def revert_expressions(expressions:str):
        expressions = "-" + expressions
        return expressions.replace(" ", " -")

    def print_locations(locs):
        for i in locs:
            print(i)

    def remove_event_by_name(eventsList, eventName):
        for e in eventsList:
            if(e.labelName == eventName):
                eventsList.remove(e)
                return

    def check_and_call_for_events(triggers, place, character, currentTime):
        for i in range(len(triggers)):
            if(triggers[i].is_triggered(place=place,character=character, currentTime=currentTime)):
                renpy.notify("Triggered event: {}".format(triggers[i].labelName))
                renpy.jump(triggers[i].labelName)

    def get_object_index(array, object):
        for a in range(len(array)):
            if(object == array[a]):
                return a

        print("Could not find object in array")
        return -1

    def get_spacing(n:int):
        n *= 1.0
        distribution = (1 / (n+1))
        return distribution

    def show_characters_by_order(enemies):
        space = get_spacing(len(enemies))
        print(space)
        for e in enemies:
            position = (space + (e.tempId * space))
            show_enemy(e, atList = [evenly_order_h(position)])
            renpy.with_statement(dissolve)

    def binarySearch(n, array):
        #check if array is empty
        if(len(array) < 1):
            return -1
        i = (len(array)-1)/2
        #Check if n was found
        if(array[i] == n):
            return i
        #If the last number is not n then it's over
        if(len(array) == 1):
            return -1
        if(array[i] < n):
            return binarySearch2(i+1, len(array)-1, n, array)
        else:
            return binarySearch2(0, i-1, n, array)

    def binarySearch2(bot, top, n, array):
        i = int( round( (top + bot) /2) )
        if(array[i] == n):
            return i
        if(top == bot):
            return -1
        if(array[i] < n):
            return binarySearch2(i+1, top, n, array)
        else:
            return binarySearch2(bot, i-1, n, array)


    #Function that erases and calls other functions to know what to draw
    def update_scene(transition=None):
        renpy.scene()
        if(transition != None):
            renpy.with_statement(transition)
        show_current_background(world, time_manager)
        character_list.set_present_characters(world, time_manager)
        #show_current_character(character_list)


    #Display the selected character
    #FIX this
    def show_current_character(characterList):
        if(not len(characterList.characters)):
            sel = characterList.get_current_character()
            next = characterList.get_next_character()
            prev = characterList.get_prev_character()
            #renpy.with_statement(move)
            renpy.show("{}".format(sel.fileName))
            if(next is not None):
                #renpy.with_statement(moveinleft)
                renpy.show("{}".format(next.fileName), at_list=[right, unselectedChar, darken])
            if(prev is not None):
                #renpy.with_statement(moveinright)
                renpy.show("{}".format(prev.fileName), at_list=[left, unselectedChar, darken])


    #Display current location
    def show_current_background(world, time_manager):
        loc = world.get_current_location()
        light = "_{}".format(time_manager.current_phase.value[1])
        if(loc.static_background):
            light = ""
        elif(time_manager.current_phase == PhaseOfDay.NIGHT):
            if(not loc.has_night_light):
                light = "_{}".format(PhaseOfDay.MIDNIGHT.value[1])

        renpy.show("bg_{}{}".format(loc.bg, light))

    #button stuff: recieves boolean, False is left, True is Right
    # TODO: This may be deleted
    def selectCharacter(dir, ind):
        #print("Selected Char before func {}".format(ind))
        if(ind > len(presentCharacters) - 1):
            ind = len(presentCharacters) - 1

        if(not dir and selectedChar > 0):
            ind = ind - 1
            #print("Selected prev character, index val > {}".format(ind))

        elif(dir and ind < len(presentCharacters) - 1):
            ind = ind + 1
            #print("Selected prev character, index val {}".format(ind))

        return ind


    def get_data_from_file(dir:str):
        try:
            data = renpy.file(dir, encoding="UTF-8").read()
            return data
        except:
            return "Chien said: File in {} not found".format(dir)

    def get_data_from_json(dir:str):
        try:
            decoder = json.JSONDecoder()
            data = decoder.decode(renpy.file(dir, encoding="UTF-8").read())
            return data
        except:
            print("Could not find file: {}".format(dir))
            return None


    def get_data_from_json2(dir:str):
        data = renpy.file("{}.json".format(dir), encoding = "UTF-8")
        data = json.load(data)
        return data

    def get_NPC_dialogue_json(chara:str, type:str):
        # Load file
        data = renpy.file("dialogue/{}/{}.json".format(chara, chara), encoding = "UTF-8")
        data = json.load(data)
        # return line
        line = renpy.random.choice(data[type])
        return line

    def remove_blank_spaces(array):
        for i in range(0, len(array)-1):
            if(array[i] == ""):
                array.pop(i)
        print(array)
        return array

    def string_array_to_int_array(arr):
        for i in range(len(arr)):
            arr[i] = int(arr[i])
        return arr

    def weighted_random(choices):
        print(choices)
        # Strongly based on Yang Zhou's version (yangzhou1993.medium.com)
        # This receives an array of tuples [(item, weight), (item, weight), ...]
        # This function should receive arrays ordered from highest to lowest weights
        sum = 0
        for i in choices:
            sum += i[1]

        r = random.randint(1, sum)

        for selected, weight in choices:
            r = r - weight
            if r <= 0:
                return selected

    def create_object(className):
        obj = globals()[className]
        return obj()

    def generate_characters(array):
        result = {}
        for i in array:
            result[i.fileName] = Character(i.name, image=i.fileName)
        return result

    def compare_names(s, array):
        for i in array:
            if(s == i.name or s == i.fileName):
                return False

        return True
