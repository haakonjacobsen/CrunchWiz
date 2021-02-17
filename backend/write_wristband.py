import random

f = open("device_output/test_data/wristband.txt", "a")
f.write(str(random.randint(0, 1000)) + "\n")
f.close()
