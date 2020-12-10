class ElevatorMaximumCapacityReached(Exception):
    def __init__(self):
        super().__init__("The elevator has reached its maximum capacity!")