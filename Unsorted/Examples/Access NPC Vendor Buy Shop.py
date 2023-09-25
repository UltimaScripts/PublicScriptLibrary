from Assistant import Engine
#0x1a0 is the mobile vendor serial
mobile = Engine.Mobiles.GetMobile(0x1a0)
#Open the npc shop inventory before playing script
#Note this is not for Player Vendors.
list = mobile.ShopBuy
if list != None:
    for l in list:
        print("___Amount___")
        print(l.Amount)
        print("___Item___")
        print(l.Item)
        print("___Name___")
        print(l.Name)
        print("___Price___")
        print(l.Price)
        ##printing the vendor serial is redundant.
        #print("___VendorSerial)___")
        #print(l.VendorSerial)
        ##comment out the Stop if you want it to print out everything.
        Stop()