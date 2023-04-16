init 4 python:
    class LocState(Enum):
        # These three have an effect on the behavior of the button
        NORMAL = 0      # Clickable Circle
        BLOCKED = 1     # Insensitive Lock
        HIDDEN = 2      # Doesn't render on screen
        # These act like NORMAL, but change both the icon and show a warning before continuing
        BOSS = 3        # Double Swords, boss warning
        DEMON = 4       # Shows skull, possible demon encounter or event warning
        IMPORTANT = 5   # Shows exclamation icon, asks if player wants to proceed

    # Using Composition for these
    class AdventureAttributes():
        def __init__(self, data):
            self.encounters = data.get("encounters")
            self.items = data.get("items")

        def add_encounter(self, enemy_set):
            #Uses [ ( [enemyId, enemyId], chance, level), (enemyId, chance, level), ...]
            self.encounters.append(enemy_set)

        def add_item(self, itemId, dropRate):
            #Adds the item Id and a weighted drop rate
            self.items.append((itemId, dropRate))

        def get_random_encounter(self):
            #Use Renpy's random function for this one!
            return weighted_random(self.encounters)

        def get_random_item(self):
            #Use a weighted list
            # Use Renpy's random function for this one!
            return

    class ShopAttributes():
        def __init__(self, data):
            self.shopkeeper = data.get("shopkeeper")
            self.items = data.get("items")
            open_data = data.get("open_range")

            self.open_range = (getattr(PhaseOfDay, open_data[0]), getattr(PhaseOfDay, open_data[1]))

        def add_item(self, item):
            self.items.append(item)

        def add_items(self, items):
            for i in items:
                self.add_item(i)

        def add_temp_item(self, item):
            self.tempItems.append(item)

        def clear_temp_items(self):
            self.tempItems.clear()

    class MapChangeAttributes():
        def __init__(self,data):
            self.maps = data.get("maps")

    class Location:
        def __init__(self, locDict):
            # Base data
            self.location_id = locDict.get("id")
            self.name = locDict.get("name")
            self.bg = locDict.get("background")

            # Functional values
            self.is_bedroom = locDict["is_bedroom"] if ("is_bedroom" in locDict) else False
            self.is_private = locDict["is_private"] if ("is_private" in locDict) else False
            self.is_indoors = locDict["is_indoors"] if ("is_indoors" in locDict) else False
            self.static_background = locDict["static_bg"] if ("static_bg" in locDict) else False
            self.has_night_light = locDict["has_night_light"] if ("has_night_light" in locDict) else False # Dictates if the location needs a night_light variant

            # Visual extras
            self.bg_tags = None # Used if I need to show something extra with the base bg
            # self.shaders = locDict["shaders"] if("shaders" in locDict) else []

            # Functional extras
            self.owner = locDict.get("owner")
            self.search_items = locDict["searchItems"] if ("searchItems" in locDict) else []
            self.location_state = LocState.NORMAL

            # Composition
            if(locDict.get("map_change")):
                self.map_change = MapChangeAttributes(locDict.get("map_change"))
            if(locDict.get("shop")):
                self.shop = ShopAttributes(locDict.get("shop"))
            if(locDict.get("adventure")):
                self.adventure = AdventureAttributes(locDict.get("adventure"))


        def __str__(self):
            return "id: {}, mapId: {}, {} / {}. Enabled? {}, locType {}".format(self.locationId, self.mapId, self.name, self.fileName, self.isEnabled, self.locType)

    # An object that contains every location in the game
    class World(store.object):
        def __init__(self):
            self.locations = {}
            self.current_location = None
            self.init_locations()
            self.current_map = "reina_villa"
            self.map_data = None
            self.get_map_data()

        def init_locations(self):
            data = get_data_from_json("data/inits/init_locations.json")
            for loc in data:
                self.locations[loc["id"]] = Location(loc)

            self.current_location = list(self.locations)[0]

        def get_current_location(self):
            return self.locations[self.current_location]

        def set_current_location(self, loc:str):
            self.current_location = loc

        def set_location_state(self, locs:[str], state:LocState):
            for l in locs:
                self.locations[l].location_state = state

        def get_map_data(self):
            self.map_data = get_data_from_json("data/map_data/{}_map.json".format(self.current_map))
