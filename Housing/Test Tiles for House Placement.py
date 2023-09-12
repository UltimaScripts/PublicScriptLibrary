# Name: Test Tiles for House Placement
# Description: Displays valid tiles for house placement.
# Usage: Stand where you want to place a house and hit play.
# Author: github.com/UltimaScripts/PublicScriptLibrary
# Version: 1.0.0
# Credits: Reetus made the Defs Impassable & SAWorldItem
# Notes:
# WARNING, This Script will Increase Client Memory Usage once ran.
# I recommened restarting the client after you're done using it.
from ClassicAssist.UO.Data import PacketWriter, Statics, TileFlags, MapInfo
from ClassicAssist.UO.Commands import RemoveObject
from Assistant import Engine
from System import *

#Keep in mind Housing Rules
#the east side needs 1 more valid tile
#the south side needs 5 valid tiles

# ===== Options Start =====
# ___remove_display___
## Set remove_display to True to remove the display.
## You can also just run off screen and they should be gone.
## Case / Capitalization matters. (True or False)
remove_display = False
#
# ___square_size___
## Never set square_size higher than 24.
## If you run it with a higher number and,
## want to run it again with a lower number,
## you will need to remove_display first.
## Can run it repeatedly with the same value.
square_size = 10
#
# ___height_tolerance___
## height_tolerance is usually 0.
height_tolerance = 0
# ===== Options End =====

# DO NOT EDIT BELOW THIS
# unless you know what you're doing.

def Impassable(x, y, map = int(Engine.Player.Map)):
    staticTiles = Statics.GetStatics( map, x, y )
    
    if staticTiles == None or staticTiles.Length == 0:
        return MapInfo.GetLandTile(map, x, y).Flags.HasFlag(TileFlags.Impassable)
    
    for x in staticTiles:
        if x.Flags.HasFlag(TileFlags.Impassable):
            return True

    return False

def SAWorldItem(serial, itemId, amount, x, y, z, hue):
      length = 26 if Engine.ClientVersion >= Version( 7, 0, 9, 0 ) else 24
      writer = PacketWriter(length)
      writer.Write(Byte( 0xF3 ))
      writer.Write(Int16( 1 ))
      writer.Write(Byte( 0 ))
      writer.Write(Int32(serial))
      writer.Write(Int16( itemId ))
      writer.Write(Byte( 0 ))
      writer.Write(Int16( amount ))
      writer.Write(Int16( amount ))
      writer.Write(Int16( x ))
      writer.Write(Int16( y ))
      writer.Write(SByte( z ))
      writer.Write(Byte( 0 ))
      writer.Write(Int16( hue ))
      writer.Write(Byte( 0x20 ))
      writer.Fill()
      return writer

# Removes the objects from the gameworld
if remove_display == True:
    remove_size = (((square_size + 1) * 2) * ((square_size + 1) * 2))
    for x in range(remove_size):
        value = (1073741824 + x)
        RemoveObject(value)
    Stop()

# Roads list is technically incomplete.
# May lead to false results, outside of roads.
Roads = [0x0071, 0x0078, 0x00E8, 0x00EB, 
         0x07AE, 0x07B1, 0x3FF4, 0x3FF4, 
         0x3FF8, 0x3FFB, 0x0442, 0x0479, 
         0x0501, 0x0510, 0x0009, 0x0015, 
         0x0150, 0x015C, 
         0x170, 0x72, 0x73, 0x74, 0x75, 
         0x76, 0x77, 0x79, 0x7A, 0x7C,
         0x7D, 0x7E, 0x82, 0x83, 0x85,
         0x86, 0x87, 0x88, 0x89, 0x8A,
         0x8B, 0x8C, 0x16f]

# Don't change count, it's hex value is 0x40000000
count = 1073741824
for xx in range(-abs(square_size),(square_size + 1)):
    for yy in range(-abs(square_size),(square_size + 1)):
        x = (X() + xx)
        y = (Y() + yy)
        z0 = Z()
        map = int(Engine.Player.Map)
        z = MapInfo.GetLandTile(map, x, y).Z
        idd = MapInfo.GetLandTile(map, x, y).ID
        count += 1
        # Impassable Check
        impass1 = Impassable(x, y)
        for xxx in range(-1,2):
            for yyy in range(-1,2):
                x1 = (x + xxx)
                y1 = (y + yyy)
                z1 = MapInfo.GetLandTile(map, x1, y1).Z
                impass2 = Impassable(x1, y1)
                if impass2 == True:
                    break
            if impass2 == True:
                    break
        # Height Check - Basic
        if not z == z0 and not impass1 == True and not impass2 == True:
            if not (z0 - height_tolerance) <= z <= (z0 + height_tolerance):
                impass2 = True
        
        # Items sent to world
        if impass1 == True or idd in Roads:
            Engine.SendPacketToClient(SAWorldItem(count, 0x1CDA, 1, x, y, z, 0))
        elif impass2 == True:
            Engine.SendPacketToClient(SAWorldItem(count, 0x1CDA, 1, x, y, z, 1259)) 
        else:
            Engine.SendPacketToClient(SAWorldItem(count, 0x1CDA, 1, x, y, z, 1271))
