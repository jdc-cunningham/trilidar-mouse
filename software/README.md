### Software

This requires 3 different i2c buses since the sensors have the same address (0x29).

I have setup bus 0, 1 and 5 in my case by modifying the `/boot/firmware/config.txt` file and having these lines in it:

```
dtparam=i2c0=on # bus 0
dtparam=i2c_arm=on # bus 1
dtoverlay=i2c5,pins_10_11 # bus 5, gpio pin numbers
```
