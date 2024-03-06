# Name: meditation trainer with jewels
# Author: Baler
# Version: 1.0.0
while not Dead("self"):
    EquipItem(0x59953c6c, "Ring")
    Pause(700)
    EquipItem(0x5a02e680, "Neck")
    Pause(700)
    EquipItem(0x59953bb8, "Earrings")
    Pause(700)
    EquipItem(0x59953b56, "Bracelet")
    Pause(700)
    EquipItem(0x59953cba, "OneHanded")
    Pause(1000)
    UseSkill("Meditation")
    SetTimer("med", 0)
    while Mana("self") < MaxMana("self"):
        Pause(200)
    while Timer("med") < 12000:
        Pause(200)
    Msg(".undress jewelry")
    Msg(".undress weapons")
    Pause(700)