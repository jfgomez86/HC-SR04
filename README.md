# README

This code demonstrates how to use the HC-SR04 sensor for measuring distances by timing  ultrasound pulses.

# Setup

The sensor uses 5v logic and the ECHO pin feeds voltage back to the GPIO therefore it is needed to implement a Voltage Divider circuit in order to reduce the voltage to 3.3v. I used three 1k Ohms resistors in order to do so:

```
5v (ECHO) --- R1 --- R2 --- R3 --- GND
                  |
                GPIO
```

The rest of the circuit is simple:

```
RPi   --> HC-SR04
5v    --> vcc
GPIO  --> Trigger
GPIO  --> Echo (Using Voltage Divider sub-circuit above)
GND   --> GND
```

# Usage

Simply load base.py into a python console and run `base.measure()`. The distance will be printed on the screen every 0.5s. Press `<Control>-C` to stop.
