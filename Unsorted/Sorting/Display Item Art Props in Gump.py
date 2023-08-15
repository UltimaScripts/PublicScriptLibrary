# Name: Display Item Art Props in Gump
# Description: Displays Item Art & Props in a Gump
# Usage: Hit Play and Target a Container,
#        Adjust Width if it's too large width wise.
# Author: github.com/UltimaScripts/PublicScriptLibrary
# Version: 1.0.0
# Notes: There is an example to Hue Text for string match
# To-Do-List: 1. Change Width to Dynamic based on,
#             Longest String In Item Props.
#             2. Make Y Dynamic for new rows,
#             This way there is no Gap.
#             3. Try to tackle pages.
from ClassicAssist.UO.Objects.Gumps import Gump
from Assistant import Engine

class MyGump(Gump):
    def __new__(self, message, textprops, art):
        gump = Gump.__new__(self, 250, 250)
        #width is important for controlling the total width
        width = 1400
        #height doesn't matter as much due to dynamic code later on
        height = 960
        self.options = textprops
        gump.Closable = True
        gump.Movable = True
        gump.AddPage(0)
        y = 40
        xloc2 = 0
        temp_y = 0
        temp_y2 = 0
        art_row_y = 0
        counting = 1
        tile_height = 0
        row = 0
        #Sorts it so items with the most props appear first, sorts the art list the same way.
        sorted_lists = sorted(zip(textprops, art), key=lambda x: len(x[0]), reverse=True)
        sorted_textprops, sorted_art = zip(*sorted_lists)
        for x in range(len(sorted_textprops)):
            tile_height = (len(sorted_textprops[x] * 20) + 40)
            gump.AddBackground(xloc2, art_row_y, 170, tile_height + 5, 9200 )
            gump.AddImageTiled(xloc2 - 2, art_row_y, 168, tile_height, 0xE14);
            gump.AddHtml(xloc2 + 40, art_row_y, 200, 20, '<basefont color=#FF6A00 size=7><b><h2>'+str(counting)+"</h2></b></basefont>",0,0)
            counting += 1
            gump.AddItem(xloc2, art_row_y, sorted_art[x])
            for xx in sorted_textprops[x]:
                gump.AddLabel(xloc2, y, 0, xx)
                #Example how to Hue Text for string partial match
                if "fire resist" in str(xx).lower():
                    gump.AddHtml(xloc2, y, 200, 20, "<basefont color=#B40000>"+str(xx)+"</basefont>",0,0)
                else:
                    gump.AddHtml(xloc2, y, 200, 20, "<basefont color=#FFFFFF>"+str(xx)+"</basefont>",0,0)
                y+=20
                if temp_y < y:
                    temp_y = y
            if xloc2 < (width - 220):
                xloc2 += 170
                if row == 0:
                    y = 40
                elif row == 1:
                    y = temp_y2
            elif xloc2 > (width - 220):
                y = temp_y + 40
                temp_y2 = temp_y + 40
                art_row_y = temp_y + 5
                temp_y = 0
                xloc2 = 0
                row += 1
            
        return gump

SysMessage("Click The Container You Want To Gumpify",66)
PromptAlias("container_to_check")
if GetAlias('container_to_check') == 0 or GetAlias('container_to_check') == -1:
    Stop()

items = Engine.Items.GetItem(GetAlias('container_to_check')).Container
imdumb = []
for x in items:
    imdumb.append(x.Serial)

selectedItems = ItemArrayGump(imdumb, True)

if len(selectedItems) > 16:
    #SysMessage("Too Many Selected\nWithout Modifying this version\nIt was setup for 5 colums and 2 rows\n a total of ten items per page.\nStopping", 32)
    SysMessage("You will need to increase Width\nIf you want more than 8 columns",32)
    Stop()

if selectedItems:
    artlist = []
    proplist = []
    for x in selectedItems:
        artlist.append(Graphic(x))
        thing = Engine.Items.GetItem(x)
        tempproplist = []
        for x in thing.Properties:
            tempproplist.append(x.Text)
        proplist.append(tempproplist)

    gump = MyGump('message', proplist,artlist)
    gump.SendGump()
else:
    SysMessage("You didn't Select Any Items",32)
    