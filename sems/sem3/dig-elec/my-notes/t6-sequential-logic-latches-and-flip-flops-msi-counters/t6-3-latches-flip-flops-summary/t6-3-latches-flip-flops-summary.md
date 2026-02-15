---
title: Sequential circuits Latches & Flip Flops
---

{1}------------------------------------------------

## Objectives

- Recognize different devices
- Understand the difference between Asynchronous and Synchronous devices
- Distinguish between different triggering methods
- Complete Timing diagrams

{2}------------------------------------------------

## Latches

![](_page_2_Picture_1.jpeg)

![](_page_2_Picture_2.jpeg)

![](_page_2_Picture_3.jpeg)

![](_page_2_Picture_4.jpeg)

![](_page_2_Picture_5.jpeg)

| S R | Q                  |
|-----|--------------------|
| 0 0 | Q<br>0             |
| 0 1 | 0                  |
| 1 0 | 1                  |
| 1 1 | Q<br>=<br>Q<br>'=0 |

| S' R' | Q                  |
|-------|--------------------|
| 0 0   | Q<br>=<br>Q<br>'=1 |
| 0 1   | 1                  |
| 1 0   | 0                  |
| 1 1   | Q<br>0             |

| E | S | R | Q           |
|---|---|---|-------------|
| 0 | X | X | NC          |
| 1 | 0 | 0 | NC          |
| 1 | 0 | 1 | 0           |
| 1 | 1 | 0 | 1           |
| 1 | 1 | 1 | Inval<br>id |

| E | D | Q  |
|---|---|----|
| 0 | 0 | NC |
| 0 | 1 | NC |
| 1 | 0 | 0  |
| 1 | 1 | 1  |

{3}------------------------------------------------

## FlipFlops

![](_page_3_Picture_1.jpeg)

![](_page_3_Picture_2.jpeg)

![](_page_3_Picture_3.jpeg)

{4}------------------------------------------------

![](_page_4_Picture_0.jpeg)

## JK Flip Flops

- The Ideal Flip Flop would look like this:
- Edge triggered
- Capable of setting or resetting the output on a clock transition
- Capable of holding a value when not being triggered
- Capable of dividing by 2
- Capable of forcing a set or reset independent of the clock cycle
- No disallowed states

{5}------------------------------------------------

![](_page_5_Picture_0.jpeg)

![](_page_5_Picture_1.jpeg)

![](_page_5_Figure_2.jpeg)

| J | K                | CLK                 | Q                                                                                                                                                       |
|---|------------------|---------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0 | 0                | <b>^</b>            | Q <sub>0</sub> (no change)                                                                                                                              |
| 1 | 0                | \ \ \               | 1                                                                                                                                                       |
| 0 | 1                |                     | 0                                                                                                                                                       |
| 1 | 1                | <del> </del>        | Q <sub>0</sub> (toggles)                                                                                                                                |
|   | J<br>0<br>1<br>0 | J K 0 0 1 0 0 1 1 1 | J         K         CLK           0         0         ↑           1         0         ↑           0         1         ↑           1         1         ↑ |


{6}------------------------------------------------

![](_page_6_Picture_0.jpeg)

## Asynchronous Inputs

- The synchronous control inputs must be used in conjunction with a clock signal to trigger the FF.
- Most clocked FFs also have one or more asynchronous inputs that operate independently of the synchronous inputs and clock input.
- The asynchronous inputs are override inputs, which can be used to override all the other inputs in order to place the FF in one state or the other. The synchronous inputs may be (set, reset, preclear, preset….etc)
- See the D-FF 7474 example next slide where we can force the output into specific values using preset and preclear it will be asynchronous

{7}------------------------------------------------

![](_page_7_Picture_0.jpeg)

## Truth Table for Preset and Preclear Pins

• Here's the Truth Table for the Preset and Preclear pins:

| Inputs |     | Outputs        |                |
|--------|-----|----------------|----------------|
| PR     | CLR | Q              | $\overline{Q}$ |
| 0      | 0   | Disallowed     |                |
| 0      | 1   | 1              | 0              |
| 1      | 0   | 0              | 1              |
| 1      | 1   | Normal Clocked |                |
|        |     | Operation      |                |

![](_page_7_Picture_4.jpeg)

• The **PR** and **CLR** pins are referred to as asynchronous because they are independent of the clock.

{8}------------------------------------------------

![](_page_8_Picture_0.jpeg)

## Block Diagram and Truth Table of JK-FF

![](_page_8_Picture_2.jpeg)

| Inputs |   |       | Outputs                              |                |  |
|--------|---|-------|--------------------------------------|----------------|--|
| J      | K | Clock | Q                                    | $\overline{Q}$ |  |
| 0      | 0 |       | No Change to Outputs                 |                |  |
| 0      | 1 |       | 0                                    | 1              |  |
| 1      | 0 |       | 1                                    | 0              |  |
| 1      | 1 |       | Outputs Toggle                       |                |  |
|        |   |       | (Q and $\overline{Q}$ change states) |                |  |
| X      | X | l     | No Change to Outputs                 |                |  |

{9}------------------------------------------------

![](_page_9_Picture_0.jpeg)

## Asynchronous JK-FF/Adding Set and Reset to JK-FF

- A fully equipped JK flip flop has two more inputs (**Set** and **Reset)** which allow the user to force the output to 1 or 0 at any time, regardless of **Clock**.
- For normal clocked operation (as above) where we are using the **J** and **K** inputs, both **Set** and **Reset** must be maintained in their inactive states.
- You are not allowed to activate both **Set** and **Reset** simultaneously this is a disallowed state which yields unreliable results

| Inputs |       | Outputs                                            |                                 |  |
|--------|-------|----------------------------------------------------|---------------------------------|--|
| Set    | Reset | Q                                                  | $\overline{\overline{\varrho}}$ |  |
| 0      | 0     | Normal Clocked Operation<br>Utilizing J and K Pins |                                 |  |
| 0      | 1     | 0                                                  | 1                               |  |
| 1      | 0     | 1                                                  | 0                               |  |
| 1      | 1     | Disallowed                                         |                                 |  |

![](_page_9_Picture_6.jpeg)

{10}------------------------------------------------

# Two Cascaded Stages of D-Flip Flops

![](_page_10_Picture_1.jpeg)

- Notice how the output only changes on a positive clock transition.
- Q1 is ½ the clock frequency.
- Q2 is ¼ the clock frequency.

![](_page_10_Picture_5.jpeg)

![](_page_10_Figure_6.jpeg)



{11}------------------------------------------------

![](_page_11_Picture_0.jpeg)

## Cascaded JK-Flip Flops

![](_page_11_Figure_2.jpeg)

{12}------------------------------------------------

![](_page_12_Picture_0.jpeg)

## Using a JK Flip Flop as a D-Flip Flop

![](_page_12_Picture_5.jpeg)

| Inputs |       | Outputs              |                           |
|--------|-------|----------------------|---------------------------|
| D      | Clock | Q                    | $\overline{oldsymbol{Q}}$ |
| 0      |       | 0                    | 1                         |
| 1      |       | 1                    | 0                         |
| X      |       | No Change to Outputs |                           |

{13}------------------------------------------------

![](_page_13_Picture_0.jpeg)

## Example

• Find the output waveform of J-K FF

![](_page_13_Figure_3.jpeg)

{14}------------------------------------------------

![](_page_14_Picture_0.jpeg)

## Example

• Solution

![](_page_14_Figure_3.jpeg)
