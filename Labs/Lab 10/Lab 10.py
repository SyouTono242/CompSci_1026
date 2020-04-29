class Car:
    def __init__(self,efficiency):
        self.efficiency = efficiency
        self.fuel = 0

    def drive(self,distance):
        self.fuel -= distance / self.efficiency

    def addGas(self,addGas):
        self.fuel = self.fuel + addGas

    def getGasLevel(self):
        return self.fuel


def main():
    myHybrid = Car(50)
    myHybrid.addGas(20)
    myHybrid.drive(100)
    print("The current fuel level is",myHybrid.getGasLevel())


main()

