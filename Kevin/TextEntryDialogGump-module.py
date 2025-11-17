#credit: kevin.eady
from System import Array, UInt32, Nullable, Type, Array, Object
from System.Reflection import BindingFlags
from Assistant import Engine
from ClassicAssist.UO.Network.PacketFilter import PacketFilterInfo, PacketDirection
from ClassicAssist.Data.Macros.Commands.MainCommands import Pause

UIManager_type = Engine.ClassicAssembly.GetType("ClassicUO.Game.Managers.UIManager")
TextEntryDialogGump_type = Engine.ClassicAssembly.GetType("ClassicUO.Game.UI.Gumps.TextEntryDialogGump")
KeyboardFocusControl_prop_info = UIManager_type.GetProperty("KeyboardFocusControl") 
KeyboardFocusControl_get_accessor = KeyboardFocusControl_prop_info.GetMethod
OnButtonClick_method = TextEntryDialogGump_type.GetMethod("OnButtonClick")
GetGump_method = UIManager_type.GetMethod(
        "GetGump",
        BindingFlags.Static | BindingFlags.Public,
        None,
        Array[Type]([Nullable[UInt32]]),  # matches the generic overload
        None
    ).MakeGenericMethod(TextEntryDialogGump_type)

def GetTextEntry():
    return GetGump_method.Invoke(None, Array[Object]([None]))  

def WaitForTextEntry(timeout):
    if GetTextEntry():
        return True
    pfi = PacketFilterInfo(0xAB)
    we = Engine.PacketWaitEntries.Add(pfi, PacketDirection.Incoming, True)
    if we.Lock.WaitOne(timeout):
        Pause(100) # Need to pause, because the gump doesn't exist yet in the client
        return True
    
    Engine.PacketWaitEntries.Remove(we)
    return False

def ReplyTextEntry(value):
    textentry_gump = GetTextEntry()
    if textentry_gump:
        control = KeyboardFocusControl_get_accessor.Invoke(None, None)
        control.Text = str(value)
        OnButtonClick_method.Invoke(textentry_gump, Array[Object]([0]))

        return True
        
    return False
