#	Name: listen for the pointer packet coming in
#	Description: x, y coordinates of the tracking arrow
#	Credit: Reetus
from Assistant import Engine
from ClassicAssist.UO.Network.PacketFilter import *
from ClassicAssist.UO.Data import PacketReader
           
pwe = Engine.PacketWaitEntries.Add(PacketFilterInfo(0xBA), PacketDirection.Incoming, True)

res = pwe.Lock.WaitOne()

if res:
    pr = PacketReader(pwe.Packet, pwe.Packet.Length, True)
    active = pr.ReadByte()
    x = pr.ReadUInt16()
    y = pr.ReadUInt16()
    print "X: {}, Y: {}".format(x, y)