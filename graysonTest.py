from time import sleep
from di_sensors.easy_light_color_sensor import EasyLightColorSensor

light_sensor = EasyLightColorSensor(led_state = True)
red_avg = 0
green_avg = 0
blue_avg = 0
clear_avg = 0
number_readings = 50

for x in range(number_readings):
    red, green, blue, clear = light_sensor.safe_raw_colors()
    red_avg += red
    green_avg += green
    blue_avg += blue
    clear_avg += clear
    print("Red: {:5.3f} Green {:5.3f} Blue: {:5.3f} Clear {:5.3f}".format(red, green, blue, clear))
    sleep(0.02)
    
red_avg = red_avg/number_readings
green_avg = green_avg/number_readings
blue_avg = blue_avg/number_readings
clear_avg = clear_avg/number_readings

print("Red avg: {:5.3f} Green avg: {:5.3f} Blue avg: {:5.3f} Clear avg: {:5.3f}".format(red_avg, green_avg, blue_avg, clear_avg))