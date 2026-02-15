

{0}------------------------------------------------

![](_page_0_Picture_0.jpeg)

# AETN 2101-ANALOG ELECTRONICS

**L6.3**

**Op-Amp Applications**

**Dr. Yasen Harrye**

{1}------------------------------------------------

## **Learning Objectives:**

Understand the operation of OP-AMP as comparator

Develop an understanding of analog-to-digital conversion techniques

Develop an understanding of digital-to-analog conversion techniques

{2}------------------------------------------------

A comparator circuit is used to compare two input signals, and indicates at the output which input has the larger signal.

A comparator circuit accepts input of linear voltages and provides a digital output that indicates when one input is less than or greater than the second.

A basic comparator circuit can be represented as

![](_page_2_Figure_4.jpeg)

![](_page_2_Figure_5.jpeg)

If the **non-inverting input** is higher than the inverting input, the output of the amplifier will saturate at the **positive** supply voltage.

If the **inverting input** is higher than the non-inverting input, the output of the amplifier will saturate at the **negative** supply voltage.

{3}------------------------------------------------

Here the reference voltage is connected to the inverting input.

$$V_{\text{ref}} = \frac{10 \text{ k}\Omega}{10 \text{ k}\Omega + 10 \text{ k}\Omega} (+12 \text{ V}) = +6 \text{ V}$$

The output will switch to its positive saturation level when the input *V<sup>i</sup>* goes more positive than the +6V reference voltage level.

![](_page_3_Figure_4.jpeg)

{4}------------------------------------------------

What is the reference voltage for each comparator in the following figure?

![](_page_4_Picture_2.jpeg)

{5}------------------------------------------------

In digital circuitry the signals are at either one of the two levels, representing the binary values of 1 or 0.

An analog–digital converter (ADC) obtains a digital value representing an input analog voltage.

A digital–analog converter (DAC) changes a digital value back into an analog voltage.