from Assistant import Engine
from ClassicAssist.UO.Data import Statics

kindling = 0xde1
dagger = 0x587de0b3
ClearJournal()
ignore_list = []
#checks 2 tiles away from the player in all directions
for xx in range(-2,3):
    for yy in range(-2,3):
        statics = Statics.GetStatics(int(Engine.Player.Map), Engine.Player.X + xx, Engine.Player.Y + yy)
        if statics is not None:
            for s in statics:
                if "tree" in s.Name:
                    if [s.X, s.Y] not in ignore_list:
                        while not InJournal("There's not enough kindlings here to cut.", "system"):
                            if Distance(s.X, s.Y) > 2:
                                break
                            UseObject(dagger)
                            WaitForTarget(5000)
                            TargetXYZ(s.X, s.Y, s.Z, s.ID)
                            Pause(2000)
                        ClearJournal()
                        ignore_list.append([s.X, s.Y])