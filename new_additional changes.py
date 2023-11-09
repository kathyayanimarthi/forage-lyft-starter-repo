class Tires:
    def __init__(self, tire_wear_array):
        self.tire_wear_array = tire_wear_array

    def needs_service(self, tire_type):
        if tire_type == "Carrigan":
            return any(wear >= 0.9 for wear in self.tire_wear_array)
        elif tire_type == "Octoprime":
            return sum(self.tire_wear_array) >= 3
        else:
            raise ValueError("Invalid tire type")
class CarFactory:
    @staticmethod
    def create_car(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear_array):
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        tires = Tires(tire_wear_array)
        return Car(engine, battery, tires)
class SpindlerBattery(Serviceable):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        # Modified service interval to 3 years (1095 days)
        return (self.current_date - self.last_service_date).days >= 1095
