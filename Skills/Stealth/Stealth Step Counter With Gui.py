# Stealth Step Counter With Gui
# Description: Counts Stealth Steps, Forces Walk & Has a Gui
# Usage: Check Options on Window, Hit Start
# Author: github.com/UltimaScripts/PublicScriptLibrary
# Version: 1.0.0
# Note: Uses ClearJournal which isn't optimal.
import sys
import clr
clr.AddReference('System.Windows.Forms')
clr.AddReference('System.Drawing')
from System.Windows.Forms import Application, Form, Button, Label, CheckBox
from System.Drawing import Color, Point, Size, Font
from System.Threading import Thread, ThreadStart
from Assistant import Engine

class MyForm(Form):
    def __init__(self):
        self.Width = 100
        self.Height = 200
        self.BackColor = Color.Gray
        self.MinimumSize = Size(100, 200)
        self.MaximumSize = Size(100, 200)
        # always on top
        self.checkBox_aot = CheckBox()
        self.checkBox_aot.Text = "Win On Top"
        self.checkBox_aot.Location = Point(0, 0)
        self.checkBox_aot.Height = 16
        self.checkBox_aot.CheckedChanged += self.aot_Checker
        self.Controls.Add(self.checkBox_aot)
        # force walk
        self.checkBox_fw = CheckBox()
        self.checkBox_fw.Text = "Stealth Walk"
        self.checkBox_fw.Location = Point(0, 18)
        self.checkBox_fw.Height = 16
        self.Controls.Add(self.checkBox_fw)
        # steps left label
        self.label_sl = Label()
        self.label_sl.Text = "Steps Left"
        self.label_sl.Location = Point(0, 37)
        self.label_sl.Size = Size(90, 14)
        self.label_sl.Font = Font("Arial", 10)
        self.Controls.Add(self.label_sl)
        # steps left overhead message checkbox
        self.checkBox_slom = CheckBox()
        self.checkBox_slom.Text = "Overhead Msg"
        self.checkBox_slom.Location = Point(0, 50)
        self.Controls.Add(self.checkBox_slom)
        # steps left system message checkbox
        self.checkBox_slsm = CheckBox()
        self.checkBox_slsm.Text = "System Msg"
        self.checkBox_slsm.Location = Point(0, 68)
        self.Controls.Add(self.checkBox_slsm)
        # count steps label
        self.label_cs = Label()
        self.label_cs.Text = "Count Steps"
        self.label_cs.Location = Point(0, 91)
        self.label_cs.Size = Size(90, 16)
        self.label_cs.Font = Font("Arial", 10)
        self.Controls.Add(self.label_cs)
        # count steps overhead message checkbox
        self.checkBox_csom = CheckBox()
        self.checkBox_csom.Text = "Overhead Msg"
        self.checkBox_csom.Location = Point(0, 102)
        self.Controls.Add(self.checkBox_csom)
        # count steps system message checkbox
        self.checkBox_cssm = CheckBox()
        self.checkBox_cssm.Text = "System Msg"
        self.checkBox_cssm.Location = Point(0, 120)
        self.Controls.Add(self.checkBox_cssm)
        # start button
        self.button_start = Button()
        self.button_start.Text = "Start"
        self.button_start.BackColor = Color.Gray
        self.button_start.Location = Point(0, 145)
        self.button_start.Size = Size(90, 30)
        self.button_start.Font = Font("Arial", 16)
        self.button_start.Click += self.start_button_Click
        self.Controls.Add(self.button_start)

    def aot_Checker(self, sender, e):
        if self.TopMost == False:
            self.TopMost = True
        elif self.TopMost == True:
            self.TopMost = False

    def start_button_Click(self, sender, event):
        #if self.checkBox_cssm.Checked:
            #print("Smelt Checkbox is checked!")
        if sender.Text == "Start":
            self.checkBox_aot.Enabled = False
            self.checkBox_fw.Enabled = False
            self.checkBox_csom.Enabled = False
            self.checkBox_cssm.Enabled = False
            self.checkBox_slom.Enabled = False
            self.checkBox_slsm.Enabled = False
            self.button_start.BackColor = Color.Salmon
            sender.Text = "Stop"
            thread = Thread(ThreadStart(self.my_function))
            thread.Start()
        elif sender.Text == "Stop":
            self.checkBox_aot.Enabled = True
            self.checkBox_fw.Enabled = True
            self.checkBox_csom.Enabled = True
            self.checkBox_cssm.Enabled = True
            self.checkBox_slom.Enabled = True
            self.checkBox_slsm.Enabled = True
            self.button_start.BackColor = Color.Gray
            sender.Text = "Start"
    
    def my_function(self):
        #using ClearJournal isn't the best solution
        ClearJournal()
        while self.button_start.Text == "Stop":
            Pause(10)
            if InJournal("You begin to move quietly."):
                ClearJournal()
                if self.checkBox_fw.Checked:
                    SetForceWalk(True)
                var_x = Engine.Player.X
                var_y = Engine.Player.Y
                steps = 0
                max_steps = 12
                while Hidden("self"):
                    Pause(10)
                    if not self.button_start.Text == "Stop":
                        break
                    if not var_x == Engine.Player.X or not var_y == Engine.Player.Y:
                        var_x = Engine.Player.X
                        var_y = Engine.Player.Y
                        steps += 1
                        sl = (max_steps - steps)
                        if self.checkBox_slom.Checked:
                            HeadMsg(str("Steps Left: " + str(sl)), "self")
                        if self.checkBox_slsm.Checked:
                            SysMessage(str("Steps Left: " + str(sl)))
                        if self.checkBox_csom.Checked:
                            HeadMsg(str("Steps: " + str(steps)), "self")
                        if self.checkBox_cssm.Checked:
                            SysMessage(str("Steps: " + str(steps)))
                SetForceWalk(False)
#######
Application.Run(MyForm())