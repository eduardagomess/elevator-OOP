from elevator import Elevator


class ElevatorController:

    def _init_(self):
        self.__elevator = None

    def ascendElevator(self,floor):
        return Elevator.ascendElevator(self.__elevator,floor)

    def descendElevator(self,floor):
        return Elevator.descendElevator(self.__elevator,floor)

    def enterInElevator(self):
        return Elevator.enterInElevator(self.__elevator)

    def getOutOftheElevator(self):
        return Elevator.getOutOftheElevator(self.__elevator)

    def initializeElevator(self, capacity, total_floors):
        self.__elevator = Elevator(capacity, total_floors)
        return self.__elevator



