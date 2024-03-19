from ClassicAssist.UO.Data import Statics
#, TileFlags
from Assistant import Engine
from ClassicAssist.Data.Macros import MacroManager

treelist = []
for xx in range(-2,3):
    for yy in range(-2,3):
        statics = Statics.GetStatics(int(Engine.Player.Map), Engine.Player.X + xx, Engine.Player.Y + yy)
        if statics is not None:
            for s in statics:
                if "tree" in s.Name and [s.X, s.Y, s.Z, s.ID] not in treelist:
                    while not Dead("self"):
                        if not FindLayer("TwoHanded"):
                            if FindType(0xf43,0,'backpack'):
                                equipEquipItem("found", "TwoHanded")
                                Pause(1000)
                            else:
                                SysMessage("No Tool Found",32)
                                Stop(str(MacroManager.GetInstance().GetCurrentMacro()))
                        #UseType(0xf43,0,'backpack')
                        UseLayer("TwoHanded")
                        WaitForTarget(5000)
                        TargetXYZ(s.X, s.Y, s.Z, s.ID)
                        ClearJournal()
                        Pause(2200)
                        #if InJournal("You chop some") or InJournal("fail to produce"):
                        #    ClearJournal()
                        #    Pause(600)
                        #    break
                        if InJournal("not enough wood") or InJournal("Target cannot be") or InJournal("is too far") or InJournal("use an axe on"):
                            treelist.append([s.X, s.Y, s.Z, s.ID])
                            Pause(200)
                            break
                        if InJournal("world is saving"):
                            ClearJournal()
                            Pause(2000)
                            break
                    treelist.append([s.X, s.Y, s.Z, s.ID])
