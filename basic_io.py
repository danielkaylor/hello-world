import RPi.GPIO as GPIO
import time

switch = 7
joystick_x = 20
joystick_y = 21
button = 12

def set_op():
	if GPIO.input(switch):
		return '*'
	elif GPIO.input(12):
		return '+'
	elif GPIO.input(20):
		return '-'
	else:
		return '/'

if __name__ == '__main__':

	GPIO.setmode(GPIO.BCM)

	# Joystick
	GPIO.setup(joystick_x, GPIO.IN)
	GPIO.setup(joystick_y, GPIO.IN)

	# Switch
	GPIO.setup(switch, GPIO.IN)

	# Button
	GPIO.setup(button, GPIO.IN)

	while True:
		time.sleep(3)
		time.sleep(.5)
		if GPIO.input(switch):
			print(GPIO.input(joystick_x))
		else:
			print(GPIO.input(joystick_y))
