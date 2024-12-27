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
    
def main():
    walk = Walk("Home", "Park", 2)

    print(f"Walk cost: {walk.calculate_cost()} Baht")


if __name__ == "__main__":
    main()
