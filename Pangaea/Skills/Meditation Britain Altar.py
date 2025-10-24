# Name: Meditation Britain Altar
# Author: Baler
# URL: github.com/UltimaScripts/PublicScriptLibrary
# Version: 1.0.1
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

def altergump(aserial):
    for delay in range(3):
        UseObject(aserial)
        Pause(1000)
        gumps = Engine.Gumps.GetGumps()
        if gumps[0] == True and gumps[1] is not None:
            for gump in gumps[1]:
                if gump is not None:
                    if gump.Strings is not None:
                        if "sacrifice" in gump.Strings[0]:
                            ReplyGump(gump.ID, 42)
                            return
    SysMessage("Can't find altar Gump, Stopping...",32)
    Stop()

def findaltar():
    alterpieces = [0x1DC1,0x1DC2,0x1DC3,0x1DC4,0x1DC5,0x1DC6]
    for piece in alterpieces:
        if FindType(piece, 1, 'ground'):
            if Name("found") == "a altar":
                return GetAlias("found")
    SysMessage("Can't find altar, Stopping...",32)
    Stop()

altarserial = findaltar()
while True:
    Checkhunger(Food_GraphicID)
    altergump(altarserial)
    while Mana("self") == MaxMana("self"):
        Pause(100)
    Pause(1000)
    while Mana("self") < MaxMana("self"): 
        UseSkill("Meditation")
        Pause(16000)
