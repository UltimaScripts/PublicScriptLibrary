# Name: Confictura Taming Semi-Auto
# Author: Ultimascripts
# 1.1.0
# Notes: Searches the screen for any creature and tries to tame.
#        It may sometimes fail, so keep an eye on it.
#        Tested on Confictura outside Brit 50 - 100.
from Assistant import Engine

# Name to rename tames before releasing, it also ignores animals with this name.
rename_name = "Snoopy"
# pet_list is for the Serials of your tamed pets or they may get released
pet_list = []
# ignore_list is Serials to ignore.
ignore_list = []
# no_tame_list is Graphic IDs to ignore, Add less skill tames IDs as they become invalid.
no_tame_list = []
Follows = Followers()
ClearJournal()

def find_mobs():
    mobs = []
    try:
        Mobs = Engine.Mobiles.SelectEntities(lambda m: not Innocent(m.Serial) and not Murderer(m.Serial)
                                         and m.Serial != Engine.Player.Serial and m.ID not in no_tame_list
                                         and m.Serial not in ignore_list and rename_name not in m.Name
                                         and m.Serial not in pet_list)
    except Exception as inst:
        #print(type(inst))
        #print(inst.args)
        #print(inst)
        SysMessage("Find Mobs Error",33)
        Pause(10000)
    if Mobs:
        Mobs = sorted(Mobs, key=lambda x: Distance(x.X, x.Y))
        return Mobs
    else:
        SysMessage("Problem Finding Mobs, Stopping.",33)
        Stop()

def goto( serial = 0, x = 0, y = 0, z = 0 ):
    if serial != 0:
        Pathfind( serial )
    else:
        Pathfind( x, y, z )
    while Pathfinding():
        Pause(100)
        if Distance(m.Serial) < 2:
            Pathfind(-1)
            Resync()

def TameFunc(mobserial):
    if Distance(m.Serial) > 2:
        goto( serial = mobserial )
    UseSkill("Tamin")
    WaitForTarget(5000)
    Target(mobserial)
    Pause(600)

def backup_release():
    mobiles = Engine.Mobiles.GetMobiles()
    for x in range(len(mobiles)):
        mobile = mobiles[x]
        if (mobile != None and mobile.Distance < 2) and Innocent(mobile) and not mobile.Serial in pet_list:
            Rename(mobile.Serial, rename_name)
            Pause(1000 + Ping())
            WaitForContext(mobile.Serial, "Release", 5000)
            WaitForGump(0x909cc741, 5000)
            ReplyGump(0x909cc741, 2)
            #Release_ignorelist.append(mobile.Serial)
            Pause(1000 + Ping())
            SysMessage(">>> Backup Release",44)

while not Dead("self"):
    Mobs = find_mobs()
    if Mobs:
        for m in Mobs:
            if m.ID in no_tame_list or m.Serial in ignore_list or m.Serial in pet_list:
                continue
            if Distance(m.Serial) > 2:
                goto( serial = m.Serial )
            ClearJournal()
            TameFunc(m.Serial)
            if InJournal("That creature cannot be tamed."):
                if m.Serial not in ignore_list:
                    SysMessage(">>> Adding Serial to List...",44)
                    ignore_list.append(m.Serial)
                ClearJournal()
                continue
            if InJournal("That is too far away."):
                ClearJournal()
                continue
            if InJournal("You have no chance of taming this creature."):
                ClearJournal()
                if m.ID not in no_tame_list:
                    SysMessage(">>> Adding ID to List",44)
                    no_tame_list.append(m.ID)
                continue
            if InJournal("That animal looks tame already."):
                if Followers() > Follows:
                    backup_release()
                ClearJournal()
                continue
            if InJournal("*You start to tame the creature.*"):
                SysMessage("Starting Tame...")
                SetTimer("safety_timer", 0)
                while True:
                    Pause(100)
                    if Timer("safety_timer") > 20000:
                        break
                    if InJournal("fail to tame"):
                        Pause(100)
                        ClearJournal()
                        SetTimer("safety_timer", 0)
                        TameFunc(m.Serial)
                    if InJournal("seems to accept") or InJournal("That wasn't even challenging."):
                        break
                    if Distance(m.Serial) > 2:
                        goto( serial = m.Serial )
            RemoveTimer("safety_timer")
            safety_count = 0
            while Followers() > Follows:
                safety_count += 1
                if safety_count > 5:
                    backup_release()
                SysMessage(">>> Releasing",44)
                if m.Serial not in ignore_list:
                    SysMessage(">>> Adding Serial to List",44)
                    ignore_list.append(m.Serial)
                #if m.Name != rename_name:
                while Name(m.Serial) != rename_name:
                    SysMessage(">>> Renaming",44)
                    Rename(m.Serial, rename_name)
                    Pause(1000 + Ping())
                if WaitForContext(m.Serial, "Release", 1000):
                    #WaitForContext(m.Serial, 8, 1000)
                    WaitForGump(0x909cc741, 1000)
                    ReplyGump(0x909cc741, 2)
                    Pause(1000 + Ping())
                Pause(100)
            break
    else:
        SysMessage("No Mobs Found, Stopping.",33)
        Stop()
#############
