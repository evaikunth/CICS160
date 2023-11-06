import Car
class GasolineCar(Car.Car): 

    def __init__(self,makeAndModel:str = "none assigned", numberOfDoors:int = 4, maximumNumberOfPassengers:int = 5, gasTankSize:int = -1):
        super().__init__(makeAndModel,numberOfDoors,maximumNumberOfPassengers)
        self.gasTankSize = gasTankSize

     #getter methods

    def getGasTankSize(self) -> int: 
        return(self.gasTankSize)
     
    #setters

    def setGasTankSize(self,gasTankSize):
        self.gasTankSize = gasTankSize

    def __str__(self):
        stringToReturn = " make model: " + self.makeModel + "\n number of doors: " + str(self.numDoors) + "\n max passengers: " + str(self.maxPassengers) + "\n gas tank size: " + str(self.gasTankSize)
        return(stringToReturn)
    
if __name__ == "__main__":
    pass
