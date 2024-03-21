class Passenger:
    def __init__(self, name, destination, seat):
        self.name = name
        self.destination = destination
        self.seat = seat

    def __str__(self):
        return f"Passenger: {self.name}\nDestination: {self.destination}\nSeat: {self.seat}"


class TrainCar:
    def __init__(self, number, capacity=10):
        self.number = number
        self.capacity = capacity
        self.passengers = []

    def __len__(self):
        return len(self.passengers)

    def add_passenger(self, passenger):
        if len(self.passengers) < self.capacity:
            self.passengers.append(passenger)
            print(f"{passenger.name} boarded the train.")

    def __str__(self):
        car_info = [f"\"traincart\": \"{self.number}\""]
        for idx, passenger in enumerate(self.passengers, start=1):
            car_info.append(f"\"passenger_name\": \"{passenger.name}\",")
            car_info.append(f"\"destination\": \"{passenger.destination}\",")
            car_info.append(f"\"place\": {idx}")
        return "\n".join(car_info)


class Train:
    def __init__(self, route):
        self.route = route
        self.cars = []
        self.stations = []

    def add_car(self, car):
        self.cars.append(car)

    def add_station(self, station):
        self.stations.append(station)

    def run(self):
        for station in self.stations:
            print(f"Train arrived at station: {station}")
            station.board_passengers()

    def __str__(self):
        return f"Train on route: {self.route}\nNumber of stations: {len(self.stations)}"


class Station:
    def __init__(self, name):
        self.name = name
        self.boarding_passengers = []

    def add_boarding_passenger(self, passenger):
        self.boarding_passengers.append(passenger)

    def board_passengers(self):
        for passenger in self.boarding_passengers:
            print(f"{passenger.name} boards the train at station {self.name}.")

    def __str__(self):
        return self.name

passenger1 = Passenger("John Dow", "Station A", 1)
passenger2 = Passenger("Alex Dowson", "Station B", 2)
passenger3 = Passenger("Emily Watson", "Station C", 3)

car1 = TrainCar("1")
car1.add_passenger(passenger1)
car1.add_passenger(passenger2)

car2 = TrainCar("2")
car2.add_passenger(passenger3)

train = Train("London-Gogwarts")
train.add_car(car1)
train.add_car(car2)

print("\nTrain:")
print(train)
train.run()

station1 = Station("London")
station2 = Station("Gogwarts")
station3 = Station("Hogsmeade")

station1.add_boarding_passenger(Passenger("John Dow", station2, 1))
station1.add_boarding_passenger(Passenger("Alex Dowson", station2, 2))
station2.add_boarding_passenger(Passenger("Emily Watson", station3, 3))

train.add_station(station1)
train.add_station(station2)
train.add_station(station3)
train.run()

