from abc import ABC, abstractmethod
#Willoughby Engine - every 60,000 miles
#Sternman Engine - when Warning Indicator is on
#Spindler Battery - Every 2 years
#Nubbin Battery - every 4 years

from abc import ABC, abstractmethod
from datetime import date

# Interface for serviceable parts
class Serviceable(ABC):
    @abstractmethod
    def needs_service(self) -> bool:
        pass

# Engine classes
class CapuletEngine(Serviceable):
    def __init__(self, last_service_mileage, current_mileage):
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage

    def needs_service(self):
        return self.current_mileage - self.last_service_mileage >= 30000

class SternmanEngine(Serviceable):
    def __init__(self, warning_light_on):
        self.warning_light_on = warning_light_on

    def needs_service(self):
        return self.warning_light_on

class WilloughbyEngine(Serviceable):
    def __init__(self, last_service_mileage, current_mileage):
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage

    def needs_service(self):
        return self.current_mileage - self.last_service_mileage >= 60000

# Battery classes
class SpindlerBattery(Serviceable):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        return (self.current_date - self.last_service_date).days >= 730

class NubbinBattery(Serviceable):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        return (self.current_date - self.last_service_date).days >= 1460

# Car Factory class
class CarFactory:
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        return Car(engine, battery)

    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        return Car(engine, battery)

    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_on):
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(last_service_date, current_date)
        return Car(engine, battery)

    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        return Car(engine, battery)

    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        return Car(engine, battery)

# Car class
class Car:
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery

# Example usage
current_date = date.today()
last_service_date = date(2021, 1, 1)
current_mileage = 45000
last_service_mileage = 30000

calliope = CarFactory.create_calliope(current_date, last_service_date, current_mileage, last_service_mileage)
if calliope.engine.needs_service() or calliope.battery.needs_service():
    print("Calliope needs service.")
else:
    print("Calliope does not need service.")
