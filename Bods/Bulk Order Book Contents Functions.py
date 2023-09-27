# Name: Bulk Order Book Contents Functions
# Description: Returns an array of Bod Book Contents Small and Large
# Usage: Open a Bulk Order Book and hit play
# Author: github.com/UltimaScripts/PublicScriptLibrary
# Version: 1.0.0
# Notes: Tested on Servuo
from Assistant import Engine
import re

def findbookgump():
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
                        if "bulk order book" in str(textentry).lower():
                            return(x.ID)
    return(0)

def bodbookinfo(debug = False):
    small_bods_list = []
    large_bods_list = []
    keep_going = True
    while keep_going == True:
        next_page = False
        bookgump = Engine.Gumps.GetGump(findbookgump())
        if bookgump[0] is False:
            SysMessage("Can't Find Bod Book Gump, Stopping.(1)",33)
            Stop()
        ele = bookgump[1].GumpElements
        for entry in range(len(ele)):
            textentry = str(ele[entry].Text)
            #print(textentry)
            if "next page" in str(textentry).lower():
                next_page = True
            if "small" == str(textentry).lower():
                #if it finds "small"
                #it advances the entry by 1
                item = entry + 1
                #the item text on servuo was +1 entry
                #if it's not on your shard, open the debug window
                #(top right corner bug icon), gump tab
                #find "Text: Small" in the bod gump
                #for example if the item is + 3 spots
                #you would use item = entry + 3
                quality = entry + 2
                material = entry + 3
                amount = entry + 4
                amounts = re.findall(r'\d+', str(ele[amount].Text))
                amount1 = int(amounts[0])
                amount2 = int(amounts[1])
                if debug == True:
                    print(str(ele[item].Text))
                    print(str(ele[quality].Text))
                    print(str(ele[material].Text))
                    print(str(ele[amount].Text))
                    print(str(amount1))
                    print(str(amount2))
                small_bods_list.append([ele[item].Text,ele[quality].Text,ele[material].Text,amount1,amount2])
            if "large" == str(textentry).lower():
                l_list = []
                while True:
                    item = entry + 1
                    if item >= len(ele) or ele[item].Text == "" or ele[item].Text == None:
                        large_bods_list.append(l_list)
                        break
                    quality = entry + 2
                    material = entry + 3
                    amount = entry + 4
                    entry = entry + 4
                    amounts = re.findall(r'\d+', str(ele[amount].Text))
                    amount1 = int(amounts[0])
                    amount2 = int(amounts[1])
                    if debug == True:
                        print(str(ele[item].Text))
                        print(str(ele[quality].Text))
                        print(str(ele[material].Text))
                        print(str(ele[amount].Text))
                        print(str(amount1))
                        print(str(amount2))
                    l_list.extend([ele[item].Text,ele[quality].Text,ele[material].Text,amount1,amount2])
        if next_page == True:
            next_page = False
            keep_going = True
            if GumpExists(bookgump[1].ID):
                ReplyGump(bookgump[1].ID, 3)
                WaitForGump(bookgump[1].ID, 5000)
            else:
                SysMessage("Can't Find Bod Book Gump, Stopping.(2)",33)
                Stop()
        else:
            keep_going = False
    return small_bods_list, large_bods_list

#bodbookinfo(False) = No 'debug' Print output
#bodbookinfo(True) = Yes 'debug' Print output
small_list, large_list = bodbookinfo(False)

#this is just for example to show what it returned.
#set to False or delete
if True:
    for x in small_list:
        print x
    for y in large_list:
        print y 