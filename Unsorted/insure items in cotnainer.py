# Make sure anything you put into the_cont (the container) -
# Can be insured, otherwise this will try to insure it.
from Assistant import Engine
SetQuietMode(True)
Loop_Delay = 500
the_cont = 0x1234
Loop = True
ignore_list = []
while Loop == True:
    container_items = Engine.Items.GetItem(the_cont).Container
    for item in container_items:
        if item.Serial not in ignore_list:
            WaitForProperties(item, 5000)
        if item.Serial not in ignore_list and not Property(item, "<b>Insured</b>"):
            WaitForContext("Self", "Toggle Item Insurance", 5000)
            WaitForTarget(5000)
            Target(item)
            #Pause(1000)
            #CancelTarget()
            ignore_list.append(item.Serial)
        elif item.Serial not in ignore_list and Property(item, "<b>Insured</b>"):
            ignore_list.append(item.Serial)
    Pause(Loop_Delay)