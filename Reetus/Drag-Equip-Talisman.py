# Credit: Reetus
# Description: Drags and equips talisman on the paperdoll
from Assistant import Engine
from ClassicAssist.UO.Network.Packets import DragItem, EquipRequest
from ClassicAssist.UO.Data import Layer

if FindLayer('Talisman'):
    Engine.SendPacketToServer(DragItem(GetAlias('found'), 1))
    Pause(50)
    Engine.SendPacketToServer(EquipRequest(GetAlias('found'), Layer.Talisman, Engine.Player.Serial))