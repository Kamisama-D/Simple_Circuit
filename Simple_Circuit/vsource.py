class Vsource:
    def __init__(self, name:str, bus1:str, v:float):
        self.name = name
        self.bus1 = bus1
        self.v = v

if __name__ == '__main__':
    vsource = Vsource("Source 1", "Main Bus", 150)
    print(f"Voltage at {vsource.bus1} from {vsource.name}: {vsource.v} V")