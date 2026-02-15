

{11}------------------------------------------------

## Bipolar Junction **Transistor**

#### BJT AC Circuit Analysis:

### Effect of source resistor (R<sub>s</sub>) and load $(R_i)$

![](_page_11_Figure_3.jpeg)

![](_page_11_Picture_4.jpeg)

#### Analysis:

Figure: Voltage bias with source resistor R<sub>c</sub> and load resistor R

- Observe from r<sub>e</sub> equivalent circuit of figure above, for voltage divider bias, load resistance is in parallel with  $R_c$  and source resistance  $R_s$  is in series with signal source vs.

Thus: 
$$Z_i = R_1 || R_2 || \beta r_e$$

$$egin{aligned} oldsymbol{Z}_o &= & r_o \parallel R_C \parallel R_L \ &= & r_o \parallel R_C & ext{(For high value of } \ &R_L \ \end{pmatrix}$$

Voltage gain due to R only:

$$A_{v_L} = \frac{V_o}{V_i} = \frac{-R_C \mid\mid r_o \mid\mid R_L}{r_e}$$

If  $r_c \ge 10R_c$ 

(For high value of 
$$A_{v_L} \simeq -\frac{R_C || R_L}{r_c}$$

Voltage gain due to  $R_{\varsigma}$ :

$$A_{v_s} = \left[ rac{Zi}{Zi + Rs} 
ight] A_{vL} \ igg( egin{array}{c} ext{Applying voltage} \ ext{divider at the} \ ext{input side} \end{array}$$

Here,  $A_{vs}$  is the overall gain from signal source Vs to output voltage Vo.

{12}------------------------------------------------

# **Discussions**

![](_page_12_Picture_1.jpeg)