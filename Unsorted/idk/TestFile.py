testlist1 = [1, [2,3]]
testlist2 = [[1,2,3]]
testlist3 = [[1,2],[3,4],[5,6]]

if 1 in testlist1:
    print("One True")
print(testlist1[0:len(testlist1)])
if 1 in testlist2:
    print("Two True")
print(testlist2[0:len(testlist2)])
if 1 in testlist3:
    print("Three True")
print(testlist3[0:len(testlist3)])

#if any(1 in sl for sl in testlist1):
#    print("True")

if any(1 in sl for sl in testlist2):
    print("1 is in testlist2 True")

print(testlist2)
print(testlist2[0])
print(testlist2[0][0])
print("-----")

for x in range(len(testlist3)):
    if 3 == testlist3[x][0] and 4 == testlist3[x][1]:
        print(testlist3[x])
        print(testlist3[x][0])
        print(testlist3[x][1])
