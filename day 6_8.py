menu=['pizza','burger','fries','coke']
print("MENU:",menu)
order=input("enter the food name from menu:")
if(order in menu):
    print("will be served to you soon, thank you")
else:
    print("Sorry!!we are not delivering this today.")
