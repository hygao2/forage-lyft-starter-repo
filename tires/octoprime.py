from abc import ABC
import datetime

from tires.tires import Tires

class OctoprimeTire(Tires):
    def __init__(self, tire_wear):
       
        self.tire_wear = tire_wear


    def needs_service(self):
        sum = 0
        for wear in self.tire_wear:
            sum += wear
            if sum >= 3:
                return True

        return False