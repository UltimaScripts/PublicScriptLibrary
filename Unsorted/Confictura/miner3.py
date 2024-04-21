#v1.2.2
from Assistant import Engine
from ClassicAssist.UO.Data import TileFlags, MapInfo

vein_sizex = 8
vein_sizey = 8

# Minable Tiles, Not complete but alot.
tiles = [220,221,222,223,224,225,226,227,228,229,230,231,236,237,238,239,240,241,242,243,
    244,245,246,247,252,253,254,255,256,257,258,259,260,261,262,263,268,269,270,271,
    272,273,274,275,276,277,278,279,286,287,288,289,290,291,292,293,294,296,296,297,
    321,322,323,324,467,468,469,470,471,472,473,474,476,477,478,479,480,481,482,483,
    484,485,486,487,492,493,494,495,543,544,545,546,547,548,549,550,551,552,553,554,
    555,556,557,558,559,560,561,562,563,564,565,566,567,568,569,570,571,572,573,574,
    575,576,577,578,579,581,582,583,584,585,586,587,588,589,590,591,592,593,594,595,
    596,597,598,599,600,601,610,611,612,613,1010,1741,1742,1743,1744,1745,1746,1747,
    1748,1749,1750,1751,1752,1753,1754,1755,1756,1757,1771,1772,1773,1774,1775,1776,
    1777,1778,1779,1780,1781,1782,1783,1784,1785,1786,1787,1788,1789,1790,1801,1802,
    1803,1804,1805,1806,1807,1808,1809,1811,1812,1813,1814,1815,1816,1817,1818,1819,
    1820,1821,1822,1823,1824,1831,1832,1833,1834,1835,1836,1837,1838,1839,1840,1841,
    1842,1843,1844,1845,1846,1847,1848,1849,1850,1851,1852,1853,1854,1861,1862,1863,
    1864,1865,1866,1867,1868,1869,1870,1871,1872,1873,1874,1875,1876,1877,1878,1879,
    1880,1881,1882,1883,1884,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,
    1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2028,2029,2030,
    2031,2032,2033,2100,2101,2102,2103,2104,2105,1339,1340,1341,1342,1343,1344,1345,
    1346,1347,1348,1349,1350,1351,1352,1353,1354,1355,1356,1357,1358,1359]

def check_weight():
    maxweight = (MaxWeight() - 12)
    if Weight() >= maxweight:
        return False
    else:
        return True

def check_tools():
    #You have worn out your tool!
    #shovel 0xf39
    #pickaxe 0xe86
    tool_types = [0xf39,0xe86]
    for tool in tool_types:
        if FindType(tool,0,'backpack',0):
            #return GetAlias('found')
            return tool
    return 0

def pack_animal(use = True):
    if use == True:
        packy = 0x10a47
        if FindObject(packy):
            if Distance(packy) < 18 and Distance(packy) > 2:
                Msg("all follow me")
                Pause(5000)
        else:
            return False
        ore_list = [0x19b9,0x19b8,0x19b7]
        for ore in ore_list:
            while FindType(ore,0,'backpack'):
                MoveItem('found', packy)
                Pause(1000)
        return True
    else:
        return False
# 0 is at max weight
# 1 is mark grid and continue
# 2 is keep looking
# 3 is no tools
def mining_loop(minex,miney):
    ClearJournal()
    tool = check_tools()
    if tool == 0:
        return False
    while True:
        UseType(tool,0)
        WaitForTarget(5000)
        TargetXYZ(minex, miney, 0)
        Pause(2250)
        if InJournal("There is no metal here to mine."):
            return 1
        if InJournal("You can't mine that.") or InJournal("Target cannot be seen."):
            return 2
        if InJournal("You have worn out your tool!"):
            tool = check_tools()
            if tool == 0:
                return 3
        if check_weight() == False:
            if use_pa == True:
                if pack_animal(use = True) == False:
                    return 0
            else:
                return 0

def CheckTiles():
    grids_list = []
    for x in range(-2,3):
        for y in range(-2,3):
            spotx = (Engine.Player.X + x)
            spoty = (Engine.Player.Y + y)
            if (MapInfo.GetLandTile(int(Engine.Player.Map), spotx, spoty)).ID in tiles:
                ex = (spotx / vein_sizex)
                ey = (spoty / vein_sizey)   
                grid = [ex,ey]
                if grid not in grids_list:
                    mining_result = mining_loop(spotx,spoty)
                    if mining_result == 0:
                        SysMessage("At Max Weight",32)
                        return
                    elif mining_result == 1:
                        SysMessage("Grid Saved",70)
                        grids_list.append([ex,ey])
                    elif mining_result == 2:
                        Pause(10)
                    elif mining_result == 3:
                        SysMessage("No Tools Found",32)
                        return

if check_weight() == True:
    CheckTiles()
SysMessage("~~~~ DONE ~~~~",99)