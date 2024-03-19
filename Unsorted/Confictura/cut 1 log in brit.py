if FindType(0x1be0,0,'backpack',0):
    if Skill("Lumberjackin") < 66.7:
        MoveItemOffset("found", 0, 0, 0, -1)
        Pause(700)
        for x in range(1,11):
            if FindType(0x1be0,0,0):
                MoveItem("found", 0x4019d36e,1)
                Pause(700)
                if FindType(0x1be0,0,'backpack',0):
                    UseObject('found')
                    WaitForTarget(5000)
                    Target(0x40062f47)
                    Pause(700)
        if FindType(0x1be0,0,-1,0):
            MoveItem("found", 0x4019d36e)
            Pause(700)
    else:
        if FindType(0x1be0,0,'backpack',0):
            UseObject('found')
            WaitForTarget(5000)
            Target(0x40062f47)

elif FindType(0x1be0,0,'backpack',1863):
    MoveItemOffset("found", 0, 0, 0, -1)
    Pause(700)
    for x in range(1,11):
        if FindType(0x1be0,0,0,1863):
            MoveItem("found", 0x4019d36e,1)
            Pause(700)
            if FindType(0x1be0,0,'backpack',1863):
                UseObject('found')
                WaitForTarget(5000)
                Target(0x40062f47)
                Pause(700)
    if FindType(0x1be0,0,0,1863):
        MoveItem("found", 0x4019d36e)
        Pause(700)

elif FindType(0x1be0,0,'backpack',1191):
    MoveItemOffset("found", 0, 0, 0, -1)
    Pause(700)
    for x in range(1,11):
        if FindType(0x1be0,0,0,1191):
            MoveItem("found", 0x4019d36e,1)
            Pause(700)
            if FindType(0x1be0,0,'backpack',1191):
                UseObject('found')
                WaitForTarget(5000)
                Target(0x40062f47)
                Pause(700)
    if FindType(0x1be0,0,0,1191):
        MoveItem("found", 0x4019d36e)
        Pause(700)
else:
    Stop()