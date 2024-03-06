# Name: food watch and eater
# Author: Baler
# Version: 1.0.3
# ##### Options Start #####
# foods is a list, add more graphic IDs you required, separate by commas
# 0xc77 carrot, 0x172a lime
foods = [0xc77,0x172a]
#
# set warning_amount to 0 do disable it.
warning_amount = 5
#
# set food_container to the Serial for the container where food is.
# 'backpack' is an Alias that's auto-setup by CA
# replace the entire GetAlias('backpack'), if you want to change it to a specific serial
food_container = GetAlias('backpack')
#
# set sound_file to 0 to disable it.
sound_file = "Bike Horn.wav"
# ##### Options End #####
while not Dead('self'):
    Pause(1000)
    if InJournal("Your Hunger Increases...", "system") or InJournal("Your appetite begins to affect your focus.", "system"):
        for foo in foods:
            if FindType(foo,0,food_container):
                while not InJournal("You are simply too full to eat any more!", "system"):
                    if warning_amount > 0 and CountType(foo, food_container) <= warning_amount:
                        HeadMsg("Get More Food!",32)
                        if sound_file != 0:
                            PlaySound(sound_file)
                    if not FindType(foo,0,food_container) and foods.index(foo) == (len(foods) - 1):
                        HeadMsg("Need Food...", "self",32)
                        if sound_file != 0:
                            PlaySound(sound_file)
                        Stop()
                    UseObject("found")
                    Pause(700)
                break
            else:
                if foods.index(foo) == (len(foods) - 1):
                    HeadMsg("You Have No Food!", "self",32)
                    if sound_file != 0:
                        PlaySound(sound_file)
                    Stop()
        ClearJournal()