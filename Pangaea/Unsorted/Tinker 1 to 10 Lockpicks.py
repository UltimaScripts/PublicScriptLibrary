from System import Byte
from ClassicAssist.UO.Data import PacketWriter
from ClassicAssist.Data.Macros import MacroManager
from Assistant import Engine

def macroname():
    return str(MacroManager.GetInstance().GetCurrentMacro())

def craft_amount_packet(num):
    if not isinstance(num, int) or num < 1 or num > 10:
        SysMessage("Must be integer number from 1 to 10, stopping", 32)
        Stop(macroname())
    if num > 0 and num < 10:
        hexnum = 0x30 + num
        sequence = [0xAC, 0x00, 0x0E, 0x01, 0xB9, 0x6F, 0x12, 0x00, 0x00, 0x01, 0x00, 0x02, hexnum, 0x00]
    elif num == 10:
        sequence = [0xAC, 0x00, 0x0F, 0x01, 0xB9, 0x6F, 0x12, 0x00, 0x00, 0x01, 0x00, 0x03, 0x31, 0x30, 0x00]
    length = len(sequence)
    writer = PacketWriter(length)
    for value in sequence:
        writer.Write(Byte( int(value) ))
    Engine.SendPacketToServer(writer)

def menustuff(var0,var1):
    menus = Engine.Menus.GetMenus()
    if menus[0] == True and menus[1] is not None:
        for m in menus[1]:
            if m is not None:
                if m.Title == var0:
                    for me in m.Entries:
                        if me is not None:
                            if me.Title == var1:
                                return me.Index
    HeadMsg("Can't Find ID, Stopping.", "self", 32)
    Stop(macroname())

def craftin(craft_count):
    if not isinstance(craft_count, int) or craft_count < 1 or craft_count > 10:
        SysMessage("Must be integer number from 1 to 10, stopping", 32)
        Stop(macroname())
    #find tinker tools, not tinker kit
    if FindType(0x1ebc, -1, "backpack"):
        if TargetExists("any"):
            CancelTarget()
            Pause(100)
        UseObject("found")
        WaitForTarget(2000)
        #find any hue ingot
        if FindType(0x1bf2, -1, "backpack"):
            Target("found")
        else:
            HeadMsg("Can't Ingots, Stopping.", "self", 32)
            Stop(macroname())
        WaitForMenu(0x0, 5000)
        lpi = menustuff("Tinkering:","Lockpicks ( 1 )")
        ReplyMenu(0x0, lpi, 0x14fb, 0)
        ClearJournal()
        Pause(500)
        #Packet function call, 1 to 10
        craft_amount_packet(craft_count)
        counting = 0
        while True:
            Pause(100)
            if InJournal("You fail, destroying some material.") or InJournal("You create the item and place it in your pack."):
                ClearJournal()
                counting += 1
                Pause(100)
            if counting >= craft_count:
                break
        Pause(2000)
    else:
        HeadMsg("Can't Find Tinker Tools, Stopping.", "self", 32)
        Stop(macroname())

while True:
    craftin(1)