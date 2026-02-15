

{6}------------------------------------------------

**D/A conversion** is an important interface process for converting digital signals to analog (linear) signals.

One method of D/A conversion uses a scaling adder with input resistor values that represent the binary weights of the digital input code.

A more common method for D/A conversion is known as the R-2R ladder method.

{7}------------------------------------------------

Following figure shows a four-digit digital-to-analog converter (DAC).

- The switch symbols represent transistor switches for applying each of the four binary digits to the inputs.
- The lowest-value resistor R corresponds to the highest weighted binary input (2<sup>3</sup> ). All of the other resistors are multiples of R and correspond to the binary weights 2<sup>2</sup> , 2<sup>1</sup> , and 2<sup>0</sup> .

![](_page_7_Figure_4.jpeg)

A scaling adder as a four-digit digital-to-analog converter (DAC).

{8}------------------------------------------------

Determine the output voltage of the DAC in following figure for digital inputs:

- a. 0011
- b. 1101

Assume a binary 1 is represented by 5V and binary 0 is represented by 0V.

a. 
$$V_{out} = -\left(\frac{R_f}{R_1}D_0 + \frac{R_f}{R_2}D_1 + \frac{R_f}{R_3}D_2 + \frac{R_f}{R_4}D_3\right)$$
  
 $V_{out} = -\left(\frac{10K}{200K} * 5 + \frac{10K}{100K} * 5 + \frac{10K}{50K} * 0 + \frac{10K}{25K} * 0\right)$   
 $V_{out} = -0.75 \text{ V}$ 

Note that *D*<sup>0</sup> is the least significant binary digit and most significant digit is *D*<sup>3</sup> .

![](_page_8_Figure_9.jpeg)

{9}------------------------------------------------

R/2R ladder is more commonly used for D/A conversion than the scaling adder and is shown in the following figure.

It requires only two resistor values. The network of resistors is called a *ladder network.* 

The output voltage is proportional to the binary weight of the input bits.

Generalized R-2R equation for 4 bit DAC is

$$V_o = \frac{D_0 \times 2^0 + D_1 \times 2^1 \times D_2 \times 2^2 + D_3 \times 2^3}{2^4} V_{\text{ref}}$$

Reference voltage Vref is the voltage used to represent binary state of "1".

![](_page_9_Figure_7.jpeg)

R/2R ladder DAC.

{10}------------------------------------------------

Determine the output voltage of the DAC in following figure for digital inputs 0110*2*. Consider Vref equal to 16 V.

### Solution:

Generalized R-2R Equation for 4 bit DAC is

$$V_o = \frac{D_0 \times 2^0 + D_1 \times 2^1 \times D_2 \times 2^2 + D_3 \times 2^3}{2^4} V_{\text{ref}}$$

$$V_o = \frac{0 \times 1 + 1 \times 2 + 1 \times 4 + 0 \times 8}{16} (16 \text{ V}) = 6 \text{ V}$$

Therefore, 0110*2* digital converts to 6 V analog.

![](_page_10_Picture_7.jpeg)