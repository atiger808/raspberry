#!/usr/bin/env python
# ---------------------------------------------------
#
#	This is a program for Passive Buzzer Module
#		It will play simple songs.
#	You could try to make songs by youselves!
# 
#		Passive buzzer 			   Pi 
#			VCC ----------------- 3.3V
#			GND ------------------ GND
#			SIG ---------------- Pin 23
#
# ---------------------------------------------------

import RPi.GPIO as GPIO
import time

BuzzerPin = 5

CL = [0, 131, 147, 165, 175, 196, 211, 248]  # Frequency of Low C notes

CM = [0, 262, 294, 330, 350, 393, 441, 495]  # Frequency of Middle C notes

CH = [0, 525, 589, 661, 700, 786, 882, 990]  # Frequency of High C notes

song_1 = [CM[3], CM[5], CM[6], CM[3], CM[2], CM[3], CM[5], CM[6],  # Notes of song1
          CH[1], CM[6], CM[5], CM[1], CM[3], CM[2], CM[2], CM[3],
          CM[5], CM[2], CM[3], CM[3], CL[6], CL[6], CL[6], CM[1],
          CM[2], CM[3], CM[2], CL[7], CL[6], CM[1], CL[5]]

beat_1 = [1, 1, 3, 1, 1, 3, 1, 1,  # Beats of song 1, 1 means 1/8 beats
          1, 1, 1, 1, 1, 1, 3, 1,
          1, 3, 1, 1, 1, 1, 1, 1,
          1, 2, 1, 1, 1, 1, 1, 1,
          1, 1, 3]

song_2 = [CM[1], CM[1], CM[1], CL[5], CM[3], CM[3], CM[3], CM[1],  # Notes of song2
          CM[1], CM[3], CM[5], CM[5], CM[4], CM[3], CM[2], CM[2],
          CM[3], CM[4], CM[4], CM[3], CM[2], CM[3], CM[1], CM[1],
          CM[3], CM[2], CL[5], CL[7], CM[2], CM[1]]

beat_2 = [1, 1, 2, 2, 1, 1, 2, 2,  # Beats of song 2, 1 means 1/8 beats
          1, 1, 2, 2, 1, 1, 3, 1,
          1, 2, 2, 1, 1, 2, 2, 1,
          1, 2, 2, 1, 1, 3]


def setup(BuzzerPin):
    GPIO.setmode(GPIO.BCM)  # Numbers GPIOs by physical location
    GPIO.setwarnings(False)
    GPIO.setup(BuzzerPin, GPIO.OUT)  # Set pins' mode is output
    global Buzz  # Assign a global variable to replace GPIO.PWM
    Buzz = GPIO.PWM(BuzzerPin, 440)  # 440 is initial frequency.
    Buzz.start(0)  # Start Buzzer pin with 50% duty ration


def beep(x):
    Buzz.start(50)
    Buzz.ChangeFrequency(787)
    time.sleep(x)
    Buzz.stop()
    time.sleep(x)


def loop():
    Buzz.start(50)
    while True:
        print('\n    Playing song 1...')
        for i in range(1, len(song_1)):  # Play song 1
            Buzz.ChangeFrequency(song_1[i])  # Change the frequency along the song note
            time.sleep(beat_1[i] * 0.5)  # delay a note for beat * 0.5s
        time.sleep(1)  # Wait a second for next song.

        print('\n\n    Playing song 2...')
        for i in range(1, len(song_2)):  # Play song 1
            Buzz.ChangeFrequency(song_2[i])  # Change the frequency along the song note
            time.sleep(beat_2[i] * 0.5)  # delay a note for beat * 0.5s


def destroy():
    Buzz.stop()  # Stop the buzzer
    GPIO.output(BuzzerPin, 1)  # Set Buzzer pin to High
    GPIO.cleanup()  # Release resource


if __name__ == '__main__':  # Program start from here
    setup(BuzzerPin)
    try:
       # beep(0.5)
       loop()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        destroy()
