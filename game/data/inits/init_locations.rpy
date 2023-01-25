init 3 python:
    class LocType(Enum):
        NORMAL = 0
        SHOP = 1
        ADVENTURE = 2
        TRANSITION = 3
        HOME = 4
        INSTANCE = 5

    class LocState(Enum):
        NORMAL = 0
        BLOCKED = 1
        HIDDEN = 2
        # Shows warning and changes icon, similar to normal
        BOSS = 3
        DEMON = 4
        # Shows warning and may change icon, similar to normal
        IMPORTANT = 5

    locationsInit = {
        0 : {
            "type" : LocType.NORMAL,
            "name" : "Noble House Entrance",
            "fileName" : "gates",
            "mapId" : map_0,
        },
        1: {
            "type" : LocType.NORMAL,
            "name" : "bg_kiosk",
            "fileName" : "kiosk",
            "mapId" : map_0,
        },
        2: {
            "type" : LocType.SHOP,
            "name" : "Store (Reina's Domain)",
            "fileName" : "storeReina",
            "mapId" : map_0,
            "shopkeeper": "shopkeeper1"
        },
        3: {
            "type" : LocType.ADVENTURE,
            "name" : "Farm (Reina's)",
            "fileName" : "bg_farm",
            "mapId" : map_0,
        },
        4: {
            "type" : LocType.TRANSITION,
            "name" : "Forest Path (Leaving Domain)",
            "fileName" : "bg_forestpath",
            "mapId" : map_0,
        },
        5: {
            "type" : LocType.TRANSITION,
            "name" : "Forest Path (Entering Domain)",
            "fileName" : "bg_forestpath",
            "mapId" : map_0,
        },
    }

    def initializeLocations():
        locations = []
        for l in range(len(locationsInit)):
            data = locationsInit[l]

            if(data["type"] == LocType.NORMAL):
                newLoc = initNormalLocation(l, data)

            elif(data["type"] == LocType.SHOP):
                newLoc = initShopLocation(l, data)

            elif(data["type"] == LocType.ADVENTURE):
                newLoc = initAdventureLocation(l, data)

            elif(data["type"] == LocType.TRANSITION):
                newLoc = initNormalLocation(l, data)

            elif(data["type"] == LocType.HOME):
                newLoc = initHomeLocation(l, data)

            locations.append(newLoc)
        return locations

    def initNormalLocation(id : int, data):
        newLoc = BaseLocation(id, data["name"], data["fileName"], data["mapId"], data["type"])
        return newLoc

    def initShopLocation(id : int, data):
        newLoc = ShopLocation(id, data["name"], data["fileName"], data["mapId"], data["type"])
        newLoc.shopkeeper = data["shopkeeper"]
        return newLoc

    def initAdventureLocation(id : int, data):
        newLoc = AdventureLocation(id, data["name"], data["fileName"], data["mapId"], data["type"])
        return newLoc

    def initTransitionLocation(id : int, data):
        newLoc = BaseLocation(id, data["name"], data["fileName"], data["mapId"], data["type"])
        return newLoc

    def initHomeLocation(id : int, data):
        newLoc = HomeLocation(id, data["name"], data["fileName"], data["mapId"], data["type"])
        newLoc.owner = data["owner"]
        return newLoc
