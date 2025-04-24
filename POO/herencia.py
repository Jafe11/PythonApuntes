class vehicle:
    def __init__(self, make, model, price):
        self.make = make
        self.model = model
        self.price = price
        self.available = True
    
    def sell(self):
        if self.available:
            self.available = False
            print(f"Sold {self.make} {self.model}.")
        else:
            print(f"{self.make} {self.model} is not available for sale.")
    
    def check_availability(self):
        return self.available
    
    def get_price(self):
        return self.price
    
    def start_engine(self):
        raise NotImplementedError("Subclasses must implement this method")
    
    def stop_engine(self):
        raise NotImplementedError("Subclasses must implement this method")

class car(vehicle):
    def start_engine(self):
        if not self.available:
            return f"Starting engine of the car {self.make} {self.model}."
        else:
            return f"the car {self.make} {self.model} is not available."
    
    def stop_engine(self):
        if not self.available:
            return f"Stopping engine of the car {self.make} {self.model}."
        else:
            return f"the car {self.make} {self.model} is not available."

class bike(vehicle):
    def start_engine(self):
        if not self.available:
            return f"the bike {self.make} {self.model} is in march"
        else:
            return f"the bike {self.make} {self.model} is not available."
        
    def stop_engine(self):
        if not self.available:
            return f"stopping the bike {self.make} {self.model}."
        else:
            return f"the bike {self.make} {self.model} is not available."

class truck(vehicle):
    def start_engine(self):
        if not self.available:
            return f"the truck {self.make} {self.model} is in march"
        else:
            return f"the truck {self.make} {self.model} is not available."
        
    def stop_engine(self):
        if not self.available:
            return f"stopping the truck {self.make} {self.model}."
        else:
            return f"the truck {self.make} {self.model} is not available."

class customer:
    def __init__(self, name):
        self.name = name
        self.purchased_vehicles = []
    
    def buy_vehicles(self, vehicle: vehicle):
        if vehicle.check_availability():
            vehicle.sell()
            self.purchased_vehicles.append(vehicle)
            print(f"{self.name} purchased {vehicle.make} {vehicle.model}.")
        else:
            print(f"{vehicle.make} {vehicle.model} is not available for sale.")
    
    def inquire_vehicles(self, vehicle: vehicle):
        if vehicle.check_availability():
            print(f"{vehicle.make} {vehicle.model} is available for sale.")
        else:
            print(f"{vehicle.make} {vehicle.model} is not available for sale.")

class dealership:
    def __init__(self):
        self.vehicles = []
        self.customers = []
    
    def add_vehicle(self, vehicle: vehicle):
        self.vehicles.append(vehicle)
        print(f"Added {vehicle.make} {vehicle.model} to the dealership.")
    
    def add_customer(self, customer: customer):
        self.customers.append(customer)
        print(f"Added customer {customer.name} to the dealership.")

    def show_vehicles(self):
        if self.vehicles:
            print("Available vehicles:")
            for vehicle in self.vehicles:
                print(f"{vehicle.make} {vehicle.model} - ${vehicle.price}")
        else:
            print("No vehicles available in the dealership.")

car1 = car("Toyota", "Corolla", 20000)
bike1 = bike("Yamaha", "YZF-R3", 5000)
truck1 = truck("Ford", "F-150", 30000)

customer1 = customer("John Doe")

dealership = dealership()
dealership.add_vehicle(car1)
dealership.add_vehicle(bike1)
dealership.add_vehicle(truck1)
dealership.add_customer(customer1)

dealership.show_vehicles()

customer1.inquire_vehicles(car1)

customer1.buy_vehicles(car1)

