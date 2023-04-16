init 7 python:
    # Init Consumable
    class ITEM_Bandage_1(Consumable):
        def __init__(self):
            Consumable.__init__(self, "Common Bandage", 10, "bandage1", hp=20)

    # Init Equipment
    class WPN_Knife_1(Equipment):
        def __init__(self):
            Equipment.__init__(self, "Worn_Knife", 10, "knife1", atk=8)

    # Init item dict
    itemDict = {
        "bandage_1": ITEM_Bandage_1(),
        "rusty_knife": WPN_Knife_1(),
    }
