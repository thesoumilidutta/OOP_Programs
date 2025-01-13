class Zoomanagement():
    def __init__(self,dict):
        self.dict=dict

    def viewAnimals(self):
        for i in self.dict:
            print(i,self.dict[i])
            
    def addAnimal(self):
        species=input("Enter the species of animal to be added :").lower()
        if species in self.dict:
            self.dict[species][1]+=1
        else:
            food=int(input("Enter the feeding quantity:"))
            self.dict[species]=[food,1]
    
    def feedingRequirements(self):
        species=input("Enter the animal whose feeding requirement is to be shown:")
        food=0
        if species in self.dict:
            food+=self.dict[species][0]*self.dict[species][1]
        print("The feeding requirements are: ",food)

species1=Zoomanagement({})
num=int(input("How many species do you wanna add?"))
for i in range(0,num):
    species1.addAnimal()
species1.viewAnimals()
species1.feedingRequirements()