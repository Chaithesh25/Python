class car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year


    def showDetails(self):
        print("car Details.......")
        print("make: ",self.make)
        print("model: ",self.model)
        print("year: ",self.year)


        
obj = car('Honda','city',2004)

obj.showDetails()