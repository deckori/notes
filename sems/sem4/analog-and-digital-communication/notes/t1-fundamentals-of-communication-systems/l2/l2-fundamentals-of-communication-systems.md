<br><span class='markdown-page-line'>---------------------------------------------<span id='page1' class='markdown-page-text'>[ 第1页 ]</span>---------------------------------------------</span><br><br>

# Introduction to Analog Communications – Fundamentals of Communication Systems (2)

AETN2121 – Analog and Digital Communication

<br><span class='markdown-page-line'>---------------------------------------------<span id='page2' class='markdown-page-text'>[ 第2页 ]</span>---------------------------------------------</span><br><br>

# Course Topics

Topic 1: Introduction to analog communication systems

![](images/01b1aa10c5eb18e0a76f161027d975c0570b86df38a1c17fdac1a65fe9da525b_97.jpg){width=97%}

<br><span class='markdown-page-line'>---------------------------------------------<span id='page3' class='markdown-page-text'>[ 第3页 ]</span>---------------------------------------------</span><br><br>

# Recap

Definition of Communication System and its components.

Communication system requirements

Electromagnetic waves and spectrum

<br><span class='markdown-page-line'>---------------------------------------------<span id='page4' class='markdown-page-text'>[ 第4页 ]</span>---------------------------------------------</span><br><br>

# Learning Outcomes

By end of this lecture, student should be able to:

Communication channel.

Baseband and carrier signals

Filters

Recognize different channel impairments

Define and calculate dB in communications

<br><span class='markdown-page-line'>---------------------------------------------<span id='page5' class='markdown-page-text'>[ 第5页 ]</span>---------------------------------------------</span><br><br>

# Communications Channel

is a section of spectrum that is set aside for a very specific service.

for example, certain channels are reserved for the purpose of FM radio, for AM radio, for TV stations, for use by mobile telephones, etc.

the frequency of the channel is at the center of the section of spectrum

<br><span class='markdown-page-line'>---------------------------------------------<span id='page6' class='markdown-page-text'>[ 第6页 ]</span>---------------------------------------------</span><br><br>

# Channel Bandwidth

Bandwidth is a measure of frequency range and is typically measured in Hz

Channel bandwidth is the difference between the highest and lowest frequencies in a channel

for example, an AM radio station typically has a bandwidth of 10 kHz

$$
\mathrm { B W } = \mathbf { f } _ { \mathrm { m a x } } - \mathbf { f } _ { \mathrm { m i n } } ~ ( \mathrm { H z } )
$$

![](images/cae4b3fff455c5a7921613ad9e3f766cccfbbce5dfca5086b87e71fbe822b267_74.jpg){width=74%}

<br><span class='markdown-page-line'>---------------------------------------------<span id='page7' class='markdown-page-text'>[ 第7页 ]</span>---------------------------------------------</span><br><br>

# Baseband Signals

Baseband

the frequency content of an information signal before modulation

baseband signals are used to modify (modulate) a higher frequency for transmission.

the original, low frequency components, are referred to as the baseband signal

the modulated, higher-frequency modified signal is referred to as the 'RF' (radio-frequency) signal

<br><span class='markdown-page-line'>---------------------------------------------<span id='page8' class='markdown-page-text'>[ 第8页 ]</span>---------------------------------------------</span><br><br>

# Carrier Signal

a carrier wave is a waveform (usually sinusoidal) that is modified to represent the information to be transmitted

a carrier wave is usually of much higher frequency than the original information signal

![](images/4ce23d0dd83178d30a1c85bc7e8b90be15eca464a0bab62c6861e4522a50ad41_13.jpg){width=13%} Signal at baseband

![](images/d419fe763e459c558fd0c58e70dffbec07fa8953a13b48b332e4105faeec28b6_27.jpg){width=27%} Signal at RF (radio frequency)

<br><span class='markdown-page-line'>---------------------------------------------<span id='page9' class='markdown-page-text'>[ 第9页 ]</span>---------------------------------------------</span><br><br>

# Filters

Low-pass, band-pass and high-pass filters:

Low-pass filter - allows low-frequency components of a signal to pass and blocks all others

Band-pass filter - removes low-frequency and high-frequency components of a signal and allows all signals between to pass

High-pass filter - allows high-frequency components of a signal to pass and blocks all others

![](images/9d7d333e64e0ff9c81ae640d4cad442370d4d16643f1b4822dec97dd1443d17e_62.jpg){width=62%}

<br><span class='markdown-page-line'>---------------------------------------------<span id='page10' class='markdown-page-text'>[ 第10页 ]</span>---------------------------------------------</span><br><br>

# Communication Channel impairments

Attenuation

Distortion

Noise

<br><span class='markdown-page-line'>---------------------------------------------<span id='page11' class='markdown-page-text'>[ 第11页 ]</span>---------------------------------------------</span><br><br>

# Communication Channel impairments - Attenuation

Attenuation can be problematic for long distance communications. This means due to signal propagate through media the initial signal power decreases if the length of the media becomes longer.

![](images/955f6ddb1f16c602d7db92898a89dc088ff9d2a7970386fbdf0ab1a0921ad8aa_59.jpg){width=59%}

<br><span class='markdown-page-line'>---------------------------------------------<span id='page12' class='markdown-page-text'>[ 第12页 ]</span>---------------------------------------------</span><br><br>

To solve the problem of attenuation, amplifiers used to amplify the signal power.

Use of digital signals are less susceptible to attenuation than analog signals.

![](images/0719095970b67677f5a00880de428665c704ad4231f7b25da17f11efdff8ec80_63.jpg){width=63%}

<br><span class='markdown-page-line'>---------------------------------------------<span id='page13' class='markdown-page-text'>[ 第13页 ]</span>---------------------------------------------</span><br><br>

# Communication Channel impairments - Distortion

The signal may have a bandwidth larger than the channel bandwidth. The distortion causes a variation in signal frequency and maybe a linear or non-linear distortion.

![](images/e67c4ca6dc99fbb3521ff1fd3412025f56b2ff267713d6e43cbd971e64ab9c2d_100.jpg){width=100%}

<br><span class='markdown-page-line'>---------------------------------------------<span id='page14' class='markdown-page-text'>[ 第14页 ]</span>---------------------------------------------</span><br><br>

# Communication Channel Impairments - Noise

Noise maybe caused by external or internal noise source.

External Sources: interference from signals transmitted on nearby channels (crosstalk), interference generated by contact switches, automobile ignition radiation, natural noise from lightning, solar radiation, etc.

Internal Sources: thermal noise (random motion of electrons in conductors, random diffusion and recombination of charged carriers in electronic devices)

<br><span class='markdown-page-line'>---------------------------------------------<span id='page15' class='markdown-page-text'>[ 第15页 ]</span>---------------------------------------------</span><br><br>

# The dB in Communications

dB (decibel) is a relative unit of measurement used frequently in electronic communications to describe power gain or loss.

dB value is calculated by taking the log of the ratio of the measured or calculated power (P2) with respect to a reference power (P1) level. This result is then multiplied by 10 to obtain the value in dB.

dB = $10\log_{10}\frac{\omega}{P_{1}}$

<br><span class='markdown-page-line'>---------------------------------------------<span id='page16' class='markdown-page-text'>[ 第16页 ]</span>---------------------------------------------</span><br><br>

# The dB in Communications

In terms of Voltages:

dB = $20 \log_{10} \left( \frac{V^2}{V_1} \right)$

dBm is dB level using 1-mW reference.

Example: a laser diode output +10dBm. Convert this value to watts.

<br><span class='markdown-page-line'>---------------------------------------------<span id='page17' class='markdown-page-text'>[ 第17页 ]</span>---------------------------------------------</span><br><br>

# The dB in Communications

In terms of Voltages:

dB = $20\log_{10}\left(\frac{V^{2}}{V_{1}}\right)$

dBm is dB level using 1-mW reference.

Example: a laser diode output +10dBm. Convert this value to

watts.

+10 dBm = 10 log $\frac{P_{2}}{0.001}$

$\log^{-1}(1) = \frac{P_{2}}{0.001} \Rightarrow 10 = \frac{P_{2}}{0.001}$

$P_{2} = 0.01$ W