import machine
import pca9685
import servo
import time

sda_pin = machine.Pin(21)
scl_pin = machine.Pin(22)




i2c = machine.I2C(sda = sda_pin, scl = scl_pin)
i2c_status = i2c.scan()
pca = pca9685.PCA9685(i2c)
pca.freq(60)

'''
Here we have some description of servos and 
where exactly they are pinned to PCA9685
-------------------------------------------
Index figner UP ->15
Index figner DOWN -> 14
------------
Pinky UP -> 13
Pinky DOWN -> 12
------------
Ring Finger UP -> 11
Ring Finger Down -> 10
------------
Middle finger UP -> 09
Middle finger DOWN -> 08
------------
'''

class Finger():
    def __init__():

