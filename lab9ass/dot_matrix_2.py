import RPi.GPIO as GPIO
import time

GPIO_MODE = GPIO.BCM
ROW_PINS = [26, 2, 12, 11, 14, 15, 16, 20]
COLUMN_PINS = [3, 21, 18, 4, 7, 22, 17, 27]


def initialize_gpio():
    GPIO.setmode(GPIO_MODE)
    for pin in ROW_PINS + COLUMN_PINS:
        GPIO.setup(pin, GPIO.OUT)

def reset_matrix():
    for row_pin in ROW_PINS:
        GPIO.output(row_pin, GPIO.LOW)
    for col_pin in COLUMN_PINS:
        GPIO.output(col_pin, GPIO.HIGH)


def display_character(pattern):
    for row_index in range(8):
        reset_matrix()
        GPIO.output(ROW_PINS[row_index], GPIO.HIGH)
        
        for col_index in range(8):
            if pattern[row_index] & (1 << (7 - col_index)):
                GPIO.output(COLUMN_PINS[col_index], GPIO.LOW)
            else:
                GPIO.output(COLUMN_PINS[col_index], GPIO.HIGH)
        
        time.sleep(0.001)


characters = {"A":[0b00111100,0b00111100,0b01100110,0b01100110,0b01111110,0b01100110,0b01100110,0b00000000],"B":[0b01111000,0b01111110,0b01100110,0b01111000,0b01111000,0b01100110,0b01111110,0b01111000]}


def main():
    initialize_gpio()
    try:
        while True:
            #print menu
            print("\n1. Display A\n2. Display B\n3. Display A and B periodically")
            while True:
                #get correct user input
                try:
                    option = int(input("Enter an Option: "))
                    break
                except ValueError:
                    print("\nInvalid Input Try Again")
            # set conditions for display
            if option == 1:
                
                pattern = characters["A"]
                while True:
                    for i in range(300):
                        display_character(pattern)
            elif option == 2:
                pattern = characters["B"]
                #display
                while True:
                    for i in range(300):
                        display_character(pattern)
            elif option == 3:
                pattern_a = characters["A"]
                pattern_b = characters["B"]
                while True:
                    for i in range(300):
                        display_character(pattern_a)
                    for i in range(300):
                        display_character(pattern_b)
            else:
                print("\nInvalid selection")

    except KeyboardInterrupt:
        GPIO.cleanup()
    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    main()
