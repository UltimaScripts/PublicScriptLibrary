list = ['Yes', "No", '2+2=']
res, index = SelectionPrompt(list,"Do You Want To Continue?",True)

if res:
    print('Option {} was selected\nYou picked {}.'.format(index,list[index]))
    if index == 0:
        print("yes")
    elif index == 1:
        print("No")
    elif index == 2:
        num = (2 + 2)
        print("2+2= {}".format(num))
else:
    print 'Cancel was pressed\nOr Closable was set to True\nAnd you closed the gump.'