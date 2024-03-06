# Name: tracking trainer
# Author: Baler
# Version: 1.0.0
from Assistant import Engine

while not Dead('self'):
    UseSkill("Tracking")
    Pause(2010)
    gumps = Engine.Gumps.GetGumps()
    if gumps[0] == True and gumps[1] is not None:
        for gump in gumps[1]:
            try:
                string = "{ NoDispose }{ NoMove }{ Page 0 }{ ResizePic 0 0 5054"
                if string in gump.Layout:
                    ReplyGump(gump.ID, 0)
            except Exception:
                pass
    Pause(4000)
