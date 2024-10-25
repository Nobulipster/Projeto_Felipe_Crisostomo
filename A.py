class A:
    def __init__(self, A1: int, A2: float):
        self._A1 = A1
        self._A2 = A2

    # Getters
    def get_A1(self) -> int:
        return self._A1

    def get_A2(self) -> float:
        return self._A2

    # Setters
    def set_A1(self, A1: int):
        self._A1 = A1

    def set_A2(self, A2: float):
        self._A2 = A2

    # Métodos
    def MA1(self):
        print("MA1")

    def MA2(self):
        print("MA2")

    def MA3(self):
        print("Alteração a classe A partir do clone")

