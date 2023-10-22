from Assistant import Engine

gumps = Engine.Gumps.GetGumps()

for g in gumps[1]:
    for t in g.GumpElements:
        if t.Text != None:
            print t.Text