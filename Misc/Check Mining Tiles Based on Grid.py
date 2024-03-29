# Name: Check Mining Tiles Based on Grid
# Description: Checks 2x2 around player for minable tiles and grids
# Usage: Stand near minable tiles and hit play
# Author: github.com/UltimaScripts/PublicScriptLibrary
# Version: 1.0.1
# Note: All tiles may not be reachable or seen by the player.
from ClassicAssist.UO.Data import TileFlags, MapInfo
from Assistant import Engine

# Set this to the ore vein size your shard uses
# Most shards use 8 tiles by 8 tiles as default
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

grids_list = []
spots_list = []
def CheckTiles():
    for x in range(-2,3):
        for y in range(-2,3):
            spotx = (Engine.Player.X + x)
            spoty = (Engine.Player.Y + y)
            if (MapInfo.GetLandTile(int(Engine.Player.Map), spotx, spoty)).ID in tiles:
                ex = (spotx / vein_sizex)
                ey = (spoty / vein_sizey)
                spot = [spotx,spoty]
                grid = [ex,ey]
                if grid not in grids_list:
                    grids_list.append([ex,ey])
                    print("In {} by {} Grid ({}, {})".format(vein_sizex,vein_sizey,ex,ey))
                if spot not in spots_list:
                    spots_list.append([spotx,spoty])
                    print("Mining Tile Found at x {} y {}".format(spotx,spoty))
    print("Standing at X:{} Y:{} you can mine {} grids".format(X(),Y(),len(grids_list)))

CheckTiles()
