
class Plane:
    def __init__(self, a2_Departure: float, b2_Departure: float, c2_Departure: float, 
                 a2_Arrival: float, b2_Arrival: float, c2_Arrival: float, design_Fuel: float):
        #Considered 0 if p-value bigger than 0.10 
        self.a2_Departure = a2_Departure 
        self.b2_Departure = b2_Departure
        self.c2_Departure = c2_Departure
        self.a2_Arrival = a2_Arrival 
        self.b2_Arrival = b2_Arrival
        self.c2_Arrival = c2_Arrival
        self.design_Fuel = design_Fuel
