# Name: GargoylePickaxe and ProspectorsTool Functions
# Description: -
# Usage: -
# Author: github.com/UltimaScripts/PublicScriptLibrary
# Version: 1.0.1
from Assistant import Engine

def ProspectorsTool(px,py):
    if FindType(0xfb4,0,'backpack'):
        UseObject("found")
        WaitForTarget(5000)
        TargetXYZ(px, py, Z())
        Pause(700)
    else:
        HeadMsg("Can't Find ProspectorsTool Returning", "self", 33)
        return

def GargoylePickaxe(equip = True):
    delay = 700
    garg_pick = 0
    if equip == True:
        if FindLayer("OneHanded"):
            item_in_hand = GetAlias('found')
            if Graphic(item_in_hand) == 0xe86 and Hue(item_in_hand) == 1900:
                garg_pick = item_in_hand
            else:
                if FindType(0xe86,0,'backpack',1900):
                    MoveItem(item_in_hand, "backpack")
                    Pause(delay)
                    EquipItem("found", "OneHanded")
                    Pause(delay)
                else:
                    HeadMsg("Can't Find GargoylePickaxe Returning", "self", 33)
                    return False
    else:
        if FindType(0xe86,0,'backpack',1900):
            garg_pick = GetAlias('found')
        else:
            HeadMsg("Can't Find GargoylePickaxe Returning", "self", 33)
            return False
    if garg_pick > 0:
        return garg_pick

def CheckOre(cx,cy):
    Good_Ore_List = ["iron ore","agapite ore","verite ore"]
    for ore in Good_Ore_List:
        if InJournal(ore, "system"):
            # set equip = True if you must equip the pickaxe
            Garg_Pickaxe = GargoylePickaxe(equip = False)
            ProspectorsTool(cx,cy)
            ClearJournal()
            Pause(100)
            # return the serial for the gargoyle pickaxe
            return Garg_Pickaxe
        else:
            return 0

def CheckGolem():
    #0x6f shadow, pet immune
    Golem_List = [0x6e,0x6f,0x6d,0x6c,0xa6,0x6b,0x71,0x70]
    for golem in Golem_List:
        if FindType(golem,2):
            found_golem = GetAlias("found")
            HeadMsg(Name(found_golem)+" Found!", found_golem,33)
            PlaySound("Bike Horn.wav")
            #combat
            #recall
            #die

#------------------
# This section was for my testing
#------------------
# x & y are the land tile you targeted with your pickaxe.
# x and y need to be set, by your own mining script
x = X('self')
y = Y('self') - 1
#Pickaxe is the non-gargoyle pickaxe you use
Pickaxe = 0x4000048b

HeadMsg(str(Pickaxe), "self")
UseObject(Pickaxe)
WaitForTarget(5000)
TargetXYZ(x, y, Z())
Pause(3500)
CheckGolem()
if Hue(Pickaxe) != 1900:
    Pick = CheckOre(x, y)
    if Pick > 0:
        Pickaxe = Pick
        HeadMsg(str(Pickaxe), "self")
SysMessage("Done",33)
#------------------
#------------------
