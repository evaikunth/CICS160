import Car
class ElectricCar(Car.Car): 

    def __init__(self,makeAndModel:str = "none assigned", numberOfDoors:int = 4, maximumNumberOfPassengers:int = 5, batterySize = -1):
        super().__init__(makeAndModel,numberOfDoors,maximumNumberOfPassengers)
        self.batterySize = batterySize

     #getter methods
  
    def getBatterySize(self) -> int:
        return(self.batterySize)
    
    #setters

    def setBatterySize(self,batterySize):
        self.batterySize = batterySize

    def __str__(self):
        stringToReturn = " make model: " + self.makeModel + "\n number of doors: " + str(self.numDoors) + "\n max passengers: " + str(self.maxPassengers) + "\n battery size " + str(self.batterySize)
        return(stringToReturn)
    
if __name__ == "__main__":
    pass
