class ElevatorDownstairs(Exception):
    def __init__(self):
        super().__init__("the elevator is already on the ground floor")