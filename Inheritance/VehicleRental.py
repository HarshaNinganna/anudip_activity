class Vehicle_rental_hub:
    def __init__(self, registration_no, brand, rent_price_perday):
        self.registration_no = registration_no
        self.brand = brand
        self.rent_price_perday = rent_price_perday
    def calculate_rental_cost(self, days):
        return self.rent_price_perday * days
    def show_details(self):
        return f"{self.brand} ({self.registration_no}) - Rs.{self.rent_price_perday}/day"
class Car(Vehicle_rental_hub):
    def __init__(self, registration_no, brand, rent_price_perday, insurance):
        super().__init__(registration_no, brand, rent_price_perday)
        self.insurance = insurance
    def calculate_rental_cost(self, days):
        base_cost = super().calculate_rental_cost(days)
        return base_cost + self.insurance
class Bike(Vehicle_rental_hub):
    def __init__(self, registration_no, brand, rent_price_perday):
        super().__init__(registration_no, brand, rent_price_perday)
    def calculate_rental_cost(self, days):
        base_cost = super().calculate_rental_cost(days)
        return base_cost + super().calculate_rental_cost(days)
class truck(Vehicle_rental_hub):
    def __init__ (self, registration_no, brand, rent_price_perday, heavy_Vehicle_fee):
        super().__init__(registration_no, brand, rent_price_perday)
    def calculate_rental_cost(self, days):
         base_cost = super().calculate_rental_cost(days)
         return base_cost + super().calculate_rental_cost(days)
car = Car("KA01AB1234", "Toyota", 2499, insurance=500)
Bike = Bike("KA16HY2001", "Royal Enfield Classic", 1499)
truck = truck("KA51EC2005", "Tata", 4589, heavy_Vehicle_fee=1499)
days = 5
print(car.show_details())
print(f"Total cost for {days} days: Rs.{car.calculate_rental_cost(days)}")
print(Bike.show_details())
print(f"Total cost for {days} days: Rs.{Bike.calculate_rental_cost(days)}")
print(truck.show_details())
print(f"Total cost for {days} days: Rs.{truck.calculate_rental_cost(days)}")
