# Name: Idoc Scanner
# Description: Checks House Signs for House Condition
# Usage: Set Options, Hit Play, Run Around
# Author: github.com/UltimaScripts/PublicScriptLibrary
# Version: 1.1.0
from Assistant import Engine

#===== OPTIONS START =====
# __Idoc Alert Type__
System_Msg_Alert = True
Head_Msg_Alert = False
Sign_Head_Msg_Alert = False
Play_Sound = False
Sound_File = "Bike Horn.wav"
#
# __Condition For Alert__
Like_New_Alert = False
Like_New_Substring = "like new"
Slightly_Worn_Alert = False
Slightly_Worn_Substring = "slightly worn"
Somewhat_Worn_Alert = False
Somewhat_Worn_Substring = "somewhat worn"
Fairly_Worn_Alert = True
Fairly_Worn_Substring = "fairly worn"
Greatly_Worn_Alert = True
Greatly_Worn_Substring = "greatly worn"
In_Danger_of_Collapsing_Alert = True
In_Danger_of_Collapsing_Substring = "in danger of collapsing"
#
# __Arrow options__
Use_Arrow = False
Remove_Arrow_On_Start = True
Remove_Arrow_Distance = 10
#
# __Map Markers__
# map markers can be found in
# Data\Client\ClassicAssist.csv
Add_Map_Marker = False
#
# __Loop options__
Loop_Delay = 2000
Use_Pulse_Msg = True
Pulse_Msg = "pulse"
#===== OPTIONS END =====
# Don't Edit Below This, Unless You Know What You're Doing.

if Remove_Arrow_On_Start == True:
    DisplayQuestPointer(0, 0, False)

house_signs_list = [0x0B95, 0x0B96, 0x0BA3, 0x0BA4, 0x0BA5, 0x0BA6, 0x0BA7, 0x0BA8, 
                    0x0BA9, 0x0BAA, 0x0BAB, 0x0BAC, 0x0BAD, 0x0BAE, 0x0BAF, 0x0BB0, 
                    0x0BB1, 0x0BB2, 0x0BB3, 0x0BB4, 0x0BB5, 0x0BB6, 0x0BB7, 0x0BB8, 
                    0x0BB9, 0x0BBA, 0x0BBB, 0x0BBC, 0x0BBD, 0x0BBE, 0x0BBF, 0x0BC0, 
                    0x0BC1, 0x0BC2, 0x0BC3, 0x0BC4, 0x0BC5, 0x0BC6, 0x0BC7, 0x0BC8, 
                    0x0BC9, 0x0BCA, 0x0BCB, 0x0BCC, 0x0BCD, 0x0BCE, 0x0BCF, 0x0BD0, 
                    0x0BD1, 0x0BD2, 0x0BD3, 0x0BD4, 0x0BD5, 0x0BD6, 0x0BD7, 0x0BD8, 
                    0x0BD9, 0x0BDA, 0x0BDB, 0x0BDC, 0x0BDD, 0x0BDE, 0x0BDF, 0x0BE0, 
                    0x0BE1, 0x0BE2, 0x0BE3, 0x0BE4, 0x0BE5, 0x0BE6, 0x0BE7, 0x0BE8, 
                    0x0BE9, 0x0BEA, 0x0BEB, 0x0BEC, 0x0BED, 0x0BEE, 0x0BEF, 0x0BF0, 
                    0x0BF1, 0x0BF2, 0x0BF3, 0x0BF4, 0x0BF5, 0x0BF6, 0x0BF7, 0x0BF8, 
                    0x0BF9, 0x0BFA, 0x0BFB, 0x0BFC, 0x0BFD, 0x0BFE, 0x0BFF, 0x0C00, 
                    0x0C01, 0x0C02, 0x0C03, 0x0C04, 0x0C05, 0x0C06, 0x0C07, 0x0C08, 
                    0x0C09, 0x0C0A, 0x0C0B, 0x0C0C, 0x0C0D, 0x0C0E]

def options(serial, x, y, text):
    if System_Msg_Alert == True:
        string = "Idoc Found: {} @ X:{} Y:{}".format(text, x, y)
        SysMessage(string,32)
    if Head_Msg_Alert == True:
        string = "Idoc Found: {} @ X:{} Y:{}".format(text, x, y)
        HeadMsg(string, GetAlias('self'), 32)
    if Sign_Head_Msg_Alert == True:
        string = "Idoc Found: {} Here!".format(text)
        HeadMsg(string, serial, 32)
    if Play_Sound == True:
        PlaySound(Sound_File)
    if Use_Arrow == True:
        DisplayQuestPointer(x, y, True)
    if Add_Map_Marker == True:
        string = "{} X:{} Y:{}".format(text, x, y)
        #RemoveMapMarker(string)
        AddMapMarker(string, x, y, Map())

sign_ignore_list = []
while not Dead('self'):
    Pause(Loop_Delay)
    if Use_Pulse_Msg == True:
        print(Pulse_Msg)
    items = Engine.Items.SelectEntities(lambda i: i.ID in house_signs_list and not i.Serial in sign_ignore_list)
    if not items == None:
        for item in items:
            sign_ignore_list.append(item.Serial)
            for props in range(len(item.Properties)):
                if Like_New_Alert == True and str(Like_New_Substring).lower() in str(item.Properties[props].Text).lower():
                    options(item.Serial, item.X, item.Y, "Like New")
                if Slightly_Worn_Alert == True and str(Slightly_Worn_Substring).lower() in str(item.Properties[props].Text).lower():
                    options(item.Serial, item.X, item.Y, "Slightly Worn")
                if Somewhat_Worn_Alert == True and str(Somewhat_Worn_Substring).lower() in str(item.Properties[props].Text).lower():
                    options(item.Serial, item.X, item.Y, "Somewhat Worn")
                if Fairly_Worn_Alert == True and str(Fairly_Worn_Substring).lower() in str(item.Properties[props].Text).lower():
                    options(item.Serial, item.X, item.Y, "Fairly Worn")
                if Greatly_Worn_Alert == True and str(Greatly_Worn_Substring).lower() in str(item.Properties[props].Text).lower():
                    options(item.Serial, item.X, item.Y, "Greatly Worn")
                if In_Danger_of_Collapsing_Alert == True and str(In_Danger_of_Collapsing_Substring).lower() in str(item.Properties[props].Text).lower():
                    options(item.Serial, item.X, item.Y, "In Danger of Collapsing")
