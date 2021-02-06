import machine
import pca9685
import servo
import time

sda_pin = machine.Pin(21)
scl_pin = machine.Pin(22)


i2c = machine.I2C(sda = sda_pin, scl = scl_pin)
pca = pca9685.PCA9685(i2c)
pca.freq(60)



print(i2c.scan())



servos = servo.Servos(i2c)

servo_pin = 15   

servos.position(servo_pin, degrees = 0)
time.sleep(2)

for degrees in range(0,180):
    servos.position(servo_pin, degrees = degrees)
    time.sleep(0.002)

#time.sleep(0.5)

servos.position(servo_pin, degrees = 0)




#Ukazovak up -> 15
#Ukazovak Down -> 14

#Malicek Up -> Nefunguje
#Malicek Down >12

#Ring Up -> 11
#Rign Down -> 10

#Middle Up -> 09
#Midle Down -> 08

'''
class Finger(PIN_UP, PIN_DOWN):
    def __init__(up, down):
        pass

    def get_position():
        pass

    def positiion(param = None):
        0 -> reset (obe sli na nulu)
        1 -> hore
        2 -> dole


    




ukazovak = Finger(15, 14)

ukazovak.position(1)


Finger.reset()'''