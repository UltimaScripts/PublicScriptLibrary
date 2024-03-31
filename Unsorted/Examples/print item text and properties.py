from Assistant import Engine

# replace 0x1234 with the item serial -
# you want to print properties for
item_serial = 0x1234

item = Engine.Items.GetItem(item_serial)

if item != None:
    for prop in item.Properties:
        print(prop.Text)
        print(prop.Arguments)
        for p in range(len(prop.Arguments)):
            print(prop.Arguments[p])

# If this doesn't work on your shard.
# You can try check for substrings -
# in the Text or use Regex on the Text.