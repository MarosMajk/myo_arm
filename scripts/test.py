import machine
import servo
import time

sda_pin = machine.Pin(21)
scl_pin = machine.Pin(22)

i2c = machine.I2C(sda = sda_pin, scl = scl_pin)

print(i2c.scan())

servos = servo.Servos(i2c)
#Ukazovak up -> 15
#Ukazovak Down -> 14
#Malicek Up -> 13
#Malicek Down >12
#Ring Up -> 11
#Rign Down -> 10
#Middle Up -> 09
#Midle Down -> 08



#def go_up():
#    for i in range(9,16,2):
#        print(i)
#        servos.position(i, degrees = 180)
#    
#    time.sleep(3)

#def go_down():
#    for i in range(8,16,2):
#        print(i)
#        servos.position(i, degrees = 180)
#    time.sleep(3)

#def release():
#    for i in range(8,16):
#        print(i)
#        servos.position(i, degrees = 0)
    
#    time.sleep(2)

#release()
#go_up()
#release()
#go_down()

#time.sleep(8)
#release()
#go_down()

#servo_pin = 15  
#servos.position(servo_pin, degrees = 0)
#time.sleep(2)
#servos.position(servo_pin, degrees = 180)
#time.sleep(5)
#servos.position(15, degrees = 0)


#prstenik
#servos.position(10, degrees = 0)
#servos.position(9, degrees = 0)

#prostredník
#for i in range(0,3):
    #servos.position(12, degrees = 0)
    
    #time.sleep(1.5)
    #servos.position(15, degrees = 180)
    #time.sleep(2)
    #servos.position(15, degrees = 0)
    #time.sleep(2)
#servos.position(7, degrees = 60)
#servos.position(6, degrees = 0)

#servos.position(3, degrees = 0)

#servos.position(8, degrees = 0)
#servos.position(7, degrees = 0)