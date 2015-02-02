__author__ = 'Jordan'

import RPi.GPIO as GPIO
import time

LED_PIN = 4
BUTTON_PIN = 17

def setup_gpio():
    GPIO.setmode(GPIO.BCM)

    # LED output
    GPIO.setup(LED_PIN, GPIO.OUT)

    # Pushbutton input
    GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


def turn_on_LED():
    GPIO.output(LED_PIN, 1)


def turn_off_LED():
    GPIO.output(LED_PIN, 0)
    

def main():
    print("Setting up GPIO...")

    try:
        setup_gpio()

        for i in range(50):
            time.sleep(1)
            print("On")
            turn_on_LED()

            time.sleep(1)
            print("Off")
            turn_off_LED()

            print("Button: {0}".format(GPIO.input(BUTTON_PIN)))
            
    finally:
        print("Done")
        GPIO.cleanup()
        

if __name__ == '__main__':
	main()
