class B:
    def __init__(self, B1: int, B2: float):
        self._B1 = B1
        self._B2 = B2

    # Getters
    def get_B1(self) -> int:
        return self._B1

    def get_B2(self) -> float:
        return self._B2

    # Setters
    def set_B1(self, B1: int):
        self._B1 = B1

    def set_B2(self, B2: float):
        self._B2 = B2

    # Métodos
    def MB1(self):
        print("MB1")

    def MB2(self):
        print("MB2")

    def MB3(self):
        print("MB3")

