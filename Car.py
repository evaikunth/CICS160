class Car:
    def __init__(self, make_model:str = "none", num_doors:int = 4, max_passengers:int = 5):
        self.makeModel = make_model
        self.numDoors = num_doors
        self.maxPassengers = max_passengers

    #getter methods
    def getMakeAndModel(self) -> str:
        return(self.makeModel)
    
    def getMaximumNumberOfPassengers    (self) -> int:
        return(self.maxPassengers)
    
    #setters

    def setMakeAndModel(self,make_model:str):
        self.makeModel = make_model
  

    def __str__(self):
        stringToReturn = " make model: " + self.makeModel + "\n number of doors: " + str(self.numDoors) + "\n max passengers: " + str(self.maxPassengers)
        return(stringToReturn)
    
if __name__ == "__main__": 
   pass
