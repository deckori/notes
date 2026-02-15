

{6}------------------------------------------------

## **Multistage Amplifiers:**

## **Example 1**

The Darlington configuration shown below. Calculate IB1, IE2, VB1and VCE2.

![](_page_6_Picture_3.jpeg)

1) 
$$I_{B_1} = \frac{V_{CC} - V_{BE_1} - V_{BE_2}}{R_B + (\beta_D + 1)R_E} = \frac{18 \text{ V} - 0.7 \text{ V} - 0.7 \text{ V}}{3.3 \text{ M}\Omega + (5001)(390 \Omega)}$$
$$= \frac{18 \text{ V} - 1.4 \text{ V}}{3.3 \text{ M}\Omega + 1.95 \text{ M}\Omega} = \frac{16.6 \text{ V}}{5.25 \text{ M}\Omega} = 3.16 \,\mu\text{A}$$

2) 
$$I_{C_2} \cong I_{E_2} = \beta_D I_{B_1} = (5000)(3.16 \text{ mA}) = 15.80 \text{ mA}$$
  
 $V_{C_1} = V_{C_2} = 18 \text{ V}$   
 $V_{E_2} = I_{E_2} R_E = (15.80 \text{ mA})(390 \Omega) = 6.16 \text{ V}$   
3)  $V_{B_1} = V_{E_2} + V_{BE_1} + V_{BE_2} = 6.16 \text{ V} + 0.7 \text{ V} + 0.7 \text{ V} = 7.56 \text{ mA}$ 

4) 
$$V_{CE_2} = V_{CC} - V_{E_2} = 18 \text{ V} - 6.16 \text{ V} = 11.84 \text{ V}$$

{7}------------------------------------------------

## **Discussions**

![](_page_7_Picture_1.jpeg)