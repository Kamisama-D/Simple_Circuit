class Load:
    def __init__(self, name:str, bus1:str, p:float, v:float):
        self.name = name
        self.bus1 = bus1
        self.p = p
        self.v = v
        self.r = float
        self.g = float
        self.calc_g()

    def calc_g(self):
        # R = V^2 / P, G = 1 / R
        if self.p > 0.0 and self.v > 0.0:
            self.r = (self.v ** 2) / self.p
            self.g = 1 / self.r

if __name__ == '__main__':
    load = Load("Load 1", "Main Bus", 1000, 500)
    print(f"{load.name} has resistance: {load.r} ohm")
    print(f"{load.name} has conductance: {load.g} S")