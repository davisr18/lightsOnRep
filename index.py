#created by Losant
import json
from gpiozero import LED, Button # Import GPIO library: https://gpiozero.readthedocs.io/en/stable/
from time import sleep
from losantmqtt import Device # Import Losant library: https://github.com/Losant/losant-mqtt-python

led_gpio = 23
button_gpio = 21

led = LED(led_gpio)
button = Button(button_gpio, pull_up=False)

# Construct Losant device
device = Device("5ade4994753ea500075d9f37", "9e7ab66e-208e-4684-a4fb-e56dc1e8f277", "ec79c25175bf081905ec4cfd0c9d80744502fc3d2e6c9474b61adc97f4147ff7")

def on_command(device, command):
    print(command["name"] + " command received.")

    # Listen for the gpioControl. This name configured in Losant
    if command["name"] == "toggle":
        # toggle the LED
        led.toggle()

def sendDeviceState():
    print("Sending Device State")
    device.send_state({"button": True})

# Listen for commands.
device.add_event_observer("command", on_command)

print("Listening for device commands")

button.when_pressed = sendDeviceState # Send device state when button is pressed

# Connect to Losant and leave the connection open
device.connect(blocking=True)
