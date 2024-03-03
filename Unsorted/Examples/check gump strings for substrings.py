# Name: check gump strings for substrings
# Examples By: github.com/UltimaScripts/PublicScriptLibrary
# Version: 1.0.0
from Assistant import Engine

# Required predefined variables
#
# gump_id
# GumpID can be in decimal or hex
# GumpID can be found using CA debug window -
#  top right on CA window Bug Icon, Gumps tab
# Example 4 doesn't require gump_id
gump_id = 0x0
#
# sub_string 
# substring is case sensitive
# if you don't know the case, -
# you can use python .lower() or .upper()
# Example 3 shows how to do this
sub_string = 'text'

# Example 1 using python length and a for loop
gump = Engine.Gumps.GetGump(gump_id)
if gump[0] == True and gump[1] is not None:
    for foo in range(len(gump[1].Strings)):
        if sub_string in gump[1].Strings[foo]:
            SysMessage("Example 1",24)
            print(gump[1].Strings[foo])
else:
    SysMessage('e.g.1 GumpID: ' + str(gump_id) + ' was not found.',32)

# Example 2 using python list comprehension
gump = Engine.Gumps.GetGump(gump_id)
if gump[0] == True and gump[1] is not None:
    if any(sub_string in strvar for strvar in gump[1].Strings):
        SysMessage("Example 2",44)
        print(hex(int(gump[1].ID)))
else:
    SysMessage('e.g.2 GumpID: ' + str(gump_id) + ' was not found.',32)

# Example 3 remove case using python .lower()
gump = Engine.Gumps.GetGump(gump_id)
if gump[0] == True and gump[1] is not None:
    for foo in range(len(gump[1].Strings)):
        if sub_string.lower() in gump[1].Strings[foo].lower():
            SysMessage("Example 3",64)
            print(gump[1].Strings[foo])
else:
    SysMessage('e.g.3 GumpID: ' + str(gump_id) + ' was not found.',32)

# Example 4 check all gumps Strings CA can see
gumps = Engine.Gumps.GetGumps()
if gumps[0] == True and gumps[1] is not None:
    for gump in gumps[1]:
        if gump is not None:
            for foo in range(len(gump.Strings)):
                if sub_string in gump.Strings[foo]:
                    SysMessage("Example 4",84)
                    print('substring found at index: {}'.format(foo))
                    print(gump.Strings[foo])
else:
    SysMessage('e.g.4 No Server Sent Gumps Found.',32)