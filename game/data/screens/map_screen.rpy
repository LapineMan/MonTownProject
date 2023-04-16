#Maps
transform map_button_transform:
    anchor (0.5, 0.5)
    on idle:
        easeout 0.1 matrixcolor TintMatrix("#AAAAAA") zoom 0.9
    on hover:
        easeout 0.1 matrixcolor TintMatrix("#FFFFFF") zoom 1.0

screen Map_Screen(world):
    modal True

    default map_data = world.map_data

    python:
        tooltip = GetTooltip()

    frame:
        background "images/maps/{}_map.png".format(world.current_map)
    for l in map_data["locations"]:
        $current_location = world.locations.get(l["loc_id"])

        # Normal sensitive button
        if(current_location.location_state == LocState.NORMAL):
            # Set icon ugliness
            imagebutton idle "images/maps/mapicon_normal.png" at map_button_transform:
                action [Return(l["loc_id"])]
                tooltip current_location.name
                xpos l["xpos"]
                ypos l["ypos"]
        # Shown but innaccessible
        elif (current_location.location_state == LocState.BLOCKED):
            imagebutton idle "images/maps/mapicon_lock.png":
                action NullAction()
                tooltip current_location.name
                xpos l["xpos"]
                ypos l["ypos"]

        elif(current_location.location_state == LocState.BOSS):
            imagebutton idle "images/maps/mapicon_bossbattle.png":
                action Confirm("A difficult enemy awaits!\nDo you wish to proceed?", [Return(l["loc_id"])])
                tooltip current_location.name
                xpos l["xpos"]
                ypos l["ypos"]

        elif(current_location.location_state == LocState.DEMON):
            imagebutton idle "images/maps/mapicon_demon.png":
                action Confirm("Something horrible lurks this place...\nProceed with caution", [Return(l["loc_id"])])
                tooltip current_location.name
                xpos l["xpos"]
                ypos l["ypos"]

        else:
            imagebutton idle "images/maps/mapicon_warning.png":
                action Confirm("Some events may become unavailable after this\nDo you wish to proceed?", [Return(l["loc_id"])])
                tooltip current_location.name
                xpos l["xpos"]
                ypos l["ypos"]

    frame:
        align (0.5, 0.05)
        text map_data["name"]:

            align (0.5, 0.5)

    # Tooltip stuff
    if tooltip:
        text "[tooltip]":
            color "#FFFFFF"
            outlines [ (absolute(8), "#000", absolute(0), absolute(0)) ]
