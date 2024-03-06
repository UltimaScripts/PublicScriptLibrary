# Name: afk check alert
# Author: Baler
# Version: 1.0.0
# Note: Check the box Run in background & Save for this script.
from Assistant import Engine

while not Dead('self'):
    Pause(10000)
    gumps = Engine.Gumps.GetGumps()
    if gumps[0] == True and gumps[1] is not None:
        for g in gumps[1]:
            if g is not None:
                if 'You are being checked for unattended' in g.Strings:
                    # default directory for sound files is located at Data\Plugins\ClassicAssist\Sounds
                    # You can specify the file location e.g. PlaySound("C:\\Folder\\Folder\\sound.wav")
                    # Sound file needs to be .wav format & it will play at full volume.
                    PlaySound("Bike Horn.wav")