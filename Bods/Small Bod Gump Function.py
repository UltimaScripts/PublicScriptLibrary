# Small Bod Gump Function
# Description: Returns desired small bod information
# Usage: Open a small bod and run the smallbodinfo function
# Author: github.com/UltimaScripts/PublicScriptLibrary
# Version: 1.0.0
# Notes: Tested with Tailoring, Alchemy, Inscription, Tinkering, 
#        Fletching, Carpentry & Cooking. Small Bods on Servuo
from Assistant import Engine

def smallbodinfo(debug = False):
    smallbod_return_list = []
    material_list = ["dull copper","shadow iron","copper","bronze","gold","agapite","verite","valorite",
                     "spined","horned","barbed"
                     "oak","ash","yew","heartwood","bloodwood","frostwood"]
    inital_gump_list = []
    gumps = Engine.Gumps.GetGumps()
    for gump in gumps:
        inital_gump_list.append(gump)
    for x in inital_gump_list[1]:
        if x.Pages != None:
                for pagecount in range(len(x.Pages)):
                    ele = x.Pages[pagecount].GumpElements
                    for entry in range(len(ele)):
                        textentry = str(ele[entry].Text)
                        if textentry != "" or textentry != None:
                            if "a bulk order" in str(textentry).lower():
                                if debug == True:
                                    print str("Gump ID (not serial): " + str(x.ID))
                                smallbod_return_list.append(int(x.ID))
                            if "amount to make:" in str(textentry).lower():
                                #if it finds "amount to make:"
                                #it advances the entry by 1
                                num1 = entry + 1
                                #the amount text on servuo was +1 entry
                                #if it's not on your shard, open the debug window
                                #(top right corner bug icon), gump tab
                                #find "amount to make:" in the bod gump
                                #for example if the text number is + 3 spots
                                #you would use num1 = entry + 3
                                if debug == True:
                                    print str(ele[num1].Text)
                                smallbod_return_list.append(int(ele[num1].Text))
                            if "item requested:" in str(textentry).lower():
                                #same applies for "item requested:"
                                #as explained for "amount to make:"
                                num2 = entry + 2
                                if debug == True:
                                    print str(ele[num2].Text)
                                smallbod_return_list.append(str(ele[num2].Text))
                            if "must be exceptional" in str(textentry).lower():
                                if debug == True:
                                    print("exceptional")
                                smallbod_return_list.append(str("exceptional"))
                            for material in material_list:
                                if material in str(textentry).lower():
                                    if debug == True:
                                        print(material)
                                    smallbod_return_list.append(str(material))
                                    break
    return smallbod_return_list

# Set debug to True, to print what it's finding.
# Open a bod gump and hit play.
smallbodresult = smallbodinfo(debug = False)
if smallbodresult != None:
    print(smallbodresult)