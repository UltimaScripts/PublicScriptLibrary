# Name: Meditation Britain Altar
# Author: Baler
# URL: github.com/UltimaScripts/PublicScriptLibrary
# Version: 1.0.0
# Notes: Altar med training caps out at 40.0 skill
## Options Start ##
## Set your food graphic ID
Food_GraphicID = 0x97b
## Options End ##

from Assistant import Engine

def Checkhunger(foodid):
    if not TimerExists("food"):
        SetTimer("food", 0)
    elif Timer("food") < 600000:
        return
    ClearJournal()
    Pause(100)
    while True:
        Msg(".hunger")
        Pause(1000)
        if InJournal("You are simply too full to eat any more!") or InJournal("You manage to eat the food, but you are stuffed!") or InJournal("You're stuffed!") or InJournal("You are quite full."):
            SetTimer("food", 0)
            return
        elif FindType(foodid,-1,"backpack"):
            UseObject("found")
            Pause(1000)
        else:
            HeadMsg("Need Food, Stopping...", "self", 32)
            PlaySound("Bike Horn.wav")
            Stop()

def altergump():
    for delay in range(6):
        Pause(1000)
        gumps = Engine.Gumps.GetGumps()
        if gumps[0] == True and gumps[1] is not None:
            for gump in gumps[1]:
                if gump is not None:
                    if gump.Strings is not None:
                        if "sacrifice" in gump.Strings[0]:
                            ReplyGump(gump.ID, 42)
                            return
    else:
        SysMessage("Can't find altar Gump, Stopping...",32)
        Stop()

def findaltar():
    if FindType(0x1dc3,1,'ground',2999):
        return GetAlias("found")
    else:
        SysMessage("Can't find altar, Stopping...",32)
        Stop()

altarserial = findaltar()
while True:
    Checkhunger(Food_GraphicID)
    UseObject(altarserial)
    altergump()
    while Mana("self") == MaxMana("self"):
        Pause(100)
    Pause(1000)
    while Mana("self") < MaxMana("self"): 
        UseSkill("Meditation")
        Pause(16000)
