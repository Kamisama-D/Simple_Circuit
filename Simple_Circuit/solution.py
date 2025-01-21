class Solution:
    def __init__(self, circuit):
        self.circuit = circuit

    def do_power_flow(self):
        if self.circuit.vsource:
            # First calculate the current using element conductance values
            self.circuit.set_i()
            self.circuit.print_circuit_current()
            # Then determine the voltage at bus A and B
            self.circuit.print_nodal_voltage("Bus A")
            self.circuit.print_nodal_voltage("Bus B")
