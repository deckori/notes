

{6}------------------------------------------------

## BJT AC Circuit Analysis

### cample - For the following circuit:

- a. Determine  $r_e$ .
- b. Find  $Z_i$  (with  $r_o = \infty \Omega$ ).
- c. Calculate  $Z_o$  (with  $r_o = \infty \Omega$ ).
- d. Determine  $A_v$  (with  $r_o = \infty \Omega$ ).

![](_page_6_Figure_6.jpeg)

#### Solution:

a. DC analysis:

$$I_B = \frac{V_{CC} - V_{BE}}{R_B} = \frac{12 \text{ V} - 0.7 \text{ V}}{470 \text{ k}\Omega} = 24.04 \,\mu\text{A}$$

$$I_E = (\beta + 1)I_B = (101)(24.04 \,\mu\text{A}) = 2.428 \,\text{mA}$$

$$r_e = \frac{26 \,\text{mV}}{I_E} = \frac{26 \,\text{mV}}{2.428 \,\text{mA}} = \mathbf{10.71} \,\Omega$$

b. 
$$\beta r_e = (100)(10.71 \ \Omega) = 1.071 \ k\Omega$$
  
 $Z_i = R_B \|\beta r_e = 470 \ k\Omega \|1.071 \ k\Omega = 1.07 \ k\Omega$ 

c. 
$$Z_o = R_C = 3 \,\mathrm{k}\Omega$$

d. 
$$A_v = -\frac{R_C}{r_e} = -\frac{3 \text{ k}\Omega}{10.71 \Omega} = -280.11$$

![](_page_6_Figure_13.jpeg)

Substituting the  $r_e$  model into the network.

{7}------------------------------------------------

# Bipolar Junction Transistor

### **BJT AC Circuit Analysis:**

lacktriangledown Voltage Divider  $r_e$  Transistor equivalent

![](_page_7_Figure_3.jpeg)

![](_page_7_Figure_4.jpeg)

![](_page_7_Picture_5.jpeg)

### Analysis:

Figure 2.19: Voltage divider ac equivalent circuit using  $r_{\rm e}$  equivalent model.

Input Impedance  $Z_i$  of the circuitQutput Impedance  $Z_o$  of the circuit:

$$Z_i = R_1 \| R_2 \| \beta r_e$$

$$Z_o = R_C \parallel r_o$$

$$If \ r_o \ge 10R_C$$

$$Z_o \cong R_C$$

### Voltage gain $A_{\nu}$ :

$$A_{v} = \frac{V_{o}}{V_{i}} = \frac{-R_{C} \mid\mid r_{o}}{r_{e}}$$
If  $r_{o} \ge 10R_{C}$ 

$$A_{v} \cong -\frac{R_{C}}{r_{e}}$$
Minus sign:
$$180^{\theta} \text{ phase}$$
shift between
$$V_{o} \text{ and } V_{i}$$

{8}------------------------------------------------

# Bipolar Junction Transistor

### BJT AC Circuit Analysis:

lacktriangledown Voltage Divider  $r_e$  Transistor equivalent

I.

![](_page_8_Figure_4.jpeg)

![](_page_8_Picture_5.jpeg)

Voltage divider ac equivalent circuit using  $r_{\scriptscriptstyle e}$  equivalent model.

For voltage divider bias circuit, we can apply the following approximate  $\beta R_{\rm E} \geq 10 R_{\rm 2}$ 

approach to find  $r_{\mbox{\tiny e}}$  and  $r_{\mbox{\tiny o}}$  if

Diode resistance: 
$$r_e = \frac{26mV}{I_E}$$

r<sub>e</sub> is the ac emitter resistance

Output impedance:  $r_o = \frac{\Delta V_{CE}}{\Delta I_c}$ 

$$r_o \cong \frac{V_A}{I_{C_Q}}$$

 $V_A$  is the early voltage.

{9}------------------------------------------------

## BJT AC Circuit Analysis

### cample - For the following circuit:

- a.  $r_e$ .
- b.  $Z_i$ .
- c.  $Z_o(r_o = \infty \Omega)$ .
- d.  $A_v(r_o = \infty \Omega)$ .

#### **Solution:**

a. DC: Testing  $\beta R_E > 10R_2$ ,

$$(90)(1.5 \,\mathrm{k}\Omega) > 10(8.2 \,\mathrm{k}\Omega)$$

 $135 \,\mathrm{k}\Omega > 82 \,\mathrm{k}\Omega$  (satisfied)

Using the approximate approach, we obtain

$$V_B = \frac{R_2}{R_1 + R_2} V_{CC} = \frac{(8.2 \text{ k}\Omega)(22 \text{ V})}{56 \text{ k}\Omega + 8.2 \text{ k}\Omega} = 2.81 \text{ V}$$

$$V_E = V_B - V_{BE} = 2.81 \text{ V} - 0.7 \text{ V} = 2.11 \text{ V}$$

$$I_E = \frac{V_E}{R_E} = \frac{2.11 \text{ V}}{1.5 \text{ k}\Omega} = 1.41 \text{ mA}$$

$$r_e = \frac{26 \text{ mV}}{I_E} = \frac{26 \text{ mV}}{1.41 \text{ mA}} = 18.44 \Omega$$

b. 
$$R' = R_1 \| R_2 = (56 \text{ k}\Omega) \| (8.2 \text{ k}\Omega) = 7.15 \text{ k}\Omega$$
  
 $Z_i = R' \| \beta r_e = 7.15 \text{ k}\Omega \| (90)(18.44 \Omega) = 7.15 \text{ k}\Omega \| 1.66 \text{ k}\Omega$   
 $= 1.35 \text{ k}\Omega$ 

c. 
$$Z_o = R_C = 6.8 \text{ k}\Omega$$
  
d.  $A_v = -\frac{R_C}{r_c} = -\frac{6.8 \text{ k}\Omega}{18.44 \Omega} = -368.76$ 

![](_page_9_Picture_14.jpeg)

![](_page_9_Figure_15.jpeg)

Substituting the  $r_e$  equivalent circuit into the ac equivalent network.

{10}------------------------------------------------

## **Analog Electronics I BJT AC Circuit Analysis:Review:**

**Effect of source resistor (Rs) and load** 

![](_page_10_Figure_2.jpeg)

Figure 2.20: Voltage bias with source resistor R<sup>s</sup> and

- So far we analysed the amplifier without any load been connected **(No load gain)** . load resistor R<sup>L</sup>
- In addition we did not consider the effect of internal resistance Rs of the source.
- On amplifier data sheets, the listed parameters and gain are all for unloaded scenario.
- The gain that results due to the application of source resistor Rs and load resistor RLwill have an effect on overall amplifier gain.