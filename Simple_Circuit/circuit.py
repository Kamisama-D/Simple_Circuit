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
        self.i = 0.0

    def add_bus(self, name:str):
        if name not in self.buses:
            self.buses[name] = Bus(name)

    def add_resistor_element(self, name:str, bus1:str, bus2:str, r:float):
        self.add_bus(bus1)
        self.add_bus(bus2)
        self.resistors[name] = Resister(name, self.buses[bus1], self.buses[bus2], r)

    def add_load_element(self, name:str, bus1:str, p:float, v:float):
        self.add_bus(bus1)
        self.loads[name] = Load(name, self.buses[bus1], p, v)
        self.set_i()
        # V_B = V_load = I * R_load
        self.loads[name].v = self.i * self.loads[name].r
        self.buses[bus1].set_bus_v(self.loads[name].v)

    def add_vsource_element(self, name:str, bus1:str, v:float):
        self.add_bus(bus1)
        self.vsource = Vsource(name, self.buses[bus1], v)
        # V_A = Vsource
        self.buses[bus1].set_bus_v(self.vsource.v)

    def set_i(self):
        # I = Vsource / (R1 + R_load)
        total_resistor = 0.0
        for resistor in self.resistors.values():
            total_resistor += resistor.r
        for load in self.loads.values():
            total_resistor += load.r
        self.i = self.vsource.v / total_resistor

    def print_nodal_voltage(self, bus:str):
        print(f"Voltage at {self.buses[bus].name}: {self.buses[bus].v} V")

    def print_circuit_current(self):
        print(f"Circuit current: {self.i} A")

if __name__ == "__main__":
    my_circuit = Circuit("Test Circuit")
    my_circuit.add_bus("Bus A")
    my_circuit.add_bus("Bus B")
    my_circuit.add_vsource_element("Source 1", "Bus A", 120)
    my_circuit.add_resistor_element("Resistor 1", "Bus A", "Bus B", 50)
    my_circuit.add_load_element("Load 1", "Bus B", 1000,100)
    my_circuit.set_i()
    my_circuit.print_nodal_voltage("Bus A")
    my_circuit.print_nodal_voltage("Bus B")
    my_circuit.print_circuit_current()

    if "Resistor 1" in my_circuit.resistors:
        print(f"Resistance R1 (Resistor 1): {my_circuit.resistors['Resistor 1'].r} ohms")

    if "Load 1" in my_circuit.loads:
        calculated_rload = my_circuit.loads["Load 1"].r
        print(f"Resistance Rload (Load 1): {calculated_rload} ohms")