from controller import Robot
robot=Robot()
timestep = 32
import time
t = 0.05
max_speed=9.42 # angular speed (If the robot get stucked somewhere so pls use 6.28 instead of 9.42)
left_motor=robot.getDevice('left-motor') #name of the left motor in the robot
right_motor=robot.getDevice('right-motor') #name of the right motor in the robot
left_motor.setPosition(float('inf'))
left_motor.setVelocity(0.0) #initial speed is 0
right_motor.setPosition(float('inf'))
right_motor.setVelocity(0.0)  #initial speed is 0
left_ir=robot.getDevice('ir_left') #name of the left sensor in the robot
left_ir.enable(timestep)
right_ir=robot.getDevice('ir_right') #name of the right sensor in the robot
right_ir.enable(timestep)
middle_ir=robot.getDevice('ir_middle') #name of the right sensor in the robot
middle_ir.enable(timestep)
left1_ir=robot.getDevice('ir_left1') #name of the left1 sensor for stop in the robot
left1_ir.enable(timestep)
right1_ir=robot.getDevice('ir_right1') #name of the right1 sensor for stop in the robot
right1_ir.enable(timestep)
while robot.step(timestep) != - 1 : # an infinite loop delibrately made
    left_ir_value=left_ir.getValue()
    right_ir_value=right_ir.getValue()
    middle_ir_value=middle_ir.getValue()
    left1_ir_value=left1_ir.getValue()  
    right1_ir_value=right1_ir.getValue()  
    print("left: {} middle: {} right: {} left1: {} right1: {}".format(left_ir_value, middle_ir_value, right_ir_value, left1_ir_value, right1_ir_value))
    if (middle_ir_value > 2 * left_ir_value) and (middle_ir_value > 2 * right_ir_value) : # Go Straight
        left_speed= max_speed
        right_speed= max_speed
        left_motor.setVelocity (left_speed)
        right_motor.setVelocity (right_speed)
    elif (middle_ir_value > 2 * right_ir_value) and (left_ir_value > 2 * right_ir_value) : # Take left
        left_speed= 0.005 * max_speed
        right_speed= max_speed
        left_motor.setVelocity (left_speed)
        right_motor.setVelocity (right_speed)
    elif (middle_ir_value > 1.2* left_ir_value) and (right_ir_value > 2 * left_ir_value) : # Take Right
        left_speed= max_speed
        right_speed= 0.005 * max_speed
        left_motor.setVelocity (left_speed)
        right_motor.setVelocity (right_speed)
    elif (middle_ir_value < 100) and (left_ir_value < 100) and (right_ir_value < 100) : # Take U-Turn
        time.sleep(t)
        left_speed= -max_speed
        right_speed= max_speed
        left_motor.setVelocity (left_speed)
        right_motor.setVelocity (right_speed)
    elif (middle_ir_value < right1_ir_value) and (middle_ir_value < left1_ir_value) : # Be Stopped
        left_speed= 0.0
        right_speed=  0.0
        left_motor.setVelocity (left_speed)
        right_motor.setVelocity (right_speed)
    elif (left_ir_value > 100) and (right_ir_value > 100) and (middle_ir_value > 100) : # Take Left (instead to be Stopped)
        left_speed= 0.005 * max_speed
        right_speed= max_speed
        left_motor.setVelocity (left_speed)
        right_motor.setVelocity (right_speed)
