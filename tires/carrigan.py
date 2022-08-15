from abc import ABC
import datetime

from tires.tires import Tires

class CarriganTire(Tires):
    def __init__(self, tire_wear):
       
        self.tire_wear = tire_wear


    def needs_service(self):
        for wear in self.tire_wear:
            if wear >= 0.9:
                return True

        return False