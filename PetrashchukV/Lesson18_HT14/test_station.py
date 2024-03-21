import pytest
from main_code import Passenger, TrainCar, Train, Station

@pytest.fixture
def setup_passengers():
    passenger1 = Passenger("John Dow", "Station A", 1)
    passenger2 = Passenger("Alex Dowson", "Station B", 2)
    passenger3 = Passenger("Emily Watson", "Station C", 3)
    return passenger1, passenger2, passenger3

@pytest.fixture
def setup_train_cars():
    car1 = TrainCar("1")
    car2 = TrainCar("2")
    return car1, car2

@pytest.fixture
def setup_train():
    train = Train("London-Gogwarts")
    return train

@pytest.fixture
def setup_stations():
    station1 = Station("London")
    station2 = Station("Gogwarts")
    station3 = Station("Hogsmeade")
    return station1, station2, station3

@pytest.mark.parametrize("name, destination, seat", [
    ("John Dow", "Station A", 1),
    ("Alex Dowson", "Station B", 2),
    ("Emily Watson", "Station C", 3),
])
def test_passenger_str(name, destination, seat):
    passenger = Passenger(name, destination, seat)
    assert str(passenger) == f"Passenger: {name}\nDestination: {destination}\nSeat: {seat}"

def test_train_car_add_passenger(setup_passengers, setup_train_cars):
    passenger1, passenger2, _ = setup_passengers
    car1, car2 = setup_train_cars

    car1.add_passenger(passenger1)
    assert len(car1) == 1
    assert car1.passengers[0] == passenger1

    car1.add_passenger(passenger2)
    assert len(car1) == 2
    assert car1.passengers[1] == passenger2

def test_train_add_car(setup_train, setup_train_cars):
    train = setup_train
    car1, car2 = setup_train_cars

    train.add_car(car1)
    train.add_car(car2)

    assert len(train.cars) == 2
    assert train.cars[0] == car1
    assert train.cars[1] == car2

def test_train_run(setup_train, setup_stations):
    train = setup_train
    station1, station2, station3 = setup_stations

    train.add_station(station1)
    train.add_station(station2)
    train.add_station(station3)

    # Mocking board_passengers method as it interacts with console
    station1.board_passengers = lambda: None
    station2.board_passengers = lambda: None
    station3.board_passengers = lambda: None

    train.run()

@pytest.mark.parametrize("name", [
    "London",
    "Gogwarts",
    "Hogsmeade",
])
def test_station_str(name):
    station = Station(name)
    assert str(station) == name
