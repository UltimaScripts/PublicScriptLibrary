#credit: kevin.eady
import sys
import clr
import System
clr.AddReference('System.Core')
from System import Linq, AppDomain
clr.ImportExtensions(Linq)
from System.Reflection import BindingFlags

from Assistant import Engine

def ClosePaperDollGump(serial):
    assembly = AppDomain.CurrentDomain.GetAssemblies() \
        .FirstOrDefault( lambda a: a.FullName.StartsWith( "ClassicUO," ) );
    
    ui_manager_type = assembly.GetType("ClassicUO.Game.Managers.UIManager")
    paper_doll_gump_type = assembly.GetType("ClassicUO.Game.UI.Gumps.PaperDollGump")
    
    get_gumps_prop_info = ui_manager_type.GetProperty("Gumps") 
    get_gumps_get_accessor = get_gumps_prop_info.GetMethod
  
    local_serial_prop_info = paper_doll_gump_type.GetProperty("LocalSerial")
    local_serial_get_accessor = local_serial_prop_info.GetMethod

    gumps = get_gumps_get_accessor.Invoke(None, None)
    
    for gump in gumps:
        local_serial = local_serial_get_accessor.Invoke(gump, None)
        if isinstance(gump, paper_doll_gump_type) and local_serial == serial:
            dispose_method_info = paper_doll_gump_type.GetMethod("Dispose")
            dispose_method_info.Invoke(gump, None)

UseObject(Engine.Player)
Pause(1000)
ClosePaperDollGump(Engine.Player.Serial)