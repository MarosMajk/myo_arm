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
Thumb UP ->
Thumb Down - >
'''



index_finger = finger.Finger("Index Finger",15,14)
pinky_finger = finger.Finger("Pinky Finger",13,12)
ring_finger = finger.Finger("Ring finger",5,4)
middle_finger = finger.Finger("Middle finger",10,8)
thumb_finger = ("Thumb,")


class Hand():
    
    def __init__(self, index, middle, ring, pinky):
        self.index_finger = index
        self.middle_finger = middle
        self.ring_finger = ring
        self.pinky_finger = pinky 

    def set_position(self, position):
        if (position == 0) or (position == 1) or (position == 2):
            self.index_finger.move(position)
            self.middle_finger.move(position)
            self.ring_finger.move(position)
            self.pinky_finger.move(position)


    def reset(self):
        self.set_position(0)

    def fist(self):
        self.set_position(2)

    def spread_fingers(self):
        self.set_position(1)

    def rock_n_roll(self):
        self.reset()
        servos.position(self.index_finger.servo_up, degrees = 180)
        servos.position(self.pinky_finger.servo_up, degrees = 180)

    def piano(self):
        pass



myo_hand = Hand(index_finger, middle_finger, ring_finger, pinky_finger)


myo_hand.reset()

#pinky_finger.move(2)


#myo_hand.spread_fingers()

#myo_hand.reset()

#myo_hand.fist()

#myo_hand.rock_n_roll()


#servos.position(2, degrees = 160)

