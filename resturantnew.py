class Menu():
    def __init__(self,dish,price):
        self.dish=dish
        self.price=price

class Order():
    def __init__(self):
        self.items=[]

    def addingItem(self,menuItem):
        self.items.append(menuItem)
        print(f"Adding {menuItem.dish} to the order list !")
    
    def removingItem(self,menuItem):
        if menuItem in self.items:
            self.items.remove(menuItem)
        print(f"{menuItem.dish} has been removed from the order list !")
    
    def price(self):
        cost=0
        for i in self.items:
            cost+=i.price
        print("The total bill is :",cost)

    def invoice(self):
        print("THE INVOICE OF THE ORDER :")
        total=0
        for i in self.items:
            print(f"{i.dish} = {i.price}")
            total+=i.price
        print("The bill total =",total)
        print("THANK YOU FOR VISITING US!")

class DineIn(Order):
    def __init__(self,tableno):
        super().__init__()
        self.tableno=tableno

    def invoice(self):
        print(f"The bill is for table {self.tableno}.")
        super().invoice()

class TakeAway(Order):
    def __init__(self,customerName):
        super().__init__()
        self.customerName=customerName

    def invoice(self):
        print(f"The order is for {self.customerName}.")
        super().invoice()

menu1=Menu("Biryani",120)
menu2=Menu("Mutton kasa",450)
menu3=Menu("Chicken curry",300)
menu4=Menu("Fried rice",180)
menu5=Menu("Chilli chicken",350)
menu6=Menu("Crispy Chilli Babycorn",280)
menu7=Menu("Chicken Afgani",380)
menu8=Menu("Chicken Tandoori",400)
menu=[menu1,menu2,menu3,menu4,menu5,menu6,menu7,menu8]

print("The MENU : ")
for i in menu:
    print(i.dish,"=",i.price)

responseDineIn=input("Do you want to dine in? (y/n)").lower()
if responseDineIn=="y":

    # OUTPUT DINE IN 
    dineIn=DineIn(12)
    numDineIn=int(input("Enter the number of items you want to order: "))
    for i in range(0,numDineIn):
        item=input("Enter the menu name:")
        for i in menu:
            if item==i.dish.lower():
                dineIn.addingItem(i)
    dineIn.invoice()
    response=input("Do you want to remove any order? (y/n)").lower()
    if response=="y":
        dineIn.removingItem(menu4)
        dineIn.invoice()
    elif response!="n":
        print("Please enter a proper response!")
responseTakeOut=input("Do you want a takeout? (y/n)").lower()
if responseTakeOut=="y":
    # OUTPUT FOR OUT
    name=input("Enter the name of the customer:")
    takeAway=TakeAway(name)
    numTakeOut=int(input("Enter the number of items you want to order: "))
    for i in range(0,numTakeOut):
        item=input("Enter the menu name:").lower()
        for i in menu:
            if item==i.dish.lower():
                takeAway.addingItem(i)
    takeAway.invoice()
    response=input("Do you want to remove any order? (y/n)").lower()
    if response=="y":
        takeAway.removingItem(menu4)
        takeAway.invoice()
    