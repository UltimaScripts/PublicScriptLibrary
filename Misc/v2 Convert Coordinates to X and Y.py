# Convert Coordinates to X and Y
# Description: Converts Coordinates to X and Y
# Usage: Input Coordinates and click Convert
# Author: github.com/UltimaScripts/PublicScriptLibrary
# Version: 2.0.0
# Credits: Karasho & Reetus for GetLatLong, GetXFromLatLong & GetYFromLatLong
import sys
import clr
clr.AddReference('System.Windows.Forms')
clr.AddReference('System.Drawing')
from System.Windows.Forms import Application, Form, Button, TextBox, CheckBox, ComboBox, Label, ComboBoxStyle, KeyPressEventHandler, Keys, MessageBox, MessageBoxButtons, DialogResult
from System.Drawing import Color, Point, Size, Font
from System.Threading import Thread, ThreadStart
from Assistant import Engine
import math, re

class MyForm(Form):
    def __init__(self):
        self.Text = "Coord to X Y"
        self.Width = 214
        self.Height = 140
        self.BackColor = Color.Gray
        self.MinimumSize = Size(214, 140)
        self.MaximumSize = Size(214, 140)
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
        self.button_start.Size = Size(90, 22)
        self.button_start.Font = Font("Arial", 13)
        self.button_start.Click += self.start_button_Click
        self.Controls.Add(self.button_start)
        # scan journal button
        self.button_sj = Button()
        self.button_sj.Text = "Scan Journal"
        self.button_sj.BackColor = Color.Gray
        self.button_sj.Location = Point(20, 70)
        self.button_sj.Size = Size(80, 20)
        self.button_sj.Click += self.sj_button_click
        self.Controls.Add(self.button_sj)
        # clear journal button
        self.button_cj = Button()
        self.button_cj.Text = "Clear Journal"
        self.button_cj.BackColor = Color.Salmon
        self.button_cj.Location = Point(102, 70)
        self.button_cj.Size = Size(80, 20)
        self.button_cj.Click += self.cj_button_click
        self.Controls.Add(self.button_cj)
        # scan gumps button
        self.button_sg = Button()
        self.button_sg.Text = "Scan Gumps"
        self.button_sg.BackColor = Color.Gray
        self.button_sg.Location = Point(60, 92)
        self.button_sg.Size = Size(80, 20)
        self.button_sg.Click += self.sg_button_click
        self.Controls.Add(self.button_sg)
        
    def aot_Checker(self, sender, e):
        if self.TopMost == False:
            self.TopMost = True
        elif self.TopMost == True:
            self.TopMost = False

    def combobox_KeyPress(self, sender, e):
        e.Handled = True  # Cancel the key press event

    def coord_magic(self, possible_string):
        proceed_onward = False
        # Credit to Reetus for these Regex that I combined to work for my needs.
        #result0 = re.search(r"\d+° \d+'\w,\s\d+° \d+'\w")
        result1 = re.search("(\d+)o\s(\d+)'(\w),\s(\d+)o\s(\d+)'(\w)", possible_string)
        result2 = re.search("(\d+)°(\d+)'(\w),(\d+)°(\d+)'(\w)", possible_string)
        result3 = re.search("(\d+)°\s(\d+)'(\w),\s(\d+)°\s(\d+)'(\w)", possible_string)
        if result1 or result2 or result3:
            result = MessageBox.Show("Use This Result: " + possible_string + " ?", "Confirmation", MessageBoxButtons.YesNo)
            if result == DialogResult.Yes:
                proceed_onward = True
        if proceed_onward:
            try:
                # Letters
                letters = re.findall(r"\d+'\b(\w)", possible_string)
                letter1, letter2 = letters[:2]
                # Numbers
                if result1:
                    numbers = re.findall(r'\d+o', possible_string)
                    number1, number3 = numbers[:2]
                if result2 or result3:
                    numbers = re.findall(r'\d+°', possible_string)
                    number1, number3 = numbers[:2]
                numberz = re.findall(r"\d+'", possible_string)
                number2, number4 = numberz[:2]
                # magic
                if "°" in str(number1):
                    number1 = str(number1).replace("°", "")
                if "o" in str(number1):
                    number1 = str(number1).replace("o", "")
                number2 = str(number2).replace("'", "")
                if "°" in str(number3):
                    number3 = str(number3).replace("°", "")
                if "o" in str(number3):
                    number3 = str(number3).replace("o", "")
                number4 = str(number4).replace("'", "")
                self.textbox1.Text = str(number1)
                self.textbox2.Text = str(number2)
                self.combobox_ns.Text = str(letter1)
                self.textbox3.Text = str(number3)
                self.textbox4.Text = str(number4)
                self.combobox_ew.Text = str(letter2)
                return True
            except Exception as e:
                print("Error:", e)

    def sg_button_click(self, sender, e):
        result = MessageBox.Show("This Feature is Not Fully Tested, Proceed?", "Confirmation", MessageBoxButtons.YesNo)
        if result == DialogResult.Yes:
            inital_gump_list = []
            gumps = Engine.Gumps.GetGumps()
            for gump in gumps:
                inital_gump_list.append(gump)
            
            for x in inital_gump_list[1]:
                #print x.ID
                if x.Pages != None:
                    for pagecount in range(len(x.Pages)):
                        ele = x.Pages[pagecount].GumpElements
                        for entry in range(len(ele)):
                            textentry = str(ele[entry].Text)
                            if textentry != "" or textentry != None:
                                self.coord_magic(textentry)

    def sj_button_click(self, sender, e):
        journal = Engine.Journal.GetBuffer()
        for j in range(len(journal) - 1, -1, -1):
            if self.coord_magic(journal[j].Text) == True:
                return

    def cj_button_click(sender, event, e):
        result = MessageBox.Show("Do you want to Clear Journal?", "Confirmation", MessageBoxButtons.YesNo)
        if result == DialogResult.Yes:
            try:
                ClearJournal()
            except Exception as e:
                print("Error:", e)

    def start_button_Click(self, sender, event):
        if sender.Text == "Convert":
            thread = Thread(ThreadStart(self.my_function))
            thread.Start()

    def my_function(self):
        #Credit to Karasho & Reetus for GetLatLong
        def GetLatLong(degreeLat, minLat, degreeLong, minLong, direction1, direction2):
            lat = degreeLat + minLat / 100.0
            longi = degreeLong + minLong / 100.0
            
            return (GetXFromLatLong(lat, longi, direction1, direction2), GetYFromLatLong(lat, longi, direction1, direction2))
        
        #Credit to Karasho & Reetus for GetXFromLatLong
        def GetXFromLatLong(lat, lon, direction1, direction2):
            centerX = 1323
            tempLon = math.floor(lon) * 60.0 + lon % 1 * 100.0 if direction2 != 'W' else -1.0 * math.ceil(lon) * 60.0 + lon % 1 * 100.0
            resultX = int((tempLon / 21600.0 * 5120.0) + centerX)
            if resultX < 0:
                resultX += 5120
            if resultX >= 5120:
                resultX -= 5120
                
            return resultX
    
        #Credit to Karasho & Reetus for GetYFromLatLong
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
            #print "{}, {}".format(x, y)
        except Exception as e:
            print("Error:", e)
#######
Application.Run(MyForm())