class cars:
    def __init__(self, make, model, year, price, amount):
        self.make = make
        self.model = model
        self.year = year
        self.price = price
        self.amount = amount
        if amount > 0:
            self.available = True
        else:
            self.avalible - False
        
    def __str__(self):
        return f"{self.year} {self.make} {self.model} - ${self.price} ({self.amount} available)"
    
    def sell(self, amount):
        if self.available:
            if amount <= self.amount:
                self.amount -= amount
                print(f"Sold {amount} {self.make} {self.model}(s). {self.amount} left.")
            else:
                print(f"Not enough stock. Only {self.amount} available.")
        else:
            print(f"{self.make} {self.model} is not available for sale.")
        
    def restock(self, amount):
        self.amount += amount
        print(f"Restocked {amount} {self.make} {self.model}(s). Total available: {self.amount}.")

    
class users:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.purchased_cars = []
    
    def __str__(self):
        return f"User {self.user_id}: {self.name}"
    
    def purchaseCar(self, car, amount):
        if car.available:
            car.sell(amount)
            self.purchased_cars.append(car)
        else:
            print(f"{car.make} {car.model} is not available for sale.")


class dealership:
    def __init__(self):
        self.cars = []
        self.users = []
    
    def addCar(self, car):
        self.cars.append(car)
        print(f"Added {car.make} {car.model} to the dealership.")
    
    def addUser(self, user):
        self.users.append(user)
        print(f"Added user {user.name} to the dealership.")
    
    def showCars(self):
        print("Available cars:")
        for car in self.cars:
            print(car)
        

car1 = cars("Toyota", "Camry", 2020, 24000, 10)
car2 = cars("Honda", "Civic", 2021, 22000, 5)
car3 = cars("Ford", "Mustang", 2022, 30000, 2)

user1 = users("Alice", 1)
user2 = users("Bob", 2)
user3 = users("Charlie", 3)

user1.purchaseCar(car1, 10)

dealership1 = dealership()
dealership1.addCar(car1)
dealership1.addCar(car2)
dealership1.addCar(car3)
dealership1.addUser(user1)
dealership1.addUser(user2)
dealership1.addUser(user3)

dealership1.showCars()



