from Assistant import Engine
#The Text File is Saved To Your Base ClassicUO Directory
#open the virtue gump to stop this script
#open the quests gump to make a line seperator

The_File_Name = r"C:\UO\rail.txt"
distance_between_spots = 6
Save_Closing_Spot = True

with open(The_File_Name, "a") as my_text_file:
    SysMessage("Active")
    px = Engine.Player.X
    py = Engine.Player.Y
    pz = Engine.Player.Z
    result = ("goto(" + str(px) + ", " + str(py) + ", " + str(pz) + ")")
    my_text_file.write(result + "\n")
    SysMessage("Spot")
    while not Dead("self"):
        Pause(50)
        if Distance(px, py) >= distance_between_spots:
            px = Engine.Player.X
            py = Engine.Player.Y
            pz = Engine.Player.Z
            result = ("goto(" + str(px) + ", " + str(py) + ", " + str(pz) + ")")
            my_text_file.write(result + "\n")
            SysMessage("Spot")
        if GumpExists(0x861db6b1):
            if Save_Closing_Spot == True:
                px = Engine.Player.X
                py = Engine.Player.Y
                pz = Engine.Player.Z
                result = ("goto(" + str(px) + ", " + str(py) + ", " + str(pz) + ")")
                my_text_file.write(result + "\n")
                SysMessage("Spot")
            SysMessage("Closed")
            ReplyGump(0x861db6b1, 0)
            Pause(100)
            my_text_file.close()
            Pause(100)
            Stop()
        if GumpExists(0x4c4c6db0):
            my_text_file.write("#-----\n")
            SysMessage("Line Seperator Added")
            ReplyGump(0x4c4c6db0, 0)
