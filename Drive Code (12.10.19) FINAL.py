
# VEX EDR Python-Project - BEST Robotics
import vex
import sys

#Notes Removed to preserve a fast download/compile time.

#CONFIGURE START
joystick1 = vex.Joystick()
right         = vex.Motor(2)
left          = vex.Motor(3)
elevator      = vex.Motor(4)
servo         = vex.Servo(5)
auto          = vex.Motor(6)
#CONFIGURE END

joystick1.set_deadband(15)  

while True:

#---------------------------------
#STANDARD (MANUAL COMMANDS)
#---------------------------------

#DRIVETRAIN CODE (FINAL)
    
    left.run(joystick1.axis2())
    right.run(joystick1.axis3())
    
#ELEVATOR CODE (FINAL)
    
    #DOWN
    if joystick1.b7down(): 
        elevator.run(25)
    
    #UP
    if joystick1.b7up():
        elevator.run(-85) 
    
#SERVO CODE (FINAL)
    
    #UP
    if joystick1.b5up():
        servo.position(100)
        pass
    
    #DOWN
    if joystick1.b5down():
        servo.position(0)
        pass
    
#ZERO / STOP ALL MOVEMENT (FINAL)

    if joystick1.b7left():
        elevator.run(0)
        auto.run(0)
        left.run(0)
        right.run(0)
    
#---------------------------------  
        
        
        
#---------------------------------
        
#NONSTANDARD CONTROL (AUTOMATIC BASIC COMMANDS)
#---------------------------------

#AIM ASSIST
    
    if joystick1.b6up():
        servo.position(0)
        elevator.run(-100)
        sys.sleep(5)
        elevator.off
        elevator.run(0)
        
        elevator.run(25)
        sys.sleep(3.6)
        elevator.off
        elevator.run(0)
        
        pass
    
#AUTO HOOK CODE (FINAL)
    if joystick1.b6down():
        auto.run(-100)
        sys.sleep(2)
        auto.off
        auto.run(0)
        
        auto.run(30)
        sys.sleep(.5)
        auto.off
        auto.run(0)    
        pass
    
#---------------------------------



#---------------------------------
#TESTING CONTROLS (BETA COMMANDS)
#---------------------------------
    #AUTONOMOUS
    
    if joystick1.b8left():
        
        left.run(50)
        right.run(50)
        sys.sleep(6.5)
        right.run(0)    
        left.off(0)
        right.off
        left.off
    
        auto.run(-15) #AUTO HOOK DROP
        sys.sleep(3)
        auto.off
        auto.run(0) 
        
        left.run(-30)
        right.run(-30)
        sys.sleep(1)
        left.off
        right.off
        
        pass

#---------------------------------



pass