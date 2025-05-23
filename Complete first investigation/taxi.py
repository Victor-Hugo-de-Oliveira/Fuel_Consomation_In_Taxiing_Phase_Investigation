import math
from plane import Plane

class Taxi:
    def __init__(self, plane: Plane, time_Departure: float, time_Arrival: float, na_Departure: int,  
                 na_Arrival: int, Tamb: float):
        self.plane = plane
        self.time_Departure = time_Departure
        self.time_Arrival = time_Arrival
        self.na_Departure = na_Departure
        self.na_Arrival = na_Arrival
        self.Tamb = Tamb

    def fuel_Departure(self) -> float:
        # Linear fit calculation
        fuel_Departure = math.sqrt(self.Tamb) * (self.plane.a2_Departure + self.plane.b2_Departure*self.time_Departure
                                                  + self.plane.c2_Departure*self.na_Departure) 
        return fuel_Departure

    def fuel_Arrival(self) -> float:
        # Linear fit calculation
        fuel_Arrival = math.sqrt(self.Tamb) * (self.plane.a2_Arrival + self.plane.b2_Arrival*self.time_Arrival
                                                + self.plane.c2_Arrival*self.na_Arrival) 
        return fuel_Arrival
    
    def fuel_Taxiing(self) -> float:
        return self.fuel_Departure() + self.fuel_Arrival()

    def ratioTaxiFuel_DesignFuel(self) -> float:
        return (self.fuel_Taxiing()/self.plane.design_Fuel)*100