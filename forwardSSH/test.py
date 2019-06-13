
myStr = "this is a test"
myList = list(myStr)

for i in myList:
    i = chr(ord(i) + 1)
    print i

print ''.join(myList)

if myStr == ''.join(myList):
    print "myStr == myList"
