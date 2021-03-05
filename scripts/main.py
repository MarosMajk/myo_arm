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
Thumb UP -> 0
Thumb Down - > 1
Thumb special -> x
------------
Index figner UP -> 15 *
Index figner DOWN -> 14
------------
Middle finger UP -> 11 *
Middle finger DOWN -> 10 *
------------
Ring Finger UP -> 5*
Ring Finger Down -> 4 *
------------
Pinky UP -> 9 *
Pinky DOWN -> 8 *
------------
'''

#thumb = ("Thumb",1,2,3)



index_finger = finger.Finger("Index Finger",14,13)
middle_finger = finger.Finger("Middle finger",11,8)
ring_finger = finger.Finger("Ring finger",5,4)
pinky_finger = finger.Finger("Pinky Finger",6,7)


class Hand():
    
    def __init__(self,index, middle, ring, pinky):
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
        time.sleep(0.1)
        servos.position(1, degrees = 0)
        time.sleep(0.1)

    def fist(self):
        self.set_position(1)
        time.sleep(0.1)
        servos.position(1, degrees = 0)
        time.sleep(0.1)
        servos.position(2, degrees = 140)
        time.sleep(0.1)

    def spread_fingers(self):
        self.set_position(2)
        time.sleep(0.1)
        servos.position(2, degrees = 0)
        time.sleep(0.1)
        servos.position(1, degrees = 180)
        time.sleep(0.1)



    def rock_n_roll(self):
        self.reset()
        servos.position(self.index_finger.servo_up, degrees = 180)
        servos.position(self.pinky_finger.servo_up, degrees = 180)

    def piano(self):
        pass


myo_hand = Hand(index_finger,middle_finger,ring_finger,pinky_finger)
time.sleep(3)
myo_hand.reset()



time.sleep(0.1)
myo_hand.spread_fingers()
time.sleep(2)
myo_hand.reset()
myo_hand.fist()
time.sleep(8)
myo_hand.spread_fingers()
time.sleep(4)
myo_hand.reset()


