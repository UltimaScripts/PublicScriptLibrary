#credit: kevin.eady
import sys
import clr

clr.AddReference('FNA')
clr.AddReference('System.Core')

from System import InvalidOperationException
from Microsoft.Xna.Framework import Point
from Assistant import Engine

def MoveContainerGump(serial, x, y):
    ui_manager_type = Engine.ClassicAssembly.GetType(
        "ClassicUO.Game.Managers.UIManager")
    container_gump_type = Engine.ClassicAssembly.GetType(
        "ClassicUO.Game.UI.Gumps.ContainerGump")
    control_type = Engine.ClassicAssembly.GetType(
        "ClassicUO.Game.UI.Controls.Control")

    get_gumps_prop_info = ui_manager_type.GetProperty("Gumps")
    get_gumps_get_accessor = get_gumps_prop_info.GetMethod

    local_serial_prop_info = container_gump_type.GetProperty("LocalSerial")
    local_serial_get_accessor = local_serial_prop_info.GetMethod

    gumps = get_gumps_get_accessor.Invoke(None, None)

    while True:
        try:
            for gump in gumps:
                local_serial = local_serial_get_accessor.Invoke(gump, None)
                if isinstance(gump,
                              container_gump_type) and local_serial == serial:
                    location_property_info = control_type.GetProperty(
                        "Location")
                    location_property_info.SetValue(gump, Point(x, y))
                    return

        # Collection was modified after the enumerator was instantiated
        except System.InvalidOperationException as ex:
            continue


WaitForContents(Engine.Player.Backpack)
Pause(1000)
MoveContainerGump(Engine.Player.Backpack.Serial, 50, 50)
