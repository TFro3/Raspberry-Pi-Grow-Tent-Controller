import RPi.GPIO as GPIO
import time

#Set relay on and off time (in seconds)
Relay_On_Time = 10
Relay_Off_Time = 1

# Define pin numbers
LIGHTS_PIN = 14
FAN_PIN = 15
HUMIDIFIER_PIN = 18
HEATER_PIN = 23
DEHUMIDIFIER_PIN = 24
PUMP_PIN = 25

#Setup GPIO
def run_relay_tests(iterations):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup([LIGHTS_PIN, FAN_PIN, HUMIDIFIER_PIN, HEATER_PIN, DEHUMIDIFIER_PIN, PUMP_PIN], GPIO.OUT)
    time.sleep(3)
    GPIO.output([LIGHTS_PIN, FAN_PIN, HUMIDIFIER_PIN, HEATER_PIN, DEHUMIDIFIER_PIN, PUMP_PIN], GPIO.HIGH)


# Set the iteration number for the amount of times you want to run the relay test(s).
iterations = 1
run_relay_tests(iterations)

#Turning on and off the relays for testing
for i in range(iterations):
    GPIO.output([LIGHTS_PIN], GPIO.LOW)
    print("Lights On")
    time.sleep(Relay_On_Time)  
    GPIO.output([LIGHTS_PIN], GPIO.HIGH)
    print("Lights Off")
    time.sleep(Relay_Off_Time)

    GPIO.output([FAN_PIN], GPIO.LOW)
    print("Fan On")
    time.sleep(Relay_On_Time)  
    GPIO.output([FAN_PIN], GPIO.HIGH)
    print("Fan Off")
    time.sleep(Relay_Off_Time)

    GPIO.output([HUMIDIFIER_PIN], GPIO.LOW)
    print("Humidifier On")
    time.sleep(Relay_On_Time)  
    GPIO.output([HUMIDIFIER_PIN], GPIO.HIGH)
    print("Humidifier Off")
    time.sleep(Relay_Off_Time)

    GPIO.output([DEHUMIDIFIER_PIN], GPIO.LOW)
    print("Dehumidifier On")
    time.sleep(Relay_On_Time)  
    GPIO.output([DEHUMIDIFIER_PIN], GPIO.HIGH)
    print("Dehumidifier Off")
    time.sleep(Relay_Off_Time)

    GPIO.output([HEATER_PIN], GPIO.LOW)
    print("Heater On")
    time.sleep(Relay_On_Time)  
    GPIO.output([HEATER_PIN], GPIO.HIGH)
    print("Heater Off")
    time.sleep(Relay_Off_Time)

    GPIO.output([PUMP_PIN], GPIO.LOW)
    print("Pump On")
    time.sleep(Relay_On_Time)  
    GPIO.output([PUMP_PIN], GPIO.HIGH)
    print("Pump Off")
    time.sleep(Relay_Off_Time)

GPIO.cleanup()

print(f"\n\033[92mAll Relays Tested {iterations} time(s)\033[0m")
time.sleep(5)