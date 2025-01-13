class Shoppingcart():
    def __init__(self,dict):
        self.dict=dict

    def displayWishlist(self):
        total=0
        for i in self.dict:
            print(i,self.dict[i])
            total+=(self.dict[i][0]*self.dict[i][1])
        print("Total=",total)
    
    def insertIntoCart(self):
        item=input("Enter item to be inserted into cart:")
        price=int(input("Enter the price"))
        if item in self.dict:
            self.dict[item][1]+=1
        else:
            self.dict[item]=[price,1]
    
    def removeFromCart(self):
        item=input("Enter item to be removed from cart:")
        if item in self.dict:
            del self.dict[item]
        
cart=Shoppingcart({})

num1=int(input("Enter the number of items to add in the shopping cart: "))
print("EXAMPLE:PLEASE ENTER THE NAME OF THE ITEM TWICE IF THE QUANTITY FOR THAT ITEM IS 2.")
for i in range(0,num1):
    cart.insertIntoCart()
cart.displayWishlist()

num2=int(input("Enter the number of items to remove in the shopping cart: "))
for i in range(0,num2):
    cart.removeFromCart()
cart.displayWishlist()