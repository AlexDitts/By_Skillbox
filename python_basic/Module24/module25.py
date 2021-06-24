class Auto:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

class Bus(Auto):
    def __init__(self, a, b, c):
        super().__init__(a, b)
