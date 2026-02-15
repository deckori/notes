

{11}------------------------------------------------

## Bipolar Junction Transistor ( BJT)

### 2. Common-Collector

An amplifier configuration where the input is applied to the base and output is taken from the emitter. The output signal is in phase with the input signal.

![](_page_11_Picture_3.jpeg)

![](_page_11_Figure_4.jpeg)

{12}------------------------------------------------

## BJT Bias Configurations

| Fixed-bias              | $R_B$ $R_C$                   | $I_B = \frac{V_{CC} - V_{BE}}{R_B}$ $I_C = \beta I_B, I_E = (\beta + 1)I_B$ $V_{CE} = V_{CC} - I_C R_C$                                                                                                                                                                                                                                                |
|-------------------------|-------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Emitter-bias            | $R_{B}$ $R_{C}$ $R_{E}$       | $I_B = \frac{V_{CC} - V_{BE}}{R_B + (\beta + 1)R_E}$ $I_C = \beta I_B, I_E = (\beta + 1)I_B$ $R_i = (\beta + 1)R_E$ $V_{CE} = V_{CC} - I_C (R_C + R_E)$                                                                                                                                                                                                |
| Voltage-divider<br>bias | $R_1$ $R_C$ $R_C$ $R_C$ $R_C$ | EXACT: $R_{Th} = R_1    R_2, E_{Th} = \frac{R_2 V_{CC}}{R_1 + R_2}$ APPROXIMATE: $\beta R_E \ge 10 R_2$ $I_B = \frac{E_{Th} - V_{BE}}{R_{Th} + (\beta + 1) R_E}$ $I_C = \beta I_B, I_E = (\beta + 1) I_B$ $V_{CE} = V_{CC} - I_C (R_C + R_E)$ $I_C = V_{CC} - I_C (R_C + R_E)$ $V_{CE} = V_{CC} - I_C (R_C + R_E)$ $V_{CE} = V_{CC} - I_C (R_C + R_E)$ |

{13}------------------------------------------------

## BJT Bias Configurations

| Collector-feedback | $R_F$ $R_C$ $R_C$ $R_C$  | $I_{B} = \frac{V_{CC} - V_{BE}}{R_{F} + \beta(R_{C} + R_{E})}$ $I_{C} = \beta I_{B}, I_{E} = (\beta + 1)I_{B}$ $V_{CE} = V_{CC} - I_{C}(R_{C} + R_{E})$    |
|--------------------|--------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Emitter-follower   | $R_B$ $R_E$ $-V_{EE}$    | $I_B = \frac{V_{EE} - V_{BE}}{R_B + (\beta + 1)R_E}$ $I_C = \beta I_B, I_E = (\beta + 1)I_B$ $V_{CE} = V_{EE} - I_E R_E$                                   |
| Common-base        | $R_E$ $R_C$ $+$ $V_{CC}$ | $I_E = \frac{V_{EE} - V_{BE}}{R_E}$ $I_B = \frac{I_E}{\beta + 1}, I_C = \beta I_B$ $V_{CE} = V_{EE} + V_{CC} - I_E(R_C + R_E)$ $V_{CB} = V_{CC} - I_C R_C$ |

{14}------------------------------------------------

# **Discussions**

![](_page_14_Picture_1.jpeg)