from time import sleep
from di_sensors.easy_light_color_sensor import EasyLightColorSensor

light_sensor = EasyLightColorSensor(led_state = True)

while True:
    red, green, blue, clear = light_sensor.safe_raw_colors()
    print("Red: {:5.3f} Green {:5.3f} Blue: {:5.3f} Clear {:5.3f}".format(red, green, blue, clear))
    sleep(0.02)