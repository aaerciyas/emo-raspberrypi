import RPi.GPIO as GPIO
import time

pwmPin = 19
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pwmPin, GPIO.OUT)

p = GPIO.PWM(pwmPin, 100) #100 frekansi temsil etmektedir
p.start(0)

while True:
	for i in range(50):
		p.ChangeDutyCycle(i)
		time.sleep(0.1)

	for i in range(50):
		p.ChangeDutyCycle(50-i)
		time.sleep(0.1)
