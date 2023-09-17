class Car:
    def __init__(self):
        self.make_model = "None Assigned"
        self.num_doors = 4
        self.max_passengers = 5

    def setMakeModel(self,make_model):
        self.make_model = make_model

    def setNumDoors(self,num_doors):
        self.num_doors = num_doors
    
    def setMaxPassengers(self, max_passengers):
        self.max_passengers = max_passengers 

    def getMakeModel(self):
        return(self.make_model) 
    
    def getNumDoors(self):
        return(self.num_doors) 
    
    def getMaxPassengers(self):
        return(self.max_passengers)
    
    def __str__(self):
        stringReturn = "Car make: " + self.getMakeModel() + "\n" + "Number of doors: " + str(self.getNumDoors()) + "\n" + "Maximum number of passengers: " + str(self.getMaxPassengers())
        return(stringReturn)


car1 = Car()
car1.setMakeModel("Dodge Dart")
car1.setNumDoors(5)
car1.setMaxPassengers(7)
print("The model of this car is a",car1.getMakeModel(),"\n",
      "The car has",car1.getNumDoors(),"doors","\n","It holds",car1.getMaxPassengers(),"passengers")
print(car1)
