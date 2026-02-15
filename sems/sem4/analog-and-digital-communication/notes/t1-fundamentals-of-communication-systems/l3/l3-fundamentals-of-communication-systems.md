<br><span class='markdown-page-line'>---------------------------------------------<span id='page1' class='markdown-page-text'>[ 第1页 ]</span>---------------------------------------------</span><br><br>

# Introduction to Analog Communications – Fundamentals of Communication Systems (3)

AETN2121 – Analog and Digital Communication

<br><span class='markdown-page-line'>---------------------------------------------<span id='page2' class='markdown-page-text'>[ 第2页 ]</span>---------------------------------------------</span><br><br>

# Course Topics

Topic 1: Introduction to analog communication systems

![](images/01b1aa10c5eb18e0a76f161027d975c0570b86df38a1c17fdac1a65fe9da525b_97.jpg){width=97%}

<br><span class='markdown-page-line'>---------------------------------------------<span id='page3' class='markdown-page-text'>[ 第3页 ]</span>---------------------------------------------</span><br><br>

# Recap

Communication channel.

Baseband and carrier signals

Filters

Recognize different channel impairments

Define and calculate dB in communications

<br><span class='markdown-page-line'>---------------------------------------------<span id='page4' class='markdown-page-text'>[ 第4页 ]</span>---------------------------------------------</span><br><br>

# Learning Outcomes:

By end of this lecture, student should be able to:

Differentiate between different mobile operations

Define different types of radio frequency interference

Define harmonic distortion

<br><span class='markdown-page-line'>---------------------------------------------<span id='page5' class='markdown-page-text'>[ 第5页 ]</span>---------------------------------------------</span><br><br>

# Signal to Noise Ratio (SNR)

SNR is a relative measure of the desired signal power to the noise power.

![](images/3af7cb30893bc3ba1cf870c93ea88cd8698f9435392030cc35c90759ea586bcb_100.jpg){width=100%}

<br><span class='markdown-page-line'>---------------------------------------------<span id='page6' class='markdown-page-text'>[ 第6页 ]</span>---------------------------------------------</span><br><br>

# Noise Figure (NF)

NF is used to specify exactly how noisy a device is

NF = $10\log_{10}\frac{S_i/N_i}{S_o/N_o} = 10\log_{10}\text{NR}$

Example: a transistor amplifier has a measured S/N power of 10 at its input and 5 at its output.

Calculate NR

Calculate NF

<br><span class='markdown-page-line'>---------------------------------------------<span id='page7' class='markdown-page-text'>[ 第7页 ]</span>---------------------------------------------</span><br><br>

# Noise Figure (NF)

NF is used to specify exactly how noisy a device is

$$
\mathrm { N F } = 10 \log _ { 10 } \frac { S _ { i } / N _ { i } } { S _ { o } / N _ { o } } = 10 \log _ { 10 } \mathrm { N R }
$$

Example: a transistor amplifier has a measured S/N power of 10 at its input and 5 at its output.

Calculate NR

Calculate NF

$$
{ \begin{array}{l} { \mathrm { N R } = { \frac { S _ { i } / N _ { i } } { S _ { o } / N _ { o } } } = { \frac { 10 } { 5 } } = 2 } \\{ \mathrm { N F } = 10 \log _ { 10 } { \frac { S _ { i } / N _ { i } } { S _ { o } / N _ { o } } } = 10 \log _ { 10 } \mathrm { N R } } \\{ = 10 \log _ { 10 } { \frac { 10 } { 5 } } = 10 \log _ { 10 } 2 } \\{ = 3 \, \mathrm { d B } } \end{array} }
$$

<br><span class='markdown-page-line'>---------------------------------------------<span id='page8' class='markdown-page-text'>[ 第8页 ]</span>---------------------------------------------</span><br><br>

# Spectrum Management

control and licensing of frequencies:

Wherever you may be in the world, there is usually some government department that manages radio spectrum.

In Qatar, it is the Supreme Council of Information and Communications Technology (SCICT).

Some of the things they would control are:

Who can use what frequency

How much power they are allowed to transmitHow much bandwidth they are allowed to use Where they can position their transmitter

<br><span class='markdown-page-line'>---------------------------------------------<span id='page9' class='markdown-page-text'>[ 第9页 ]</span>---------------------------------------------</span><br><br>

# Basic Mobile Operation

Calling Patterns in Mobile Communication Systems:

Simplex - one-way communications where one station can only

:ransmit and the other can only receive.

An example is a common radio or television station.

Half-duplex - two-way communications where only one station

can transmit at a time. Each station takes turns transmitting.

An example is two people using "walkie-talkies".

![](images/37dd0d6b2ade17abd3731cda28419476bc52d3a38e0cf80e1371ad2fc91c5faf_38.jpg){width=38%}

![](images/a4036b80288a1e4da2ba832771fd72de575b289bb6dff3ee71a5ccce4d3e830d_26.jpg){width=26%}

<br><span class='markdown-page-line'>---------------------------------------------<span id='page10' class='markdown-page-text'>[ 第10页 ]</span>---------------------------------------------</span><br><br>

Full-duplex - two-way communications where both stations can transmit and receive at the same time.

An example involves two people using mobile phones to communicate. Both people can speak at the same time.

![](images/1a2f17139180d2cca3fba136e16f420ad9ebdfee4a7f65debe677e16a5847d19_40.jpg){width=40%}

<br><span class='markdown-page-line'>---------------------------------------------<span id='page11' class='markdown-page-text'>[ 第11页 ]</span>---------------------------------------------</span><br><br>

# Radio Frequency Interference

Radio frequency interference (RFI) is the presence of unwanted signals that detrimentally impact a radio communication system.

Types of Radio Frequency Interference:

Co-Channel Interference (CCI) - Two different radio transmitters operating on the same frequency.

The separation between the 2 transmitter sites should be enough to ensure their coverage does not overlap.

If coverage does overlap you will have co-channel interference issues.

![](images/150e613e06904ba90e079ccfac1b3c3db245c60bc5d6c21ad05de317bd082209_28.jpg){width=28%}

![](images/cc4ec2ee70a12751cd85818b3cb62329722a054b43a3a7efc7f1a5eb5f85c6e6_21.jpg){width=21%} Cellular Coverage Pattern of frequency No. 1

<br><span class='markdown-page-line'>---------------------------------------------<span id='page12' class='markdown-page-text'>[ 第12页 ]</span>---------------------------------------------</span><br><br>

# Radio Frequency Interference:

Adjacent Channel Interference - It is the interference caused to the signal which is adjacent in frequency to the desired signal. Imperfect receiver side filters allow the neighboring signal to mix with the actual pass band.

If one transmitter is operating on 150 MHz and the channel width is 30 KHz then the adjacent channels are 149.970 MHz and 150.030 MHz for example.

Adjacent channels can be a cause of Receiver Desensitization.receiving filter

![](images/84e268e773104d6405501904f5326545a0a7d0f147d6ba5d6c64829c3adcbdcc_64.jpg){width=64%}

<br><span class='markdown-page-line'>---------------------------------------------<span id='page13' class='markdown-page-text'>[ 第13页 ]</span>---------------------------------------------</span><br><br>

Harmonic distortion

A harmonic is a wave or signal whose frequency is an integer multiple of the frequency of the same reference signal or wave.

In ideal system, a pure sinusoidal signal would result in a single peak at a specific frequency. Fundamental

![](images/07ffd28ad2d23f18fab512873df5d68d3d066963c7d4c8f2011dff703c7fa2dd_43.jpg){width=43%}

<br><span class='markdown-page-line'>---------------------------------------------<span id='page14' class='markdown-page-text'>[ 第14页 ]</span>---------------------------------------------</span><br><br>

# Radio Frequency Interference (RFI) – Harmonic Distortion

# 

#UN FOF

Harmonic distortion can be seen in any analog signal that experiences some level of nonlinearity. When a signal of $f_{1}$ frequency passes through a nonlinear system (for example. Power amplifier), the output of the system consists of $f_{1}$ and its harmonics.

![](images/3a8515a8cea034f0fe78f58327a28d04ce6381e23e694bda023531b2ad39d5b5_59.jpg){width=59%} Harmonic generation in a power amplifier

!

Good filtering can remove most of them

<br><span class='markdown-page-line'>---------------------------------------------<span id='page15' class='markdown-page-text'>[ 第15页 ]</span>---------------------------------------------</span><br><br>

# Example

Determine

$2^{nd}$, $3^{rd}$, and $12^{th}$ harmonics for a 1 kHz repetitive wave

Solution:

Harmonic frequencies are simply integer multiples of the fundamental frequency:

$2^{\mathrm{nd}}$ harmonic = 2 x fundamental frequency = $2 \times 1$ kHz = $2$ kHz

$3^{\mathrm{rd}}$ harmonic = 3 x fundamental frequency = $3 \times 1$ kHz = $3$ kHz

$12^{\mathrm{th}}$ harmonic = $12$ x fundamental frequency = $12 \times 1$ kHz = $12$ k