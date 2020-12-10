from elevatorMaximumCapacityReached import ElevatorMaximumCapacityReached
from emptyElevator import EmptyElevator
from elevatorDownstairs import ElevatorDownstairs
from elevatorTopFloor import ElevatorTopFloor

class Elevator:
    def __init__(self, capacity, total_floors, elevator_floor = 0, amount_of_people = 0):
        self.elevator_floor = elevator_floor
        self.amount_of_people = amount_of_people
        self.__capacity = capacity
        self.__total_floors = total_floors

    @property
    def elevatorFloor(self):
        return self.elevator_floor

    @property
    def amountOfPeople(self):
        return self.amount_of_people

    def enterInElevator(self):
        if self.amount_of_people <= self.__capacity:
            self.amount_of_people += 1
            return self.amount_of_people
        raise ElevatorMaximumCapacityReached

    def getOutOftheElevator(self):
        if self.amount_of_people > 0:
            self.amount_of_people -= 1
            return self.amount_of_people
        raise EmptyElevator

    def ascendElevator(self, floor):
        if floor < self.__total_floors:
            self.elevator_floor = floor
            return self.elevator_floor
        raise ElevatorTopFloor

    def descendElevator(self, floor):
        if floor > 0:
            self.elevator_floor = floor
            return self.elevator_floor
        raise ElevatorDownstairs



