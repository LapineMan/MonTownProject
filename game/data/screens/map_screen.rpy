#Maps


transform Map_Icon_Transform:
    on idle:
        linear 0.1 matrixcolor TintMatrix("#AAAAAA")
    on hover:
        linear 0.1 matrixcolor TintMatrix("#FFFFFF")

screen Map_Screen(world):
    modal True

    default map = world.get_current_map()
    default mapData = map["locations"]
    default mapName = map["name"]
    default mapId = map["mapId"]
    default iconString = ""
    python:
        tooltip = GetTooltip()

    frame:
        background "images/maps/map_{}.png".format(mapId)
    frame:
        background "images/maps/mapframe.png"
    for i in mapData:
        $current = world.locations[i["locRef"]]
        # Normal sensitive button
        if(current.locState == LocState.NORMAL):
            # Set icon ugliness
            python:
                if(current.locType == LocType.NORMAL):
                    iconString = "normal"
                elif(current.locType == LocType.SHOP):
                    iconString = "shop"
                elif(current.locType == LocType.ADVENTURE):
                    iconString = "adventure"
                elif(current.locType == LocType.TRANSITION):
                    iconString = "transition"
                elif(current.locType == LocType.HOME):
                    iconString = "home"
                else:
                    iconString = "skull"

            imagebutton idle "images/maps/mapicon_{}.png".format(iconString) at Map_Icon_Transform:
                action [Return(i["locRef"])]
                tooltip world.get_location_name(i["locRef"])
                xpos i["xpos"]
                ypos i["ypos"]
        # Shown but innaccessible
        elif (current.locState == LocState.BLOCKED):
            imagebutton idle "images/maps/mapicon_lock.png":
                action NullAction()
                tooltip world.get_location_name(i["locRef"])
                xpos i["xpos"]
                ypos i["ypos"]

        elif(current.locState == LocState.BOSS):
            imagebutton idle "images/maps/mapicon_bossbattle.png":
                action NullAction()
                tooltip world.get_location_name(i["locRef"])
                xpos i["xpos"]
                ypos i["ypos"]

        elif(current.locState == LocState.DEMON):
            imagebutton idle "images/maps/mapicon_demon.png":
                action NullAction()
                tooltip world.get_location_name(i["locRef"])
                xpos i["xpos"]
                ypos i["ypos"]

        else:
            imagebutton idle "images/maps/mapicon_warning.png":
                action NullAction()
                tooltip world.get_location_name(i["locRef"])
                xpos i["xpos"]
                ypos i["ypos"]

    # Tooltip stuff
    if tooltip:
        text "[tooltip]":
            color "#FFFFFF"
            outlines [ (absolute(8), "#000", absolute(0), absolute(0)) ]
