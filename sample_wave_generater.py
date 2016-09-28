#! /usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

def wave_generater(n, periods = [2, 5, 7],
                   white_noise = False,
                   burst_rate = 0.1,
                   burst_time = 10):
    data = []
    btime = 0
    for i in range(n):
        x = 0
        for p in periods:
            x += np.sin(2.0 * np.pi * i / p)
        if white_noise:
            x += np.random.randn()
        if np.random.rand() <= burst_rate:
            btime = burst_time
        if btime > 0:
            x += 2 * np.random.rand()
            btime += -1
        data.append(x)

    return np.array(data)

if __name__ == '__main__':
    from recurrence_plot import *
    import cv2
    w = wave_generater(n = 500, white_noise = True, periods = [10, 17, 51, 130], burst_rate = 0.0)
    plt.plot(w)
    plt.savefig("wave.png")
    m = mapping(w)
    cv2.imwrite('sample_wave.jpg',m)
