# Pulse Width Modulation

Pulse width modulation or pulse duration modulation is a technique where we vary the width of a square pulse to control the power supplied to a connected device.

**Pulse Width** - The duty cycle is the percentage of the ratio of the pulse width of the signal to the total time period T . Formula to calculate pulse width

$$ %Duty Cycle = \frac{T_{ON}}{T_{ON}+T_{OFF}} $$

The following figure shows the pulses of different widths

![Duty Cycle](/duty.png "Duty Cycle")


There are six PWM pins in Arduino Uno. Arduino Uno PWM channel has 8-bitresolution. These PWM pins are represented by the symbol ‘∼ ’. The Arduino PWM pins are 3,5,6,9,10 and 11.

| PWM Pins           | Frequency |
|--------------------|-----------|
| 5, 6              | 980 Hz    |
| 3, 9, 10, 11      | 490 Hz    |

