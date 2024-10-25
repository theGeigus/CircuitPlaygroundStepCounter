# in-class example, Oct 16
import time
import math
from adafruit_circuitplayground import cp

read_delay = 0.1 # (s) how often do we sample acceleration? 0.2 seems good.
g=9.8 # (m/s^2) standard g value for acceleration

cutoff = .7
cacheSize = 10
accelCache = [(0, 0)] * cacheSize
pos = 0

def readAccel():
    global pos, accelCache, g

    x, y, z = cp.acceleration
    a = math.sqrt(x*x+y*y+z*z)/g
    t = time.monotonic()
    # print(t,a,x,y,z)
    accelCache[pos] = (a, t)
    time.sleep(read_delay)

def isStep():
    # print(accelCache[pos][0], accelCache[pos-5][0], accelCache[pos][1], accelCache[pos-5][1])
    slope = (accelCache[pos][0]-accelCache[pos-5][0])/(accelCache[pos][1]-accelCache[pos-5][1])
    return True and steps = steps + 1 if(slope >= cutoff) else False

def main():
    global pos, cacheSize
    while (1 == 1):
        readAccel()
        print(isStep())
        update_pixels()
        pos = (pos + 1) % cacheSize
        if cp.button_a:
            if button_mode == "a":
                button_mode = "b"
            elif button_mode == "b":
                button_mode = "c"
            elif button_mode == "c":
                button_mode = "d"
            elif button_mode == "d":
                button_mode = "e"
            else:
                button_mode = "a"
            cp.pixels.fill((0, 0, 0))  # Clear pixels for a moment
            time.sleep(0.25)
        elif cp.button_b:
            if button_mode == "e":
                button_mode = "d"
            elif button_mode == "d":
                button_mode = "c"
            elif button_mode == "c":
                button_mode = "b"
            elif button_mode == "b":
                button_mode = "a"
            else:
                button_mode = "e"
            cp.pixels.fill((0, 0, 0))  # Clear pixels for a moment
            time.sleep(0.25)
        
def update_pixels():
    # Calculate the number based on steps and other parameters
    number = steps 
    x = number % 10
    y = (number // 10) % 10
    z = (number // 100) % 10
    a = (number // 1000) % 10
    b = (number // 10000) % 10

    if button_mode == "a":
        for i in range(10):
            if i < x:
                cp.pixels[i] = (224, 0, 224)  # Purple
            else:
                cp.pixels[i] = (3, 0, 3)  # Off
    elif button_mode == "b":
        for i in range(10):
            if i < y:
                cp.pixels[i] = (0, 0, 254)  # Blue
            else:
                cp.pixels[i] = (0, 0, 3)  # Off
    elif button_mode == "c":
        for i in range(10):
            if i < z:
                cp.pixels[i] = (0, 225, 0)  # Green
            else:
                cp.pixels[i] = (0, 3, 0)  # Off
    elif button_mode == "d":
        for i in range(10):
            if i < a:
                cp.pixels[i] = (100, 100, 0)  # Yellow
            else:
                cp.pixels[i] = (3, 3, 0)  # Off
    elif button_mode == "e":
        for i in range(10):
            if i < b:
                cp.pixels[i] = (225, 0, 0)  # Red
            else:
                cp.pixels[i] = (3, 0, 0)  # Off



if(__name__ == "__main__"):
    main()


