# Name: get dress agent entry serials
# Author: Reetus
# Usages: Change 'Dress-1' to match the -
#    dress agent name you want the serials from.
# Note: if you don't put in the correct -
#    dress agent name it will error NoneType.
import clr
import System
clr.AddReference("System.Core")
clr.ImportExtensions(System.Linq)
from ClassicAssist.Data.Dress import DressManager

dressAgentEntry = DressManager.GetInstance().Items.FirstOrDefault(lambda d: d.Name == 'Dress-1')

if dressAgentEntry == 'None':
    print 'No dress entry'
    
for x in dressAgentEntry.Items:
    print x.Serial