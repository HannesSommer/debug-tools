#!/usr/bin/env python
import matplotlib

matplotlib.use('GTK')

import matplotlib.pyplot as plt
import numpy as np
import sys
import time;

plt.ion()

n = 50;
t = []
v = []

startTime = time.clock();

for i in range(n):
    v.append(0);
    t.append(startTime - i * 0.01)

fig = plt.figure()
ax = fig.add_subplot(111)
line1, = ax.plot(np.array(t), np.array(v), 'r-') # Returns a tuple of line objects, thus the comma

while True:
    line = sys.stdin.readline()
    if not line: break;

    parts = line.split('=',2)
    if len(parts) == 2:
        var = parts[0]
        val = parts[1]
        if var != 'presentPosition': continue
    else:
        continue
    try:
        nv = float(val);
    except:
        continue
    del v[0]
    del t[0]
    v.append(nv)
    t.append(time.clock() - startTime)
    print nv;
    ax.set_ylim([np.min(np.array(v)), np.max(np.array(v))])
    ax.set_xlim([np.min(np.array(t)), np.max(np.array(t))])
    line1.set_xdata(np.array(t))
    line1.set_ydata(np.array(v))
    fig.canvas.draw()
