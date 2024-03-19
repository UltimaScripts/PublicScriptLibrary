from Assistant import Engine

while FindType(0xc76):
    carrot_plants = Engine.Items.SelectEntities(lambda i: i.ID == 0xc76)
    if carrot_plants == None:
        HeadMsg("No Carrots Found", "self",32)
        Stop()
    #WaitForProperties(carrot_plants,5000)
    scp = []
    scp = sorted(carrot_plants, key=lambda x: Distance(x.X, x.Y))
    if Distance(scp[0].Serial) > 1:
        Pathfind(scp[0].X, scp[0].Y, scp[0].Z)
        while Pathfinding():
            Pause(50)
            if Distance(scp[0].Serial) <= 1:
                Pathfind(-1)
    ClearJournal()
    UseObject(scp[0].Serial)
    while not InJournal("There's nothing more here to harvest.", "system"):
        Pause(200)
        if Distance(scp[0].Serial) > 1:
            break

#if InJournal("You start harvesting...", "system"):
#if InJournal("There's nothing more here to harvest.", "system"):
