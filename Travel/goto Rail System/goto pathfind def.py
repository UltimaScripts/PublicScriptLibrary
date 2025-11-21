def goto(xx, yy, zz, tolerance=0):
    Pathfind(xx, yy, zz)
    while Pathfinding():
        Pause(100)
        if Distance(xx, yy) <= tolerance:
            Pathfind(-1)
