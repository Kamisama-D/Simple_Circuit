class Bus:
    def __init__(self, name, v = 0.0):
        self.name = name
        self.v = v

    def set_bus_v(self, bus_v):
        self.v = bus_v

if __name__ == '__main__':
    bus = Bus("Bus A")
    print(f"Initial voltage at {bus.name}: {bus.v} V")

    bus.set_bus_v(15.0)
    print(f"Updated voltage at {bus.name}: {bus.v} V")