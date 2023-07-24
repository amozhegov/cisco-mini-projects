from gpio import *
from time import *

def switch_all_leds(leds, value):
    for i in range(1, leds+1):
        digitalWrite(i, value)

def main():
    pinMode (0, IN)
    
    initial = 1
    last = 8
    
    button_pressed = False
    total_leds = 8
    switch_all_leds(total_leds, LOW)
    
    while True:
        value_read = digitalRead(0) # Read button value
        if value_read > 0 and button_pressed == False:
            digitalWrite(initial, HIGH)
            digitalWrite(last, LOW)
            button_pressed = True
        elif value_read == 0 and button_pressed == True:
            switch_all_leds(total_leds, LOW)
            button_pressed = False
            last = initial 
            initial = (initial % 8) + 1
        sleep(0.5)

main()