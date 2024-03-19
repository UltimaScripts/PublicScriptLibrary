CancelTarget()
ClearObjectQueue()
ClearTargetQueue()

def chek():
    while Poisoned("self"):
        CancelTarget()
        while Poisoned("self") and not TargetExists("Any"):
            Cast("Cure")
            WaitForTarget(500)
        Target("self")
        Pause(1000)
        if not Poisoned("self"):
            CancelTarget()
            ClearObjectQueue()
            ClearTargetQueue()
    if Hits("self") < 40:
        PlaySound("Bike Horn.wav")

SetTimer("rota", 11000)
while not Dead('self'):
    Pause(500)
    chek()
    if Timer("rota") >= 11000 and not Poisoned("self"):
        UseSkill("Item Identification")
        WaitForTarget(5000)
        Target(0x587ce448)
        Pause(100)
        UseObject(0x5a140510)
        SetTimer("rota", 0)