screen Inventory_Screen(player, inventory):

    modal True
    #Declare stuff that needs to be a set variable 1 time
    default inv_page = 0
    default grid_size = 3
    default next_page_allowed = False
    # 0 means items, 1 means key items
    default section = 0

    # Here we update the variables that must keep changing
    python:
        tooltip = GetTooltip()

        #Needed for the grid generation
        if(section == 0):
            inv_size = len(inventory.items)
        else:
            inv_size = len(inventory.keyItems)

        #Check if you can go to the next page of the inventory
        if(inv_size <= (inv_page + 1) * (grid_size * grid_size)):
            next_page_allowed = False

            #Check if you aren't in an empty space after deleting an item
            if(inv_page > 0 and inv_size <= inv_page * (grid_size * grid_size)):
                inv_page -= 1
        else:
            next_page_allowed = True

        # Debug
        player_hp = player.hp


    # Tooltip stuff
    if tooltip:
        text "[tooltip]":
            color "#FFFFFF"
            outlines [ (absolute(8), "#000", absolute(0), absolute(0)) ]


    #Debug
    if False:
        vbox:
            text "Page: {}".format(inv_page)
            text "Section {}".format(section)
            text "Player HP: {}".format(player_hp)
            textbutton "Hurt player":
                action Function(player.deal_damage, 1, 2)

    frame:
        align (0.5,0.5)
        xysize (700, 600)
        padding (25, 25)
        background "screens/bg_inventory.png"
        # background "gui/bg_simple.png"
        vbox:
            align (0.5,0.5)
            textbutton "Close":
                xalign 1.0
                tooltip "Close inventory"
                action [Hide("Inventory_Screen")]

            hbox:
                spacing 20
                textbutton "Items":
                    action SetScreenVariable("section", 0)
                textbutton "Key Items":
                    action SetScreenVariable("section", 1)

            viewport:
                spacing 20
                draggable True
                scrollbars "vertical"
                if section == 0:
                    vbox:
                        for i in inventory.items:
                            button:
                                action ShowTransient("Selected_Item", player=player, inventory=inventory, i=i)

                                hbox:
                                    xfill True
                                    frame:
                                        xysize (150, 150)
                                        background "items/{}.png".format(itemDict[i["item"]].img)
                                    vbox:
                                        yalign 0.5
                                        text "{}".format(itemDict[i["item"]].name)
                                        text "{}".format(itemDict[i["item"]].get_desc())
                                    text "x{}".format(i["quantity"]) yalign 0.5

                elif section == 1:
                    vbox:
                        # Key items
                        # TODO: unfinished
                        for i in inventory.keyItems:
                            button:
                                action Show("Selected_Item", player=player, inventory=inventory, i=i)
                                hbox:
                                    xfill True
                                    frame:
                                        xysize (150, 150)
                                        background "items/{}.png".format(itemDict[i["item"]].img)
                                    vbox:
                                        yalign 0.5
                                        text "{}".format(itemDict[i["item"]].name)
                                        text "{}".format(itemDict[i["item"]].get_desc())
                                    text "x{}".format(i["quantity"]) yalign 0.5

            hbox:
                if inv_page > 0:
                    textbutton "Prev Page":
                        action SetScreenVariable("inv_page", inv_page-1)

                if next_page_allowed:
                    textbutton "Next Page":
                        action SetScreenVariable("inv_page", inv_page+1)

screen Selected_Item(player, inventory, i):
    modal True
    frame:
        align (0.5, 0.5)
        xysize (500, 300)
        vbox:
            text "{}".format(itemDict[i["item"]].name)
            text "{}".format(itemDict[i["item"]].get_desc())
            align (0.5, 0.5)
            if not inventory.is_in_battle:
                textbutton "Use":
                    action [Function(inventory.use_item, player, i["item"]), Hide("Selected_Item")]
            else:
                textbutton "Use in battle":
                    action [Return({"action":7, "item":itemDict[i["item"]]})]

            textbutton "Drop":
                action Show("Confirmation_For_Drop",player=player, inventory=inventory, i=i["item"])

            textbutton "Cancel":
                action Hide("Selected_Item")

screen Confirmation_For_Drop(player, inventory, i):
    modal True
    frame:
        padding (20, 20)
        align (0.5, 0.5)
        xysize (600, 250)
        vbox:
            align (0.5, 0.5)
            text "Are you sure you want to drop this item?"
            hbox:
                align (0.5, 0.5)
                spacing 75
                textbutton "Yes":
                    action [Function(inventory.drop_item, i, 1), Hide("Confirmation_For_Drop"), Hide("Selected_Item")]
                textbutton "No":
                    action Hide("Confirmation_For_Drop")
