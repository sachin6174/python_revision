import math
import random

for i in range(1, 8):
    a = math.floor((random.random() *26))+ord('a')
    # print(i, a)
    print(chr(a),end='')
print(chr(122))