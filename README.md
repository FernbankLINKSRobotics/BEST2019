# BEST2019
Mind the comments...

This is a single-line, python3 program, run through a VEX
EDR Cortex.

There are three main operations:
1. Autonomous Mission.
2. Elevator Function.
3. Two Motor Drive Train.

Evaluation:
1. i. The autonomous mission was designed around dropping a game piece, 
the conduit, at one or both of two destinations.  This process
only required the use of two main parts of the robot, the drive-
train and the small motor controlling the conduit "cradle," or box.

    ii. A. Firstly, to start the "autonomous period," the drive must
press one of the buttons, which was noted a being, for example,
"if joystick.b8up(True):"

    ii. B. The autonomous mission was completed through the use of the
"sys.sleep()" function, which simply tells the robot to stop all
other processes besides which is running in the lines before it.

For example:
#MAKE SURE TO VIEW THIS IN RAW TEXT!
#----------------------------------------------------------------------------------------------
"""                                                                                           |
while True:                 |   To keep the program running (not just one time!).             |
                            |                                                                 |
  if joystick.b8up(True):   |   Starting the autonomous period.                               |
                            |                                                                 |
    left.run(100)           |   Beginning the run of the left-side drive motor.               |
    right.run(100)          |   Beginning the run of the right-side drive motor.              |
                            |                                                                 |
    sys.sleep(2)            |   Telling the system to only run both motors for "2" seconds.   |
                            |                                                                 |
    left.off                |   Ending the run of the left-side drive motor.                  |
    #left.run(0)            |   Setting the run of the left-side motor to 0% power.           |
    right.off               |   Ending the run of the right-side drive motor.                 |
    #right.run(0)           |   Setting the run of the right-side motor to 0% power           |
                            |                                                                 |
    pass                    |   Telling the program to continue after this task is completed. |
"""                                                                                           |
#----------------------------------------------------------------------------------------------

Explained:
  This bit of code simply tells the robot to drive forward for 2 seconds, both drive motors at 
100% power usage.  Of course, after this 2 second period, both motors will continue driving if
not dictated otherwise.  That is why "left.off" or "left.run(0)" are part of the program, simply
telling the program to discontinue motor usage after the 2 second period, either through telling
the program to turn off the motors or to run both motors at 0% power usage (synonymous).



+ Further Evaluation:
  Using a continuous "while True" statement, this program was run until the Cortex or the Joystick
  were unplugged, although one could add an "if" statement regarding a button on the joystick to 
  activate a "quit()" command.  Although, not included in the "while True" statement were the variables
  and deadband establishment.  In other words, although it should influence the software (by putting
  the variables and deadband within the "while True" statement), it is not necessary.  

+ Within RobotMeshNet Studio Code, one cannot possibly add more Python "Imports" specifically since 
  this platform is a third party operating away from any possibility of downloading more additional
  software for your own software.  Therefore, one is limited to the import of "sys" and "vex."  It is 
  only through the process of purchasing and installing the "Desktop Version" of RobotMeshNet Studio 
  Code that one could possibly download more Python imports.



+ Debugging/Finding and Identifying Errors:
  Since this is only a third-party software for injecting code, it is not very updated and expansive.
  With this in mind, it should be clear to the programmer that troubleshooting and debugging are not
  very profound, meaning there are very few Wikis and those that exist provide very little help.


+ If you receive an error within the browser version of RobotMeshNet Studio Code, go back and double
  -check the program.  Keep in mind that RobotMeshNet Studio Code (in general) is very picky when it
  comes to the placement of certain statements.  With that clear, ensure that indent and syntax are
  accounted for and do not become errors.  

+ If you have already checked you program, have someone else check over it.  Since two pairs of eyes
  are greatly better than one.  

+ If you continue to receive an error that RobotMeshNet Studio does not catch: after updating your
  program, make sure to watch the blinking lights on the cortex, specifically the top two LED lights.
  
+ If, after you have finished "Running without Debugger," the "Robot" LED Light is blinking Red, 
  the problem could be one of three things:
 
  - The Program.
  - The Battery.
  - The wiring/electrical connection.
  
+ While dealing with the Program, I would suggest returning to a version of your program that you 
  know has worked in the past.  If you run this program and you see that it is not working, make sure
  that first, check and/or switch out the battery, then check all the wiring (meticulously).  If neither
  of these solutions work, try turning on and off the cortex and updating it (turning off, unplugging
  the USB-USB cord, turning on, and plugging the USB-USB cord back in, then update program).

+ Disclaimer, be patient while working with this process of fixing the robot, since one of the 
  overwhelming possibilities for error is someone else's doing (e.g. Accidentally unplugging or 
  misplacing dejected wires.).  
  

  


+ Updating Programs:
  First: Connect to Robot's cortex (through USB-USB Male Cord)
  Second: Click on "Download" and wait until complete.
  Third: Click on "Compile" and wait until complete.
  Fourth: Click on "Run without Debugger" and wait until complete.
  Fifth: Disconnect from Robot's cortex.

+ Disclaimer:
  This method worked as of October of 2019 and has not been tried as of the publishing of this 
  README.
  
+ For any commments/questions, email me at "ryanb44363@gmail.com" with the subject "BEST2019 Query"
  plus your name.
  
  Thank you.
