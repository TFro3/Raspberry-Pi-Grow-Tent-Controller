# Raspberry-Pi-Grow-Tent-Controller
Raspberry Pi based grow controller for your grow tent/room. Utilizing temperature &amp; humidity sensor and relays to help automate grows and save you from having to buy another expensive device.

**The problem (for me) I'm solving:** 

All the grow tent controllers I've come across require you to use their fans, lights, etc for everything to work out of the box OR purchase an additional adapter to convert their proprietary plugs to a standard outlet so you can use your own devices. 

**My Solution/Features:** 

Using components I already had laying around I created a controller that is easily configurable to your needs. Even if you have to purchase all items to build you'll still be saving money.

**You'll be able to control the following:**

1. Lights (Based on time schedule in the 12 hour clock format)
2. Exhuast Fan (Based on Sensor readings)
3. Humidity (Based on Sensor readings)
4. Temperature (Based on Sensor readings)
5. Water Pump (Based on a set interval schedule) 


**For this project you will need the following:**
  - Raspberry Pi (I'm using a Raspberry Pi Zero W)
  - AM3203/DHT22 Temperature/Humidity Sensor
  - 10k Ohm Resistor (unless your AM3202/DHT22 has one built in
  - 5v relay bank (I'm using a bank of 8 but the program only uses 6 as of right now)
  - Jumper cables
  - 14/2 romex/housing wire
  - (3) 15amp outlets
  - Wires to connect the sensor to the Pi (I'm using come Cat5e cable I had laying around)
  - Some sort of box to house the Pi, relay(s), and outlets
  - OPTIONAL: OLED display that will show current temp, humidity, and status of relays

**You can edit the following to customize to your needs:**

Simply input the time you want the lights to turn on and off at.
```python
# Define lights on and off times (in 12-hour format with AM/PM)
lights_on_time = datetime.datetime.strptime('6:00 AM', '%I:%M %p').time()  # Change to your desired on time
lights_off_time = datetime.datetime.strptime('10:00 PM', '%I:%M %p').time()  # Change to your desired off time
```

You can set the desired temperature and humidity thresholds which will trigger the relays based off the sensor readings every 60 seconds
```python
# Define temperature and humidity thresholds
Temperature_Threshold_Fan = 80  # Change to your desired temperature threshold in Fahrenheit
Temperature_Threshold_Heat = 55  # Change to your desired temperature threshold in Fahrenheit
Humidity_Threshold_Fan = 85  # Change to your desired humidity threshold in percentage
Humidity_Threshold_Humidifier = 50  # Change to your desired humidity threshold in percentage
Humidity_Threshold_Dehumidifier = 75  # Change to your desired humidity threshold in percentage
```

Here you can how often you want the pump to run and for how long.
```python
# Define pump runtime and interval (in seconds)
pump_runtime = 90  # Change to your desired pump runtime in seconds
pump_interval = 600  # Change to your desired pump interval in seconds
```

If you're not using a particular appliance/relat you can simply change the value from "True" to "False". If set to False, the program will ignore that logic as well as print "Disabled" on the device status output to remind/tell you that the device is disabled.
```python
# Define appliance control flags (True: Enabled, False: Disabled)
lights_enabled = True  # Change to True or False
fan_enabled = True  # Change to True or False
humidifier_enabled = True  # Change to True or False
heater_enabled = True  # Change to True or False
dehumidifier_enabled = True  # Change to True or False
pump_enabled = True  # Change to True or False
```



