# Simple_Circuit_Simulator
 
### 1. Project Overview

#### 1.1 Introduction
The Simple Circuit Simulator (SCS) is a Python-based tool designed to model and solve a direct current (DC) circuit that includes a voltage source, a series resistor, and a load resistor connected between buses A and B, as shown in [Figure 1](https://github.com/Kamisama-D/Simple_Circuit/blob/main/Simple%20Circuit.png). The purpose of this simulator is to facilitate the analysis of the DC circuit. 

**Key features and functionalities of this simulator include:**
- **Model DC Circuit:** Users can construct simple DC circuits by adding multiple circuit elements such as voltage source, buses, resistors, and load and specifying component values.
- **Solve DC Circuit:** The simulator calculates and displays the voltage at each bus and the current flowing through the circuit, providing instant output on the circuit's behavior.

<img src="/Simple%20Circuit.png" alt="Figure 1. Schematic of the DC Circuit" width="600"/>


#### 1.2 Problem Solving and Real-World Applications
The SCS provides a virtual environment where users can experiment with circuit configurations and instantly observe the outcomes. Its real-world applications are:
- **Educational Tools:** Acts as a teaching aid in classrooms to demonstrate the fundamental principles of DC circuit design and analysis.
- **Prototype Testing:** Allows engineers to test DC circuit configurations before building physical prototypes, saving time and resources.
- **Troubleshooting:** Helps in diagnosing issues with DC circuit designs by allowing for hypothetical modifications and observing potential impacts on circuit functionality.

### 2. Class Diagrams
[Figure 2](https://github.com/Kamisama-D/Simple_Circuit/blob/main/diagram.png) shows the class diagrams of the SCS. The diagrams are generated using the [diagram.puml](https://github.com/Kamisama-D/Simple_Circuit/blob/main/Simple_Circuit/diagram.puml) file, which is processed by the PlantUML plugin in PyCharm.

<img src="/diagram.png" alt="Figure 2. Diagram of the DC Circuit" width="600"/>

### 3. Relevant Equations
The equations used in the SCS include Ohm’s law, power-voltage relationship, conductance calculations, and KVL to solve for circuit voltages and current.

#### 3.1 Ohm’s Law
Ohm's Law is for determining the current flowing through a component in an electrical circuit. It is expressed as: 
```
I = V / R
```
where `I` is the current through the component (in amperes, A), `V` is the voltage across the component (in volts, V), and `R` is the resistance of the component (in ohms, Ω).

#### 3.2 Power-Voltage Relationship
The power consumed by a component in a DC circuit can be calculated using the power-voltage relationship, which is given by: 
```
P = V * I
```
where `P` is the power (in watts, W), `I` is the current through the component (in amperes, A), and `V` is the voltage across the component (in volts, V).  
By combining Ohm’s law and power-voltage relationship, the resistance `R` of a component can be calculated using its voltage `V` and power `P`: 
```
R = V^2 / P
```

#### 3.3 Conductance Calculations
The conductance of a component is the inverse of its resistance: 
```
G = 1 / R
```
where `G` is the conductance (in siemens, S), and `R` is the resistance of the component (in ohms, Ω).

#### 3.4 Kirchhoff’s Voltage Law (KVL) to Solve for System Voltages and Current
KVL ensures the sum of the voltage drops around the circuit equals the voltage of the source. KVL can be represented as: 
```
V_source = V_1 + V_2 = I * R_1 + I * R_2
```
where `V_source` is the voltage of the source, `I` is the current,  `V_1`, `V_2` are voltages of all the other components of the circuit, and `R_1`, `R_2` are the resistors. 

### 4. Example Case

#### 4.1 Problem Definition
The circuit in [Figure 1](https://github.com/Kamisama-D/Simple_Circuit/blob/main/Simple%20Circuit.png) is defined as:
- Buses A and B are added to the circuit.
- Voltage source `V_a` is connected at bus A with `120 V`.
- Resistor `R_ab` is connected between buses A and B with `50 Ohms`.
- Load `L_b` is connected to bus B with power `P = 1000 W` and nominal voltage of `V_load= 100 V`. The load model is constant impedance.

The problem is to solve the current of the circuit, and the voltages of bus A and B.

#### 4.2 Solution Process
The solution details are in the `Solution` class in [solution.py](https://github.com/Kamisama-D/Simple_Circuit/blob/main/Simple_Circuit/solution.py) file. The total resistance along the circuit is computed by summing the resistances of the resistor element and the load element: 
```
R_total = R_ab + R_load = R_ab + V_load^2 / P = 50 + 100^2 / 1000 = 60 Ohms
```

Using Ohm's Law, the current (`I`) flowing through the circuit is calculated as: 
```
I = V_a / R_total = 120 / 60 = 2 A
```

The voltage at bus A (`V_busA`) is set equal to the source voltage since it is directly connected to the voltage source: 
```
V_busA = V_a = 120 V
```

The voltage at bus B (`V_busB`) is calculated using the current through the circuit and the resistance of the load: 
```
V_busB = I * R_load = 2 × 10 = 20 V
```


#### 4.3 Expected Output
In the [main.py](https://github.com/Kamisama-D/Simple_Circuit/blob/main/Simple_Circuit/main.py) file, create a DC circuit instance `my_circuit` named “Simple DC Circuit” and add variables using the given example:
```
def main():
    my_circuit = Circuit("Simple DC Circuit")
    my_circuit.add_bus("Bus A")
    my_circuit.add_bus("Bus B")
    my_circuit.add_vsource_element("Va", "Bus A", 120)
    my_circuit.add_resistor_element("Rab", "Bus A", "Bus B", 50)
    my_circuit.add_load_element("Lb", "Bus B", 1000, 100)
```

Next, pass the created circuit `my_circuit` to the `Solution` class and call `the do_power_flow()` function to solve the problem:
```
    solution = Solution(my_circuit)
    solution.do_power_flow()
```

Then, run the `main()` function:
```
if __name__ == '__main__':
    main()
```

Finally, the expected output would be displayed:
```
Circuit Current = 2.0 A
Bus A Voltage = 120.0 V
Bus B Voltage = 20.0 V
```

