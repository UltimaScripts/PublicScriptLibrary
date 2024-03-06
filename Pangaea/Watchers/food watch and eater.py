# Name: food watch and eater
# Author: Baler
# Version: 1.0.5
from ClassicAssist.Data.Macros import MacroManager

# _____Options Start_____
# foods is a list, add more graphic IDs you required, separate by commas
# 0xc77 carrot, 0x172a lime
foods = [0xc77,0x172a]
# set warning_amount to 0 do disable it.
warning_amount = 5
# set food_container to the Serial for the container where food is.
# 'backpack' is an Alias that's auto-setup by CA
# replace the entire GetAlias('backpack'), if you want to change it to a specific serial
food_container = GetAlias('backpack')
# set sound_file to 0 to disable it.
sound_file = "Bike Horn.wav"
# set use_stop to True or False if you want the macro to stop if no food found.
use_stop = False
# set loop_delay milliseconds pause time for the main while not dead loop.
loop_delay = 2000
# set use_text_alert to True or False if you want to recieve a msg about lack of food.
use_text_alert = True
# set text_alert_type to 1 for HeadMsg or 2 for SysMessage
text_alert_type = 1
# set text_alert_hue to change the text hue, 32 is red
text_alert_hue = 32
# _____Options End_____

def macroname():
    return str(MacroManager.GetInstance().GetCurrentMacro())

def checksound():
    if sound_file != 0:
        PlaySound(sound_file)

def checkstop():
    if use_stop == True:
        Stop(macroname())

def textalert(ta_type,ta_string,ta_hue):
    if use_text_alert == True:
        if ta_type == 1:
            HeadMsg(ta_string, "self", ta_hue)
        if ta_type == 2:
            SysMessage(ta_string, ta_hue)
        else:
            SysMessage("text_alert_type not set properly",32)

while not Dead('self'):
    Pause(loop_delay)
    if InJournal("Your Hunger Increases...", "system") or InJournal("Your appetite begins to affect your focus.", "system"):
        for foo in foods:
            if FindType(foo,0,food_container):
                while not InJournal("You are simply too full to eat any more!", "system"):
                    if warning_amount > 0 and CountType(foo, food_container) <= warning_amount:
                        textalert(text_alert_type,"Get More Food!",text_alert_hue)
                        checksound()
                    if not FindType(foo,0,food_container) and foods.index(foo) == (len(foods) - 1):
                        textalert(text_alert_type,"Need Food...", text_alert_hue)
                        checksound()
                        checkstop()
                    UseObject("found")
                    Pause(700)
                break
            else:
                if foods.index(foo) == (len(foods) - 1):
                    textalert(text_alert_type,"You Have No Food!", text_alert_hue)
                    checksound()
                    checkstop()
        ClearJournal()
