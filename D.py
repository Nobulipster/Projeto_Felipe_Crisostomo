class D:
    def __init__(self, D1: int, D2: str):
        self._D1 = D1
        self._D2 = D2

    # Getters
    def get_D1(self) -> int:
        return self._D1

    def get_D2(self) -> str:
        return self._D2

    # Setters
    def set_D1(self, D1: int):
        self._D1 = D1

    def set_D2(self, D2: str):
        self._D2 = D2

    # Métodos
    def MD1(self):
        print("MD1")

    def MD2(self):
        print("MD2")

    def MD4(self):
        print("MD4")
