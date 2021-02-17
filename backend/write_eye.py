import random

f = open("device_output/test_data/eye.txt", "a")
f.write(str(random.randint(0, 100)) + "\n")
f.close()
