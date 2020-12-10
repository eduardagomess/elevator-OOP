class EmptyElevator(Exception):
    def __init__(self):
        super().__init__("The elevator is empty")