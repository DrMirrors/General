import datetime
currentDT = datetime.datetime.now()
print (currentDT.strftime("%I:%M:%S %p"))
print (currentDT.strftime("%a, %b %d, %Y"))
if int(currentDT.strftime("%H")) < (12):
    print("Good Morning!")
    pass
elif int(currentDT.strftime("%H")) < (19):
    print("Good Afternoon!")
    pass
else:
    print("Have a good night!")
    pass
