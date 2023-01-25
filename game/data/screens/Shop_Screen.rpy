screen Shop_Screen(player, inventory, itemList):
    default xgrid = 3
    default ygrid = 3
    default page = 0
    default section = 0
    default canBuy = False

    default currentShop = world.get_current_location_obj()

    modal True


    textbutton "Leave":
        align (0.95, 0.05)
        action Return()
    frame:
        align (1.0, 1.0)
        xysize (0.5, 0.25)
        text "{}".format(shopTemp):
            align (0.5, 0.5)
    frame:
        xysize (0.5, 1.0)
        xpadding 30
        ypadding 20
        background "screens/bg_shop.png"
        vbox:
            xfill True
            yfill True
            spacing 30
        #    hbox:
        #        align (0.5, 0.5)
        #        spacing 50
        #        textbutton "Buy":
        #            action [SetScreenVariable("page", 0), SetScreenVariable("section", 0)]
        #            selected (section == 0)
        #        textbutton "Sell":
        #            action [SetScreenVariable("page", 0), SetScreenVariable("section", 1)]
        #            selected (section == 1)
        #        textbutton "Talk":
        #            action [NullAction()]
            text "Gold: {}".format(inventory.gold)
            null height 10
            viewport:
                spacing 20
                draggable True
                scrollbars "vertical"
                if section == 0:
                    vbox:
                        for i in itemList:
                            $canBuy = (inventory.gold >= itemDict[i].price)
                            button:
                                action Confirm("Do you want to buy {}".format(i), [Function(inventory.buy_item, i), SetVariable("shopTemp", get_NPC_dialogue_json(world.get_current_location_obj().shopkeeper, "bought"))])
                                #action Show("Confirm_Item_Buy", inventory=inventory, item=i)
                                sensitive canBuy
                                hbox:
                                    xfill True
                                    frame:
                                        xysize (150, 150)
                                        background "items/{}.png".format(itemDict[i].img)
                                    vbox:
                                        yalign 0.5
                                        text "{}".format(itemDict[i].name)
                                        text "{}".format(itemDict[i].get_desc())
                                    text "{}G".format(itemDict[i].price):
                                        yalign 0.5
                                        if(not canBuy):
                                            color "#f00"
            textbutton "Done":
                xalign 1.0
                action [Return()]



screen Confirm_Item_Buy(inventory, item):
    modal True
    frame:
        align (0.5, 0.5)
        xysize (0.5, 0.5)
        vbox:
            align (0.5, 0.5)
            text "Do you want to buy" xalign 0.5
            text "{}".format(item) xalign 0.5
            hbox:
                align (0.5, 0.5)
                xfill True
                frame:
                    xysize (150, 150)
                    background "items/{}.png".format(itemDict[item].img)
                vbox:
                    yalign 0.5
                    text "{}".format(itemDict[item].name)
                    text "{}".format(itemDict[item].get_desc())
                text "{}G".format(itemDict[item].price) yalign 0.5

            hbox:
                spacing 50
                align (0.5, 0.5)
                textbutton "Yes":
                    action [Function(inventory.buy_item, item), SetVariable("shopTemp", get_NPC_dialogue_json(world.get_current_location_obj().shopkeeper, "bought")), Hide("Confirm_Item_Buy")]
                textbutton "No":
                    action [Hide("Confirm_Item_Buy")]
