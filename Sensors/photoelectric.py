import RPi.GPIO as GPIO
import time

# Pin Definitions
button_pin_up = 23  # BCM pin 18, BOARD pin 12
button_pin_down = 22
led_pin_green = 18
led_pin_red = 17

def main():
    
    # Pin Setup:
    GPIO.setmode(GPIO.BCM)  # BCM pin-numbering scheme from Raspberry Pi
    GPIO.setup(button_pin_up, GPIO.IN)  # set pin as an input pin
    GPIO.setup(button_pin_down, GPIO.IN)  # set pin as an input pin
    GPIO.setup(led_pin_green, GPIO.OUT, initial = GPIO.LOW)  # set pin as an output pin
    GPIO.setup(led_pin_red, GPIO.OUT, initial = GPIO.LOW)  # set pin as an output pin
    curr_value_red = GPIO.LOW
    curr_value_green = GPIO.LOW
    print("Starting demo now! Press CTRL+C to exit")
    try:
        while True:

            value_green = GPIO.output(led_pin_green, curr_value_green)
            value_red = GPIO.output(led_pin_red, curr_value_red)
            value_up = GPIO.input(button_pin_up)
            value_down = GPIO.input(button_pin_down)
	    
            if value_up == GPIO.HIGH:
                  value_str_up = "HIGH"
            else:
                  value_str_up = "LOW"

            if value_down == GPIO.HIGH:
                  value_str_down = "HIGH"
            else:
                  value_str_down = "LOW"
            print(value_green)
            print(value_red)
            print(value_str_up)
            print(value_str_down)
            time.sleep(1)

    finally:
        GPIO.cleanup()

if __name__ == '__main__':
    main()
