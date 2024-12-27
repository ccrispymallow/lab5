from abc import ABC, abstractmethod

class Transportation(ABC):
    def __init__(self, start_place, end_place, distance):
        self.start_place = start_place
        self.end_place = end_place
        self.distance = distance

    @abstractmethod
    def calculate_cost(self):
        pass

class Walk(Transportation):
    def __init__(self, start_place, end_place, distance):
        super().__init__(start_place, end_place, distance)

    def calculate_cost(self):
        return 0

class Taxi(Transportation):
    def __init__(self, start_place, end_place, distance):
        super().__init__(start_place, end_place, distance)

    def calculate_cost(self):
        return 40*self.distance
    
class Train(Transportation):
    def __init__(self, start_place, end_place, distance, stations):
        super().__init__(start_place, end_place, distance)
        self.stations = stations
    def calculate_cost(self):
        return 5 * self.stations
    
def main():
    walk = Walk("Home", "Park", 2)
    taxi = Taxi("Home", "Airport", 10)
    train = Train("Station A", "Station B", 15, 5)

    print(f"Walk cost: {walk.calculate_cost()} Baht")
    print(f"Taxi cost: {taxi.calculate_cost()} Baht")
    print(f"Train cost: {train.calculate_cost()} Baht")


if __name__ == "__main__":
    main()