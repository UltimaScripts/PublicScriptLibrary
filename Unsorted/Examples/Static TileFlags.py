from ClassicAssist.UO.Data import TileData, TileFlags
# 0xcdd == big oak tree
static_graphicid = 0xcdd
#Print out the Flags the Static Has
print TileData.GetStaticTile(static_graphicid).Flags
#Print out True/False if it has flag Container
print TileData.GetStaticTile(static_graphicid).Flags.HasFlag( TileFlags.Container )
#Print out True/False if it has flag Impassable
print TileData.GetStaticTile(static_graphicid).Flags.HasFlag( TileFlags.Impassable )