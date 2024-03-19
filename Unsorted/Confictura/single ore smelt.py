from Assistant import Engine
from ClassicAssist.UO.Data import Statics
from ClassicAssist.Data.Macros import MacroManager

def macroname():
    return str(MacroManager.GetInstance().GetCurrentMacro())

def find_forge():
    for xx in range(-2,3):
        for yy in range(-2,3):
            statics = Statics.GetStatics(int(Engine.Player.Map), Engine.Player.X + xx, Engine.Player.Y + yy)
            for s in statics:
                if "forge" in s.Name:
                    return [s.X, s.Y, s.Z, s.ID]
    return 0

frg = find_forge()
if frg == 0:
    SysMessage("No Forge Found, Stopping.",32)
    Stop(macroname())

container1 = GetAlias('backpack')
container2 = 0x4019d372
hue = 0
UseObject(container2)
Pause(1000)
while FindType(0x19b9, 0, container1, hue):
    MoveItem("found", container2, 1)
    Pause(1000)
    if FindType(0x19b9, 0, container2, hue):
        UseObject("found")
        WaitForTarget(5000)
        TargetXYZ(frg[0], frg[1], frg[2], frg[3])
        Pause(1000)
        if FindType(0x19b8, 0, container2, hue):
            UseObject("found")
            WaitForTarget(5000)
            TargetXYZ(frg[0], frg[1], frg[2], frg[3])
            Pause(1000)
ClearIgnoreList()
while FindType(0x19b7, 0, container2, hue):
    MoveItem("found", container2)
    IgnoreObject("found")
    Pause(1000)
ClearIgnoreList()
while FindType(0x19b7, 0, container2, hue, 2):
    UseObject("found")
    WaitForTarget(5000)
    TargetXYZ(frg[0], frg[1], frg[2], frg[3])
    Pause(1000)