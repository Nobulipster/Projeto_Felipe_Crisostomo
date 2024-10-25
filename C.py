class C:
    def __init__(self, C1: str, C2: int):
        self._C1 = C1
        self._C2 = C2

    # Getters
    def get_C1(self) -> str:
        return self._C1

    def get_C2(self) -> int:
        return self._C2

    # Setters
    def set_C1(self, C1: str):
        self._C1 = C1

    def set_C2(self, C2: int):
        self._C2 = C2

    # Métodos
    def MC1(self):
        print("MC1")

    def MC2(self):
        print("MC2")

    def MC3(self):
        print("MC3")
