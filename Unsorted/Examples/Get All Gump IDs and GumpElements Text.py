from Assistant import Engine

inital_gump_list = []
gumps = Engine.Gumps.GetGumps()
for gump in gumps:
    inital_gump_list.append(gump)

for x in inital_gump_list[1]:
    #prints all the gump IDs CA can see.
    print x.ID
    #Set this to True, it will print all the text in GumpElements
    if False:
        if x.Pages != None:
            for pagecount in range(len(x.Pages)):
                ele = x.Pages[pagecount].GumpElements
                for entry in range(len(ele)):
                    textentry = str(ele[entry].Text)
                    if textentry != "" or textentry != None:
                        print textentry