# Simple demo of the DRV2605 haptic feedback motor driver.
# Will play all 123 effects in order for about a half second each.
# Author: Tony DiCola
import time

import board
import busio

import adafruit_drv2605

def playHeartBeat(heartRate):

    # Initialize I2C bus and DRV2605 module.
    i2c = busio.I2C(board.SCL, board.SDA)
    drv = adafruit_drv2605.DRV2605(i2c)

    # Main loop runs forever trying each effect (1-123).
    # See table 11.2 in the datasheet for a list of all the effect names and IDs.
    #   http://www.ti.com/lit/ds/symlink/drv2605.pdf
    softPulse = 21
    hardPulse = 17
    beatLength = 0.5
    #heartRate = 68
    if heartRate > 0 and heartRate < 120:
        heartrate = 68

    pauseLength = (60 / heartRate) - beatLength
    
    if pauseLength < 0:
        pauseLength = 0.1

    counter = 0
    while True:
        
#             print('Playing effect #{0}'.format("softPulse: " + str(softPulse)))
            drv.sequence[0] = adafruit_drv2605.Effect(softPulse)  # Set the effect on slot 0.
            
#             print('Playing effect #{0}'.format("hardPulse: " + str(hardPulse)))
            drv.sequence[1] = adafruit_drv2605.Effect(hardPulse)  # Set the effect on slot 0.
            
            # You can assign effects to up to 7 different slots to combine
            # them in interesting ways. Index the sequence property with a
            # slot number 0 to 6.
            # Optionally, you can assign a pause to a slot. E.g.
            # drv.sequence[1] = adafruit_drv2605.Pause(0.5)  # Pause for half a second
            drv.play()       # play the effect
            time.sleep(beatLength)  # for 0.5 seconds
            drv.stop()      # and then stop (if it's still running)
            time.sleep(pauseLength)

#playHeartBeat(68)

