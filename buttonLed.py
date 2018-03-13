import RPi.GPIO as GPIO
import time

button = 29
led = 31

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(button, GPIO.IN,pull_up_down = GPIO.PUD_UP)
while True:
	button_state = GPIO.input(button)
	if(button_state == False):
		GPIO.output(led, True)
		print('button pressed')
		time.sleep(0.2)#for bouncing
	else:
		GPIO.output(led,False)
