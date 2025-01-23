class Solution:
    def __init__(self, circuit):
        self.circuit = circuit

    def do_power_flow(self):

        # Calculate the current using element conductance values
        r_ab = sum(resistor.r for resistor in self.circuit.resistors.values())
        r_load = sum(load.r for load in self.circuit.loads.values())
        if (r_ab + r_load) > 0:
            i = self.circuit.vsource.v / (r_ab + r_load) # I = Vsource / (R1 + R_load)
            self.circuit.set_i(i)
        self.circuit.print_circuit_current()

        # Determine the voltage at bus A and B
        bus_list = list(self.circuit.buses)
        bus1 = bus_list[0]
        bus2 = bus_list[1]

        v_a = self.circuit.vsource.v # V_A = Vsource
        self.circuit.buses[bus1].set_bus_v(v_a)

        v_b = self.circuit.i * r_load # V_B = V_load = I * R_load
        self.circuit.buses[bus2].set_bus_v(v_b)

        self.circuit.print_nodal_voltage()