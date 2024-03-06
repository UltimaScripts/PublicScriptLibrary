# Name: armslore trainer
# Author: Baler
# Version: 1.0.0
# set item_serial to the serial of the item -
#  that you plan to use Arms Lore on.
item_serial = 0x587ce448
while not Dead('self'):
    UseSkill("Arms Lore")
    WaitForTarget(1000)
    Target(item_serial)
    Pause(10100)