# make sure Run in backround is not already checked(True)
# Run in background won't show checked unless you -
#  click off the current macro and back onto it.
from ClassicAssist.Data.Macros import MacroManager

if MacroManager.GetInstance().CurrentMacro.IsBackground == False:
    try:
        MacroManager.GetInstance().CurrentMacro.IsBackground = True
    except:
        pass

print(MacroManager.GetInstance().CurrentMacro.IsBackground)