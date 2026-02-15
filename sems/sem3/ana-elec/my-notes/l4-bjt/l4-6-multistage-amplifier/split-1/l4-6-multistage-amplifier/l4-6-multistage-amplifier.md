

{0}------------------------------------------------

![](_page_0_Picture_0.jpeg)

# AETN 2101-ANALOG ELECTRONICS

**L4.6 Multistage Amplifiers**

**Dr. Yasen Harrye**

{1}------------------------------------------------

### **Introduction:**

- Many applications cannot be handled with single-transistor amplifiers in order to meet the specification of a given amplification gain, input resistance and output resistance.
- As a solution a transistor amplifier circuits can be connected in series or as a cascaded amplifiers.
- This can be done either to increase the overall small-signal voltage gain or provide an overall voltage gain greater than l with a very low output resistance.

{2}------------------------------------------------

#### **Darlington Connection**

 A very popular connection of two bipolar junction transistors for operation is "superbeta" transistor.

![](_page_2_Picture_3.jpeg)

![](_page_2_Picture_4.jpeg)

 The main feature of the Darlington connection is that the current gain is the product of the current gains of the individual transistors.

![](_page_2_Picture_6.jpeg)

$$\beta_D = \beta_1 \beta_2$$

{3}------------------------------------------------

#### **III Darlington Amplifier: Emitter Follower Configuration**

- Impact of using the Darlington configuration is an input impedance much larger than that obtained with a singletransistor network.
- The current gain is also larger.
- But the voltage gain for a singletransistor or Darlington configuration remains slightly less than one.

![](_page_3_Picture_5.jpeg)

Emitter Follower Darlington amplifier

{4}------------------------------------------------

#### **III Darlington Amplifier: Emitter Follower Configuration**

![](_page_4_Picture_2.jpeg)

$$V_{CC} - V_{RB} - V_{BE1} - V_{BE2} - V_{RE} = 0$$

$$V_{CC} - V_{CE2} - V_{RE} = 0$$

DC Bias Analysis 
$$V_{CC}-I_{B1}R_B-V_{BE1}-V_{BE2}-I_{E2}R_E=0$$

$$I_{B1} = \frac{V_{\text{CC}} - V_{\text{BE1}} - V_{\text{BE2}}}{R_{\text{B}} + (\beta_D + 1)R_{\text{E}}}$$

Beta of transistor replaced by β<sup>D</sup>

The emitter current of *Q1* is equal to the base current of *Q2* so that

$$I_{E2} = (\beta_D + 1)I_B$$

Hence,

$$I_{C_2} \cong I_{E_2} = \beta_D I_{B_1}$$

$$V_{C_1} = V_{C_2} = V_{CC}$$

$$V_{E_2} = I_{E_2} R_E$$

The base voltage of transistor *Q<sup>1</sup>*

$$V_{B_1} = V_{CC} - I_{B_1}R_B = V_{E_2} + V_{BE_1} + V_{BE_2}$$

Collector emitter voltage of transistor *Q2*

$$V_{CE_2} = V_{C_2} - V_{E_2} = V_{CC} - V_{E_2}$$

{5}------------------------------------------------

#### **Example 1**

The Darlington configuration shown below. Calculate IB1, IE2, VB1and VCE2.

![](_page_5_Figure_3.jpeg)