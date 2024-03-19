#v1.0
#shovel 0xf39
#pickaxe
def check_weight():
    maxweight = (MaxWeight() - 12)
    if Weight() >= maxweight:
        return False
    else:
        return True

ClearJournal()
while True:
    UseType(0xe86,0)
    WaitForTarget(5000)
    TargetXYZ(2955, 1099, 0)
    Pause(2250)
    if InJournal("There is no metal here to mine."):
        break
    if check_weight() == False:
        SysMessage("At Max Weight",32)
        break
print True
#You loosen some rocks but fail to find any useable ore.
#You dig up some ore.
#You have worn out your tool!
