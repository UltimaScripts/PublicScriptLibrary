# Name: Taste ID Trainer
# Description: Uses taste id on potions.
# Author: github.com/UltimaScripts/PublicScriptLibrary
# Version: 1.0.0
# Requirements: Potions: Nightsight, Lesser POison, -
#  Normal Poison, Greater Poison, Deadly Poison, Plague Potion
# Notes: 80 to 100 is slow gains
from ClassicAssist.Data.Macros import MacroManager
from Assistant import Engine

## Option Start
## Set potion container Serial
container = 0x5a0f372a
## Set your food graphic id, 0 to disable
foodgraphicid = 0x97b
## Option End

def macroname():
    return str(MacroManager.GetInstance().GetCurrentMacro())

def stopscript(string = "generic stop message.",hue = 0):
    SysMessage(string,hue)
    Stop(macroname())

def checkhunger(foodid):
    if Dead("self"):
        stopscript("Ghost's can't do this, Stopping.")
    if foodid == 0:
        return
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
            stopscript("Can't find food, stopping.", 32)

def train(hue,container):
    UseSkill("Taste Identification")
    WaitForTarget(5000)
    if FindType(0xf0e, 0, container, hue):
        Target("found")
    else:
        stopscript("Can't find potion, Stopping....", 32)
    Pause(10200)

while True:
    checkhunger(foodgraphicid)
    if Skill("Taste Identification") < 20:
        #name hue max_skill
        #an nightsight potion 1109 20
        train(1109, container)
    elif Skill("Taste Identification") < 35:
        #an lesser poison potion 1270 35
        train(1270, container)
    elif Skill("Taste Identification") < 45:
        #an poison potion 1269 45
        train(1269, container)
    elif Skill("Taste Identification") < 60:
        #an greater poison potion 1268 60
        train(1268, container)
    elif Skill("Taste Identification") < 80:
        #an deadly poison potion 1267 80
        train(1267, container)
    elif Skill("Taste Identification") < 100:
        #an plague potion 2071 100
        train(2071, container)
    else:
        stopscript("Congrats you're done, for now...", 69)
