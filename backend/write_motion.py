import random

f = open("device_output/test_data/motion.txt", "a")
f.write(str(random.randint(-10, 0)) + "\n")
f.close()
