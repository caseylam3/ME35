#Takes an image using a raspberry pi camera & finds the percentage of pixels in the image that are red
#by Maddie Pero

#import libraries 
from picamera2 import Picamera2 
import cv2 as cv 
import numpy as np
from libcamera import controls
import time
#libraries for motor
import RPi.GPIO as GPIO
from ThreadStepperLib import Stepper


picam2 = Picamera2()

#configure the picamera
capture_config = picam2.create_still_configuration() #automatically 4608x2592 width by height (columns by rows) pixels
picam2.configure(capture_config)
picam2.set_controls({"AfMode": controls.AfModeEnum.Continuous}) #sets auto focus mode

picam2.start() #must start the camera before taking any images
time.sleep(0.1)

def moveSteps(stepright, stepleft):
    
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(Motor1[0], GPIO.OUT)
    GPIO.setup(Motor1[1], GPIO.OUT)
    GPIO.setup(Motor1[2], GPIO.OUT)
    GPIO.setup(Motor1[3], GPIO.OUT)

    GPIO.output(Motor1[0], GPIO.LOW)
    GPIO.output(Motor1[1], GPIO.LOW)
    GPIO.output(Motor1[2], GPIO.LOW)
    GPIO.output(Motor1[3], GPIO.LOW)

    GPIO.setup(Motor2[0], GPIO.OUT)
    GPIO.setup(Motor2[1], GPIO.OUT)
    GPIO.setup(Motor2[2], GPIO.OUT)
    GPIO.setup(Motor2[3], GPIO.OUT)

    GPIO.output(Motor2[0], GPIO.LOW)
    GPIO.output(Motor2[1], GPIO.LOW)
    GPIO.output(Motor2[2], GPIO.LOW)
    GPIO.output(Motor2[3], GPIO.LOW)

    try: 
        # Define the steps per revolution for the motor 
        steps_rev = 200

        # Set the thread number, thread ID, motor, number of steps to move, steps per revolution,
        # and the speed in revolutions per minute
        stepper1 = Stepper(1,"Motor #1",Motor1, -1-stepright, steps_rev, 20)
        stepper2 = Stepper(2,"Motor #2",Motor2, 1+stepleft, steps_rev, 20)

        # Start the motor threads
        stepper1.start()
        stepper2.start()

        # Check to see if both threads are done and clean up GPIO pins when done
        while True:
            if stepper1.is_alive() == False and stepper2.is_alive() ==False:
                GPIO.cleanup()
                break

    except KeyboardInterrupt:
        GPIO.cleanup()


while True:

    Motor1 = [40,36,38,32]
    Motor2 = [37,33,35,31]

    img_name = 'image.jpg'
    picam2.capture_file(img_name) #take image 

    img = cv.imread("image.jpg") #read image with open cv, to get the bgr value of one pixel index using print(img[row][col])

    total_pixels = img.shape #returns [2529, 4608] as the shape of the image

    #create boundary for red values as two arrays
    lower = np.array([115,0,0]) #lower range of bgr values for blue
    upper = np.array([255,70,70]) #upper range of bgr values for blue

    #determine if the pixel in the image has bgr values within the range
    image_mask = cv.inRange(img,lower,upper) #returns array of 0s & 255s, 255=white=within range, 0=black=not in range
    cv.imwrite("image2.jpg", image_mask) #write the mask to a new file so that it can be viewed 

    in_range = np.count_nonzero(image_mask) #count the number of elements in the array that are not zero (in other words elements that are in the red range)
    not_in_range = total_pixels[0]*total_pixels[1] - in_range 
    total = total_pixels[0]*total_pixels[1]

    percent_blue = round((in_range/total)*100)
    print(percent_blue, "%")

   # picam2.stop() #stop the picam 

    if percent_blue >= 60: #value here that corresponds to too much blue (over-rotation to the tape):
        moveSteps(1, 2)
    elif percent_blue <= 40: #value here that corresponds to too much white (over-rotation to the paper):
        moveSteps(2, 1)
    else:
        moveSteps(0, 0)
    

   
