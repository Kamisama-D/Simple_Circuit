from bus import Bus
from resistor import Resister
from load import Load
from vsource import Vsource

class Circuit:
    def __init__(self, name:str):
        self.name = name
        self.buses = {}
        self.resistors = {}
        self.loads = {}
        self.vsource = None
        self.i = float

    def add_bus(self, name:str):
        if name not in self.buses:
            self.buses[name] = Bus(name)

    def add_resistor_element(self, name:str, bus1:str, bus2:str, r:float):
        self.resistors[name] = Resister(name, self.buses[bus1], self.buses[bus2], r)

    def add_load_element(self, name:str, bus1:str, p:float, v:float):
        self.loads[name] = Load(name, self.buses[bus1], p, v)

    def add_vsource_element(self, name:str, bus1:str, v:float):
        self.vsource = Vsource(name, self.buses[bus1], v)

    def set_i(self, i:float):
        self.i = i

    def print_nodal_voltage(self):
        for bus_name, bus in self.buses.items():
            print(f"{bus_name} Voltage = {bus.v} V")

    def print_circuit_current(self):
        print(f"Circuit current = {self.i} A")

if __name__ == "__main__":
    my_circuit = Circuit("Test Circuit")
    my_circuit.add_bus("Bus A")
    my_circuit.add_bus("Bus B")
    my_circuit.add_vsource_element("Source 1", "Bus A", 120)
    my_circuit.add_resistor_element("Resistor 1", "Bus A", "Bus B", 50)
    my_circuit.add_load_element("Load 1", "Bus B", 1000,100)
    my_circuit.print_nodal_voltage()
    my_circuit.print_circuit_current()