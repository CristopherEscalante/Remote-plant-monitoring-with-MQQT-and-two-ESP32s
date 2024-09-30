import network
import time
from machine import Pin, ADC
import dht
from umqtt.simple import MQTTClient
from onewire import OneWire
from ds18x20 import DS18X20


#WIFI parameters
WIFI_SSID  = "SHARE-RESIDENTE"
WIFI_PASSWD = "Share@residente23"

# GPIO36 (ADC0) that connects to AOUT pin of moisture sensor
AOUT_PIN = 34
# GPIO17 connected to DS18B 20 sensor's DATA pin
SENSOR_PIN = 17

#Create a WLAN network interface object. STA_IF = station aka client, connects to upstream WiFi access points
print("Connecting to WiFi", end="")
nic = network.WLAN(network.STA_IF)
nic.active(True)
nic.connect(WIFI_SSID, WIFI_PASSWD)
while not nic.isconnected():  
    print(".", end="")  
    time.sleep(0.1)
print(" Connected!")

# NEW PART
def connectMQTT():
    client = MQTTClient(client_id=b"esp32_envio_datos_14494432",
    server=b"c2881a8ac93240d0a5845937e12a4499.s2.eu.hivemq.cloud",
    port=0,
    user=b"esp32_envio_datos_14494432",
    password=b"Projetofinal1234",
    keepalive=7200,
    ssl=True,
    ssl_params={'server_hostname':'c2881a8ac93240d0a5845937e12a4499.s2.eu.hivemq.cloud'}
    )
    client.connect()
    return client

client = connectMQTT()

def publish(topic, value):
    print(topic)
    print(value)
    client.publish(topic, value)
    print("publish Done")
    

# Initialize ADC
adc = ADC(Pin(AOUT_PIN))

# Set ADC range (0-4095 for 12-bit resolution)
adc.atten(ADC.ATTN_11DB)

# Create OneWire object
one_wire = OneWire(Pin(SENSOR_PIN))

# Create DS18X20 object
ds18b20 = DS18X20(one_wire)

roms = ds18b20.scan()

# Initialize serial communication (Note: MicroPython REPL can be used for serial output)
# Replace with appropriate UART setup if needed
# UART setup might be required based on your specific MicroPython environment
# For example: uart = UART(1, baudrate=9600, tx=17, rx=16)
# uart.init(9600, bits=8, parity=None, stop=1, tx=17, rx=16)

# Initialize the DS18B20 sensor
ds18b20.convert_temp()

prev_weather = ""
while True:  
    print("Measuring soil conditions... ", end="")
    # Read the analog value from the sensor
    value = adc.read()

    # Print moisture value
    print("Moisture value:", value)
    
    # Wait for the temperature conversion to complete
    time.sleep_ms(750)
    
    # Read temperature in Celsius
    for rom in roms:
        temp_c = ds18b20.read_temp(rom)

    # Print temperature in both Celsius and Fahrenheit
    print("Temperature: {:.2f}°C".format(temp_c))

    # Convert temperature again for the next iteration
    ds18b20.convert_temp()

    #message="field1={moisture}&field2={temp}&status=MQTTPUBLISH".format(moisture=value,temp=temp_c) 
    message = "{},{}".format(temp_c, value)
    
    #publish as MQTT payload
    publish('soil_data', message)
    print("Sending data...")
    print(message)
    #delay 5 seconds
    

