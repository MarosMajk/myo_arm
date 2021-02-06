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

class Finger():
    def __init__(self,name, servo_up, servo_down):
        self.name = name
        self.servo_up = servo_up
        self.servo_down = servo_down

    def servo_movement(self, servo, target_degree = None):

        '''Function set servomotor position to target degree'''
        
        if target_degree == None: target_degree = 180
        
        for degree in range(0, target_degree):
            servos.position(servo, degrees = degree)
            time.sleep(0.002)

        time.sleep(0.5)
        

    def movement(self, direction):
        if direction == "Up":
            servos.position(self.servo_down, degrees = 0)
            time.sleep(0.75)
            self.servo_movement(self.servo_up)
            time.sleep(0.5)


        if direction == "Down":
            servos.position(self.servo_up, degrees = 0)
            time.sleep(0.75)
            self.servo_movement(self.servo_down)
            time.sleep(0.5)
            
    def release(self):
        servos.position(self.servo_up, degrees = 0)
        time.sleep(0.5)
        servos.position(self.servo_down, degrees = 0)
        time.sleep(0.5)



index_finger = Finger("index finger",15,14)
middle_finger = Finger("Middle finger",9,8)
ring_finger = Finger("Ring finger",11,10)
pinky = Finger("pinky",13,12)




index_finger.release()
index_finger.movement("Up")
index_finger.movement("Down")
index_finger.release()



