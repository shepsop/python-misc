class Car:
    
    def __init__(self,make,model,year,color) -> None:
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print('this car is driving')

    def park(self):
        print('this car is parking')

    def stop(self):
        print('this car is stopped')