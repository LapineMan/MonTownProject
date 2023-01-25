init 6 python:

    #classes
    class Item:
        def __init__(self, name, price, img):
            self.name = name
            self.price = price
            self.img = img

        def use_item(self, target):
            print("Item use_item()")

        def get_desc(self):
            return "item description"


    class Consumable(Item):
        def __init__(self, name, price, img, hp=0, mp=0):
            Item.__init__(self, name, price, img)
            self.hp = hp
            self.mp = mp

        def use_item(self, target):
            target.heal_hp(self.hp)
            target.heal_mp(self.mp)
            diag = "{} used {} and recovered:\n".format(target.name, self.name)
            if self.hp != 0 : diag += "{} hp\n".format(self.hp)
            if self.mp != 0 : diag += "{} mp\n".format(self.mp)
            renpy.say(None, diag)
            return True

        def get_desc(self):
            result = "Restores:"
            if(self.hp != 0):
                result += " {} HP".format(self.hp)
            if(self.mp != 0):
                result += " {} MP".format(self.mp)
            return result

    class Equipment(Item):
        def __init__(self, name, price, img, hp=0 , mp=0, atk=0, dfn=0, mag=0, res=0, wil=0):
            Item.__init__(self, name, price, img)
            self.Hp = hp
            self.Mp = mp
            self.Atk = atk
            self.Dfn = dfn
            self.Mag = mag
            self.Res = res
            self.Wil = wil

        def equip(self, player, inventory, slot=0):
            if slot == 0:
                if not player.HeadSlot:
                    inventory.append(player.HeadSlot)
                player.HeadSlot = self

        def un_equip(self, player, inventory):
            print("Un equip")

        def effect(self):
            print("Effect")


    # Init items
    # Init Consumable
    class Bandage_1(Consumable):
        def __init__(self):
            Consumable.__init__(self, "Bandage", 10, "bandage", hp=20)

    # Init Equipment
    class Wooden_Sword(Equipment):
        def __init__(self):
            Equipment.__init__(self, "Wooden_Sword", 10, "wooden_sword", atk=8)

    # Init Equipment
    class Worn_Knife(Equipment):
        def __init__(self):
            Equipment.__init__(self, "Rusty_Knife", 10, "hatchet", atk=8)


    # Init Equipment
    class Worn_Hatchet(Equipment):
        def __init__(self):
            Equipment.__init__(self, "Worn_Hatchet", 10, "hunting_knife", atk=8)



    # Init item dict
    itemDict = {
        "bandage_1": Bandage_1(),
        "wooden_sword": Wooden_Sword(),
        "rusty_knife": Worn_Knife(),
        "worn_hatchet": Worn_Hatchet()
    }

    # Inventory
    class Inventory:
        def __init__(self):
            # Item stuffs
            self.maxSize = 20
            self.items = []
            self.keyItems = []

            #Money
            self.maxGold = 500
            self.gold = 0

            # Some variables
            self.is_in_battle = False

        def add_gold(self, qty):
            self.gold = min(self.maxGold, self.gold + qty)

        def buy_item(self, item):
            if itemDict[item].price > self.gold:
                # Cannot buy
                return False

            if self.add_item(item):
                self.gold -= itemDict[item].price
            else:
                print("Bought nothing")

        # This one should show dialogue

        def search_item(self, item):
            for i in self.items:
                if(i["item"] == item):
                    return i
            return None

        def get_capacity(self, ):
            total = 0
            for i in self.items:
                total += i["quantity"]
            return total

        def add_item(self, item):
            newItem = self.search_item(item)
            # Check if item would fit the inventory
            if(self.get_capacity() < 20):
                if(newItem == None):
                    self.items.append(
                        {
                        "item":item,
                        "quantity":1
                        }
                    )
                else:
                    newItem["quantity"] += 1
                return True
            return False

        def drop_item(self, item, quantity):
            selectedItem = self.search_item(item)
            if(quantity >= selectedItem["quantity"]):
                self.items.remove(selectedItem)
                return True
            selectedItem["quantity"] -= 1

        def use_item(self, target, item):
            itemDict[item].use_item(target)
            self.drop_item(item, 1)
