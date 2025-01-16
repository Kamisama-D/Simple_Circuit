class Register:
    def __init__(self, name, bus1, bus2, r):
        self.name = name
        self.bus1 = bus1
        self.bus2 = bus2
        self.r = r
        self.g = 0.0
        self.calc_g()

    def calc_g(self):
        if self.r != 0:
            self.g = 1 / self.r
        else:
            self.g = float('inf')

if __name__ == '__main__':
    resistor = Register("R1", "Bus A", "Bus B", 5.0)
    print(f"Resistor {resistor.name} has conductance: {resistor.g} S")