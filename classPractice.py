class car:
    def __init__(self, seats):
        #writing pass here removes syntax errors, but runtime will fail
        self.seats = seats
    def enter_race_mode(self): #strips seats for speed
        self.seats = 2

class SUV(car): #revisiting with inheritance, provide the super class in ()
    def __init__(self, seats):
        super().__init__(seats) #system-provided, super init handles the parent class init
        sliding_doors = True #proceed to construct normally with additional data
    def enter_race_mode(self):
        #super().enter_race_mode() #overloading works normally, call super again to recover parent method and add if wanted 
        print("Not family friendly")