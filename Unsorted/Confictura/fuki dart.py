def boards_and_tools():
    stuff = []
    if FindType(0x1bd7,2,0x4008a0e8):
        stuff.append([True,GetAlias("found")])
        #print stuff
    else: 
        stuff.append([False])
    if FindType(0x1f2c,0,'backpack') and stuff[0][0] == True:
        #stuff[0][0] = True
        stuff[0].append(GetAlias("found"))
        #print stuff
    else:
        stuff[0][0] = False
    return stuff

UseObject(0x4008a0e8)
Pause(1000)
loop = True
while loop == True:
    stufflist = boards_and_tools()
    if stufflist[0][0] == False:
        break
    else:
        MoveItem(stufflist[0][1], "backpack",1)
        Pause(1000)
        UseObject(stufflist[0][2])
        WaitForGump(0x38920abd, 5000)
        ReplyGump(0x38920abd, 8)
        WaitForGump(0x38920abd, 5000)
        ReplyGump(0x38920abd, 16)
        WaitForGump(0x38920abd, 5000)
        while FindType(0x2806,0,"backpack"):
            MoveItem("found", 0x40009861)
            Pause(1000)