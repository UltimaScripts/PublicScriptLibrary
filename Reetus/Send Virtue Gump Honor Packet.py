#Send Virtue Gump Honor Packet
#Author: Reetus
#note: Heres doing it the same way as clicking the button
from ClassicAssist.UO.Data import PacketWriter
from Assistant import Engine
from System import Byte

def honor():
    writer = PacketWriter(0x0F)
    writer.Write(Byte(0xB1))
    writer.Write(Byte(0x00))
    writer.Write(Byte(0x0F))
    writer.Write(Byte(Engine.Player.Serial >> 24))
    writer.Write(Byte(Engine.Player.Serial >> 16))
    writer.Write(Byte(Engine.Player.Serial >> 8))
    writer.Write(Byte(Engine.Player.Serial))
    writer.Write(Byte(0x00))
    writer.Write(Byte(0x00))
    writer.Write(Byte(0x01))
    writer.Write(Byte(0xCD))
    writer.Write(Byte(0x00))
    writer.Write(Byte(0x00))
    writer.Write(Byte(0x00))
    writer.Write(Byte(0x6B))
    Engine.SendPacketToServer(writer)
    
honor()