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


