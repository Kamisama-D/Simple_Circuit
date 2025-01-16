import math
from bus import Bus

class Load:
    def __init__(self, name, bus1, p, q):
        self.name = name
        self.bus1 = bus1
        self.p = p
        self.q = q
        self.g = 0.0
        self.calc_g()

    def calc_g(self):
        v = self.bus1.v
        s = math.sqrt(self.p ** 2 + self.q ** 2) # apparent power
        if s != 0 and v != 0:
            z = v ** 2 / s # impedance
            self.g  = 1 / z # conductance
        else:
            self.g = float('inf')

if __name__ == '__main__':
    bus = Bus("Main Bus", 150)
    load = Load("Load 1", bus, 1000, 500)
    print(f"{load.name} has conductance: {load.g} S")