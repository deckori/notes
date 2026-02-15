

{0}------------------------------------------------

![](_page_0_Picture_0.jpeg)

# **AETN 2201 Analog Electronics**

**Fall 2025 Project**

 **10% of overall score**

# **Shunt Current Sensing Using Op Amp with Zener Protection and LED Indicators**

**Submission deadline: 29/11/2025at 11:59pm**

{1}------------------------------------------------

## **1. Introduction**

This laboratory project involves design, implementation, and analysis of a current sensing circuit using a shunt resistor and operational amplifier configuration. It should be enhanced with Zener diode protection and LED indicators to create a practical current monitoring system with visual feedback and circuit protection.

## **2. Objectives**

- Design and implement a shunt resistor-based current sensing circuit.
- Understand the operation of operational amplifiers in differential amplification.
- Implement Zener diode protection for overvoltage conditions.
- Create LED indicator circuits for visual current level monitoring.
- Analyze circuit performance, accuracy, and limitations.
- Develop troubleshooting and measurement skills.

### **3. Theoretical Background**

### **3.1 Shunt Current Sensing Principles**

Current sensing using a shunt resistor relies on Ohm's Law (V = IR). By placing a small-value resistor in series with the load, the current flowing through the circuit creates a proportional voltage drop across the resistor. This voltage can be measured and amplified to determine the current magnitude.

### **3.2 Operational Amplifier Configurations**

The differential amplifier configuration is ideal for current sensing applications as it can amplify the small voltage difference across the shunt resistor while rejecting common-mode noise.

## **3.3 Zener Diodes**

Zener diodes operate in reverse breakdown mode to establish a fixed voltage. They can be used for voltage regulation and protection against transients by clamping voltages to their breakdown value.

### **3.4 LED Indicators**

LEDs provide visual indication of circuit conditions. By connecting LEDs to comparator outputs, we can create visual representations of current levels and alert conditions.

{2}------------------------------------------------

## **4. Shunt Current Sensing Project - Group Assignment Variations**

| Group | Shunt<br>Resistor<br>Value | Op-Amp<br>Type | Zener<br>Diode<br>Voltage | Current<br>Range | Fault<br>Condition | Operating<br>Parameters | Indicator                                        |
|-------|----------------------------|----------------|---------------------------|------------------|--------------------|-------------------------|--------------------------------------------------|
| 1     | 0.1Ω                       | LM358          | 5.1V                      | 0-1A             | 0-1A               | >1.2A                   | Green LED<br>for normal,<br>Red LED<br>for fault |
| 2     | 0.5Ω                       | LM324          | 12V                       | 0-<br>500mA      | 0-500mA            | >550mA                  | Green LED<br>for normal,<br>Red LED<br>for fault |
| 3     | 0.01Ω                      | LM358          | 3.3V                      | 0-5A             | 0-5A               | >1A                     | Green LED<br>for normal,<br>Red LED<br>for fault |
| 4     | 1.0Ω                       | LM324          | 6.8V                      | 0-<br>100mA      | 0-100mA            | >120mA                  | Green LED<br>for normal,<br>Red LED<br>for fault |
| 5     | 0.22Ω                      | LM358          | 15V                       | 0-2A             | 0-2A               | >2.5A                   | Green LED<br>for normal,<br>Red LED<br>for fault |
| 6     | 0.05Ω                      | LM324          | 4.7V                      | 0-3A             | 0-3A               | >3.5A                   | Green LED<br>for normal,<br>Red LED<br>for fault |
| 7     | 0.33Ω                      | LM358          | 9.1V                      | 0-<br>750mA      | 0-750mA            | >800mA                  | Green LED<br>for normal,<br>Red LED<br>for fault |
| 8     | 0.47Ω                      | LM324          | 10V                       | 0-<br>250mA      | 0-250mA            | >300mA                  | Green LED<br>for normal,<br>Red LED<br>for fault |
| 9     | 0.03Ω                      | LM358          | 7.5V                      | 0-8A             | 0-8A               | >1A                     | Green LED<br>for normal,<br>Red LED<br>for fault |
| 10    | 0.68Ω                      | LM324          | 5.6V                      | 0-<br>150mA      | 0-150mA            | >175mA                  | Green LED<br>for normal,<br>Red LED<br>for fault |

### **5. Resources and requirements**

- a) Set Range as directed by your instructor.
- b) LED currents must be within **10% of desired value** by designing the appropriate resistor for the LED colour (note that each colour LED has a different forward voltage, you may have to measure this voltage

{3}------------------------------------------------

c) Report and Data required

## **A 15 to 20-page main text report must be submitted through D2L (Please see attached report format) and should include**

- Circuit design with precise threshold detection for fault conditions
- Mathematical analysis of the current sensing circuit
- Calibration procedure for accurate fault detection
- Error analysis and sensitivity calculations
- Response time analysis for fault detection
- Power supply requirements analysis
- Component tolerance impact assessment
- A 20 page report with all test procedures uploaded to d2l (deadline 29/11/2025)

### **Procedure:**

- 1. Start your understanding of the op-amp based shunt current sensor design research using the links below:
  - - [https://labprojectsbd.com/2020/05/09/dc-current-measurement-using](https://labprojectsbd.com/2020/05/09/dc-current-measurement-using-shunt-resistor-and-op-amp-circuit/)[shunt-resistor-and-op-amp-circuit/](https://labprojectsbd.com/2020/05/09/dc-current-measurement-using-shunt-resistor-and-op-amp-circuit/)
  - -<https://www.youtube.com/watch?v=keMtqf4LPVc>