# Credit: kevin.eady
# Reason: Was used to test gold coins in backpack, -
#         on an older shard, to test if CA saw them correctly.
# Note: Replace "Console.WriteLine" with "print" if you run this without an IDE
from Assistant import Engine
from System import Console

items = Engine.Items.SelectEntities(lambda x: x.RootOwner == Engine.Player.Serial and x.ID == 0xeed) or []

serials = "\n- ".join(map(lambda item: "{} owner {}".format(item.Serial, item.Owner or  "[no owner]"), items))
Console.WriteLine("{} gold coin items:\n- {}\n".format(len(items), serials))


Console.WriteLine("gold coins in backpack.Container:")
items = Engine.Items.GetItem(GetAlias('backpack')).Container
for item in items:
    if item.ID == 0xeed:
        Console.WriteLine("- {} owner {}".format(item.Serial, item.Owner or "[no owner]"))