from Assistant import Engine

#animaltamer_serial = 0xcdeb
#WaitForContext(animaltamer_serial, 2, 5000)
#WaitForGump(0x307b71a8, 5000)

def check_gump():
    list1 = ["chicken","sheep","goat","bull","cow","pig",
             "dog","grey wolf","timer wolf","white wolf",
             "dire wolf","hell hound"]
    list2 = ["cat","panther","cougar","hell cat","brown bear",
             "grizzly bear","black bear","polar bear"]
    
    # Check if the Gump Exists
    if GumpExists(0x307b71a8):
        # Get the gump from the engine
        gump = Engine.Gumps.GetGump(0x307b71a8)
        # get the elements of the gump
        gump_elements = gump[1].GumpElements
        # iterate through the number of elements
        for entry in range(len(gump_elements)):
            # check the Text for each element
            # set the variable textentry as entry text
            textentry = str(gump_elements[entry].Text)
            # check for string in the text entry lowercase
            if "amount to tame:" in str(textentry).lower():
                # set entry_move to entry plus 1
                # which is the next element
                # in this case the amount number
                entry_move = entry + 1
                # set entry_jump to entry plus 4
                # which is plus 4 elements
                # in this case it's the animal name
                entry_jump = entry + 4
                # check the text in this next element
                # checking for 15 or 20
                if "15" in str(gump_elements[entry_move].Text).lower():
                    # iterate through list1
                    for foo in list1:
                        # check if any string in list1 is in 
                        # gump element number entry_jump Text
                        if str(foo) in str(gump_elements[entry_jump].Text).lower():
                            return True
                if "20" in str(gump_elements[entry_move].Text).lower():
                    # iterate through list2
                    for foo in list2:
                        # check if any string in list2 is in 
                        # gump element number entry_jump Text
                        if str(foo) in str(gump_elements[entry_jump].Text).lower():
                            return True
                #if "10" in str(gump_elements[entry_move].Text).lower():
                #    if "snow leopard" in str(gump_elements[entry_jump].Text).lower():
                #        return True
    return False

print check_gump()

#For reference here are all the gump elements
#This can be found in the debug window
#Page 0 elements (19):
#
#X: 25, Y: 10, Type: resizepic, Cliloc: 0, Text: 
#X: 33, Y: 20, Type: gumppictiled, Cliloc: 0, Text: 
#X: 33, Y: 20, Type: checkertrans, Cliloc: 0, Text: 
#X: 20, Y: 5, Type: gumppic, Cliloc: 0, Text: 
#X: 430, Y: 5, Type: gumppic, Cliloc: 0, Text: 
#X: 20, Y: 249, Type: gumppic, Cliloc: 0, Text: 
#X: 430, Y: 249, Type: gumppic, Cliloc: 0, Text: 
#X: 190, Y: 25, Type: xmfhtmlgumpcolor, Cliloc: 1045133, Text: A bulk order
#X: 40, Y: 48, Type: xmfhtmlgumpcolor, Cliloc: 1045135, Text: Ah!  Thanks for the goods!  Would you help me out?
#X: 40, Y: 72, Type: text, Cliloc: 0, Text: Amount to tame:
#X: 250, Y: 72, Type: text, Cliloc: 0, Text: 10
#X: 40, Y: 96, Type: xmfhtmlgumpcolor, Cliloc: 1045136, Text: Item requested:
#X: 385, Y: 96, Type: tilepic, Cliloc: 0, Text: 
#X: 40, Y: 120, Type: text, Cliloc: 0, Text: Snow Leopard
#X: 40, Y: 216, Type: xmfhtmlgumpcolor, Cliloc: 1045139, Text: Do you want to accept this order?
#X: 100, Y: 240, Type: button, Cliloc: 0, Text: 
#X: 135, Y: 240, Type: xmfhtmlgumpcolor, Cliloc: 1006044, Text: OK
#X: 275, Y: 240, Type: button, Cliloc: 0, Text: 
#X: 310, Y: 240, Type: xmfhtmlgumpcolor, Cliloc: 1011012, Text: CANCEL

#'''Leaving this here just for example sake'''
#if InGump(0x307b71a8, "Snow Leopard") and InGump(0x307b71a8, "10"):
#    print('true')