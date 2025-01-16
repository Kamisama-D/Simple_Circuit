from bus import Bus

class Vsource:
    def __init__(self, name, bus1, v):
        self.name = name
        self.bus1 = bus1
        self.v = v
        self.bus1.set_bus_v(self.v)

if __name__ == '__main__':
    bus = Bus("Main Bus")
    vsource = Vsource("Source 1", bus, 150)
    print(f"Voltage at {bus.name} from {vsource.name}: {bus.v} V")