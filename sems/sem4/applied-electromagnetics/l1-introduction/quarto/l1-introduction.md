

<!-- split 1 -->



{0}------------------------------------------------

![](images/_page_0_Picture_0.jpeg)

# AETN 3111 Applied Electromagnetics

## Introduction

**Dr. Mohamed Ouda Electrical Engineering Department UDST**

![](images/_page_0_Picture_4.jpeg)

Fall 2025

{1}------------------------------------------------

#### **Electromagnetic Spectrum**

Watch the video <a href="https://youtu.be/lwfJPc-rSXw">https://youtu.be/lwfJPc-rSXw</a>

![](images/_page_1_Picture_2.jpeg)

{2}------------------------------------------------

![](images/_page_2_Picture_1.jpeg)

{3}------------------------------------------------

![](images/_page_3_Picture_0.jpeg)

## Plane-Wave Propagation in Lossless Media

![](images/_page_3_Figure_2.jpeg)

https://empossible.net/wp-content/uploads/2018/03/Wave\_in\_Dielectric.gif

1/7/2026

4

{4}------------------------------------------------

![](images/_page_4_Picture_0.jpeg)

## Plane-Wave Propagation in Lossy Media

![](images/_page_4_Picture_2.jpeg)

1/7/2026 <sup>5</sup>https://empossible.net/wp-content/uploads/2018/03/Wave\_in\_Lossy-Dielectric.gif

<!-- split 2 -->



{5}------------------------------------------------

![](images/_page_5_Picture_0.jpeg)

# Why Study Electromagnetics?

This course is about electromagnetics (EM), the electrical foundation of Electrical and Computer Engineering, or, how electricity *really* works.

- Linear Circuit is a simple part of EM, so it was taught first. However there are an increasing number of cases in ECE where circuit theory fails (e.g. faster computers, higher communications frequencies, power electronics, power system transients,), and therefore EM must supplement circuit theory.
- Also EM is the basis for many devices (machinery, antennas, etc.), and one of the physical foundations of any active electronic device

{6}------------------------------------------------

![](images/_page_6_Picture_0.jpeg)

## Why Study Electromagnetics?

- ❑ Electrical Engineering is Applied Electromagnetics
- ❑ **Electromagnetics is Everywhere**
- ❑ **Electromagnetics is fundamental to the advancement of electrical and computer technology**
- As devices get smaller, and frequencies get higher, circuit theory is less able to adequately describe the performance or to predict the operation of circuits.
- At very high frequencies, transmission line and guided wave theory must be used in applications such as high speed electronics, micro/nano electronics, integrated circuits.
- Other applications include: Fiber Optics, Microwave Communication Systems, Antennas and Wave Propagation, Optical Computing, Electromagnetic Interference, Electromagnetic Compatibility, Biology and Medicine/Biomedical Imaging.

{7}------------------------------------------------

![](images/_page_7_Picture_0.jpeg)

## Why Study Electromagnetics?

- As use of the electromagnetic frequency spectrum increases, the demand for engineers who have practical working knowledge in the area of electromagnetics continues to grow.
- Electromagnetic engineers design: high frequency or optoelectronic circuits, antennas and waveguides; electrical circuits that function properly in the presence of external interference while not interfering with other equipment.
- The electromagnetics technical specialty prepares future engineers for employment in industry in the areas of radar, antennas, fiber optics, high frequency circuits, electromagnetic compatibility and microwave communication.

{8}------------------------------------------------

#### Examples of Electromagnetic Applications

![](images/_page_8_Picture_1.jpeg)

![](images/_page_8_Picture_2.jpeg)

![](images/_page_8_Picture_3.jpeg)

![](images/_page_8_Picture_4.jpeg)

![](images/_page_8_Picture_6.jpeg)

![](images/_page_8_Picture_7.jpeg)

![](images/_page_8_Picture_10.jpeg)

![](images/_page_8_Picture_12.jpeg)

![](images/_page_8_Picture_13.jpeg)

![](images/_page_8_Picture_14.jpeg)

{9}------------------------------------------------

![](images/_page_9_Picture_0.jpeg)

#### What is Electromagnetics?

- Electromagnetics is the study of Charges:
  - (i) at rest (ii) in motion
- The subject of electromagnetics may be divided into 3 branches:

| Branch                            | Condition                                              | Field Quantities (Units)                                                                                                            |
|-----------------------------------|--------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| Electrostatics                    | Stationary charges $(\partial q/\partial t = 0)$       | Electric field intensity <b>E</b> (V/m)<br>Electric flux density <b>D</b> (C/m <sup>2</sup> )<br>$\mathbf{D} = \epsilon \mathbf{E}$ |
| Magnetostatics                    | Steady currents $(\partial I/\partial t = 0)$          | Magnetic flux density <b>B</b> (T)<br>Magnetic field intensity <b>H</b> (A/m)<br>$\mathbf{B} = \mu \mathbf{H}$                      |
| Dynamics<br>(time-varying fields) | Time-varying currents $(\partial I/\partial t \neq 0)$ | E, D, B, and H (E, D) coupled to (B, H)                                                                                             |

<!-- split 3 -->



{10}------------------------------------------------

![](images/_page_10_Picture_0.jpeg)

# Why is Electromagnetics Difficult?

#### Electric and Magnetic Field:

- are 3-dimensional !
- are vectors !
- vary in space and as well as in time !
- are governed by PDEs (partial differential equations)

#### Therefore →

- Solution of electromagnetic problems requires a high level of abstract thinking !
- Students must develop a deep physical understanding !

**Math is just a powerful tool !** 

{11}------------------------------------------------

## What are electromagnetic waves?

- Electromagnetic waves are transverse waves made up of electric and magnetic fields.
- All electromagnetic waves travel at the same speed.
- In a vacuum (space), they travel at 300,000,000 m/s!

![](images/_page_11_Figure_5.jpeg)

{12}------------------------------------------------

## How do electromagnetic waves differ?

![](images/_page_12_Picture_1.jpeg)

- Different electromagnetic waves carry different amounts of energy.
- For example, microwaves carry less energy than X-rays.
- The amount of energy carried by an electromagnetic wave depends on the wavelength:
- the shorter the wavelength, the higher its energy.
- Wavelength and frequency are linked properties of a wave: the shorter the wavelength, the higher its frequency.
- So, frequency also tells you about the energy of a wave:
- the higher its frequency, the higher is energy.

![](images/_page_12_Picture_9.jpeg)

![](images/_page_12_Picture_10.jpeg)

{13}------------------------------------------------

# What happens when waves hit a surface**?**

![](images/_page_13_Picture_6.jpeg)

![](images/_page_13_Picture_7.jpeg)

{14}------------------------------------------------

### EM Spectrum Relative Sizes

![](images/_page_14_Figure_1.jpeg)

<!-- split 4 -->



{15}------------------------------------------------

![](images/_page_15_Picture_0.jpeg)

## Electromagnetic spectrum

$$\lambda = \frac{c}{f}$$

![](images/_page_15_Figure_3.jpeg)

{16}------------------------------------------------

## Electromagnetic Frequency Spectrum

![](images/_page_16_Figure_1.jpeg)

{17}------------------------------------------------

![](images/_page_17_Figure_0.jpeg)

18

{18}------------------------------------------------

![](images/_page_18_Picture_0.jpeg)

Symbols, Quantities, and Units

{19}------------------------------------------------

![](images/_page_19_Picture_0.jpeg)

## Dimensions, Units, and Notation

- The *International System of Units*, abbreviated *SI* after its French name *Syst` eme Internationale*, is the standard system used in today's scientific literature for expressing the units of physical quantities.
- In EM we work with scalar and vector quantities.
- **Scalar quantity:** medium-weight italic, such as *C* for capacitance.
- **Units:** medium-weight roman, as in V/m for volts per meter.
- **Vector quantities:** boldface roman, such as **E** for
- **Unit vectors:** boldface roman with circumflex (ˆ) over the letter, as in **x** ˆ or a<sup>x</sup>
- **Phasors:** a tilde (∼) over the letter; *E* is the phasor counterpart of the sinusoidally time-varying scalar field *E(t)*, and **E** is the phasor counterpart of the sinusoidally time-varying vector field **E***(t)*.

<!-- split 5 -->



{20}------------------------------------------------

| Dimension               | Unit     | Symbol |
|-------------------------|----------|--------|
| Length                  | meter    | m      |
| Mass                    | kilogram | kg     |
| Time                    | second   | S      |
| <b>Electric Current</b> | ampere   | A      |
| Temperature             | kelvin   | K      |
| Amount of substance     | mole     | mol    |

| Prefix | Symbol | Magnitude        |
|--------|--------|------------------|
| exa    | Е      | 10 <sup>18</sup> |
| peta   | P      | $10^{15}$        |
| tera   | T      | $10^{12}$        |
| giga   | G      | $10^9$           |
| mega   | M      | $10^{6}$         |
| kilo   | k      | $10^{3}$         |
| milli  | m      | $10^{-3}$        |
| micro  | $\mu$  | $10^{-6}$        |
| nano   | n      | $10^{-9}$        |
| pico   | p      | $10^{-12}$       |
| femto  | f      | $10^{-15}$       |
| atto   | a      | $10^{-18}$       |

{21}------------------------------------------------

# Complex Numbers

## We will find it is useful to represent sinusoids as complex numbers

$$j = \sqrt{-1}$$

$$z = x + jy$$

$$z=|z|\angle\theta=|z|e^{j\theta}$$

#### **Rectangular coordinates**

#### **Polar coordinates**

$$Re(z) = x$$
  
 $Im(z) = y$ 

![](images/_page_21_Figure_9.jpeg)

### **Relations based on Euler's Identity**

$$e^{\pm j\theta} = \cos\theta \pm j\sin\theta$$

{22}------------------------------------------------

![](images/_page_22_Picture_0.jpeg)

## Relations for Complex Numbers

| Euler's Identity: $e^{j\theta}$ | $=\cos\theta+i\sin\theta$ |
|---------------------------------|---------------------------|
|---------------------------------|---------------------------|

$$\sin\theta = \frac{e^{j\theta} - e^{-j\theta}}{2j}$$

$$\cos \theta = \frac{e^{j\theta} + e^{-j\theta}}{2}$$

$$\mathbf{z} = x + jy = |\mathbf{z}|e^{j\theta}$$

$$\mathbf{z}^* = x - jy = |\mathbf{z}|e^{-j\theta}$$

$$x = \Re \mathfrak{e}(\mathbf{z}) = |\mathbf{z}| \cos \theta$$

$$|\mathbf{z}| = \sqrt[+]{\mathbf{z}\mathbf{z}^*} = \sqrt[+]{x^2 + y^2}$$

$$y = \mathfrak{Im}(\mathbf{z}) = |\mathbf{z}| \sin \theta$$

$$\theta = \tan^{-1}(y/x)$$

$$\mathbf{z}^n = |\mathbf{z}|^n e^{jn\theta}$$

$$\mathbf{z}^{1/2} = \pm |\mathbf{z}|^{1/2} e^{j\theta/2}$$

$$\mathbf{z}_1 = x_1 + jy_1$$

$$\mathbf{z}_2 = x_2 + i y_2$$

$$\mathbf{z}_1 = \mathbf{z}_2 \text{ iff } x_1 = x_2 \text{ and } y_1 = y_2$$

$$\mathbf{z}_1 = \mathbf{z}_2 \text{ iff } x_1 = x_2 \text{ and } y_1 = y_2 \quad \mathbf{z}_1 + \mathbf{z}_2 = (x_1 + x_2) + j(y_1 + y_2)$$

$$\mathbf{z}_1\mathbf{z}_2 = |\mathbf{z}_1||\mathbf{z}_2|e^{j(\theta_1+\theta_2)}$$

$$\frac{\mathbf{z}_1}{\mathbf{z}_2} = \frac{|\mathbf{z}_1|}{|\mathbf{z}_2|} e^{j(\theta_1 - \theta_2)}$$

$$-1 = e^{j\pi} = e^{-j\pi} = 1 \angle \pm 180^{\circ}$$

$$j = e^{j\pi/2} = 1 \angle 90^{\circ}$$

$$-j = e^{-j\pi/2} = 1\angle -90^{\circ}$$

$$\sqrt{j} = \pm e^{j\pi/4} = \pm \frac{(1+j)}{\sqrt{2}}$$

$$\sqrt{j} = \pm e^{j\pi/4} = \pm \frac{(1+j)}{\sqrt{2}}$$
  $\sqrt{-j} = \pm e^{-j\pi/4} = \pm \frac{(1-j)}{\sqrt{2}}$ 

Learn how to perform these with your calculator/computer

{23}------------------------------------------------

# Phasor Domain

- 1. The phasor-analysis technique transforms equations from the time domain to the phasor domain.
- 2. Integro-differential equations get converted into linear equations with no sinusoidal functions.
- 3. After solving for the desired variable--such as a particular voltage or current-- in the phasor domain, conversion back to the time domain provides the same solution that would have been obtained had the original integro-differential equations been solved entirely in the time domain.

{24}------------------------------------------------

### Phasor Domain

$$v(t) = V_0 \cos(\omega t + \phi)$$
$$= \Re \left[ V_0 e^{j\phi} e^{j\omega t} \right]$$

Phasor counterpart of v(t)

#### **Time Domain**

$$v(t) = V_0 \cos \omega t$$

$$v(t) = V_0 \cos(\omega t + \phi) \iff \mathbf{V} = V_0 e^{j\phi}.$$

If 
$$\phi = -\pi/2$$
,

$$v(t) = V_0 \cos(\omega t - \pi/2) \quad \longleftrightarrow \quad \mathbf{V} = V_0 e^{-j\pi/2}.$$

#### **Phasor Domain**

$$\leftarrow$$
 **V** =  $V_0$ 

$$\mathbf{V} = V_0 e^{j\phi}$$

<!-- split 6 -->



{25}------------------------------------------------

![](images/_page_25_Picture_0.jpeg)

# Time and Phasor Domain

| x(t)                                   |                   | X                               |
|----------------------------------------|-------------------|---------------------------------|
| $A\cos\omega t$                        | $\leftrightarrow$ | A                               |
| $A\cos(\omega t + \phi)$               | $\leftrightarrow$ | $Ae^{j\phi}$                    |
| $-A\cos(\omega t + \phi)$              | $\leftrightarrow$ | $Ae^{j(\phi\pm\pi)}$            |
| $A \sin \omega t$                      | $\leftrightarrow$ | $Ae^{-j\pi/2} = -jA$            |
| $A\sin(\omega t + \phi)$               | $\leftrightarrow$ | $Ae^{j(\phi-\pi/2)}$            |
| $-A\sin(\omega t + \phi)$              | $\leftrightarrow$ | $Ae^{j(\phi+\pi/2)}$            |
| $\frac{d}{dt}(x(t))$                   | $\leftrightarrow$ | $j\omega\mathbf{X}$             |
| $\frac{d}{dt}[A\cos(\omega t + \phi)]$ | $\leftrightarrow$ | $j\omega Ae^{j\phi}$            |
| $\int x(t) dt$                         | $\leftrightarrow$ | $\frac{1}{j\omega} \mathbf{X}$  |
| $\int A\cos(\omega t + \phi) dt$       |                   | $\frac{1}{j\omega} A e^{j\phi}$ |

It is much easier to deal with exponentials in the phasor domain than sinusoidal relations in the time domain

Just need to track magnitude/phase, knowing that everything is at frequency w

{26}------------------------------------------------

# Phasor Relation for Resistors

![](images/_page_26_Picture_1.jpeg)

## Current through resistor

![](images/_page_26_Picture_4.jpeg)

### Time Domain Frequency Domain

![](images/_page_26_Figure_6.jpeg)

## Time domain

$$i = I_{\rm m} \cos(\omega t + \varphi)$$
  
 $v = iR = RI_{\rm m} \cos(\omega t + \varphi)$ 

## Phasor Domain

$$\mathbf{V} = R\mathbf{I}$$
$$V = RI_{\mathbf{m}} \angle \varphi$$

{27}------------------------------------------------

## Phasor Relation for Inductors

![](images/_page_27_Picture_1.jpeg)

### Time Domain

![](images/_page_27_Figure_3.jpeg)

## Frequency Domain

![](images/_page_27_Figure_5.jpeg)

![](images/_page_27_Figure_6.jpeg)

## $\mathbf{V} = j\omega L\mathbf{I}$

## Time domain

and

$$i_{\rm L} = \Re \left[ \mathbf{I}_{\rm L} e^{j\omega t} \right].$$

 $v_{\rm L} = \Re [\mathbf{V}_{\rm L} e^{j\omega t}]$ 

 $v = L \frac{di}{dt}$ 

Consequently,

$$\Re [\mathbf{V}_{L}e^{j\omega t}] = L \frac{d}{dt} [\Re (\mathbf{I}_{L}e^{j\omega t})]$$
$$= \Re [j\omega L\mathbf{I}_{L}e^{j\omega t}],$$

which leads to

$$\mathbf{V}_{\mathrm{L}} = j\omega L \mathbf{I}_{\mathrm{L}}$$

and

$$\mathbf{Z}_{\mathrm{L}} = \frac{\mathbf{V}_{\mathrm{L}}}{\mathbf{I}_{\mathrm{L}}} = j\omega L.$$

{28}------------------------------------------------

# Phasor Relation for Capacitors

![](images/_page_28_Picture_1.jpeg)

![](images/_page_28_Figure_3.jpeg)

![](images/_page_28_Figure_5.jpeg)

$$\begin{array}{c}
\overline{\phantom{a}} \\
\overline{\phantom{a}} \\
I = j\omega CV
\end{array}$$

## Time domain

$$i = C \frac{dv}{dt}$$

## Phasor Domain

$$\mathbf{I}_{\mathrm{C}} = j\omega C \mathbf{V}_{\mathrm{C}}$$

$$\mathbf{Z}_{\mathrm{C}} = \frac{\mathbf{V}_{\mathrm{C}}}{\mathbf{I}_{\mathrm{C}}} = \frac{1}{j\omega C}.$$

{29}------------------------------------------------

![](images/_page_29_Picture_0.jpeg)

## AC Phasor Analysis: General Procedure

### Step 1

Adopt Cosine Reference (Time Domain)

![](images/_page_29_Figure_4.jpeg)

### Step 3

Cast Equations in Phasor Form

$$\mathbf{I}\left(R + \frac{1}{j\omega C}\right) = \mathbf{V}_{s}$$

### Step 2

Transfer to Phasor Domain

$$i \longrightarrow \mathbf{I}$$

$$V \longrightarrow V$$

$$R \longrightarrow \mathbf{Z}_{R} = R$$

$$L \longrightarrow \mathbf{Z}_{L} = j\omega L$$

$$C \longrightarrow \mathbf{Z}_{\mathbf{C}} = 1/j\omega C$$

![](images/_page_29_Figure_14.jpeg)

### Step 4

Solve for Unknown Variable (Phasor Domain)

$$\mathbf{I} = \frac{\mathbf{V}_{s}}{R + \frac{1}{j\omega C}}$$

### Step 5

Transform Solution
Back to Time Domain

$$i(t) = \Re \mathbf{e} [\mathbf{I}e^{j\omega t}]$$

$$= 6 \cos(\omega t - 105^{\circ})$$
(mA)

<!-- split 7 -->



{30}------------------------------------------------

![](images/_page_30_Picture_0.jpeg)

## Example 1-4: RL Circuit

The voltage source of the circuit shown in Fig. 7-8(a) is given by

$$v_{\rm s}(t) = 15\sin(4 \times 10^4 t - 30^\circ) \text{ V}.$$

Also,  $R=3~\Omega$  and L=0.1 mH. Obtain an expression for th voltage across the inductor.

## **Solution:**

Step 1: Convert  $v_s(t)$  to the cosine reference

$$v_s(t) = 15\sin(4 \times 10^4 t - 30^\circ)$$
  
= 15\cos(4 \times 10^4 t - 30^\circ - 90^\circ)  
= 15\cos(4 \times 10^4 t - 120^\circ) V,

and its corresponding phasor  $V_s$  is given by

$$V_s = 15e^{-j120^{\circ}} V.$$

Step 2: Transform circuit to the phasor domain

![](images/_page_30_Figure_11.jpeg)

![](images/_page_30_Figure_12.jpeg)

![](images/_page_30_Figure_13.jpeg)

(b) Phasor domain

Cont

{31}------------------------------------------------

## Example 1-4: RL Circuit cont.

![](images/_page_31_Picture_1.jpeg)

Step 3: Cast KVL in phasor domain

$$R\mathbf{I} + j\omega L\mathbf{I} = \mathbf{V}_{s}$$
.

Step 4: Solve for unknown variable

$$\mathbf{I} = \frac{\mathbf{V}_{s}}{R + j\omega L} = \frac{15e^{-j120^{\circ}}}{3 + j4 \times 10^{4} \times 10^{-4}}$$
$$= \frac{15e^{-j120^{\circ}}}{3 + j4} = \frac{15e^{-j120^{\circ}}}{5e^{j53.1^{\circ}}} = 3e^{-j173.1^{\circ}} \text{ A.}$$

The phasor voltage across the inductor is related to I by

$$\begin{aligned} \mathbf{V}_{\mathrm{L}} &= j\omega L \mathbf{I} \\ &= j4 \times 10^{4} \times 10^{-4} \times 3e^{-j173.1^{\circ}} \\ &= j12e^{-j173.1^{\circ}} \\ &= 12e^{-j173.1^{\circ}} \cdot e^{j90^{\circ}} = 12e^{-j83.1^{\circ}} \, \mathrm{V}, \end{aligned}$$

Step 5: Transform solution to the time domain

The corresponding time-domain voltage is

$$v_{L}(t) = \Re [\mathbf{V}_{L} e^{j\omega t}]$$

$$= \Re [12e^{-j83.1^{\circ}} e^{j4 \times 10^{4} t}]$$

$$= 12 \cos(4 \times 10^{4} t - 83.1^{\circ}) \text{ V}.$$

where we replaced j with  $e^{j90^{\circ}}$ .

{32}------------------------------------------------

**Table 1-5:** Time-domain sinusoidal functions z(t) and their cosine-reference phasor-domain counterparts  $\widetilde{Z}$ , where  $z(t) = \Re \left[\widetilde{Z}e^{j\omega t}\right]$ .

![](images/_page_32_Picture_1.jpeg)

| Z(t)                                                                                                                                                                           |                   | $\widetilde{Z}$                                                                                                               |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|-------------------------------------------------------------------------------------------------------------------------------|
| $A\cos \omega t$ $A\cos(\omega t + \phi_0)$ $A\cos(\omega t + \beta x + \phi_0)$ $Ae^{-\alpha x}\cos(\omega t + \beta x + \phi_0)$ $A\sin \omega t$ $A\sin(\omega t + \phi_0)$ | <b>‡ ‡ ‡ ‡ ‡</b>  | $A$ $Ae^{j\phi_0}$ $Ae^{j(\beta x + \phi_0)}$ $Ae^{-\alpha x}e^{j(\beta x + \phi_0)}$ $Ae^{-j\pi/2}$ $Ae^{j(\phi_0 - \pi/2)}$ |
| $\frac{d}{dt}(z(t))$                                                                                                                                                           | $\leftrightarrow$ | $j\omega\widetilde{Z}$                                                                                                        |
| $\frac{d}{dt}[A\cos(\omega t + \phi_0)]$                                                                                                                                       | $\leftrightarrow$ | $j\omega Ae^{j\phi_0}$                                                                                                        |
| $\int z(t) dt$                                                                                                                                                                 |                   | $\frac{1}{j\omega}\widetilde{Z}$                                                                                              |
| $\int A\sin(\omega t + \phi_0) dt$                                                                                                                                             | $\leftrightarrow$ | $\frac{1}{j\omega}Ae^{j(\phi_0-\pi/2)}$                                                                                       |

{33}------------------------------------------------

![](images/_page_33_Picture_0.jpeg)

## 1-7.2 Traveling Waves in the Phasor Domain

According to Table 1-5, if we set  $\phi_0 = 0$ , its third entry becomes

$$A\cos(\omega t + \beta x) \iff Ae^{j\beta x}.$$
 (1.74)

From the discussion associated with Eq. (1.31), we concluded that  $A \cos(\omega t + \beta x)$  describes a wave traveling in the negative x-direction.

In the phasor domain, a wave of amplitude A traveling in the positive x-direction in a lossless medium with phase constant  $\beta$  is given by the negative exponential  $Ae^{-j\beta x}$ , and conversely, a wave traveling in the negative x-direction is given by  $Ae^{j\beta x}$ . Thus, the sign of x in the exponential is opposite to the direction of travel.
