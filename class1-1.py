class Member:

    def __int__(self, no: int, name: str, weight: float) -> None:
        self.no = no
        self.name = name
        self.weight = weight

    def print(self) -> None:
        print("{}: {} {}kg".format(self.no, self.name, self.weight))
    
yamada = Member(15, "山田太郎", 72.7)
sekine = Member(37, "関根信", 65.3)

yamada.print()
sekine.print()