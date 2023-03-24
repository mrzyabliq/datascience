import numpy as np
a = input().split(',')
b = [0]*6
for i in range(6):
    b[i] = int(a[i])
disp = np.var(b, ddof = 0)
print(disp)
