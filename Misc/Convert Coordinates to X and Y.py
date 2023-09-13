# Convert Coordinates to X and Y
# Description: Converts Coordinates to X and Y
# Usage: Input Coordinates and click Convert
# Author: github.com/UltimaScripts/PublicScriptLibrary
# Version: 1.0.0
# Credits: Reetus wrote GetLatLong, GetXFromLatLong & GetYFromLatLong
import sys
import clr
clr.AddReference('System.Windows.Forms')
clr.AddReference('System.Drawing')
from System.Windows.Forms import Application, Form, Button, TextBox, CheckBox, ComboBox, Label, ComboBoxStyle, KeyPressEventHandler, Keys
from System.Drawing import Color, Point, Size, Font
from System.Threading import Thread, ThreadStart
from Assistant import Engine
import math

class MyForm(Form):
    def __init__(self):
        self.Text = "Coord to X Y"
        self.Width = 214
        self.Height = 100
        self.BackColor = Color.Gray
        self.MinimumSize = Size(214, 100)
        self.MaximumSize = Size(214, 100)
        # coordinates label
        self.label_coord = Label()
        self.label_coord.Text = "Enter Coordinates"
        self.label_coord.Location = Point(0, 0)
        self.label_coord.Width = 166
        self.label_coord.Height = 18
        self.label_coord.Font = Font("Arial", 14)
        self.Controls.Add(self.label_coord)
        # always on top
        self.checkBox_aot = CheckBox()
        self.checkBox_aot.Text = "Top"
        self.checkBox_aot.Location = Point(166, 0)
        self.checkBox_aot.Height = 16
        self.checkBox_aot.CheckedChanged += self.aot_Checker
        self.Controls.Add(self.checkBox_aot)
        # coordinate input 1
        self.textbox1 = TextBox()
        self.textbox1.Location = Point(0, 20)
        self.textbox1.Width = 30
        self.Controls.Add(self.textbox1)
        # coordinate input 2
        self.textbox2 = TextBox()
        self.textbox2.Location = Point(32, 20)
        self.textbox2.Width = 30
        self.Controls.Add(self.textbox2)
        # NS combo box
        self.combobox_ns = ComboBox()
        self.combobox_ns.Location = Point(64, 20)
        self.combobox_ns.Width = 36
        self.combobox_ns.Items.Add("N")
        self.combobox_ns.Items.Add("S")
        self.combobox_ns.KeyPress += self.combobox_KeyPress
        self.Controls.Add(self.combobox_ns)
        # coordinate input 3
        self.textbox3 = TextBox()
        self.textbox3.Location = Point(102, 20)
        self.textbox3.Width = 30
        self.Controls.Add(self.textbox3)
        # coordinate input 4
        self.textbox4 = TextBox()
        self.textbox4.Location = Point(134, 20)
        self.textbox4.Width = 30
        self.Controls.Add(self.textbox4)
        # EW combo box
        self.combobox_ew = ComboBox()
        self.combobox_ew.Location = Point(166, 20)
        self.combobox_ew.Width = 36
        self.combobox_ew.Items.Add("E")
        self.combobox_ew.Items.Add("W")
        self.combobox_ew.KeyPress += self.combobox_KeyPress
        self.Controls.Add(self.combobox_ew)
        # X label
        self.label_x = Label()
        self.label_x.Text = "X"
        self.label_x.Location = Point(0, 45)
        self.label_x.Width = 20
        self.label_x.Height = 18
        self.label_x.Font = Font("Arial", 16)
        self.Controls.Add(self.label_x)
        # x result textbox
        self.textbox_xr = TextBox()
        self.textbox_xr.Location = Point(20, 45)
        self.textbox_xr.Width = 30
        self.Controls.Add(self.textbox_xr)
        # Y label
        self.label_x = Label()
        self.label_x.Text = "Y"
        self.label_x.Location = Point(52, 45)
        self.label_x.Width = 20
        self.label_x.Height = 18
        self.label_x.Font = Font("Arial", 16)
        self.Controls.Add(self.label_x)
        # y result textbox
        self.textbox_yr = TextBox()
        self.textbox_yr.Location = Point(74, 45)
        self.textbox_yr.Width = 30
        self.Controls.Add(self.textbox_yr)
        # start button
        self.button_start = Button()
        self.button_start.Text = "Convert"
        self.button_start.BackColor = Color.Gray
        self.button_start.Location = Point(110, 45)
        self.button_start.Size = Size(90, 24)
        self.button_start.Font = Font("Arial", 14)
        self.button_start.Click += self.start_button_Click
        self.Controls.Add(self.button_start)

    def aot_Checker(self, sender, e):
        if self.TopMost == False:
            self.TopMost = True
        elif self.TopMost == True:
            self.TopMost = False

    def combobox_KeyPress(self, sender, e):
        e.Handled = True  # Cancel the key press event

    def start_button_Click(self, sender, event):
        if sender.Text == "Convert":
            thread = Thread(ThreadStart(self.my_function))
            thread.Start()

    def my_function(self):
        #Credit to Reetus for GetLatLong
        def GetLatLong(degreeLat, minLat, degreeLong, minLong, direction1, direction2):
            lat = degreeLat + minLat / 100.0
            longi = degreeLong + minLong / 100.0
            
            return (GetXFromLatLong(lat, longi, direction1, direction2), GetYFromLatLong(lat, longi, direction1, direction2))
        
        #Credit to Reetus for GetXFromLatLong
        def GetXFromLatLong(lat, lon, direction1, direction2):
            centerX = 1323
            tempLon = math.floor(lon) * 60.0 + lon % 1 * 100.0 if direction2 != 'W' else -1.0 * math.ceil(lon) * 60.0 + lon % 1 * 100.0
            resultX = int((tempLon / 21600.0 * 5120.0) + centerX)
            if resultX < 0:
                resultX += 5120
            if resultX >= 5120:
                resultX -= 5120
                
            return resultX
    
        #Credit to Reetus for GetYFromLatLong
        def GetYFromLatLong(lat, lon, direction1, direction2):
            centerY = 1624
            tempLat = math.floor(lat) * 60.0 + lat % 1 * 100.0 if direction1 != 'N' else -1.0 * math.ceil(lat) * 60.0 + lat % 1.0 * 100.0
            resultY = int((tempLat / 21600.0 * 4096.0) + centerY)
            if resultY < 0:
                resultY += 4096
            if resultY >= 4096:
                resultY -= 4096
            
            return resultY

        degreeLat = self.textbox1.Text
        if degreeLat.isdigit() == False:
            print("Input 1, Requires Only a Number")
            return
        minLat = self.textbox2.Text
        if minLat.isdigit() == False:
            print("Input 2, Requires Only a Number")
            return
        direction1 = self.combobox_ns.Text
        if direction1 == "":
            print("N or S Missing")
            return
        degreeLong = self.textbox3.Text
        if degreeLong.isdigit() == False:
            print("Input 3, Requires Only a Number")
            return
        minLong = self.textbox4.Text
        if minLong.isdigit() == False:
            print("Input 4, Requires Only a Number")
            return
        direction2 = self.combobox_ns.Text
        if direction2 == "":
            print("E or W Missing")
            return
        try:
            [x, y] = GetLatLong(int(degreeLat), int(minLat), int(degreeLong), int(minLong), direction1, direction2)
            self.textbox_xr.Text = str(x)
            self.textbox_yr.Text = str(y)
            print "{}, {}".format(x, y)
        except Exception as e:
            print("Error:", e)
#######
Application.Run(MyForm())