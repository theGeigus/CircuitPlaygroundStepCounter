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
    return True if(slope >= cutoff) else False

def main():
    global pos, cacheSize
    while (1 == 1):
        readAccel()
        print(isStep())
        pos = (pos + 1) % cacheSize

if(__name__ == "__main__"):
    main()
