# Send Honor Virtue Packet
from ClassicAssist.UO.Data import PacketWriter
from Assistant import Engine
from System import Byte

def honor():
    length = 6
    writer = PacketWriter(length)
    writer.Write(Byte( 0x12 ))
    writer.Write(Byte( 0x00 ))
    writer.Write(Byte( 0x06 ))
    writer.Write(Byte( 0xF4 ))
    writer.Write(Byte( 0x31 )) #Honor
    writer.Write(Byte( 0x00 ))
    Engine.SendPacketToServer(writer)

honor()