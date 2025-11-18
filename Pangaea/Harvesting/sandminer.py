# Name: Sand Miner
# Description: Digs sand around player
# Usage: play with sand in viewable area
# Author: github.com/UltimaScripts/PublicScriptLibrary
# Version: 1.0.0
# Credits: 
from ClassicAssist.UO.Data import TileFlags, MapInfo
from ClassicAssist.Data.Macros import MacroManager
from Assistant import Engine

##### Options Start #####
## Food Graphic ID
foodgraphic = 0x97b
## Search area options
## viewable area is 18x18
minx = -18
maxx = 18
miny = -18
maxy = 18
## Direction to dig
## True == bottom left to top right
## False == top right to bottom left
digdirection = True
##### Options End #####
## Don't edit below here unless you know what you're doing.

def stopscript(string = "generic stop message.", hue = 0, sound = False, soundfile = "Bike Horn.wav"):
    if sound == True:
        PlaySound(soundfile)
    SysMessage(string,hue)
    Stop(str(MacroManager.GetInstance().GetCurrentMacro()))

def Findtool():
    Tools = [0xf39]
    SetAlias("found", 0)
    for t in Tools:
        if FindType(t, -1, "backpack"):
            return GetAlias("found")
    stopscript("No Tool Found, Stopping",32,True)

def path(x,y,z,tol):
    Pathfind(x, y, z)
    if not TimerExists("pathtimer"):
        SetTimer("pathtimer", 0)
    while Pathfinding():
        Pause(100)
        if Distance(x,y) <= tol:
            Pathfind(-1)
            break
        elif Timer("pathtimer") > 5000:
            path(x,y,z,tol)
    RemoveTimer("pathtimer")
    Pause(50)

def Journ():
    SetTimer("journaltimer", 0)
    while True:
        Pause(100)
        if Timer("journaltimer") > 120000:
            break
        if InJournal("You can't mine there.","",-1,-1,"miningjournal"):
            break
        if InJournal("There's not enough sand here to harvest.","",-1,-1,"miningjournal"):
            break
        if InJournal("You have dug up all the sand.","",-1,-1,"miningjournal"):
            break
        if InJournal("You have worn out your tool!","",-1,-1,"miningjournal"):
            break
        if InJournal("Your movements have interrupted your work.","",-1,-1,"miningjournal"):
            break
    RemoveTimer("journaltimer")

def Mine(minex,miney):
    mytool = Findtool()
    HeadMsg("Mining!..", "self",60)
    ClearJournal("miningjournal")
    if TargetExists("any"):
        CancelTarget()
        Pause(200)
    UseObject(mytool)
    WaitForTarget(5000)
    TargetXYZ(minex, miney, 0)
    Pause(1000)
    Journ()
    #HeadMsg("Completed!..", "self",80)

def CheckTiles(minx, maxx, miny, maxy, direction):
    spots_list = []
    for x in range(minx,maxx):
        for y in range(miny,maxy):
            Pause(10)
            spotx = (Engine.Player.X + x)
            spoty = (Engine.Player.Y + y)
            if (MapInfo.GetLandTile(int(Engine.Player.Map), spotx, spoty)).Name is 'sand':
                if (MapInfo.GetLandTile(int(Engine.Player.Map), spotx, spoty).Flags.HasFlag(TileFlags.Impassable)):
                    continue
                spot = [spotx,spoty,Distance(spotx,spoty)]
                if spot not in spots_list:
                    spots_list.append(spot)
    if len(spots_list) > 0:
        scp = []
        if direction == True or direction != False:
            scp = sorted(spots_list, key=lambda x: (-x[1], -x[0]) )
        elif direction == False:
            scp = sorted(spots_list, key=lambda x: (-x[1], x[0]) )
        return scp
    return 0

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

# start
#Can take 15-30s depending on cpu
SysMessage("Building sand_list please wait...", 64)
sand_list = CheckTiles(minx, (maxx + 1), miny, (maxy + 1), digdirection)
if sand_list != 0:
    for ssc in range(len(sand_list)):
        if Distance(sand_list[ssc][0], sand_list[ssc][1]) > 2:
            path(sand_list[ssc][0], sand_list[ssc][1], 0, 2)
        checkhunger(foodgraphic)
        Mine(sand_list[ssc][0], sand_list[ssc][1])
        Pause(10)
else:
    stopscript("No sand found.", 32)

stopscript("")
