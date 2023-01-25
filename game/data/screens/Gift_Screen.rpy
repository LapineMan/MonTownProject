screen Gift_Screen(inventory):

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


    # Tooltip stuff
    if tooltip:
        text "[tooltip]":
            color "#FFFFFF"
            outlines [ (absolute(8), "#000", absolute(0), absolute(0)) ]

    frame:
        align (0.5,0.5)
        xysize (700, 600)
        padding (25, 25)
        background "gui/bg_simple.png"
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

            grid grid_size grid_size:
                spacing 20

                if section == 0:
                    #Generate the grid based on items
                    for i in range(inv_page * 9, (inv_page * 9) + 9):
                        if i < inv_size:
                            imagebutton idle "items/{}.png".format(inventory.items[i].img):
                                action Show("Gift_Selected_Item", inventory=inventory, i=i)
                                tooltip "{}: {}".format(inventory.items[i].name, inventory.items[i].get_desc())

                        else:
                            null


            hbox:
                if inv_page > 0:
                    textbutton "Prev Page":
                        action SetScreenVariable("inv_page", inv_page-1)

                if next_page_allowed:
                    textbutton "Next Page":
                        action SetScreenVariable("inv_page", inv_page+1)

screen Gift_Selected_Item(inventory, i):
    modal True
    frame:
        align (0.5, 0.5)
        xysize (500, 300)
        vbox:
            text "{}".format(i)
            text "{}: {}".format(inventory.items[i].name, inventory.items[i].get_desc())
            align (0.5, 0.5)
            textbutton "Give":
                action [Show("Confirmation_For_Gift", inventory, i)]

            textbutton "Cancel":
                action Hide("Selected_Item")

screen Confirmation_For_Gift(inventory, i):
    modal True
    frame:
        padding (20, 20)
        align (0.5, 0.5)
        xysize (600, 250)
        vbox:
            align (0.5, 0.5)
            text "Do you want to give this item?"
            hbox:
                align (0.5, 0.5)
                spacing 75
                textbutton "Yes":
                    action [Function(inventory.drop_item, i), Hide("Confirmation_For_Gift"), Hide("Gift_Selected_Item")]
                textbutton "No":
                    action Hide("Confirmation_For_Gift")
