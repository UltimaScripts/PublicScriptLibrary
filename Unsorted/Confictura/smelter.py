#v1.0
from ClassicAssist.UO.Data import Statics
from Assistant import Engine
#0x19b7
ore_list = [0x19b9,0x19b8]
pack_animal = 0
delay = 800

def smelter():
    for xx in range(-2,3):
        for yy in range(-2,3):
            statics = Statics.GetStatics(int(Engine.Player.Map), Engine.Player.X + xx, Engine.Player.Y + yy)
            for s in statics:
                if "forge" in s.Name:
                    for ore in ore_list:
                        #if ore type = 0x19b7 need 2 or more
                        if pack_animal == 0:
                            while FindType(ore,0,'backpack',0):
                                UseType(ore,0,'backpack')
                                WaitForTarget(5000)
                                TargetXYZ(s.X, s.Y, s.Z, s.ID)
                                Pause(delay)
                        else:
                            while FindType(ore,0,pack_animal):
                                UseType(ore,0,pack_animal)
                                WaitForTarget(5000)
                                TargetXYZ(s.X, s.Y, s.Z, s.ID)
                                Pause(delay)

smelter()