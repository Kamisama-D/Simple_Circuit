class Resister:
    def __init__(self, name:str, bus1:str, bus2:str, r:float):
        self.name = name
        self.bus1 = bus1
        self.bus2 = bus2
        self.r = r
        self.g = float
        self.calc_g()

    def calc_g(self):
        if self.r > 0:
            self.g = 1 / self.r
        else:
            self.g = float('inf')

if __name__ == '__main__':
    resistor = Resister("R1", "Bus A", "Bus B", 5.0)
    print(f"Resistor {resistor.name} has resistance: {resistor.r} ohm")
    print(f"Resistor {resistor.name} has conductance: {resistor.g} S")