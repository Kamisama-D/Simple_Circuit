from circuit import Circuit
from solution import Solution

def main():
    my_circuit = Circuit("Simple DC Circuit")
    my_circuit.add_bus("Bus A")
    my_circuit.add_bus("Bus B")
    my_circuit.add_vsource_element("Va", "Bus A", 100)
    my_circuit.add_resistor_element("Rab", "Bus A", "Bus B", 5)
    my_circuit.add_load_element("Lb", "Bus B", 2000, 100)

    solution = Solution(my_circuit)
    solution.do_power_flow()

if __name__ == '__main__':
    main()