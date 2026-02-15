<br><span class='markdown-page-line'>---------------------------------------------<span id='page1' class='markdown-page-text'>[ 第1页 ]</span>---------------------------------------------</span><br><br>

# Introduction to Analog Communications – Fundamentals of Communication Systems

AETN2121 – Analog and Digital Communication

<br><span class='markdown-page-line'>---------------------------------------------<span id='page2' class='markdown-page-text'>[ 第2页 ]</span>---------------------------------------------</span><br><br>

# Course Topics

Topic 1: Introduction to analog communication systemsTopic 2: Signals in the frequency domainTopic 3: AM modulation and demodulationTopic 4: FM modulation and demodulationTopic 5: Complex systems (FM stereo)Topic 6: Sampling and QuantizationTopic 7: Binary modulationTopic 8: M-ary ModulationTopic 9: BER performance and bandwidth efficiency

<br><span class='markdown-page-line'>---------------------------------------------<span id='page3' class='markdown-page-text'>[ 第3页 ]</span>---------------------------------------------</span><br><br>

# Course Topics

# Topic 1: Introduction to analog communication systems

![](images/b87e6e178f5802452b5bcae262f6842bb203e9a3e2b1fa1b484267fe408376a3_97.jpg){width=97%}

<br><span class='markdown-page-line'>---------------------------------------------<span id='page4' class='markdown-page-text'>[ 第4页 ]</span>---------------------------------------------</span><br><br>

# Learning Outcomes

By end of this lecture, student should be able to:

Define the radio frequency spectrum

Define general communication system components

Recognize basic requirements and limitations of a communication system

<br><span class='markdown-page-line'>---------------------------------------------<span id='page5' class='markdown-page-text'>[ 第5页 ]</span>---------------------------------------------</span><br><br>

# The Electromagnetic Spectrum

Electromagnetic energy travels in the form of a wave.

![](images/1c82fb73d8b68278a56afcdbb8ce03a81ee8d0fafac1076595c9cfc8ecedb6d8_90.jpg){width=90%}

Frequency and wavelength. (a) One cycle. (b) One wavelength.

<br><span class='markdown-page-line'>---------------------------------------------<span id='page6' class='markdown-page-text'>[ 第6页 ]</span>---------------------------------------------</span><br><br>

# The Electromagnetic Spectrum

Waves have three characteristics:

1- wave velocity (v): depends on the medium. For example · sound wave at sea level travels at 335 m/s · an EM wave in vacuum travels at c =3 x $10^{8}$ m/s 2- frequency (f): rate of wave repetition

3- wavelength ($\lambda$): length of one cycle in the medium

These three characteristics are related to each other by this equation:

$\lambda = \vee / f;$

For EM waves, $\lambda = \mathrm{c} / \mathrm{f}$

<br><span class='markdown-page-line'>---------------------------------------------<span id='page7' class='markdown-page-text'>[ 第7页 ]</span>---------------------------------------------</span><br><br>

# Electromagnetic Spectrum

Table 1-6 International Telecommunications Union (ITU) Band Designations

| Band Number | Frequency Range a | Designations |
| --- | --- | --- |
| 2 | 30 Hz-300 Hz | ELF (extremely low frequencies) |
| 3 | 0.3 kHz-3 kHz | VF (voice frequencies) |
| 4 | 3 kHz-30 kHz | VLF (very low frequencies) |
| 5 | 30 kHz-300 kHz | LF (low frequencies) |
| 6 | 0.3 MHz-3 MHz | MF (medium frequencies) |
| 7 | 3 MHz-30 MHz | HF (high frequencies) |
| 8 | 30 MHz-300 MHz | VHF (very high frequencies) |
| 9 | 300 MHz-3 GHz | UHF (ultrahigh frequencies) |
| 10 | 3 GHz-30 GHz | SHF (superhigh frequencies) |
| 11 | 30 GHz-300 GHz | EHF (extremely high frequencies) |
| 12 | 0.3 THz-3 THz | Infrared light |
| 13 | 3 THz-30 THz | Infrared light |
| 14 | 30 THz-300 THz | Infrared light |
| 15 | 0.3 PHz-3 PHz | Visible light |
| 16 | 3 PHz-30 PHz | Ultraviolet light |
| 17 | 30 PHz-300 PHz | X rays |
| 18 | 0.3 EHz-3 EHz | Gamma rays |
| 19 | 3 EHz-30 EHz | Cosmic rays |$^{a}10^{0}$, hertz (Hz); $10^{3}$, kilohertz (kHz); $10^{6}$, megahertz (MHz); $10^{9}$, gigahertz (GHz); $10^{12}$, terahertz (THz); $10^{15}$, petahertz (PHz); $10^{18}$, exahertz (EHz).

<br><span class='markdown-page-line'>---------------------------------------------<span id='page8' class='markdown-page-text'>[ 第8页 ]</span>---------------------------------------------</span><br><br>

# Electromagnetic Spectrum

# The range of electromagnetic signals encompassing all frequencies is referred to as the electromagnetic spectrum.

← Increasing Frequency (v)

![](images/bd53a868327d8c4771b56a2020307c541d95f3f1327129b81d1235ad97979d23_79.jpg){width=79%}

<br><span class='markdown-page-line'>---------------------------------------------<span id='page9' class='markdown-page-text'>[ 第9页 ]</span>---------------------------------------------</span><br><br>

# Electromagnetic Spectrum

The electromagnetic spectrum starts at 0 Hz, and extends to higher and higher frequencies.

As the frequency increases, its energy level also increases. Signals in the X-ray band, for example, are very energetic and can pass through most materials.

EM spectrum is a national resource, and it is up to the government of each country to regulate the spectrum within its borders.

e.g. a radio station needs a license before it can begin to broadcast over a particular frequency.

<br><span class='markdown-page-line'>---------------------------------------------<span id='page10' class='markdown-page-text'>[ 第10页 ]</span>---------------------------------------------</span><br><br>

# Signals

Analogue

AMPLITUDE

![](images/51977e32ea9311de036eedf2b3ec49b8e54804dd3aea24daabe0279dc02ba360_34.jpg){width=34%}

![](images/230c5ffe8d817e9cd235167a2b9cab871b3c371682608fb3e21cf0b23e979150_34.jpg){width=34%} Digital

take any value in their domain continuous in time

Limited set of values

For digital communications, also discrete in time

Binary has only two values o and 1

<br><span class='markdown-page-line'>---------------------------------------------<span id='page11' class='markdown-page-text'>[ 第11页 ]</span>---------------------------------------------</span><br><br>

# Signal Properties

Two properties of signals that are important for communication:

# 1. Power

# 2. Bandwidth

Lower transmit power implies longer battery life for your smartphone

Bandwidth is the total range of frequencies associated with a signal or a device or a channel

But lower transmit power also makes signal harder to detect at the receiver in the presence of noise!

Example: for speech/human voice signals, frequency ranges from 300 Hz to 3100 Hz. Therefore speech signal has a bandwidth of 2800 Hz

<br><span class='markdown-page-line'>---------------------------------------------<span id='page12' class='markdown-page-text'>[ 第12页 ]</span>---------------------------------------------</span><br><br>

# Definition

# Communication is the process of exchanging information.

![](images/c3a6a309be6b19ede9ff081dd512d6a0a059b93fb665b46258056e2578e13812_90.jpg){width=90%}

Elements of a communication system.

<br><span class='markdown-page-line'>---------------------------------------------<span id='page13' class='markdown-page-text'>[ 第13页 ]</span>---------------------------------------------</span><br><br>

# Block Diagram Components

Source of information: May be analogue (voice, music, video), or digital (e.g., e-mail, any file on your computer)

Transmitter: converts electrical signal into form suitable for channel. Modulator. Amlifier

Channel: medium used to transmit the signal to the receiver - E.g., optical fibre, wireless channel, magnetic recording... May distort transmitted signal, e.g., add noise or attenuate it Receiver: reconstructs the source of information from the received signal. Demodulator. Amplifier User of Information: for whom the information is intended Noise degrades or interferes with transmitted information.

<br><span class='markdown-page-line'>---------------------------------------------<span id='page14' class='markdown-page-text'>[ 第14页 ]</span>---------------------------------------------</span><br><br>

# Basic Requirements of Communication System

#Jagamcée duhoña#for science & technology#UNIVERSITY OF DOHA#FOR SCIENCE & TECHNOLOGY

Rate of information transfer:

how fast the information can be transferred

Purity of signal received:

whether the signal received is the same as the signal being transmit

Simplicity of the system

the simpler the system, the better

Reliability