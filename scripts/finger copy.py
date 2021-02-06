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

class Finger():
    def __init__(self,name, servo_up, servo_down):
        self.name = name
        self.servo_up = servo_up
        self.servo_down = servo_down
        self.up_position = 0
        self.down_position = 0

    def load_class_servos(self):
        type(self).servo_up_pin = self.servo_up
        type(self).servo_down_pin = self.servo_down


    def servo_movement(self, servo, target_degree = None):
        '''Function set servomotor position to target degree'''

        if target_degree == None: target_degree = 180

        if servo == self.servo_down: self.down_position = target_degree
        if servo == self.servo_up: self.down_position = target_degree
        
        for degree in range(0, target_degree):
            servos.position(servo, degrees = degree)
            time.sleep(0.002)

        time.sleep(0.5)

    def release(self):
        servos.position(self.servo_up, degrees = 0)
        time.sleep(0.5)
        servos.position(self.servo_down, degrees = 0)
        time.sleep(0.5)

    def move(self, direction):

        '''
        The function executes the motion of the finger according to the direction that was specified as a parameter
        Direction has 3 positions, 0 -> rest, 1 -> Move up, 2 -> Move down
        '''

        if direction == 0:
            self.release()
            time.sleep(0.2)
        
        if direction == 1 :
            servos.position(self.servo_down, degrees = 0)
            self.down_position = 0
            time.sleep(0.25)
            self.servo_movement(self.servo_up)
            time.sleep(0.5)

        
        if direction == 2:
            servos.position(self.servo_up, degrees = 0)
            time.sleep(0.5)
            self.servo_movement(self.servo_down)
            time.sleep(0.5)
    

    def get_position(self):
        return [self.up_position,self.down_position]   