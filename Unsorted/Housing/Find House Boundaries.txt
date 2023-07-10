# Name: Find House Boundaries
# Description: Finds a House Multi and Prints the min x, min y, max x and max y of the house.
# Usage: Stand near a house and hit play, Center of the house needs to be on screen.
# Author: github.com/UltimaScripts/PublicScriptLibrary
# Version: 1.1.0
# Credits: Reetus, Darah Bomba & TrueUO
import clr
import System
clr.AddReference('System.Core')
clr.ImportExtensions(System.Linq)
from Assistant import Engine

#Options
#Set True if you want stairs to be added to,
# the final Max Y coordinates
Add_Stairs = True

#note 0x76, 0x77, 0x78 & 0x79 don't factor the L shape of the multi
#note 0x7A & 0x7B may or may not factor in the west & east Wings
#[multigraphic,minx,miny,maxx,maxy,'HouseNameString']
HouseList = [[0x64,-3,-3,4,4,'Small Stone and Plaster House'],[0x65,-3,-3,4,4,'Small Stone and Plaster House'],
    [0x66,-3,-3,4,4,'Small Fieldstone House'],[0x67,-3,-3,4,4,'Small Fieldstone House'],
    [0x68,-3,-3,4,4,'Small Brick House'],[0x69,-3,-3,4,4,'Small Brick House'],
    [0x6A,-3,-3,4,4,'Small Wood House'],[0x6B,-3,-3,4,4,'Small Wood House'],
    [0x6C,-3,-3,4,4,'Small Wood and Plaster House'],[0x6D,-3,-3,4,4,'Small Wood and Plaster House'],
    [0x6E,-3,-3,4,4,'Small Thatched Roof House'],[0x6F,-3,-3,4,4,'Small Thatched Roof House'],
    [0x70,-3,-3,4,4,'Blue Tent'],[0x71,-3,-3,4,4,'Blue Tent'],
    [0x72,-3,-3,4,4,'Green Tent'],[0x73,-3,-3,4,4,'Green Tent'],
    [0x74,-7,-7,7,7,'Large Brick House'],[0x75,-7,-7,7,7,'Large Brick House'],
    [0x76,-7,-7,7,7,'Two Story Wood and Plaster House'],[0x77,-7,-7,7,7,'Two Story Wood and Plaster House'],
    [0x78,-7,-7,7,7,'Two Story Stone and Plaster House'],[0x79,-7,-7,7,7,'Two Story Stone and Plaster House'],
    [0x7A,-11,-7,12,8,'Large Tower'],[0x7B,-11,-7,12,8,'Large Tower'],
    [0x7C,-11,-11,12,12,'Stone Keep'],[0x7D,-11,-11,12,12,'Stone Keep'],
    [0x7E,-15,-15,15,16,'Castle'],[0x7F,-15,-15,15,16,'Castle'],
    [0x87,-7,-7,8,7,'Large Patio House'],[0x8C,-7,-7,8,7,'Large Patio House'],
    [0x8D,-7,-7,8,7,'Large Patio House'],[0x96,-7,-7,7,7,'Large Marble Patio House'],
    [0x98,-3,-3,4,4,'Small Tower'],[0x9A,-3,-6,4,7,'Log Cabin'],
    [0x9C,-5,-4,6,5,'Sandstone Patio House'],[0x9E,-5,-5,6,6,'Two-Story Villa'],
    [0xA0,-3,-3,4,4,'Small Stone Workshop'],[0xA2,-3,-3,3,4,'Small Marble Workshop'],
    [0x13EC,-3,-3,3,3,'7x7 Custom House'],[0x13ED,-3,-3,3,4,'7x8 Custom House'],
    [0x13EE,-3,-4,3,4,'7x9 Custom House'],[0x13EF,-3,-4,3,5,'7x10 Custom House'],
    [0x13F0,-3,-5,3,5,'7x11 Custom House'],[0x13F1,-3,-5,3,6,'7x12 Custom House'],
    [0x13F8,-3,-3,4,3,'8x7 Custom House'],[0x13F9,-3,-3,4,4,'8x8 Custom House'],
    [0x13FA,-3,-4,4,4,'8x9 Custom House'],[0x13FB,-3,-4,4,5,'8x10 Custom House'],
    [0x13FC,-3,-5,4,5,'8x11 Custom House'],[0x13FD,-3,-5,4,6,'8x12 Custom House'],
    [0x13FE,-3,-6,4,6,'8x13 Custom House'],[0x1404,-4,-3,4,3,'9x7 Custom House'],
    [0x1405,-4,-3,4,4,'9x8 Custom House'],[0x1406,-4,-4,4,4,'9x9 Custom House'],
    [0x1407,-4,-4,4,5,'9x10 Custom House'],[0x1408,-4,-5,4,5,'9x11 Custom House'],
    [0x1409,-4,-5,4,6,'9x12 Custom House'],[0x140A,-4,-6,4,6,'9x13 Custom House'],
    [0x140B,-4,-6,4,7,'9x14 Custom House'],[0x1410,-4,-3,5,3,'10x7 Custom House'],
    [0x1411,-4,-3,5,4,'10x8 Custom House'],[0x1412,-4,-4,5,4,'10x9 Custom House'],
    [0x1413,-4,-4,5,5,'10x10 Custom House'],[0x1414,-4,-5,5,5,'10x11 Custom House'],
    [0x1415,-4,-5,5,6,'10x12 Custom House'],[0x1416,-4,-6,5,6,'10x13 Custom House'],
    [0x1417,-4,-6,5,7,'10x14 Custom House'],[0x1418,-4,-7,5,7,'10x15 Custom House'],
    [0x141C,-5,-3,5,3,'11x7 Custom House'],[0x141D,-5,-3,5,4,'11x8 Custom House'],
    [0x141E,-5,-4,5,4,'11x9 Custom House'],[0x141F,-5,-4,5,5,'11x10 Custom House'],
    [0x1420,-5,-5,5,5,'11x11 Custom House'],[0x1421,-5,-5,5,6,'11x12 Custom House'],
    [0x1422,-5,-6,5,6,'11x13 Custom House'],[0x1423,-5,-6,5,7,'11x14 Custom House'],
    [0x1424,-5,-7,5,7,'11x15 Custom House'],[0x1425,-5,-7,5,8,'11x16 Custom House'],
    [0x1428,-5,-3,6,3,'12x7 Custom House'],[0x1429,-5,-3,6,4,'12x8 Custom House'],
    [0x142A,-5,-4,6,4,'12x9 Custom House'],[0x142B,-5,-4,6,5,'12x10 Custom House'],
    [0x142C,-5,-5,6,5,'12x11 Custom House'],[0x142D,-5,-5,6,6,'12x12 Custom House'],
    [0x142E,-5,-6,6,6,'12x13 Custom House'],[0x142F,-5,-6,6,7,'12x14 Custom House'],
    [0x1430,-5,-7,6,7,'12x15 Custom House'],[0x1431,-5,-7,6,8,'12x16 Custom House'],
    [0x1432,-5,-8,6,8,'12x17 Custom House'],[0x1435,-6,-3,6,4,'13x8 Custom House'],
    [0x1436,-6,-4,6,4,'13x9 Custom House'],[0x1437,-6,-4,6,5,'13x10 Custom House'],
    [0x1438,-6,-5,6,5,'13x11 Custom House'],[0x1439,-6,-5,6,6,'13x12 Custom House'],
    [0x143A,-6,-6,6,6,'13x13 Custom House'],[0x143B,-6,-6,6,7,'13x14 Custom House'],
    [0x143C,-6,-7,6,7,'13x15 Custom House'],[0x143D,-6,-7,6,8,'13x16 Custom House'],
    [0x143E,-6,-8,6,8,'13x17 Custom House'],[0x143F,-6,-8,6,9,'13x18 Custom House'],
    [0x1442,-6,-4,7,4,'14x9 Custom House'],[0x1443,-6,-4,7,5,'14x10 Custom House'],
    [0x1444,-6,-5,7,5,'14x11 Custom House'],[0x1445,-6,-5,7,6,'14x12 Custom House'],
    [0x1446,-6,-6,7,6,'14x13 Custom House'],[0x1447,-6,-6,7,7,'14x14 Custom House'],
    [0x1448,-6,-7,7,7,'14x15 Custom House'],[0x1449,-6,-7,7,8,'14x16 Custom House'],
    [0x144A,-6,-8,7,8,'14x17 Custom House'],[0x144B,-6,-8,7,9,'14x18 Custom House'],
    [0x144F,-7,-4,7,5,'15x10 Custom House'],[0x1450,-7,-5,7,5,'15x11 Custom House'],
    [0x1451,-7,-5,7,6,'15x12 Custom House'],[0x1452,-7,-6,7,6,'15x13 Custom House'],
    [0x1453,-7,-6,7,7,'15x14 Custom House'],[0x1454,-7,-7,7,7,'15x15 Custom House'],
    [0x1455,-7,-7,7,8,'15x16 Custom House'],[0x1456,-7,-8,7,8,'15x17 Custom House'],
    [0x1457,-7,-8,7,9,'15x18 Custom House'],[0x145C,-7,-5,8,5,'16x11 Custom House'],
    [0x145D,-7,-5,8,6,'16x12 Custom House'],[0x145E,-7,-6,8,6,'16x13 Custom House'],
    [0x145F,-7,-6,8,7,'16x14 Custom House'],[0x1460,-7,-7,8,7,'16x15 Custom House'],
    [0x1461,-7,-7,8,8,'16x16 Custom House'],[0x1462,-7,-8,8,8,'16x17 Custom House'],
    [0x1463,-7,-8,8,9,'16x18 Custom House'],[0x1469,-8,-5,8,6,'17x12 Custom House'],
    [0x146A,-8,-6,8,6,'17x13 Custom House'],[0x146B,-8,-6,8,7,'17x14 Custom House'],
    [0x146C,-8,-7,8,7,'17x15 Custom House'],[0x146D,-8,-7,8,8,'17x16 Custom House'],
    [0x146E,-8,-8,8,8,'17x17 Custom House'],[0x146F,-8,-8,8,9,'17x18 Custom House'],
    [0x1476,-8,-6,9,6,'18x13 Custom House'],[0x1477,-8,-6,9,7,'18x14 Custom House'],
    [0x1478,-8,-7,9,7,'18x15 Custom House'],[0x1479,-8,-7,9,8,'18x16 Custom House'],
    [0x147A,-8,-8,9,8,'18x17 Custom House'],[0x147B,-8,-8,9,9,'18x18 Custom House'],
    [0x147C,-11,-11,12,12,'23x23 Custom House'],[0x147D,-15,-15,15,15,'32x32 Custom House'],
    [0x147E,-11,-11,12,12,'Trinsic Keep'],[0x147F,-15,-15,15,15,'Gothic Rose Castle'],
    [0x1480,-15,-15,15,15,'Elsa Castle'],[0x1481,-15,-15,15,15,'Spires'],
    [0x1482,-15,-15,15,15,'Castle Of Oceania'],[0x1483,-15,-15,15,15,'Feudal Castle'],
    [0x1484,-11,-11,12,12,'Robins Nest'],[0x1485,-11,-11,12,12,'Traditional Keep'],
    [0x1486,-11,-11,12,12,'Villa Crowley'],[0x1487,-11,-11,12,12,'Darkthorn Keep'],
    [0x1488,-11,-11,12,12,'Sandalwood Keep'],[0x1489,-11,-11,12,12,'Casa Moga'],
    [0x148A,-15,-15,15,15,'Robins Roost'],[0x148B,-15,-15,15,15,'Camelot'],
    [0x148C,-15,-15,15,15,'Lacrimae In Caelo'],[0x148D,-15,-15,15,15,'Okinawa Sweet Dream Castle'],
    [0x148E,-15,-15,15,15,'The Sandstone Castle'],[0x148F,-15,-15,15,15,'Grimswind Sisters'],
    [0x1490,-11,-11,12,12,'Fortress Of Lestat'],[0x1491,-11,-11,12,12,'Citadel Of The Far East'],
    [0x1492,-11,-11,12,12,'Keep Incarcerated'],[0x1493,-11,-11,12,12,'Sally Trees Refurbished Keep'],
    [0x1494,-11,-11,12,12,'Desert Rose'],[0x1495,-11,-11,12,12,'The Clovers Keep'],
    [0x1496,-15,-15,15,15,'The Sorceres Castle'],[0x1497,-15,-15,15,15,'The Castle Cascade'],
    [0x1498,-15,-15,15,15,'The House Built On The Ruins'],[0x1499,-15,-15,15,15,'The Sandstone Fortress Of Grand'],
    [0x149A,-15,-15,15,15,'The Dragonstone Castle'],[0x149B,-15,-15,15,15,'The Terrace Gardens'],
    [0x149C,-11,-11,12,12,'The Keep Calm And Carry On Keep'],[0x149D,-11,-11,12,12,'The Ravenloft Keep'],
    [0x149E,-11,-11,12,12,'The Queens Retreat Keep']
    ]

multis = Engine.Items.Where(lambda i: i.ArtDataID == 2)

for x in multis:
    for num in range(len(HouseList)):
        if Graphic(x.Serial) == HouseList[num][0]:
            HeadMsg(str(HouseList[num][5]), x.Serial)
            print(HouseList[num])
            print('The Multi is at X:' + str(X(x.Serial)) + ' Y:' + str(Y(x.Serial)))
            minx = (X(x.Serial) + HouseList[num][1])
            miny = (Y(x.Serial) + HouseList[num][2])
            maxx = (X(x.Serial) + HouseList[num][3])
            if Add_Stairs == True:
                maxy = ((Y(x.Serial) + HouseList[num][4]) + 1)
            else:
                maxy = (Y(x.Serial) + HouseList[num][4])
            print('The Boundaries of the house are: ' + str(minx) + ',' + str(miny) + ' by ' + str(maxx) + ',' + str(maxy))

#Changelog
#1.1.0
#Added 23x23 & 32x32 Custom Houses
#Added Stairs Boolean Option
