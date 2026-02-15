

{11}------------------------------------------------

## **Analog-to-Digital Conversion**

**A/D conversion** is an interfacing process often used when a linear **analog** system must provide inputs to a **digital** system.

*Flash* method of A/D conversion uses parallel comparators to compare the linear input signal with various reference voltages developed by a voltage divider.

- When the input voltage exceeds the reference voltage for a given comparator, a high level is produced on that comparator's output.
- 2 n - 1 comparators are required for conversion to an n-digit binary number.

Priority encoder is a digital device that produces a binary number on its output representing the highest value at its input. 3-bit analog-to-digital converter

![](_page_11_Figure_6.jpeg)

using op-amps as comparators.

{12}------------------------------------------------

## **Analog-to-Digital Conversion**

2-bit Analogue to Digital Converter (ADC) circuit is shown in the figure.

This will give us a 2-bit output code for all four possible values of analogue input.

![](_page_12_Figure_3.jpeg)

| Analogue Input<br>Voltage (V <sub>IN</sub> ) | Comparator Outputs |                |                |                | Digital<br>Outputs |       |
|----------------------------------------------|--------------------|----------------|----------------|----------------|--------------------|-------|
|                                              | D <sub>3</sub>     | D <sub>2</sub> | D <sub>1</sub> | D <sub>0</sub> | Q <sub>1</sub>     | $Q_0$ |
| 0 to 1 V                                     | 0                  | 0              | 0              | 0              | 0                  | 0     |
| 1 to 2 V                                     | 0                  | 0              | 1              | Х              | 0                  | 1     |
| 2 to 3 V                                     | 0                  | 1              | Х              | Х              | 1                  | 0     |
| 3 to 4 V                                     | 1                  | X              | X              | Х              | 1                  | 1     |

{13}------------------------------------------------

## **Discussions**

![](_page_13_Picture_1.jpeg)