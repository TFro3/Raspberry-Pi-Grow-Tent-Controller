import RPi.GPIO as GPIO
import datetime
import time
import threading
import Adafruit_DHT


# Define pin numbers
LIGHTS_PIN = 14
FAN_PIN = 15
HUMIDIFIER_PIN = 18
HEATER_PIN = 23
DEHUMIDIFIER_PIN = 24
PUMP_PIN = 25
SENSOR_PIN = 17  # DHT22 Sensor

# ------------ You CAN edit values starting here ------------ #

# Define lights on and off times (in 12-hour format with AM/PM)
lights_on_time = datetime.datetime.strptime('6:00 AM', '%I:%M %p').time()  # Change to your desired on time
lights_off_time = datetime.datetime.strptime('10:00 PM', '%I:%M %p').time()  # Change to your desired off time

# Define pump runtime and interval (in seconds)
pump_runtime = 90  # Change to your desired pump runtime in seconds
pump_interval = 600  # Change to your desired pump interval in seconds

# Define temperature and humidity thresholds
Temperature_Threshold_Fan = 75  # Will turn on Fan if temperature in Fahrenheit (F) is above this value.
Temperature_Threshold_Heat = 63  # Will turn on Heat if temperature in Fahrenheit (F) is below this value.
Humidity_Threshold_Fan = 85  # Will turn on Fan once humidity is above this percentage (%) to try and move lower humidity air in. Disable this if humidity outside the tent/room is higher.
Humidity_Threshold_Humidifier = 70  # Will turn on Humidifier once humidity is below this percentage (%).
Humidity_Threshold_Dehumidifier = 80  # Will turn on Dehumidifier once humidity is above this percentage (%).

# Define appliance control flags (True: Enabled, False: Disabled)
lights_enabled = True  # Change to True or False
fan_enabled = True  # Change to True or False
humidifier_enabled = True  # Change to True or False
heater_enabled = True  # Change to True or False
dehumidifier_enabled = True  # Change to True or False
pump_enabled = True  # Change to True or False

# ------------ Do NOT edit values past here ------------ #


# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup([LIGHTS_PIN, FAN_PIN, HUMIDIFIER_PIN, HEATER_PIN, DEHUMIDIFIER_PIN, PUMP_PIN], GPIO.OUT)

# Function to print status with device and status information
def print_status(device, status):
    if device == "Lights" and not lights_enabled:
        print(f"{device}: \033[91mDisabled\033[0m")
    elif device == "Fan" and not fan_enabled:
        print(f"{device}: \033[91mDisabled\033[0m")
    elif device == "Humidifier" and not humidifier_enabled:
        print(f"{device}: \033[91mDisabled\033[0m")
    elif device == "Dehumidifier" and not dehumidifier_enabled:
        print(f"{device}: \033[91mDisabled\033[0m")
    elif device == "Heater" and not heater_enabled:
        print(f"{device}: \033[91mDisabled\033[0m")
    elif device == "Pump" and not pump_enabled:
        print(f"{device}: \033[91mDisabled\033[0m")
    else:
        print(f"{device}: {status}")

# Function to read temperature from DHT22 sensor
def get_temperature():
    sensor = Adafruit_DHT.DHT22
    humidity, temperature = Adafruit_DHT.read_retry(sensor, SENSOR_PIN)
    if temperature is not None:
        return temperature * 9/5.0 + 32  # Convert Celsius to Fahrenheit
    else:
        return None  # Return None if reading failed

# Function to read humidity from DHT22 sensor
def get_humidity():
    sensor = Adafruit_DHT.DHT22
    humidity, temperature = Adafruit_DHT.read_retry(sensor, SENSOR_PIN)
    if humidity is not None:
        return humidity
    else:
        return None  # Return None if reading failed

# Function to control the pump based on configured runtime and interval
def control_pump():
    while True:
        if pump_enabled:
            GPIO.output(PUMP_PIN, GPIO.LOW)  # Turn on the pump relay
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %I:%M:%S %p")
            print(f"Current Pump Status:\nPump: \033[92mON\033[0m for {pump_runtime} seconds\nTimestamp: {timestamp}\n")
            time.sleep(pump_runtime)  # Run the pump for the specified duration
            GPIO.output(PUMP_PIN, GPIO.HIGH)  # Turn off the pump relay
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %I:%M:%S %p")
            print(f"Current Pump Status:\nPump: \033[93mOFF\033[0m for {pump_interval} seconds\nTimestamp: {timestamp}\n")
            time.sleep(pump_interval - pump_runtime)  # Wait for the remaining interval
        else:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %I:%M:%S %p")
            time.sleep(60)  # Wait for 1 minute if the pump is disabled

# Start the pump control loop in a separate thread
pump_thread = threading.Thread(target=control_pump)
pump_thread.daemon = True  # Daemonize the thread to allow main program exit
pump_thread.start()

try:
    # Startup sequence to test relay functionality
    print("\033[92m\nRaspberry Pi Grow Tent/Room Controller - Version 1.0\033[0m")
    print("\033[94mDedicated to Emma. My dog who loved to smell flowers and eat vegetables right off the plants.\nMay she rest in peace.\n\033[0m")
    time.sleep(5)
    print("Startup Sequence: \033[93mTesting Relays...\033[0m")
    GPIO.output([LIGHTS_PIN, FAN_PIN, HUMIDIFIER_PIN, HEATER_PIN, DEHUMIDIFIER_PIN], GPIO.LOW)  # Turn on all relays except the pump
    time.sleep(5)  # Keep all relays on for 10 seconds
    GPIO.output([LIGHTS_PIN, FAN_PIN, HUMIDIFIER_PIN, HEATER_PIN, DEHUMIDIFIER_PIN], GPIO.HIGH)  # Turn off all relays except the pump
    print("Startup Sequence: \033[92mRelay Test Complete.\033[0m\n")
    time.sleep(3)
    # Main loop for controlling relays based on thresholds...
    while True:
        print("Current Status:")
        check_time = datetime.datetime.now().time()
        if lights_enabled and lights_on_time <= check_time < lights_off_time:
            GPIO.output(LIGHTS_PIN, GPIO.LOW)
            print_status("Lights", "\033[92mON\033[0m")
        else:
            GPIO.output(LIGHTS_PIN, GPIO.HIGH)
            print_status("Lights", "\033[93mOFF\033[0m")

        temperature = get_temperature()
        humidity = get_humidity()

        if fan_enabled and (temperature >= Temperature_Threshold_Fan or humidity >= Humidity_Threshold_Fan):
            GPIO.output(FAN_PIN, GPIO.LOW)
            print_status("Fan", "\033[92mON\033[0m")
        else:
            GPIO.output(FAN_PIN, GPIO.HIGH)
            print_status("Fan", "\033[93mOFF\033[0m")

        if humidifier_enabled and humidity < Humidity_Threshold_Humidifier:
            GPIO.output(HUMIDIFIER_PIN, GPIO.LOW)
            print_status("Humidifier", "\033[92mON\033[0m")
        else:
            GPIO.output(HUMIDIFIER_PIN, GPIO.HIGH)
            print_status("Humidifier", "\033[93mOFF\033[0m")

        if dehumidifier_enabled and humidity > Humidity_Threshold_Dehumidifier:
            GPIO.output(DEHUMIDIFIER_PIN, GPIO.LOW)
            print_status("Dehumidifier", "\033[92mON\033[0m")
        else:
            GPIO.output(DEHUMIDIFIER_PIN, GPIO.HIGH)
            print_status("Dehumidifier", "\033[93mOFF\033[0m")

        if heater_enabled and temperature < Temperature_Threshold_Heat:
            GPIO.output(HEATER_PIN, GPIO.LOW)
            print_status("Heater", "\033[92mON\033[0m")
        else:
            GPIO.output(HEATER_PIN, GPIO.HIGH)
            print_status("Heater", "\033[93mOFF\033[0m")

        if not pump_enabled:
            print_status("Pump", "\033[91mDisabled\033[0m")
        else:
            print_status("Pump", "\033[92mEnabled\033[0m")            

        if temperature is not None:
            print(f"Temperature: \033[36m{temperature:.2f} F\033[0m")

        if humidity is not None:
            print(f"Humidity: \033[36m{humidity:.2f} %\033[0m")

        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %I:%M:%S %p")
        print(f"Timestamp: {timestamp}\n")

        time.sleep(60)  # Adjust this sleep duration as needed

except KeyboardInterrupt:
    GPIO.cleanup()
except Exception as e:
    print(f"An error occurred: {str(e)}")
    GPIO.cleanup()
