init 4 python:
    # TODO: Cambiar herencia a agregacion
    #Objects which contain info for every individual location
    class BaseLocation:
        def __init__(self, locId:int, name:str, fileName:str, mapId, locType:LocType):
            self.locationId = locId
            self.name = name
            self.fileName = fileName
            self.mapId = mapId
            self.locState = LocState.NORMAL
            self.locType = locType

        def __str__(self):
            return "id: {}, mapId: {}, {} / {}. Enabled? {}, locType {}".format(self.locationId, self.mapId, self.name, self.fileName, self.isEnabled, self.locType)


    class AdventureLocation(BaseLocation):
        def __init__(self, locId:int, name:str, fileName:str, mapId:int, locType:LocType):
            BaseLocation.__init__(self, locId, name, fileName, mapId, locType)
            self.encounters = []
            self.items = []
            self.randomEncounterChance = 0.25

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


    class ShopLocation(BaseLocation):
        def __init__(self, locId:int, name:str, fileName:str, mapId:int, locType:LocType):
            BaseLocation.__init__(self, locId, name, fileName, mapId, locType)
            self.shopkeeper = None
            self.items = []
            self.tempItems = []

        def add_item(self, item):
            self.items.append(item)

        def add_items(self, items):
            for i in items:
                self.add_item(i)

        def add_temp_item(self, item):
            self.tempItems.append(item)

        def clear_temp_items(self):
            self.tempItems.clear()


    class HomeLocation(BaseLocation):
        def __init__(self, locId:int, name:str, fileName:str, mapId:int, locType:LocType):
            BaseLocation.__init__(self, locationId, name, fileName, mapId, locType)
            self.storage = []
            self.garden = []
            self.owner = owner

        def sleep(self):
            return

        def rest(self):
            return

        def cook(self):
            return

        def take_bath(self):
            return


    # An area which contains various locations and maps
    class Zone:
        def __init__(self, zone_id, name, map, locations):
            self.zoneId = zoneId
            self.name = name
            self.map = map
            self.locations = locations

        def set_enable_all(self, val):
            for loc in self.locations:
                loc.isEnabled = val

    # An object that contains every location in the game
    class World(store.object):
        def __init__(self):
            self.locations = initializeLocations()
            self.currentLoc = 0

        def enable_locations(self, idList):
            for i in idList:
                self.enable_location(i)

        def disable_all(self):
            for loc in self.locations:
                loc.isEnabled = False

        def enable_location(self, id):
            self.locations[id].isEnabled = True

        def get_current_location_type(self):
            return self.locations[self.currentLoc].locType

        def set_current_location(self, locationId):
            self.currentLoc = locationId

        def get_current_location(self):
            return self.currentLoc

        def get_current_location_obj(self):
            return self.locations[self.currentLoc]

        def get_location_name(self, index):
            try:
                return self.locations[index].name
            except:
                return "Got an error trying to get that location"

        def get_current_location_name(self):
            return self.locations[self.currentLoc].name

        def get_current_location_file_name(self):
            return self.locations[self.currentLoc].fileName

        def get_current_map(self):
            return self.locations[self.currentLoc].mapId

        def is_location_enabled(self, locationId):
            if(locationId >= len(self.locations)):
                return False
            return self.locations[locationId].isEnabled

        def is_current_location_enabled(self):
            return self.locations[self.currentLoc].isEnabled
