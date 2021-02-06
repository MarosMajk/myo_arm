import machine
import pca9685
import servo
import time
import finger



sda_pin = machine.Pin(21)
scl_pin = machine.Pin(22)


i2c = machine.I2C(sda = sda_pin, scl = scl_pin)

i2c_status = i2c.scan()
pca = pca9685.PCA9685(i2c)
pca.freq(60)


servos = servo.Servos(i2c)


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


index_f = ("Index Finger",15,14)
pinky_f = ("Pinky Finger",13,12)
ring_f = ("Ring finger",11,10)
middle_f = ("Middle finger",9,8)

class Hand():
    
    def __init__(self, index, middle, ring, pinky):
        self.index_finger = index
        self.middle_finger = middle
        self.ring_finger = ring
        self.pinky_finger = pinky 


    def check_input(self):
        all_variables = self.__dict__.keys()
        print(self.index_finger[0])





myo_hand = Hand(index_f, middle_f, ring_f, pinky_f)


myo_hand.check_input()