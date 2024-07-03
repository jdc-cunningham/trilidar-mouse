# https://github.com/johnbryanmoore/VL53L0X_rasp_python/blob/master/python/VL53L0X_example.py
import time
import sys

sys.path.append('/home/pi/projects/trilidar-mouse/software/test/VL53L0X-python')

from python import VL53L0X

# Create a VL53L0X object
tof1 = VL53L0X.VL53L0X(i2c_bus=1,i2c_address=0x29) # top
tof2 = VL53L0X.VL53L0X(i2c_bus=0,i2c_address=0x29) # right
tof3 = VL53L0X.VL53L0X(i2c_bus=5,i2c_address=0x29) # left

# I2C Address can change before tof.open()
# tof.change_address(0x32)
tof1.open()
tof2.open()
tof3.open()

# Start ranging
tof1.start_ranging(VL53L0X.Vl53l0xAccuracyMode.BETTER)
tof2.start_ranging(VL53L0X.Vl53l0xAccuracyMode.BETTER)
tof3.start_ranging(VL53L0X.Vl53l0xAccuracyMode.BETTER)

# timing = tof1.get_timing()

# if timing < 20000:
#     timing = 20000
# print("Timing %d ms" % (timing/1000))

def to_in(cm):
  return cm * 0.393701

count = 0

d1a = []
d2a = []
d3a = []

while True:
    count += 1
    distance1 = tof1.get_distance()

    # if distance1 > 0:
    #     print("top %d mm, %d cm, %d in, %d" % (distance1, (distance1/10), to_in(distance1 / 10), count))

    time.sleep(0.04)

    
    distance2 = tof2.get_distance()

    # if distance2 > 0:
    #     print("left %d mm, %d cm, %d in, %d" % (distance2, (distance2/10), to_in(distance2 / 10), count))

    time.sleep(0.04)

    
    distance3 = tof3.get_distance()
    
    # if distance3 > 0:
    #     print("right %d mm, %d cm, %d in, %d" % (distance3, (distance3/10), to_in(distance3 / 10), count))

    time.sleep(0.04)

    d1 = to_in(distance1 / 10)
    d2 = to_in(distance2 / 10)
    d3 = to_in(distance3 / 10)

    print(str(d1) + ', ' + str(d2) + ', ' + str(d3))

    if (len(d1a) < 3):
        d1a.append(d1)
        d2a.append(d2)
        d3a.append(d3)
    else:
        d1a.pop(0)
        d2a.pop(0)
        d3a.pop(0)

        d1a.append(d1)
        d2a.append(d2)
        d3a.append(d3)

        d1av = round((sum(d1a) / 3), 2)
        d2av = round((sum(d2a) / 3), 2)
        d3av = round((sum(d3a) / 3), 2)

        print('top ' + str(d1av) + ', ' + 'left ' + str(d3av) + ', ' + 'right ' + str(d2av))
        # print(str(d1av))

    # time.sleep(timing/1000000.00)
